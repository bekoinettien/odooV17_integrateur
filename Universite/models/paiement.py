# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversitePaiement(models.Model):
    _name = 'universite.paiement'
    _description = 'Payment Details'

    etudiant_id = fields.Many2one('universite.etudiant', string='etudiant', required=True)
    amount = fields.Float(string='Amount', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    paid_date = fields.Date(string='Paid Date')
    remaining_amount = fields.Float(string='Remaining Amount', compute='_compute_remaining_amount', store=True)
    matricule = fields.Char(string='Matricule')
    name = fields.Char(string='Name', required=True)
    prenom = fields.Char(string='Prenom')
    telephone = fields.Char(string='Telephone')
    date_ins = fields.Date(string='Date Inscription', default=fields.Date.today())

    @api.depends('amount', 'paid_date')
    def _compute_remaining_amount(self):
        for paiement in self:
            if paiement.paid_date:
                paiement.remaining_amount = 0.0
            else:
                paiement.remaining_amount = paiement.amount

    def mark_as_paid(self):
        for paiement in self:
            paiement.write({'paid_date': fields.Date.today()})

            # Appel de la fonction pour obtenir les informations de l'étudiant
            etudiant_info = paiement.etudiant_id.get_student_info()
            payment.write({
                'matricule': paiement.etudiant_id.matricule,
                'name': etudiant_info['name'],
                'prenom': etudiant_info['prenom'],
                'telephone': etudiant_info['telephone'],
                'date_ins': etudiant_info['date_ins'],
                'total_paid': etudiant_info['total_paid'],
                'remaining_amount': etudiant_info['remaining_amount'],
            })
