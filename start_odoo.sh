#!/bin/bash

# Configuration
ODOO_BIN="/home/bhakimi/workspace/source/community/v 16.0/odoo/odoo-bin"
ADDONS_PATH="/home/bhakimi/workspace/source/community/v 16.0/odoo/addons"
# ENTERPRISE_ADDONS="/home/bhakimi/workspace/source/enterprise/v 16.0/odoo/addons"
# CUSTOM_ADDONS="/home/bhakimi/workspace/source/community/v 16.0/my_modules,/home/bhakimi/workspace/source/community/v 16.0/myaddons"
CUSTOM_ADDONS="/home/bhakimi/workspace/source/community/v 16.0/odoo-IFRC-addon"
DB_NAME="community_db"
MODULE_TO_UPDATE="volunteer_management"

# Start Odoo with configurable options
source venv/bin/activate
python3 "$ODOO_BIN" --addons-path="$ADDONS_PATH,$CUSTOM_ADDONS" --xmlrpc-port=8069 --dev xml -u "$MODULE_TO_UPDATE"
