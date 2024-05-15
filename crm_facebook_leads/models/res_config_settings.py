from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    crm_fb_access_token = fields.Char("Access Token", config_parameter="crm_facebook_leads.crm_fb_access_token")
    crm_fb_page_id = fields.Char("Page Id", config_parameter="crm_facebook_leads.crm_fb_page_id")
    # crm_fb_access_token_state = fields.Selection([('valid', 'Valid'), ('invalid', 'Invalid'), ('unknown', 'Unknown')],
    #                                              compute='_get_access_token_state', string='Token State')
    # crm_fb_access_token_state_message = fields.Text(compute='_get_access_token_state', string='Error Message')
