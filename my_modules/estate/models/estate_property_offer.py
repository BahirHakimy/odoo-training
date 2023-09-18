from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _rec_name = "partner_id"

    price = fields.Float()
    status = fields.Selection(
        [("accepted", "Accepted"), ("refused", "Refused")], copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", ondelete="cascade", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Datetime(
        compute="_compute_date_deadline", inverse="_inverse_date_deadline"
    )
    property_type_id = fields.Many2one(related="property_id.property_type_id")
    _sql_constraints = [
        ("check_price", "CHECK(price >= 0)", "An offer price must be strictly positive")
    ]

    _order = "price desc"

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = False
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(
                    days=record.validity
                )

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date).days

    def action_accept(self):
        for record in self:
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id.id

    def action_refuse(self):
        for record in self:
            record.status = "refused"

    @api.model
    def create(self, vals):
        price = vals["price"]
        property_id = vals["property_id"]
        property = self.env["estate.property"].browse(property_id)
        if price < property.best_price:
            raise ValidationError(
                "The price mush be higher than {0}".format(property.best_price)
            )

        res = super(EstatePropertyOffer, self).create(vals)

        if property.state != "offer_received":
            property.state = "offer_received"

        return res
