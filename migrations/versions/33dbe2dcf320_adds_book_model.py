"""adds Book model

Revision ID: 33dbe2dcf320
Revises: 
Create Date: 2021-10-22 09:45:54.170875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33dbe2dcf320'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###