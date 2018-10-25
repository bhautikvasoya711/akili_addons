# -*- coding: utf-8 -*-

{
    'name': 'Variants show in website',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Number of variants of products show in website',
    'description': """
        Shows number of variants on website if variants are more than 1.
    """,
    'depends':['website_sale'],
    'data': [
        'views/templates.xml',
    ],
    'image':[
       'static/description/icon.png',
    ],
    'installable' : True,
    'auto_install' : False,
}
