"""removed db columns

Revision ID: d68b4387a623
Revises: c1a156df52f4
Create Date: 2024-02-04 19:39:20.130419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd68b4387a623'
down_revision = 'c1a156df52f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_first_name')
        batch_op.drop_index('ix_users_last_name')
        batch_op.drop_column('last_name')
        batch_op.drop_column('password_hash')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=120), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=64), nullable=True))
        batch_op.create_index('ix_users_last_name', ['last_name'], unique=False)
        batch_op.create_index('ix_users_first_name', ['first_name'], unique=False)

    # ### end Alembic commands ###