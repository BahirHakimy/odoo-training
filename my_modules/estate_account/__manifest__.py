# -*- coding: utf-8 -*-
{
    "application": True,
    "name": "estate_account",
    "summary": """
        Invoicing moudle for estate property""",
    "description": """
        Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["estate", "account"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views_inherit.xml",
    ],
}
