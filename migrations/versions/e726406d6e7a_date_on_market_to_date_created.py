"""date_on_market_to_date_created

Revision ID: e726406d6e7a
Revises: b0ad9fe591de
Create Date: 2020-08-02 16:09:07.071775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'e726406d6e7a'
down_revision = 'b0ad9fe591de'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('product', sa.Column(
        'date_created',
        sa.DateTime(),
        nullable=False,
        server_default=func.now()
    ))
    op.drop_column('product', 'date_on_market')


def downgrade():
    op.add_column('product', sa.Column('date_on_market', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('product', 'date_created')
