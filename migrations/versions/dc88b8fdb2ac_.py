"""empty message

Revision ID: dc88b8fdb2ac
Revises: 9c4ee26cfaa7
Create Date: 2019-10-10 16:23:31.034263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc88b8fdb2ac'
down_revision = '9c4ee26cfaa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('is_approve', sa.Boolean(), nullable=True))
    op.drop_column('answers', 'is_admin_answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('is_admin_answer', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('answers', 'is_approve')
    # ### end Alembic commands ###