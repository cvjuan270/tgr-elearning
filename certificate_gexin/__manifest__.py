{
    "name": "certificate_gexin",
    "summary": """Personalizacion de Certificados para Gexin Diagnostic""",
    "author": "Juan D. Collado Vasquez",
    "website": "https://github.com/cvjuan270/tgr-elearning",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "16.0.1.0.1",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["base", "survey"],
    # always loaded
    "data": ["views/survey_report_template.xml"],
    "assets": {
        "web.report_assets_common": [
            "certificate_gexin/static/src/scss/survey_reports.scss"
        ],
    },
}
