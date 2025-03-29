"""Fix relationships and schema

Revision ID: 4669b114073a
Revises: e12248813180
Create Date: 2025-03-25 15:43:50.430725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4669b114073a'
down_revision: Union[str, None] = 'e12248813180'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
