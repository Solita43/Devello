"""empty message

Revision ID: 64259b6f9fe9
Revises: 
Create Date: 2023-06-15 15:28:38.107437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64259b6f9fe9'
down_revision = None
branch_labels = None
depends_on = None

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=55), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=35), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=35), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('purpose', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE projects SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE boards SET SCHEMA {SCHEMA};")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('boards')
    op.drop_table('projects')
    op.drop_table('users')
    # ### end Alembic commands ###