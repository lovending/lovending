# -*- coding: utf-8 -*-
{
    'name': "lovending",

    'summary': """lovending Module""",

    'description': """lovending""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'license': "OPL-1",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'sale_management', 'sale', 'sale_subscription', 'account', 'stock', 'account_accountant', 'purchase', 'point_of_sale', 'hr_expense', 'documents', 'hr', 'mail', 'stock_barcode', 'hr_contract'],
    'installable': True,
    'active': True,
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand_view.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
