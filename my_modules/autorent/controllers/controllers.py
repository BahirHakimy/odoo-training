# -*- coding: utf-8 -*-
# from odoo import http


# class Autorent(http.Controller):
#     @http.route('/autorent/autorent', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autorent/autorent/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('autorent.listing', {
#             'root': '/autorent/autorent',
#             'objects': http.request.env['autorent.autorent'].search([]),
#         })

#     @http.route('/autorent/autorent/objects/<model("autorent.autorent"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autorent.object', {
#             'object': obj
#         })
