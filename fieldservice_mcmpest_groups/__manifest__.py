# Copyright (C) 2019, Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service Groups for McMPest',
    'summary': 'Security and group modifications for Field Service',
    'version': '12.0.0.1.0',
    'category': 'Field Service',
    'author': 'Brian McMaster',
    'depends': [
        'fieldservice'
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/hide_tech_views.xml',
        'views/new_tech_views.xml',
        'views/new_user_views.xml',
    ],
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': ['brian10048'],
}
