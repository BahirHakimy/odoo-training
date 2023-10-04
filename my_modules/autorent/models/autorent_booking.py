from odoo import fields, models, api


class AutoRentBooking(models.Model):
    _name = "autorent.booking"
    _description = "AutoRent Booking"
    _rec_name = "booking_number"

    booking_number = fields.Char(
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "generate.autorent.booking.sequence"
        ),
        readonly=True,
    )
    partner_id = fields.Many2one("res.partner", ondelete="cascade")
    car_id = fields.Many2one("autorent.car", ondelete="cascade")
    pick_up_location = fields.Char(string="Pick up location")
    drop_off_location = fields.Char(string="Drop off location")
    pick_up_date = fields.Datetime(string="Pick up date")
    drop_off_date = fields.Datetime(string="Drop off date")
    payment_type = fields.Selection(
        [
            ("days", "By Days"),
            ("distance", "By Distance"),
        ],
        string="Payment Type",
    )
    payment_amount = fields.Float(string="Payment Amount")
    currency_id = fields.Many2one(
        "res.currency", default=lambda self: self.env.company.currency_id
    )
    total_cost = fields.Monetary(
        compute="_compute_total_cost", string="Total Cost", store=True
    )
    state = fields.Selection(
        [
            ("idle", "Idle"),
            ("upcomming", "Upcomming"),
            ("active", "Active"),
            ("completed", "Completed"),
            ("canceled", "Canceled"),
        ]
    )

    @api.depends("payment_type", "payment_amount")
    def _compute_total_cost(self):
        for rec in self:
            if rec.payment_type == "days":
                rec.total_cost = rec.payment_amount * rec.car_id.price_per_day
            elif rec.payment_type == "distance":
                rec.total_cost = rec.payment_amount * rec.car_id.price_per_km
            else:
                rec.total_cost = 0

    def open_user(self):
        for rec in self:
            return {
                "name": "Autorent Booking Partner",
                "res_model": "res.partner",
                "res_id": rec.partner_id.id,
                "type": "ir.actions.act_window",
                "view_mode": "form",
            }

    def open_car(self):
        for rec in self:
            return {
                "name": "Autorent Car",
                "res_model": "autorent.car",
                "res_id": rec.car_id.id,
                "type": "ir.actions.act_window",
                "view_mode": "form",
            }
