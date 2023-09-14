# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Autorent(models.Model):
    _name = "autorent.autorent"
    _description = "autorent.autorent"

    name = fields.Char()
    description = fields.Text()


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
