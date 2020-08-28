# Copyright (C) 2019 - Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - Flow for McMPest',
    'summary': 'Field Service workflow for McMPest',
    'version': '12.0.1.0.0',
    'category': 'Field Service',
    'author':
        'Brian McMaster',
    'website': 'https://github.com/OCA/field-service',
    'depends': [
        'fieldservice_mcmpest_groups',
    ],
    'data': [
        'wizard/order_complete_wizard.xml',
        'wizard/order_not_finished_wizard.xml',
        'data/fsm_stage.xml',
        'views/fsm_order.xml',
    ],
    'application': False,
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': ['brian10048'],
}
