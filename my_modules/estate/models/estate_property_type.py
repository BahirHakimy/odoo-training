from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property types"

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "id")
    sequence = fields.Integer("Sequence", default=1)
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offers_count = fields.Integer(compute="_compute_offers_count")

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "This property type already exists.")
    ]

    _order = "sequence, name"

    def open_offers(self):
        
        for rec in self:
            return {
                "name": "Type Offers",
                "type": "ir.actions.act_window",
                "res_model": "estate.property.offer",
                "view_mode": "tree,form",
                "domain": [("property_type_id", "=", rec.id)],
            }

    @api.depends("offer_ids")
    def _compute_offers_count(self):
        for rec in self:
            rec.offers_count = len(rec.offer_ids)
