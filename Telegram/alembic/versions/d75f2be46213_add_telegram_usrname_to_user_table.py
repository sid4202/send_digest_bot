"""add telegram usrname to user table

Revision ID: d75f2be46213
Revises: 618739cc08dd
Create Date: 2024-05-06 23:07:49.789540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd75f2be46213'
down_revision: Union[str, None] = '618739cc08dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'user',
        sa.Column('username', sa.String)
    )


def downgrade() -> None:
    op.drop_column(
        'user',
        'username'
    )
