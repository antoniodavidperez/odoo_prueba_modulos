from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'colegio.profesor'
    dni = fields.Char('DNI', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    edad = fields.Integer('Edad', required = True)
    asignatura = fields.Char('Asignatura', required = True)