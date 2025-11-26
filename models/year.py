from odoo import models, fields, api


class Group(models.Model):
    _name = "aca_timetable.group"
    _description = "Group"

    _sql_constraints = [('unique_group_per_year_level', 'UNIQUE(name,year_level_id)',
                         'Group shoul be unique by year level')]

    name = fields.Char(required=True)

    year_level_id = fields.Many2one(
        'aca_timetable.year_level', string="Year Level", required=True)

    parent_id = fields.Many2one(
        'aca_timetable.group', string="Parent",
        required=False,
        domain=lambda self: [
            ('id', '!=', self.id)]

    )

    @api.model
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} - {record.year_level_id.display_name or ''}"

    # available_parents_ids = fields.Many2many(
    #     'aca_timetable.group',
    #     compute='_compute_available_parents',
    #     string='Available Parents'
    # )

    # @api.depends('year_level_id')
    # def _compute_available_parents(self):
    #     for rec in self:
    #         rec.available_parents_ids = self.search([
    #             ('year_level_id', '=', rec.year_level_id.id),
    #             ('id', '!=', rec.id)
    #         ])


class Level(models.Model):
    _name = "aca_timetable.level"
    _description = "Level"

    name = fields.Char(required=True)


class Speciality(models.Model):
    _name = "aca_timetable.speciality"
    _description = "Speciality"

    name = fields.Char(required=True)


class Year(models.Model):
    _name = 'aca_timetable.year'
    _description = 'aca_timetable.year'

    name = fields.Char(required=True)

    levels_ids = fields.One2many(
        'aca_timetable.year_level', 'year_id', string="Level")


class YearLevel(models.Model):
    _name = "aca_timetable.year_level"
    _description = "Year_Level"

    year_id = fields.Many2one('aca_timetable.year',
                              string="Year", required=True)
    level_id = fields.Many2one(
        'aca_timetable.level', string="Level", required=True)
    speciality_id = fields.Many2one(
        'aca_timetable.speciality', string="Speciality", required=True)

    group_ids = fields.One2many(
        'aca_timetable.group', 'year_level_id', string="Groups")

    @api.model
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.year_id.name or ''} - {record.level_id.name or ''} - {record.speciality_id.name or ''}"
