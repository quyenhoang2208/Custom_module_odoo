# -*- coding: utf-8 -*-
from odoo import http

# class SeatekMrpReport(http.Controller):
#     @http.route('/seatek_mrp_report/seatek_mrp_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seatek_mrp_report/seatek_mrp_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seatek_mrp_report.listing', {
#             'root': '/seatek_mrp_report/seatek_mrp_report',
#             'objects': http.request.env['seatek_mrp_report.seatek_mrp_report'].search([]),
#         })

#     @http.route('/seatek_mrp_report/seatek_mrp_report/objects/<model("seatek_mrp_report.seatek_mrp_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seatek_mrp_report.object', {
#             'object': obj
#         })