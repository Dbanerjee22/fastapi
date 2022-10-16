"""create posts table

Revision ID: 0e92dfb214a4
Revises: 
Create Date: 2022-10-16 12:26:59.044525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e92dfb214a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(),nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
