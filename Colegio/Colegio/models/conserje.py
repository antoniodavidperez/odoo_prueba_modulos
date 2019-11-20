from odoo import models, fields, api

class Conserje(models.Model):
    _name = 'colegio.conserje'
    dni = fields.Char('DNI', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    antiguedad = fields.Integer('Antiguedad', required = True)