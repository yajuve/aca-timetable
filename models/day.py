from odoo import models, fields, api


class Day(models.Model):
    _name = 'aca_timetable.day'
    _description = 'aca_timetable.day'

    name = fields.Char()
