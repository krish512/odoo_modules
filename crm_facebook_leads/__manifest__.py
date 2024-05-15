# -*- coding: utf-8 -*-
{
    "name": "CRM Facebook Leads",
    "summary": "Module to insert leads from Facebook",
    "description": """
    Module to fetch leads from Facebook and insert them into CRM
    """,
    "author": "CodeAngle Technologies Pvt Ltd",
    "website": "https://codeangle.in",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sales/CRM",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["crm"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/crm_menu_views.xml",
        "views/res_config_settings_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
