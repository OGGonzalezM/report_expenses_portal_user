# -*- coding: utf-8 -*-
{
    'name': "Mantenimiento extended",

    'summary':
        """
            * Extendido el módulo de mantenimiento
        """,

    'description':
        """
            * Crear Ordenes de trabajo para el mantenimiento
            * Datos agregados a las tareas.
        """,

    'author': "Soluciones4G - OGM",
    'website': "www.soluciones4g.com",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'maintenance',
        'project',
        'hr',
        'stock'
    ],

    'demo': [],

    'data': [
        'views/hr_employee_extended_view.xml',
        'views/project_task_extended_view.xml',
        'views/orden_trabajo_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
