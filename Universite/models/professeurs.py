# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteProfesseur(models.Model):
    _name = 'universite.professeur'
    matricule = fields.Char('Matricule')
    name = fields.Char('Nom')
    prenom = fields.Char('Prenoms')
    sexe = fields.Selection([('M', 'M'),('F', 'F')])
    adresse = fields.Text('Adresse')
    telephone = fields.Char('Telephone')
    email = fields.Char()
    date_nais = fields.Date('date de naissance')
    #chaque professeurs est affecte a un departement et chaque professeur a une matiere
    departement_id = fields.Many2one(comodel_name ='universite.departement')
        #chaque professeurs est affecte a une matiere
    matiere_ids = fields.Many2many(comodel_name ='universite.matiere' , string = 'matieres enseignees')
    classe_ids = fields.Many2many(comodel_name ='universite.classe', relation ='prof_classe_rel', column1='name', column2='c_name')

    #pour concatener un ensemble de nom qu'on souhaite on utilise la fonction name_get
    #dans notre cas nous allons definir le departement dans lequel le prof enseigne

    #@api.multi
    #def name_get(self):
        #result = []
        #for prof in self:
            #name = '[' + prof.departement_id.name + '] '  + prof.name + '' + prof.prenom
            #result.deppend((prof.id , name))
        #return result
