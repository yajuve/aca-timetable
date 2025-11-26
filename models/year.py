from odoo import models, fields, api


class Year(models.Model):
    _name = 'aca_timetable.year'
    _description = 'aca_timetable.year'

    name = fields.Char()
