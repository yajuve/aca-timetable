from odoo import models, fields, api


class TimetableLine(models.Model):
    _name = 'aca_timetable.timetableline'
    _description = 'aca_timetable.timetableline'

    room_id = fields.Many2one(
        "aca_timetable.room", string="Room", required=True, tracking=True)
    hour_id = fields.Many2one(
        "aca_timetable.hour", string="Hour", required=True, tracking=True)
    day_id = fields.Many2one(
        "aca_timetable.day", string="Day", required=True, tracking=True)
