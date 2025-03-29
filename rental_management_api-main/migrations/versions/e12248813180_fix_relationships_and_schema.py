"""Fix relationships and schema

Revision ID: e12248813180
Revises: e8ff3d81965e
Create Date: 2025-03-22 21:57:52.486438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e12248813180'
down_revision: Union[str, None] = 'e8ff3d81965e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
