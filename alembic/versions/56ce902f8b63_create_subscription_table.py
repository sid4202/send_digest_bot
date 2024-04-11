"""create subscription table

Revision ID: 56ce902f8b63
Revises: a0ea9cc3d505
Create Date: 2024-04-12 02:39:50.235548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56ce902f8b63'
down_revision: Union[str, None] = 'a0ea9cc3d505'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
