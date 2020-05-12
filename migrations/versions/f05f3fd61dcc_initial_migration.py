"""Initial Migration

Revision ID: f05f3fd61dcc
Revises: cbc782031dd9
Create Date: 2020-05-10 18:50:29.677910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f05f3fd61dcc'
down_revision = 'cbc782031dd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('content', sa.String(length=255), nullable=True))
    op.add_column('blogs', sa.Column('subtitle', sa.String(length=255), nullable=True))
    op.add_column('blogs', sa.Column('title', sa.String(length=255), nullable=True))
    op.drop_column('blogs', 'mysubtitle')
    op.drop_column('blogs', 'mycontent')
    op.drop_column('blogs', 'mytitle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('mytitle', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('mycontent', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('mysubtitle', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('blogs', 'title')
    op.drop_column('blogs', 'subtitle')
    op.drop_column('blogs', 'content')
    # ### end Alembic commands ###