# -*- coding: utf-8 -*-
{
    'name': "hit_company_code",

    'summary': """
        Menambahkan field Company Code""",

    'description': """
        Menambahkan field Company Code
    """,

    'author': "Angga Kawa",
    'website': "http://www.hasnurgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/company_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
