# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteClasse(models.Model):
    _name = 'universite.classe'
    #l'attribut _rec_name permet d'afficher le nom qu'on souhaite dans l'indicaction de l'enregistrement
    _rec_name = 'c_name'
    _inherit ='mail.thread'
    code = fields.Char('Code')
    c_name = fields.Char('Libelle')
    prix = fields.Integer('Prix')
    etudiant_ids = fields.One2many(comodel_name='universite.etudiant' , inverse_name ='classe_id')
    professeur_ids = fields.Many2many(comodel_name ='universite.professeur', relation ='classe_prof_rel', column1='c_name', column2='name')
    matiere_ids = fields.Many2many(comodel_name ='universite.matiere', relation ='classe_mat_rel', column1='c_name', column2='m_name')

    num_prof = fields.Integer(string='Nombre de professeur' , compute='compt_prof')
    num_etud = fields.Integer(string="Nombre d'etudiant" , compute='compt_etud')
    num_mat = fields.Integer(string='Nombre de matiere' , compute='compt_mat')
#ces trois fonctions permettent de calculer le nombre d'enregistrement de chaque champs
    def compt_prof(self):
        self.num_prof= len(self.professeur_ids)

    def compt_etud(self):
        self.num_etud= len(self.etudiant_ids)

    def compt_mat(self):
        self.num_mat= len(self.matiere_ids)
#api.onchange:  cette option permet de conditionner le nombre total etudiant que cette classe doit ocuper
    @api.onchange('etudiant_ids')
    def _check_etudiant(self):
        if len(self.etudiant_ids) > 30 :
            return {'warnig': {'title': 'Erreur',
                              'message': 'Le nombre total des etudiants est atteint dans cette classe!!'}}


class CahierAppel(models.Model):
    _name = 'cahier.appel'

    date_du_jour = fields.Date('Date du jour')
    heure_debut = fields.Datetime('Heure début', widget='time')
    heure_fin = fields.Datetime('Heure fin', widget='time')
    signature_prof = fields.Binary('Signature professeur')
    classe_id = fields.Many2one('universite.classe' , 'Classe')
    etudiants_ids = fields.Many2many('universite.etudiant', 'cahier_appel_etudiant_rel', 'cahier_appel_id', 'etudiant_id', 'Liste des etudiants', default=lambda self: self.env['universite.etudiant'].search([('id', '!=', 1)]))

    # @api.constrains("heure_debut" , "heure_fin")
    # def check_date(self):
    #     for record in self:
    #         if record.heure_fin < record.heure_debut:
    #             raise ValidationError(_("Date de fin est inferieur a la date du debut"))


    @api.constrains("heure_debut", "heure_fin")
    def check_date(self):
        for record in self:
            if record.heure_fin < record.heure_debut:
                raise ValidationError({
                    'name': _("Heure incorrecte"),
                    'message': _("Date de fin est inférieure à la date du début"),
                })
