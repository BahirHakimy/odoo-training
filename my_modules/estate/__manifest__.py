# -*- coding: utf-8 -*-
{
    "name": "Real Estate",
    "summary": """
        Real Estate App""",
    "description": """
        Long description of module's purpose
    """,
    "application": True,
    "author": "Netlinks LTD",
    "website": "https://www.netlinks.net",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_view.xml",
        "views/user_properties_view.xml",
        "wizards/accept_reason_view.xml",
    ],
    # only loaded in demonstration mode
    "license": "LGPL-3",
}
