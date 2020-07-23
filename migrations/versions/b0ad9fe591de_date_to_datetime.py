"""Date to datetime

Revision ID: b0ad9fe591de
Revises: fa1b9301f850
Create Date: 2020-07-23 19:40:26.259479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0ad9fe591de'
down_revision = 'fa1b9301f850'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('price', 'date',
                    existing_type=sa.DATE(),
                    type_=sa.DateTime(),
                    existing_nullable=False)
    op.alter_column('product', 'date_on_market',
                    existing_type=sa.DATE(),
                    type_=sa.DateTime(),
                    existing_nullable=False)


def downgrade():
    op.alter_column('product', 'date_on_market',
                    existing_type=sa.DateTime(),
                    type_=sa.DATE(),
                    existing_nullable=False)
    op.alter_column('price', 'date',
                    existing_type=sa.DateTime(),
                    type_=sa.DATE(),
                    existing_nullable=False)
