from odoo import fields, models, api

class Sessions(models.Model):
    _name = 'sessions.sessions'
    _description = 'gestion cdes sessions'
    date_debut = fields.Date(string='Date du début', required=True)
    date_fin = fields.Date(string='Date fin', required=True)
    duree = fields.Float(string='Durée')
    nb_place = fields.Integer(string='Nombre de place')
    course_id = fields.Many2one(comodel_name='course.course',string='Cours',required=True)
    instructeur_id = fields.Many2one(comodel_name='res.partner',string='Instructeur', required=True)

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = "%s - %s" % (record.course_id, record.instructeur_id)  # Format personnalisé pour le nom
    #         result.append((record.id, name))
    #     return result