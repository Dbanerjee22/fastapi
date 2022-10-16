"""add content column to post table

Revision ID: 2c61f3185eef
Revises: 0e92dfb214a4
Create Date: 2022-10-16 15:09:03.184857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c61f3185eef'
down_revision = '0e92dfb214a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
