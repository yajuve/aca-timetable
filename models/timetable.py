from odoo import models, fields, api


class Timetable(models.Model):
    _name = 'aca_timetable.timetable'
    _description = 'aca_timetable.timetable'

    year_id = fields.Many2one(
        "aca_timetable.year", string="Year", required=True, tracking=True)
