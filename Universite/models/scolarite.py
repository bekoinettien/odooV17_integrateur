# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteScolarite(models.Model):
    _name = 'universite.scolarite'
    _description = 'Paiement de la scolarité'

    etudiant_id = fields.Many2one('universite.etudiant', string='Étudiant', required=True)
    amount = fields.Float(string='Montant du paiement', required=True)
    payment_date = fields.Date(string='Date du paiement', default=fields.Date.today())
    payment_method = fields.Selection([
        ('cheque', 'Chèque'),
        ('virement', 'Virement bancaire'),
        ('espece', 'Espèces'),
    ], string='Méthode de paiement', default='espece')

    @api.model
    def create(self, values):
        # Vous pouvez ajouter des validations ou des logiques supplémentaires ici
        return super(ScolaritePayment, self).create(values)
