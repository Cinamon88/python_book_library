"""authors table

Revision ID: 7001e21cedbb
Revises: 
Create Date: 2023-03-22 09:13:08.332171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7001e21cedbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('lastName', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author')
    # ### end Alembic commands ###
