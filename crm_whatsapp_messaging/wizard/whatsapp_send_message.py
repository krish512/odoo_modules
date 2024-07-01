from odoo import fields, models


class WhatsappSendMessage(models.TransientModel):
    """This model is used for sending WhatsApp messages through Odoo."""

    _name = "whatsapp.send.message"
    _description = "Whatsapp Wizard"

    def _get_lead_mobile(self):
        # self.ensure_one()
        current_lead_id = self.env.context.get("lead_id")
        record = self.env["crm.lead"].browse(current_lead_id)
        return record.mobile

    mobile = fields.Char(string="Mobile", required=True, default=_get_lead_mobile)
    message = fields.Text(string="Message", required=True)

    def action_send_message(self):
        """This method is called to send the WhatsApp message using the
        provided details."""
        if self.message and self.mobile:
            message_string = ""
            message = self.message.split(" ")
            for msg in message:
                message_string = message_string + msg + "%20"
            message_string = message_string[: (len(message_string) - 3)]
            return {
                "type": "ir.actions.act_url",
                "url": "https://api.whatsapp.com/send?phone=" + self.mobile + "&text=" + message_string,
                "target": "new",
                "res_id": self.id,
            }
