# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Universite',
    'version': '1.2',
    'category': 'crm',
    'sequence': -100,
    'summary': '',
    'description': "",
    'website': 'https://www.odoo.com/app',
    'depends': [
        'web', 'base_setup', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'security/bekoin_security.xml',
        'views/etudiant.xml',
        'views/professeurs.xml',
        'views/departement.xml',
        'views/matiere.xml',
        'views/classe.xml',
        'views/scolarite.xml',
        'views/note.xml',
        'views/paiement.xml',
        'menus/classe.xml',
        'menus/departement.xml',
        'menus/matiere.xml',
        'menus/etudiant.xml',
        'menus/professeur.xml',
        'menus/scolarite.xml',




    ],

    'demo': [

    ],

    # 'web.assets_qweb': [
    # ],
    'qweb':[],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,

}
