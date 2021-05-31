# -*- coding: utf-8 -*-
{
    'name': "ebs_mas_sales_crm",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'sale', 'product', 'sale_stock', 'stock','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/partner_sequence.xml',
        'views/views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
