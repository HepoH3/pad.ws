"""Create padws schema

Revision ID: 0ed2c80b0270
Revises: 
Create Date: 2025-04-30 03:56:33.469180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ed2c80b0270'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute('CREATE SCHEMA IF NOT EXISTS padws')
    
def downgrade():
    op.execute('DROP SCHEMA IF EXISTS padws CASCADE')