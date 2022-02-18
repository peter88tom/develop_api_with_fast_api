"""Add content column to posts table

Revision ID: 7af752f764d6
Revises: 68af9c744f7c
Create Date: 2022-02-18 05:38:11.644036

Command used to generate this migration file:
>alembic revision -m "add content column to posts table

To which current migrations/revision you are in use
>alembic current

Show current available heads
>alembic heads

To run this migration:
> alembic upgrade 7af752f764d6 or alembic upgrade heads

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7af752f764d6'
down_revision = '68af9c744f7c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
