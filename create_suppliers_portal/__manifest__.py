# -*- coding: utf-8 -*-
{
    'name': "Create Vendors from website",

    'summary':
        """
            * Create a supplier from the website.
        """,

    'description':
        """
            * A employee has a portal user, this user can create a supplier
            * The employee must have the create contacts rights
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
        'contacts'
    ],

    'demo': [],

    'data': [
        'views/create_supplier_portal_templates.xml',    
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
