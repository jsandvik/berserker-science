"""initial schema

Revision ID: 0650d601423b
Revises: 
Create Date: 2019-04-07 01:19:35.618589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0650d601423b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moves',
    sa.Column('move_id', sa.Integer(), nullable=False),
    sa.Column('notation', sa.String(), nullable=False),
    sa.Column('impact_frames', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('move_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moves')
    # ### end Alembic commands ###