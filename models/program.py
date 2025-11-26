from odoo import models, fields, api


class Program(models.Model):
    _name = 'aca_timetable.program'
    _description = 'aca_timetable.program'

    name = fields.Char()