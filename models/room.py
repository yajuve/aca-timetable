from odoo import models, fields, api


class Room(models.Model):
    _name = 'aca_timetable.room'
    _description = 'aca_timetable.room'

    name = fields.Char()
