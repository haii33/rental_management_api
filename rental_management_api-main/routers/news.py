from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import NewsCreate, NewsSchema
from models import News
from database import get_db

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/", response_model=list[NewsSchema])
async def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()

@router.post("/", response_model=NewsSchema)
async def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):
    new_news = News(**news_data.dict())
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news

@router.put("/{news_id}", response_model=NewsSchema)
async def update_news(news_id: int, news_data: NewsCreate, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    for key, value in news_data.dict(exclude_unset=True).items():
        setattr(news, key, value)
    db.commit()
    db.refresh(news)
    return news

@router.delete("/{news_id}")
async def delete_news(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    db.delete(news)
    db.commit()
    return {"detail": "News deleted successfully"}
