"""empty message

Revision ID: b935b91a26fd
Revises: 5d7f4b08c415
Create Date: 2023-06-26 17:17:38.503156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b935b91a26fd'
down_revision = '5d7f4b08c415'
branch_labels = None
depends_on = None

import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=SCHEMA if environment == "production" else None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(), nullable=False))
        batch_op.alter_column('order',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=SCHEMA if environment == "production" else None) as batch_op:
        batch_op.alter_column('order',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('status')

    # ### end Alembic commands ###