"""add new columns to posts table

Revision ID: d77f556c7c6f
Revises: f69f6980454b
Create Date: 2023-03-10 13:16:54.032114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd77f556c7c6f'
down_revision = 'f69f6980454b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('rating', sa.Integer(),
                  nullable=False))
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     server_default=sa.text('now()'), nullable=False))

    pass


def downgrade():
    op.drop_column('posts', 'rating')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
