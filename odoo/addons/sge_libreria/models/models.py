# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sge_libreria(models.Model):
#     _name = 'sge_libreria.sge_libreria'
#     _description = 'sge_libreria.sge_libreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

