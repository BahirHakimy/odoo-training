from odoo import fields, models, api


class AutoRentCarType(models.Model):
    _name = "autorent.car.type"
    _description = "Auto Rent Car Type"

    name = fields.Char()
