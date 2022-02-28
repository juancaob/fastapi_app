"""Add last few columns to posts table

Revision ID: 642b18d05dde
Revises: b52ae03b5bc1
Create Date: 2022-02-28 10:05:13.712113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642b18d05dde'
down_revision = 'b52ae03b5bc1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="1"),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
