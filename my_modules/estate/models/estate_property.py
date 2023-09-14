# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_is_zero, float_compare
from odoo.exceptions import ValidationError
from datetime import date, timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availbility = fields.Date(
        copy=False, default=lambda self: date.today() + timedelta(days=90)
    )
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    seller_id = fields.Many2one(
        "res.users", string="Salesman", default=lambda self: self.env.user.id
    )
    buyer_id = fields.Many2one("res.partner")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    best_price = fields.Float(compute="_compute_best_price")
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")]
    )
    total_area = fields.Integer(compute="_compute_total_area")
    active = fields.Boolean(default=False)
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        default="new",
    )

    _sql_constraints = [
        (
            "check_expected_price",
            "CHECK(expected_price >= 0)",
            "The expected price must be strictly positive",
        ),
        (
            "check_selling_price",
            "CHECK(selling_price >= 0)",
            "The selling price must be strictly positive",
        ),
    ]

    _order = "id desc"

    @api.depends("living_area", "total_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = False
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_orientation = "north"
            self.garden_area = 10
        else:
            self.garden_orientation = False
            self.garden_area = False

    def action_sold(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("Canceled properties cannot be sold")
            record.state = "sold"

    def action_cancel(self):
        for record in self:
            if record.state == "sold":
                raise UserError("You cannot cancel already sold properties")
            record.state = "canceled"

    @api.constrains("selling_price", "expected_price")
    def _check_selling_price(self):
        for record in self:
            if float_is_zero(record.selling_price, precision_digits=2):
                pass
            elif (
                float_compare(
                    record.selling_price,
                    0.9 * record.expected_price,
                    precision_digits=2,
                )
                < 0
            ):
                raise ValidationError(
                    "The selling_price must be at least 90% of expected price"
                )
