from odoo import fields, models, api
#
#
class AgenceMarque(models.Model):
   _name = 'agence.marque'
   _description = 'les marques de vehicule'
   name = fields.Char('Nom de la marque')
   logo = fields.Binary('logo')
   vehicules_ids = fields.One2many(comodel_name='agence.vehicule',inverse_name='marque_id',string='Vehicule de cette marque',required=True)
