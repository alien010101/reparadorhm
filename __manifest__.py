# -*- coding: utf-8 -*-
{
    'name': "reparator",

    'summary': 'Reparators control for repair module using employee module',

    'description': """
        The following topics are added to repair module:
    * Assign reparator to a reparation order
    """,

    'author': "Robot1984 dev",
    'website': "http://www.robot1984dev.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'repair', 'hr'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/repair_extend.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}