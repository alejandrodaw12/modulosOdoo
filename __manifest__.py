# -*- coding: utf-8 -*-
{
    'name': "proyectos",

    'summary': """
        Esta aplicacion esta fuera de mi casa""",

    'description': """
        La mejor de mi casa
    """,

    'author': "Aitor Menta",
    'website': "http://http://infsalinas.sytes.net:10150/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'UnaMuyBuena',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/proyectos_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True , 
}
