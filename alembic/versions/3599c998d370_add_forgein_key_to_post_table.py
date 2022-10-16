"""add forgein key to post table

Revision ID: 3599c998d370
Revises: 7ff3e8441a53
Create Date: 2022-10-16 15:47:39.791981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3599c998d370'
down_revision = '7ff3e8441a53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fk', source_table='posts',referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fk',table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
