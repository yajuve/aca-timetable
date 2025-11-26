from odoo import models, fields, api


class TimetableLine(models.Model):
    _name = 'aca_timetable.timetableline'
    _description = 'aca_timetable.timetableline'

    _sql_constraints = [
        ('unique_room', 'UNIQUE(room_id, hour_id, day_id)',
         'One room for one day for one hour'),

        ('unique_group', 'UNIQUE(group_id, hour_id, day_id)',
         'A group should not have two sessions in the same time'),
    ]

    # timetable_id = fields.Many2one(
    #     "aca_timetable.timetable", string="Timetable", required=True, tracking=True)
    room_id = fields.Many2one(
        "aca_timetable.room", string="Room", required=True)
    hour_id = fields.Many2one(
        "aca_timetable.hour", string="Hour", required=True)
    day_id = fields.Many2one(
        "aca_timetable.day", string="Day", required=True)
    group_id = fields.Many2one(
        "aca_timetable.group", string="Group", required=True)
