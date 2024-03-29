"""amount constraints

Revision ID: 218f3a97805a
Revises: 196462260a57
Create Date: 2023-09-06 10:01:04.554736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218f3a97805a'
down_revision = '196462260a57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('donation', 'to_reserve')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donation', sa.Column('to_reserve', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###
