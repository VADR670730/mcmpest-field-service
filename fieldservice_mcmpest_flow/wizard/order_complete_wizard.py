# Copyright (c) 2019 - Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class order_complete_wizard(models.TransientModel):
    """Wizard to update required fields at FSM Order completion."""
    _name = 'order.complete.wizard'
    _description = 'FSM Order Completion Wizard'

    fsm_order_id = fields.Many2one('fsm.order', string='FSM Order',
                                   required=True)
    resolution = fields.Char('Resolution Notes')

    def action_finish_wizard(self):
        """Wizard action that updates FSM Order"""
        for wiz in self:
            wiz.fsm_order_id.write({
                'resolution': wiz.resolution,
                'date_end': wiz.fsm_order_id.date_end or fields.Datetime.now()
            })
            wiz.fsm_order_id.action_complete()
        return False
