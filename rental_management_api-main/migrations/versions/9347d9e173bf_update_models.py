"""Update models

Revision ID: 9347d9e173bf
Revises: a410a9249bfe
Create Date: 2025-03-22 18:01:41.672627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9347d9e173bf'
down_revision: Union[str, None] = 'a410a9249bfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
