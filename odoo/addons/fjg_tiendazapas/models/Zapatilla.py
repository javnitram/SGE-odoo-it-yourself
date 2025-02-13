# -*- coding: utf-8 -*-

from odoo import models, fields

class Zapatilla(models.Model):
    _name = 'fjg_tiendazapas.zapatilla'
    _description = 'zapatilla'
    
    name = fields.Char('Nombre',required=True)
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Cantidad')
    fecha_compra = fields.Date('Fecha de compra')
    segmano = fields.Binary('Segunda mano')
    estado = fields.Selection([
        ('0', 'CasiNuevo'),
        ('1', 'SemiNuevo'),
        ('2', 'Bastane usadas'),
    ], string='Estado', default='0')