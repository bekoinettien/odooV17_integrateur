from odoo import fields, models, api


class Course(models.Model):
    _name = 'course.course'
    _description = 'Description'

    name = fields.Char("CODE")
    designation = fields.Char("LIBELLE")
    responsable_id = fields.Many2one(comodel_name='res.users',string='Responsable',required=True)
    active = fields.Boolean(string='Active', required=True)
    sessions_ids = fields.One2many( comodel_name='sessions.sessions', inverse_name='course_id', string='Sessions',required=True)


