# -*- coding: utf-8 -*-
from odoo import http

# class Reparator(http.Controller):
#     @http.route('/reparator/reparator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reparator/reparator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reparator.listing', {
#             'root': '/reparator/reparator',
#             'objects': http.request.env['reparator.reparator'].search([]),
#         })

#     @http.route('/reparator/reparator/objects/<model("reparator.reparator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reparator.object', {
#             'object': obj
#         })