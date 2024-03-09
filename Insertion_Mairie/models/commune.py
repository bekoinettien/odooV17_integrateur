# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class InsertionCommune(models.Model):
    _name = 'insertion.commune'
    _description = 'insertion des communes'
    code = fields.Char('Code')
    libelle = fields.Char('Libelle')
