"""Add create users table

Revision ID: 17dc102b6e52
Revises: 7af752f764d6
Create Date: 2022-02-18 06:00:39.874579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17dc102b6e52'
down_revision = '7af752f764d6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
