"""empty message

Revision ID: d79e9ab953fd
Revises: 
Create Date: 2018-10-30 09:32:30.709092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd79e9ab953fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('environ_mapping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tp_ip', sa.String(length=64), nullable=True),
    sa.Column('tms_ip', sa.String(length=64), nullable=True),
    sa.Column('user_prefix', sa.String(length=64), nullable=True),
    sa.Column('tms_db', sa.String(length=64), nullable=True),
    sa.Column('tp_db', sa.String(length=64), nullable=True),
    sa.Column('tms_dsn', sa.String(length=64), nullable=True),
    sa.Column('tp_dsn', sa.String(length=64), nullable=True),
    sa.Column('db_password', sa.String(length=64), nullable=True),
    sa.Column('redis_peer', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_environ_mapping_tms_ip'), 'environ_mapping', ['tms_ip'], unique=False)
    op.create_table('pageview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('view', sa.String(length=64), nullable=True),
    sa.Column('pv', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('last_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pageview_view'), 'pageview', ['view'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('save_sql',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('SQL_statements', sa.String(length=64), nullable=True),
    sa.Column('instance', sa.String(length=64), nullable=True),
    sa.Column('creator', sa.String(length=64), nullable=True),
    sa.Column('modifier', sa.String(length=64), nullable=True),
    sa.Column('CREATE_DATE', sa.Date(), nullable=True),
    sa.Column('UPDATE_DATE', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('CREATE_DATE'),
    sa.UniqueConstraint('UPDATE_DATE')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('save_sql')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_pageview_view'), table_name='pageview')
    op.drop_table('pageview')
    op.drop_index(op.f('ix_environ_mapping_tms_ip'), table_name='environ_mapping')
    op.drop_table('environ_mapping')
    # ### end Alembic commands ###