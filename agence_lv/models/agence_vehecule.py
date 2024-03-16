from odoo import api, fields, models
class AgenceVehicule(models.Model) :
    _name ="agence.vehicule"
    _description = "agence de location de vehicule"
    # _rec_name = 'designation_vehicule'
    marque_id = fields.Many2one(comodel_name='agence.marque',string='Marque',required=True)
    modele = fields.Char('Modèle', required=True)
    matricule = fields.Char('Matricule')
    designation_vehicule = fields.Char('Designation')
    date_achat = fields.Date('Date d Achat')
    chauffeur_ids = fields.Many2many('res.partner',string='Chauffeur')

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         # rec_name = "%s-%s-%s" % (record.marque_id, record.modele, record.matricule)
    #         result.append((record.id,rec_name))
    #     return result
    note = fields.Text('Note Interne', translate=True)
    state = fields.Selection([('new','Nouveau'),('fonctional','Fonctionnel'),('on_repair','En Reparation'),
                            ('declassed','Déclassé')], 'Etat', default="new")
    description = fields.Html('Description')
    image_v = fields.Binary('Image du vehicule')
    active = fields.Boolean('Active', default=True)
    veh_service = fields.Boolean('Vehicule en service?', default=False)
    nb_place = fields.Integer('Nombre de place', default=5)
    dern_kilometrage = fields.Float('Dernier kilometrage', digits=(14, 2),
                                    groups='base.group_user', #droit d'acces a ce champs
                                    states={'on_repair': [('readonly',True)],#mode lectuer seul si la voiture est en reparation
                                            'declassed': [('invisible',True)]},# invisible si la voiture est declasse
                                    help='Mettez ici le dernier kilometrage')
    prix_achat_v = fields.Float('Prix Achat')
    currency_id = fields.Many2one('res.currency', string='Symbole Monetaire')
    prix_vente_v = fields.Monetary('Prix de vente', digits='Prix vehicule', currency_field='currency_id')
    #Contrainte avec la base de donnée SQL
    _sql_constraints = [
        ('mat_uniq', 'UNIQUE(matricule)',#permet au vehicule d'avoir un matricule UNIQUE
         'Les matricules doivent etre unique'),
        ('nb_place' , 'CHECK(nb_place<=5)',#permet de verifier le nombre de place
         'le nombre de place ne doit pas depassés 5 ')
    ]
    @api.constrains('date_achat')
    def _check_date_achat(self):
        for record in self:
            if record.date_achat and record.date_achat>fields.Date.today():
                raise models.ValidationError('La date d achat ne doit pas depassée la date du jours')

