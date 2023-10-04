from odoo import models, api, fields


class AutoRentSearchCar(models.TransientModel):
    _name = "autorent.search.car"
    _description = "AutoRent Search Car"

    pick_up_date = fields.Datetime(string="Pick up date")
    drop_off_date = fields.Datetime(string="Drop off date")

    def action_search(self):
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
