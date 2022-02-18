"""create post table

Revision ID: 68af9c744f7c
Revises: 
Create Date: 2022-02-18 05:14:10.302427

Command used to generate this migration file:
>alembic revision -m "Create posts table"
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68af9c744f7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
