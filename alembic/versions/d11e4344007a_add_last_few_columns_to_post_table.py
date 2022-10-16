"""add last few columns to post table

Revision ID: d11e4344007a
Revises: 3599c998d370
Create Date: 2022-10-16 15:59:18.053478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd11e4344007a'
down_revision = '3599c998d370'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published', sa.Boolean(),nullable=False,server_default='True'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'punlished')
    op.drop_column('posts', 'created_at')
    pass
