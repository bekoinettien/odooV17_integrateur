from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CategorieVehicule(models.Model):
    _name = 'categorie.vehicule'
    _description = 'Description'
    _parent_store = True
    _parent_name = "parent_id"
    parent_path = fields.Char(index=True)
    name = fields.Char('Categorie')
    parent_id= fields.Many2one('categorie.vehicule', ondelete='restrict',
                               string='Caregorie Mère',index=True)
    child_ids = fields.One2many(
        comodel_name='categorie.vehicule',
        inverse_name='parent_id',
        string='Sous-categorie',ondelete='restrict',
        required=True)
    @api.constrains('parent_id')
    def _check_hierarchy(self):
       if not self._check_recursion():
           raise models.ValidationError('ERREUR')

