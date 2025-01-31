# -*- coding: utf-8 -*-
# from odoo import http


# class SgLibreria(http.Controller):
#     @http.route('/sg_libreria/sg_libreria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sg_libreria/sg_libreria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sg_libreria.listing', {
#             'root': '/sg_libreria/sg_libreria',
#             'objects': http.request.env['sg_libreria.sg_libreria'].search([]),
#         })

#     @http.route('/sg_libreria/sg_libreria/objects/<model("sg_libreria.sg_libreria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sg_libreria.object', {
#             'object': obj
#         })

