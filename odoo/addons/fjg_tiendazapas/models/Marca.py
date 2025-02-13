# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Marca(models.Model):
    _name = 'fjg_tiendazapas.marca'
    _description = 'Marca'

    name = fields.Char('Marca', required=True, help='Introduzca un nombre de la marca')
    description = fields.Char('Descripcion', help='Introduzca la descripcion') 
