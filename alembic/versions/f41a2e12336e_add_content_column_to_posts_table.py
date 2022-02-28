"""Add content column to posts table

Revision ID: f41a2e12336e
Revises: 5781de69abc7
Create Date: 2022-02-27 12:49:51.452421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f41a2e12336e'
down_revision = '5781de69abc7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("content", sa.String(150), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
