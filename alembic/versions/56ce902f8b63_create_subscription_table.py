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
down_revision: Union[str, None] = 'befa921aa1bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'subscription',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('last_payment', sa.TIMESTAMP),
        sa.Column('expired_at', sa.TIMESTAMP),
        sa.Column('has_expired', sa.BOOLEAN),
        sa.Column('is_corporate', sa.BOOLEAN),
        sa.Column('digest_config_id', sa.Integer, sa.ForeignKey('digest_config.id'))
    )

    def downgrade() -> None:
        op.drop_table('subscription')
