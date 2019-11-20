from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'colegio.alumno'
    numeroMatricula = fields.Integer('Numero de matrícula', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    edad = fields.Integer('Edad', required = True)