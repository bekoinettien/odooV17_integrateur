
from odoo import fields, models
class DigiSchool(models.Model) :
    _name = 'digischool.digischool'
    _description = 'gestion ecole'
    name = fields.Char('code')
    description = fields.Char('libelle')
    responsible = fields.Many2one(
        comodel_name="res.partner",
        string='Responsible',
        required=True)
