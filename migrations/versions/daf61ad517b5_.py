"""empty message

Revision ID: daf61ad517b5
Revises: 
Create Date: 2023-08-17 22:51:38.536779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daf61ad517b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('destinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('country', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.String(length=120), nullable=True),
    sa.Column('flightProvider', sa.String(length=120), nullable=True),
    sa.Column('depatureDate', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('recovery_question', sa.String(length=80), nullable=True),
    sa.Column('recovery_answer', sa.String(length=80), nullable=True),
    sa.Column('country', sa.String(length=120), nullable=True),
    sa.Column('territory_state', sa.String(length=80), nullable=True),
    sa.Column('dob', sa.String(length=80), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('User_id', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(length=120), nullable=True),
    sa.Column('territory_state', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('flights')
    op.drop_table('destinations')
    # ### end Alembic commands ###