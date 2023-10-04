from odoo import models, api, fields


class AcceptReason(models.TransientModel):
    _name = "accept.reason"
    _description = "Accept Reason"

    reason = fields.Html()
    date = fields.Date(default=fields.Date.context_today)
    offer_id = fields.Many2one("estate.property.offer")
    property_id = fields.Many2one("estate.property")

    def action_accept(self):
        for rec in self:
            rec.property_id.write(
                {
                    "selling_price": rec.offer_id.price,
                    "buyer_id": rec.offer_id.partner_id.id,
                    "state": "offer_accepted",
                    "offer_accept_reason": rec.reason,
                }
            )
            rec.offer_id.status = "accepted"
