# -*- coding: utf-8 -*-
# from odoo import http


# class IvgMoviles(http.Controller):
#     @http.route('/ivg_moviles/ivg_moviles', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ivg_moviles/ivg_moviles/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ivg_moviles.listing', {
#             'root': '/ivg_moviles/ivg_moviles',
#             'objects': http.request.env['ivg_moviles.ivg_moviles'].search([]),
#         })

#     @http.route('/ivg_moviles/ivg_moviles/objects/<model("ivg_moviles.ivg_moviles"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ivg_moviles.object', {
#             'object': obj
#         })

