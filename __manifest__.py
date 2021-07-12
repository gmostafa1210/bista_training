# -*- coding: utf-8 -*-

{
    'name' : 'Bista Training Management System',
    'version' : '1.0',
    'sequence' : 1,
    'summary': 'Bista Training Management System - BGD Summary.',
    'description' : 'Bista Training Management System - BGD Description.',
    'depends' : ['base'],
    'data' : [
        'security/training_security.xml',
        'security/training_record_rules.xml',
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/bista_training_menus.xml',
        'views/trainee_views.xml',
        'views/trainer_views.xml',
        'views/location_views.xml',
        'views/role_views.xml',
        'views/subject_views.xml',
        'views/topics_views.xml',
        'views/stages_views.xml',
        'views/attendance_views.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
