# -*- coding: utf-8 -*-
{
    "name": "CRM Facebook Leads",
    "summary": "Sync Facebook Leads with Odoo CRM",
    "description": """
    Sync Facebook Leads with Odoo CRM
    """,
    "author": "CodeAngle Technologies Pvt Ltd",
    "website": "https://codeangle.in",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sales/CRM",
    "version": "17.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["crm", "utm"],
    # always loaded
    "data": [
        "data/ir_config_parameter_data.xml",
        "data/ir_cron_data.xml",
        "security/ir.model.access.csv",
        "views/crm_menu_views.xml",
        "views/crm_facebook_form_views.xml",
        "views/crm_facebook_page_views.xml",
        "views/crm_lead_views.xml",
    ],
    "application": True,
    "installable": True,
    "license": "GPL-3",
}
