"""create user_ company table

Revision ID: 6da3e8d10336
Revises: 4f5e8137866d
Create Date: 2024-04-12 02:40:34.942021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6da3e8d10336'
down_revision: Union[str, None] = '4f5e8137866d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_company',
        sa.Column('user_id', sa.Integer, ),
        sa.Column('company_id', sa.Integer, )
    )


def downgrade() -> None:
    op.drop_table('user_company')
