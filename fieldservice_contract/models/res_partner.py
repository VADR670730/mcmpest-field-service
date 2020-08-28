# Copyright (C) 2019 - Brian McMaster <brian@mcmpest.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def act_show_contract(self):
        """ This opens contract view
            @return: the contract view
        """    
        action = super().act_show_contract()
        location = self.env['fsm.location'].search(
            [('partner_id', '=', self.id)])
        context = action.get('context', {})
        context.update({'default_fsm_location_id': location.id})
        action['context'] = context
        return action
