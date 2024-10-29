"""fix user table

Revision ID: 618739cc08dd
Revises: 6da3e8d10336
Create Date: 2024-05-06 22:24:47.071199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '618739cc08dd'
down_revision: Union[str, None] = '6da3e8d10336'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'user',
        'password',
        nullable=True
    )
    op.alter_column(
        'user',
        'password',
        nullable=True
    )

    op.alter_column(
        'user',
        'is_subscriber',
        server_default=False
    )
    op.alter_column(
        'user',
        'is_company_superuser',
        server_default=False
    )

    op.alter_column(
        'user',
        'is_employer',
        server_default=False
    )
    op.alter_column(
        'user',
        'subscription_id',
        nullable=True
    )

def downgrade() -> None:
    op.alter_column(
        'user',
        'password',
        nullable=False
    )
    op.alter_column(
        'user',
        'password',
        nullable=False
    )

    op.alter_column(
        'user',
        'is_subscriber',
        server_default=None
    )
    op.alter_column(
        'user',
        'is_company_superuser',
        server_default=None
    )

    op.alter_column(
        'user',
        'is_employer',
        server_default=None
    )
    op.alter_column(
        'user',
        'subscription_id',
        nullable=False
    )
