"""initial schema

Revision ID: 4f2a05d983af
Revises: 
Create Date: 2019-04-08 18:59:23.112938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f2a05d983af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('character_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('moves',
    sa.Column('move_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('command', sa.String(), nullable=False),
    sa.Column('impact_frames', sa.Integer(), nullable=False),
    sa.Column('block_frames', sa.Integer(), nullable=False),
    sa.Column('hit_frames', sa.Integer(), nullable=False),
    sa.Column('counter_frames', sa.Integer(), nullable=False),
    sa.Column('damage', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['characters.character_id'], ),
    sa.PrimaryKeyConstraint('move_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moves')
    op.drop_table('characters')
    # ### end Alembic commands ###