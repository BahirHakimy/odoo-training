from odoo import fields, api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    property_id = fields.Many2one("estate.property", ondelete="cascade")

    def open_property(self):
        for rec in self:
            return {
                "name": "Open Property",
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "estate.property",
                "res_id": rec.property_id.id,
            }
