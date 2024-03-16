# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteEtudiant(models.Model):
    _name = 'universite.etudiant'
    matricule = fields.Char('Matricule', required=True)
    name = fields.Char('Nom')
    prenom = fields.Char('Prenoms')
    sexe = fields.Selection([('M', 'M'),('F', 'F')])
    adresse = fields.Text('Adresse')
    telephone = fields.Char('Telephone')
    email = fields.Char()
    date_nais = fields.Date('date de naissance')
    date_ins = fields.Date('date inscrit')
    state = fields.Selection([('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3'), ('M1', 'Master 1') , ('M2', 'Master 2'), ('Ter', 'Terminer')], string='State', default='L1')
    paiement = fields.One2many('universite.paiement', 'etudiant_id', string='paiements')
    #chaque etudiants est affecte a un departement/mais un departement recois plusieurs etudiant
    departement_id = fields.Many2one(comodel_name ='universite.departement')
    #chaque etudiants est affecte a une classe/mais une classe recois plusieurs etudiant
    classe_id = fields.Many2one(comodel_name ='universite.classe')
    matiere_ids = fields.Many2many(related='classe_id.matiere_ids')

    def get_etudiant_info(self):
        etudiant = self.search([('matricule', '=', self.matricule)], limit=1)
        if not etudiant:
            raise UserError("No student found with this registration number.")
        return {
            'name': etudiant.name,
            'prenom': etudiant.prenom,
            'telephone': etudiant.telephone,
            'date_ins': student.date_ins,
            'total_paid': sum(paiement.amount for paiement in etudiant.paiements if paiement.paid_date),
            'remaining_amount': sum(paiement.remaining_amount for paiement in etudiant.paiements),
        }

    @api.constrains('date_nais', 'date_ins')
    def __comparaison_date(self):
        if self.date_ins < self.date_nais :
            raise ValidationError("La date de naissance ne doit pas etre superieur a la date inscrite")
            # {
            #     'name': _("date incorrecte"),
            #     'message': _("La date de naissance ne doit pas etre superieur a la date inscrite"),
            # })
    #@api.multi
    def suivant(self):
        self.ensure_one()
        if self.state == 'L1':
            return self.write({'state' : 'L2'})
        elif self.state == 'L2':
            return self.write({'state' : 'L3'})
        elif self.state == 'L3':
            return self.write({'state' : 'M1'})
        elif self.state == 'M1':
            return self.write({'state' : 'M2'})
        elif self.state == 'M2':
            return self.write({'state' : 'Ter'})
        else:
            raise ValidationError("l'etudiant a termimé son cursus")
