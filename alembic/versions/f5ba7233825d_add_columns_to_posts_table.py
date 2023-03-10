"""add columns to posts table

Revision ID: f5ba7233825d
Revises: 6c711f77d832
Create Date: 2023-03-10 12:50:55.828392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5ba7233825d'
down_revision = '6c711f77d832'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
