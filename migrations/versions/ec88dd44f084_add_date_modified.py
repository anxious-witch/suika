"""add_date_modified

Revision ID: ec88dd44f084
Revises: e726406d6e7a
Create Date: 2020-08-02 16:21:36.367872

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'ec88dd44f084'
down_revision = 'e726406d6e7a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('price', sa.Column('date_created', sa.DateTime(), server_default=func.now(), nullable=False))
    op.add_column('price', sa.Column(
        'date_modified',
        sa.DateTime(),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    ))
    op.drop_column('price', 'date')
    op.add_column('product', sa.Column(
        'date_modified',
        sa.DateTime(),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    ))


def downgrade():
    op.drop_column('product', 'date_modified')
    op.add_column('price', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('price', 'date_modified')
    op.drop_column('price', 'date_created')
