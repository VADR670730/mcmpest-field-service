# Copyright (C) 2020, Brian McMaster
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FSMPerson(models.Model):
    _inherit = 'fsm.person'

    def _compute_order_open_count(self):
        order_data = self.env['fsm.order'].read_group(
            [('person_id', 'in', self.ids), ('stage_id.is_closed', '=', False)],
            ['person_id'], ['person_id'])
        result = {data['person_id'][0]: int(data['person_id_count'])
                  for data in order_data}
        for person in self:
            person.order_open_count = result.get(person.id, 0)

    def _compute_order_need_schedule_count(self):
        order_data = self.env['fsm.order'].read_group(
            [('person_id', 'in', self.ids),
             ('scheduled_date_start', '=', False)],
            ['person_id'], ['person_id'])
        result = {data['person_id'][0]: int(data['person_id_count'])
                  for data in order_data}
        for person in self:
            person.order_need_schedule_count = result.get(person.id, 0)

    order_open_count = fields.Integer(
        compute='_compute_order_open_count',
        string="Orders Count")
    order_need_schedule_count = fields.Integer(
        compute='_compute_order_need_schedule_count',
        string="Orders to Schedule")

    team_id = fields.Many2one(
        'fsm.team',
        string='Team')
