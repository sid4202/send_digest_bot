"""create user table

Revision ID: a0ea9cc3d505
Revises: 
Create Date: 2024-04-10 01:52:00.939008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0ea9cc3d505'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=True),
        sa.Column('name', sa.String, nullable=True),
        sa.Column('surname', sa.String, nullable=True),
        sa.Column('phone_number', sa.String, nullable=True),
        sa.Column('job_name', sa.String, nullable=True),
        sa.Column('password', sa.String),
        sa.Column('is_subscriber', sa.BOOLEAN),
        sa.Column('is_company_superuser', sa.BOOLEAN),
        sa.Column('is_employer', sa.BOOLEAN)
    )


def downgrade() -> None:
    op.drop_table('user')
