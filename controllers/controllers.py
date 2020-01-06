# -*- coding: utf-8 -*-
from odoo import http

# class NpwpPartner(http.Controller):
#     @http.route('/npwp_partner/npwp_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/npwp_partner/npwp_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('npwp_partner.listing', {
#             'root': '/npwp_partner/npwp_partner',
#             'objects': http.request.env['npwp_partner.npwp_partner'].search([]),
#         })

#     @http.route('/npwp_partner/npwp_partner/objects/<model("npwp_partner.npwp_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('npwp_partner.object', {
#             'object': obj
#         })