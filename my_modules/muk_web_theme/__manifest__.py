###################################################################################
#
#    Copyright (c) 2017-today MuK IT GmbH.
#
#    This file is part of MuK Backend Theme
#    (see https://mukit.at).
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
###################################################################################

{
    "name": "MuK Backend Theme",
    "summary": "Odoo Community Backend Theme",
    "version": "16.0.1.0.7",
    "category": "Themes/Backend",
    "license": "LGPL-3",
    "author": "MuK IT",
    "website": "http://www.mukit.at",
    "live_test_url": "https://mukit.at/r/SgN",
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "depends": [
        "base_setup",
        "web_editor",
        "mail",
    ],
    "excludes": ["web_enterprise"],
    "data": [],
    "assets": {},
    "images": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "uninstall_hook": "_uninstall_cleanup",
}
