from odoo import models, fields, api


class Hour(models.Model):
    _name = 'aca_timetable.hour'
    _description = 'aca_timetable.hour'

    name = fields.Char(required=True)
    desc = fields.Char(required=True)
