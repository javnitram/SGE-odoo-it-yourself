# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Categoria(models.Model):
    _name = 'sge_libreria.categoria'
    _description = 'Categoria'

    name = fields.Char('Categoria', required=True, help='Introduzca un nombre de categoria')
    description = fields.Char('Descripcion', help='Introduzca la descripcion')
    
