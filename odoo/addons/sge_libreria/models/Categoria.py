# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    _name = 'sge_libreria.categoria' #ivg_cine.categoriaqsea
    _description = 'Categoria' 

    name = fields.Char('Categoria',required=True, help='Introduzca nombre de categoria')
    description = fields.Char('Descripción', help='Introduzca descripción')


    
    