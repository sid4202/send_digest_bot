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
down_revision: Union[str, None] = 'a0ea9cc3d505'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'company',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('is_subscriber', sa.BOOLEAN),
        sa.Column('superuser_password', sa.String),
        sa.Column('subscription_id', sa.Integer, sa.ForeignKey('subscription.id'))
    )


def downgrade() -> None:
    op.drop_table('company')