# Copyright (C) 2018, Open Source Integrators
# Copyright (c) 2019, Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _
from odoo.exceptions import ValidationError
import urllib.parse


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    # def action_confirm(self):
    #     return self.write({'stage_id': self.env.ref(
    #         'fieldservice_mcmpest_flow.fsm_stage_confirmed').id})

    def action_assign(self):
        if self.person_id:
            return self.write({'stage_id': self.env.ref(
                'fieldservice_mcmpest_flow.fsm_stage_assigned').id})
        else:
            raise ValidationError(_("Cannot move to Assigned " +
                                    "until 'Assigned To' is filled in"))

    def action_schedule(self):
        if self.scheduled_date_start and self.person_id:
            return self.write({'stage_id': self.env.ref(
                'fieldservice_mcmpest_flow.fsm_stage_scheduled').id})
        else:
            raise ValidationError(_("Cannot move to Scheduled " +
                                    "until both 'Assigned To' and " +
                                    "'Scheduled Start Date' are filled in"))

    def action_enroute(self):
        return self.write({'stage_id': self.env.ref(
            'fieldservice_mcmpest_flow.fsm_stage_enroute').id})

    def action_navigate(self):
        maps_url = 'https://www.google.com/maps/dir/?api=1&destination='
        address = '%s, %s, %s %s' % (
            self.street, self.city, self.state_name, self.zip)
        nav_end = '&dir_action=navigate'
        nav_url = maps_url + (urllib.parse.quote_plus(address)) + nav_end
        self.action_enroute()
        return {
            'type': 'ir.actions.act_url',
            'url': nav_url,
            'target': 'self',
            'res_id': self.id,
        }

    def action_start(self):
        start_date = self.date_start or fields.Datetime.now()
        return self.write({
            'stage_id': self.env.ref(
                'fieldservice_mcmpest_flow.fsm_stage_started').id,
            'date_start': start_date,
        })

    def action_not_finished(self):
        return {
            'name': _("Unservicable: %s") % self.name,
            'id': self.id,
            'type': 'ir.actions.act_window',
            'views': [[False, 'form']],
            'target': 'new',
            'context': {'default_fsm_order_id': self.id},
            'res_model': 'order.not.finished.wizard'
        }

    def action_complete(self):
        if not self.resolution:
            return self.launch_complete_wizard()
        else:
            self.date_end = self.date_end or fields.Datetime.now()
            return super().action_complete()

    def launch_complete_wizard(self):
        return {
            'name': _("Complete %s") % self.name,
            'id': self.id,
            'type': 'ir.actions.act_window',
            'views': [[False, 'form']],
            'target': 'new',
            'context': {'default_fsm_order_id': self.id},
            'res_model': 'order.complete.wizard'
        }

