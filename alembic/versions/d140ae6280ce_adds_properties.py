"""adds properties

Revision ID: d140ae6280ce
Revises: a113bcc9572e
Create Date: 2019-04-10 02:09:47.839538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd140ae6280ce'
down_revision = 'a113bcc9572e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('moves', sa.Column('counter_property', sa.String(), nullable=True))
    op.add_column('moves', sa.Column('hit_property', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('moves', 'hit_property')
    op.drop_column('moves', 'counter_property')
    # ### end Alembic commands ###
