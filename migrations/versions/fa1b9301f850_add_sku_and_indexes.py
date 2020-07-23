"""Add SKU and indexes

Revision ID: fa1b9301f850
Revises: a6b6ff5a0ca8
Create Date: 2020-07-23 18:53:25.432118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa1b9301f850'
down_revision = 'a6b6ff5a0ca8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('product', sa.Column('sku', sa.String(), nullable=False))
    op.create_index(op.f('ix_product_sku'), 'product', ['sku'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_product_sku'), table_name='product')
    op.drop_column('product', 'sku')
