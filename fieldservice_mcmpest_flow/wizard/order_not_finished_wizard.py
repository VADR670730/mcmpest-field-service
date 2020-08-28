# Copyright (c) 2019 - Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _

class order_not_finished_wizard(models.TransientModel):
    """Wizard to update required fields at FSM Order completion."""
    _name = 'order.not.finished.wizard'
    _description = 'FSM Order Not Finished Wizard'

    fsm_order_id = fields.Many2one('fsm.order', string='FSM Order',
                                   required=True)
    reason = fields.Char('Reason order not completed')

    def action_not_finish_wizard(self):
        """Wizard action that makes an activity for dispatcher"""
        for wiz in self:
            msg = _(
                """Order not serviceable reason: %s""") % (wiz.reason)
            wiz.fsm_order_id.message_post(body=msg)
            wiz.fsm_order_id.write({
                'stage_id': self.env.ref(
                    'fieldservice_mcmpest_flow.fsm_stage_assigned').id,
                'date_start': False,
            })
        return False
