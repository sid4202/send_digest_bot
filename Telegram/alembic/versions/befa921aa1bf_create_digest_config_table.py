"""create digest config table

Revision ID: befa921aa1bf
Revises: 6da3e8d10336
Create Date: 2024-04-12 02:41:01.935413

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'befa921aa1bf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'digest_config',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('schdeule', sa.String),
        sa.Column('category', sa.String),
        sa.Column('channel_to_send', sa.String),
        sa.Column('sending_time', sa.TIMESTAMP),
    )


    def downgrade() -> None:
        op.drop_table('digest_config')
