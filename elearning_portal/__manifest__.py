{
    "name": "elearning_portal",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "author": "Juan D. Collado Vasquez",
    "website": "https://github.com/cvjuan270/tgr-elearning",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "16.0.1.0.1",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["base", "portal", "website_profile"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/elearning_portal_template.xml",
    ],
    "assets": {
        "web.assets.frontend": [
            "elearning_portal/static/src/js/slides_portal.js",
            # "elearning_portal/static/src/scss/website_profile.scss",
        ],
    },
}
