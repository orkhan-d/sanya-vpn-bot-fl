"""add server credentials

Revision ID: cb7fce3bb41f
Revises: 5cd99727c84c
Create Date: 2024-10-09 18:56:18.393442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb7fce3bb41f'
down_revision: Union[str, None] = '5cd99727c84c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('servers', sa.Column('username', sa.String(), nullable=False))
    op.add_column('servers', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('servers', 'password')
    op.drop_column('servers', 'username')
    # ### end Alembic commands ###
