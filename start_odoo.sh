#!/bin/bash

# Configuration
ODOO_BIN="/home/bhakimi/workspace/source/community/v 16.0/odoo/odoo-bin"
ADDONS_PATH="/home/bhakimi/workspace/source/community/v 16.0/odoo/addons"
ENTERPRISE_ADDONS="/home/bhakimi/workspace/source/enterprise/v 16.0/odoo/addons"
CUSTOM_ADDONS="/home/bhakimi/workspace/source/community/v 16.0/my_modules,/home/bhakimi/workspace/source/community/v 16.0/myaddons"
DB_NAME="fleet_flow_db"
MODULE_TO_UPDATE="fleet_flow"

# Start Odoo with configurable options
source venv/bin/activate
python3 "$ODOO_BIN" --addons-path="$ADDONS_PATH,$ENTERPRISE_ADDONS,$CUSTOM_ADDONS" -d "$DB_NAME" -u $MODULE_TO_UPDATE --dev xml
