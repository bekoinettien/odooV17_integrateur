from odoo import fields, models, api

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'chauffeur'
    vehicules_autorises_ids = fields.Many2many(comodel_name='agence.vehicule',
                                               string='Vehicules_autorises',
                                               relation='library_book_res_partner_rel')



