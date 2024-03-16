# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging


class UniversitePersonnel(models.Model):
    _name = "universite.personnel"

    matricule = fields.Char('Matricule')
    name = fields.Char("Nom")
    prenom = fields.Char("Prenoms")
    sexe = fields.Selection([('m', 'M'),('f', 'F')])
    fonction = fields.Selection([('comptable', 'Comptable'),('secretaire', 'Secretaire'),('educ', 'Educateur/Educatrice')])
    adresse = fields.Text('Adresse')
    telephone = fields.Char('Telephone')
    email = fields.Char()
    date_nais = fields.Date('Date de naissance')
