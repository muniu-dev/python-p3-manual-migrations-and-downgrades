"""Renaming students to scholars

Revision ID: bcdb339f0710
Revises: 791279dd0760
Create Date: 2024-02-13 18:13:37.765924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcdb339f0710'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
