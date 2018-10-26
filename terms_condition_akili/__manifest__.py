# -*- coding: utf-8 -*-

{
    'name': 'Terms_&_Condition',
    'summary': """Aggrement on terms and condition of company""",
    'description': """Enable the feature of aggrement ,and show the terms and condition of company on website""",
    'company': "Akil Systems Pvt. Ltd.",
    'author': "Akil System Pvt. Ltd.",
    'website': "http://www.akilisystems.in/",
    'category': 'Website',
    'depends': ['website_sale'],
    'version': '10.0.1.0.0',
    'data': [
        'views/assets.xml',  
        'views/res_company_views.xml',
        'views/templates.xml',
        'views/sale_order_views.xml',
    ],
    'images': [
        'static/description/image.jpg',
    ],
    'installable': True,
    'auto_install': False,
}
