"""Add created_at and published column to posts table

Revision ID: f8a00c9c9a9a
Revises: ae53c67f1878
Create Date: 2022-02-18 07:12:12.061757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8a00c9c9a9a'
down_revision = 'ae53c67f1878'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="True")),
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,
                                     server_default=sa.text("now()")))

    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
