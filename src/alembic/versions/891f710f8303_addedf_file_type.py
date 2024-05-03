"""Addedf File Type

Revision ID: 891f710f8303
Revises: 
Create Date: 2024-05-03 13:53:21.920067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '891f710f8303'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=8), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_fk', sa.Integer(), nullable=False),
    sa.Column('payment_fk', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('rest', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('text_invoice_file_path', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['payment_fk'], ['payment.id'], ),
    sa.ForeignKeyConstraint(['user_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('invoice_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_fk'], ['invoice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('invoice')
    op.drop_table('users')
    op.drop_table('payment')
    # ### end Alembic commands ###