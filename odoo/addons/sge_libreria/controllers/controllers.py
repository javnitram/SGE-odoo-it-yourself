# -*- coding: utf-8 -*-
# from odoo import http


# class SgeLibreria(http.Controller):
#     @http.route('/sge_libreria/sge_libreria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sge_libreria/sge_libreria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sge_libreria.listing', {
#             'root': '/sge_libreria/sge_libreria',
#             'objects': http.request.env['sge_libreria.sge_libreria'].search([]),
#         })

#     @http.route('/sge_libreria/sge_libreria/objects/<model("sge_libreria.sge_libreria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sge_libreria.object', {
#             'object': obj
#         })

