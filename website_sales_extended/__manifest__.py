# encoding: utf-8
{
    'name': "Website extended",

    'summary':
        """
            * Edited views in ecommerce views. \n
        """,

    'description':
        """
            * Develop some views to the website sales.
        """,

    'author': "Soluciones4G - OGM",
    'website': "www.soluciones4g.com",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'web',
        'website_form',
        'website_sale',
        'product',
    ],

    'demo': [],

    'data': [
        'views/extended_main_ecommerce_product_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
