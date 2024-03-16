# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteMatiere(models.Model):
    _name = 'universite.matiere'
    code = fields.Char('Code')
    name = fields.Char('Libelle')
    #chaque matiere est affecte a un departement
    departement_id = fields.Many2one(comodel_name ='universite.departement')
    #professeur_ids = fields.One2many(comodel_name='universite.professeur' , inverse_name ='matiere_id')
    # professeur_ids = fields.Many2many(comodel_name ='universite.professeur')
    # # , relation ='mat_prof_rel', column1='m_name', column2='name')
