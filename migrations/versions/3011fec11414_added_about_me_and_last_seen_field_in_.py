"""Added about_me and last_seen field in user model

Revision ID: 3011fec11414
Revises: 44756b6787af
Create Date: 2018-06-25 15:12:24.465002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3011fec11414'
down_revision = '44756b6787af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
