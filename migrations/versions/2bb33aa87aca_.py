"""empty message

Revision ID: 2bb33aa87aca
Revises: 81f117203333
Create Date: 2018-08-31 21:14:19.236335

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2bb33aa87aca'
down_revision = '81f117203333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'roles', 'user', ['user_id'], ['id'])
    op.drop_column('roles', 'capabilities')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('capabilities', mysql.VARCHAR(length=200), nullable=True))
    op.drop_constraint(None, 'roles', type_='foreignkey')
    op.drop_column('roles', 'user_id')
    # ### end Alembic commands ###
