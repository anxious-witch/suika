"""Initial migration

Revision ID: a6b6ff5a0ca8
Revises:
Create Date: 2020-07-23 18:02:37.572878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6b6ff5a0ca8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('volume', sa.Float(), nullable=False),
                    sa.Column('abv', sa.Float(), nullable=False),
                    sa.Column('country_of_origin', sa.String(), nullable=False),
                    sa.Column('available', sa.Boolean(), nullable=False),
                    sa.Column('container_type', sa.String(), nullable=False),
                    sa.Column('style', sa.String(), nullable=False),
                    sa.Column('sub_style', sa.String(), nullable=False),
                    sa.Column('producer', sa.String(), nullable=False),
                    sa.Column('short_description', sa.Text(), nullable=True),
                    sa.Column('date_on_market', sa.Date(), nullable=False),
                    sa.Column('season', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('price',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('date', sa.Date(), nullable=False),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('price')
    op.drop_table('product')
