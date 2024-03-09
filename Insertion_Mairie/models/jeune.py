# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class InsertionJeune(models.Model):
    _name ='insertion.jeune'
    _description ='insertion des jeunes'
    name = fields.Char('Nom & Prenoms')
    sexe = fields.Selection([('M', 'M'),('F', 'F')])
    adresse = fields.Text('Adresse')
    telephone = fields.Char('Telephone')
    email = fields.Char()
    date_nais = fields.Date('date de naissance')
    date_ins = fields.Date('date inscrit')
