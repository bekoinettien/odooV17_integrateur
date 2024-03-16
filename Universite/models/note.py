# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api, tools
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _
import logging

class UniversiteNote(models.Model):
    _name ='universite.note'
    _description ='enregistrement des notes etudiants'
    libelle = fields.Selection([('Int', 'Interrogation'),('Dev', 'Devoir'),('Exam', 'Examen')])
    note = fields.Float(string='Note')
    coeff = fields.Float(string='coefficients')
    note_coefficiente = fields.Float(string='note coefficiente', compute='_compute_note_coefficiente')
    etudiant_id = fields.Many2one(comodel_name ='universite.etudiant')
    matiere_id = fields.Many2one(comodel_name ='universite.matiere')
    professeur_id = fields.Many2one(comodel_name ='universite.professeur')



    @api.depends('note', 'coeff')
    def _compute_note_coefficiente(self):
        for record in self:
            # Votre logique de calcul ici
            note_coefficiente = record.note * record.coeff
            record.note_coefficiente = note_coefficiente
