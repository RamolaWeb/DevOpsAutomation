"""Created Initial table

Revision ID: 2f69d04059cb
Revises: 
Create Date: 2018-08-31 05:03:15.029108

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2f69d04059cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ip', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('dbUser', sa.String(length=100), nullable=False),
    sa.Column('dbName', sa.String(length=100), nullable=False),
    sa.Column('dbPass', sa.String(length=100), nullable=False),
    sa.Column('sshUser', sa.String(length=100), nullable=False),
    sa.Column('sshPass', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('capabilities', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('tokens', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # op.drop_index('email', table_name='User')
    # op.drop_table('User')
    # op.drop_table('Roles')
    # op.drop_table('Instances')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Instances',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('ip', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('dbUser', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('dbName', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('dbPass', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('sshUser', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('sshPass', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('Roles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('role', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('capabilities', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('User',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('role', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('avatar', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('tokens', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_index('email', 'User', ['email'], unique=True)
    op.drop_table('user')
    op.drop_table('roles')
    op.drop_table('instances')
    # ### end Alembic commands ###
