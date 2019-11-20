from odoo import models, fields, api

class Aula(models.Model):
    _name = 'colegio.aula'
    planta = fields.Char('Planta', required = True)
    piso = fields.Char('Piso', required = True)
    letra = fields.Char('Letra', required = True)
    asignatura = fields.Integer('Asignatura', required = True)