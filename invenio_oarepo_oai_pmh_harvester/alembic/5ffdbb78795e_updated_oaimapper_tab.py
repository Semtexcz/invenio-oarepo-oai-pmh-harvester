#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Updated OAIMapper tab"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ffdbb78795e'
down_revision = 'a0ccc82bae06'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('oarepo_oai_mapper', sa.Column('provider_id', sa.Integer(), nullable=True))
    # op.drop_constraint('fk_oarepo_oai_mapper_parser_id_oarepo_oai_parser', 'oarepo_oai_mapper', type_='foreignkey')
    # op.create_foreign_key(op.f('fk_oarepo_oai_mapper_provider_id_oarepo_oai_provider'), 'oarepo_oai_mapper', 'oarepo_oai_provider', ['provider_id'], ['id'])
    # op.drop_column('oarepo_oai_mapper', 'parser_id')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oarepo_oai_mapper', sa.Column('parser_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(op.f('fk_oarepo_oai_mapper_provider_id_oarepo_oai_provider'), 'oarepo_oai_mapper', type_='foreignkey')
    op.create_foreign_key('fk_oarepo_oai_mapper_parser_id_oarepo_oai_parser', 'oarepo_oai_mapper', 'oarepo_oai_parser', ['parser_id'], ['id'])
    op.drop_column('oarepo_oai_mapper', 'provider_id')
    # ### end Alembic commands ###