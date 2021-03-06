"""followers

Revision ID: 18aad51f2ec5
Revises: c21828b0d947
Create Date: 2018-04-11 15:19:50.944540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18aad51f2ec5'
down_revision = 'c21828b0d947'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
