from odoo import models, fields

class Movil(models.Model):
    _name = 'ivg_moviles_movil'
    _description = 'Movil'

    marca = fields.Char('Marca',required=True)
    modelo = fields.Char('Modelo',required=True)
    precio = fields.Float('Precio')
    ram = fields.Integer('RAM')
    almacenamiento = fields.Integer('Fecha de compra')
    pantalla = fields.Char('Pantalla')
    camara = fields.Char('Camara')
    procesador = fields.Char('Procesador')
    
    