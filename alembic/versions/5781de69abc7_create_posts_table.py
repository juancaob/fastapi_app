"""Create posts table

Revision ID: 5781de69abc7
Revises: 
Create Date: 2022-02-27 12:34:30.620516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5781de69abc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(100), nullable=False))
    pass


def downgrade():
    op.drop_column("posts")
    pass
