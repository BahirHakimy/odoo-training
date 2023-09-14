from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tags"

    name = fields.Char(required=True)
    color = fields.Integer()

    _sql_constraints = [("unique_name", "UNIQUE(name)", "This tag already exists.")]

    _order = "name"
