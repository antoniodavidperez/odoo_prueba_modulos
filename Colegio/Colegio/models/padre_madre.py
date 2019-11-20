from odoo import models, fields, api

class PadreMadre(models.Model):
    _name = 'colegio.padre_madre'
    dni = fields.Char('DNI', required = True)
    nombreHijo = fields.Char('Nombre del hijo matriculado', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)