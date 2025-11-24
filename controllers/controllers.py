# -*- coding: utf-8 -*-
# from odoo import http


# class AcaTimetable(http.Controller):
#     @http.route('/aca_timetable/aca_timetable', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aca_timetable/aca_timetable/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aca_timetable.listing', {
#             'root': '/aca_timetable/aca_timetable',
#             'objects': http.request.env['aca_timetable.aca_timetable'].search([]),
#         })

#     @http.route('/aca_timetable/aca_timetable/objects/<model("aca_timetable.aca_timetable"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aca_timetable.object', {
#             'object': obj
#         })

