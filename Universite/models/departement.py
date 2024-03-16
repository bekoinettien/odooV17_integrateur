# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteDepartement(models.Model):
    _name = 'universite.departement'
    code = fields.Char('Code')
    name = fields.Char('Libelle')
    professeur_ids = fields.One2many(comodel_name='universite.professeur' , inverse_name ='departement_id')
    etudiant_ids = fields.One2many(comodel_name='universite.etudiant' , inverse_name ='departement_id')
