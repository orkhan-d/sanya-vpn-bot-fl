"""add order canceled

Revision ID: ab89aedb077f
Revises: b82abde8d334
Create Date: 2024-10-10 16:37:59.991095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab89aedb077f'
down_revision: Union[str, None] = 'b82abde8d334'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('canceled', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'canceled')
    # ### end Alembic commands ###
