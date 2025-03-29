"""Add payment_method column to payments

Revision ID: e8ff3d81965e
Revises: 9347d9e173bf
Create Date: 2025-03-22 20:53:04.491583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8ff3d81965e'
down_revision: Union[str, None] = '9347d9e173bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
