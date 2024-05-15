from odoo import fields, models


class CrmFacebookForm(models.Model):
    _name = "crm.facebook.form"
    _description = "Facebook Form Page"

    name = fields.Char(required=True)
    facebook_form_id = fields.Char(required=True, string="Form ID")
    # mappings = fields.One2many("crm.facebook.form.field", "form_id")
    team_id = fields.Many2one(
        "crm.team", domain=["|", ("use_leads", "=", True), ("use_opportunities", "=", True)], string="Sales Team"
    )
    date_retrieval = fields.Datetime(string="Fetch Leads After")

    # def get_fields(self):
    #     self.mappings.unlink()
    #     r = requests.get(
    #         "https://graph.facebook.com/v7.0/" + self.facebook_form_id,
    #         params={"access_token": self.access_token, "fields": "questions"},
    #     ).json()
    #     if r.get("error"):
    #         raise ValidationError(r["error"]["message"])
    #     if r.get("questions"):
    #         for question in r.get("questions"):
    #             self.env["crm.facebook.form.field"].create(
    #                 {
    #                     "form_id": self.id,
    #                     "name": question["label"],
    #                     "facebook_field": question["key"],
    #                     "odoo_field": self.env["crm.facebook.form.mapping"].search(
    #                         [("facebook_field", "=", question["key"])], limit=1
    #                     )
    #                     and self.env["crm.facebook.form.mapping"]
    #                     .search([("facebook_field", "=", question["key"])], limit=1)
    #                     .odoo_field.id
    #                     or "",
    #                 }
    #             )

    def action_guess_mapping(self):
        for rec in self:
            rec.mappings.action_guess_mapping()


class CrmFacebookFormField(models.Model):
    _name = "crm.facebook.form.field"
    _description = "Facebook form fields"

    form_id = fields.Many2one("crm.facebook.form", required=True, ondelete="cascade", string="Form")
    name = fields.Char()
    odoo_field = fields.Many2one(
        "ir.model.fields",
        domain=[
            ("model", "=", "crm.lead"),
            ("store", "=", True),
            (
                "ttype",
                "in",
                (
                    "char",
                    "date",
                    "datetime",
                    "float",
                    "html",
                    "integer",
                    "monetary",
                    "many2one",
                    "selection",
                    "phone",
                    "text",
                ),
            ),
        ],
        ondelete="set null",
        required=False,
    )
    facebook_field = fields.Char(required=True)

    def action_guess_mapping(self):
        for rec in self:
            mapping = self.env["crm.facebook.form.mapping"].search(
                [("facebook_field", "=", rec.facebook_field)], limit=1
            )
            if mapping:
                rec.odoo_field = mapping.odoo_field

    _sql_constraints = [
        ("field_unique", "unique(form_id, odoo_field, facebook_field)", "Mapping must be unique per form")
    ]


class CrmFacebookFormMapping(models.Model):
    _name = "crm.facebook.form.mapping"
    _description = "Default field mapping for new forms"

    odoo_field = fields.Many2one(
        "ir.model.fields",
        domain=[
            ("model", "=", "crm.lead"),
            ("store", "=", True),
            (
                "ttype",
                "in",
                (
                    "char",
                    "date",
                    "datetime",
                    "float",
                    "html",
                    "integer",
                    "monetary",
                    "many2one",
                    "selection",
                    "phone",
                    "text",
                ),
            ),
        ],
        ondelete="cascade",
        required=True,
    )
    facebook_field = fields.Char(required=True)

    _sql_constraints = [("map_unique", "unique(odoo_field, facebook_field)", "Default Mapping must be unique")]
