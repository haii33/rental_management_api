from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import InvoiceCreate, InvoiceSchema
from models import Invoice
from database import get_db

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.get("/", response_model=list[InvoiceSchema])
async def get_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()

@router.get("/{invoice_id}", response_model=InvoiceSchema)
async def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.post("/pay/{invoice_id}")
async def pay_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    if invoice.status == "Paid":
        raise HTTPException(status_code=400, detail="Invoice already paid")
    invoice.status = "Paid"
    db.commit()
    return {"detail": "Invoice paid successfully"}

@router.get("/download/{invoice_id}")
async def download_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"detail": "Download link for invoice"}
