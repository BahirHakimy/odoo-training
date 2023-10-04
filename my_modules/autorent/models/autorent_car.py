# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AutoRentCar(models.Model):
    _name = "autorent.car"
    _description = "AutoRent Car model"

    car_type_id = fields.Many2one("autorent.car.type")
    image = fields.Image(string="Image")
    model = fields.Char()
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id
    )
    price_per_day = fields.Monetary(string="Price per day")
    price_per_km = fields.Monetary(string="Price per km")
    number_of_seats = fields.Integer(string="Number of seats")
    availability = fields.Boolean(default=True)
    booking_id = fields.One2many("autorent.booking", inverse_name="car_id")
    description = fields.Text()

    def _compute_availability(self):
        for rec in self:
            if rec.price_per_day and rec.price_per_km:
                rec.availability = True
            else:
                rec.availability = False
