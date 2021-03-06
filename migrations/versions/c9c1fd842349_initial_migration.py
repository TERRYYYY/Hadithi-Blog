"""Initial Migration

Revision ID: c9c1fd842349
Revises: b637326cc0d1
Create Date: 2020-05-09 20:38:13.864586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9c1fd842349'
down_revision = 'b637326cc0d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
