"""Add foreing key to posts table

Revision ID: b52ae03b5bc1
Revises: fad89cbbc28d
Create Date: 2022-02-28 09:55:02.134235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b52ae03b5bc1'
down_revision = 'fad89cbbc28d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk", source_table="posts", referent_table="users", 
        local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE"
        )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts","owner_id")
    pass
