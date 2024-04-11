"""create company  table

Revision ID: 4f5e8137866d
Revises: 56ce902f8b63
Create Date: 2024-04-12 02:40:12.284721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f5e8137866d'
down_revision: Union[str, None] = '56ce902f8b63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
