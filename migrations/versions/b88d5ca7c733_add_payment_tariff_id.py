"""add payment tariff id

Revision ID: b88d5ca7c733
Revises: 973df9969834
Create Date: 2024-10-09 17:26:14.492688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b88d5ca7c733'
down_revision: Union[str, None] = '973df9969834'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payments', sa.Column('tariff_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'payments', 'tariffs', ['tariff_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payments', type_='foreignkey')
    op.drop_column('payments', 'tariff_id')
    # ### end Alembic commands ###
