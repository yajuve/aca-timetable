from odoo import models, fields, api


class Timetable(models.Model):
    _name = 'aca_timetable.timetable'
    _description = 'aca_timetable.timetable'

    year_id = fields.Many2one(
        "aca_timetable.year", string="Year", required=True)

    program_id = fields.Many2one(
        "aca_timetable.program", string="Program", required=True)
    
    @api.model
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.program_id.name or ''} {record.year_id.name or ''}"
