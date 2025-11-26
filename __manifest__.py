# -*- coding: utf-8 -*-
{
    'name': "Aca Timetable",

    'summary': "Manage Academic Timetable",

    'description': """
Manage Academic Timetable
    """,

    'author': "K.M.Raouf",
    'website': "https://github.com/yajuve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/room.xml',
        'demo/day.xml',
        'demo/hour.xml',
        'demo/year.xml',
        'demo/timetable.xml',
        'demo/timetableline.xml',
    ],
}

