from odoo import models, fields

class Movil(models.Model):
    _name = 'ivg_moviles.cliente'
    _description = 'Clientes'

    name = fields.Char('Nombre',required=True)
    apellidos = fields.Char('Apellidos',required=True)
    correo = fields.Char('Correo')
    telefono = fields.Integer('Telefono')
