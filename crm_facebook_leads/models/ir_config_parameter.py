from odoo.models import Model, api


class IrConfigParameter(Model):
    _inherit = "ir.config_parameter"

    @api.model
    def get_crm_facebook_config(self):
        get_param = self.sudo().get_param
        return {
            "crm_fb_access_token": get_param("crm_facebook_leads.crm_fb_access_token", "False"),
            "crm_fb_page_id": get_param("crm_facebook_leads.crm_fb_page_id", "False"),
        }
