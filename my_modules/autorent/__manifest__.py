# -*- coding: utf-8 -*-
{
    "application": True,
    "name": "autorent",
    "summary": """
        AutoRent Car Rentals""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Bahir Hakimi",
    "website": "https://netlinks.net",
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
        "views/autorent_search_views.xml",
        "views/autorent_car_views.xml",
        "views/autorent_booking_views.xml",
        "data/sequence.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
