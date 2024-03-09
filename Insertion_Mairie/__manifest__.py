# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Insertion des jeunes',
    'version': '1.2',
    'category': 'crm',
    'sequence': 0,
    'summary': '',
    'description': "",
    'website': 'https://www.odoo.com/app',
    'depends': [
        'web', 'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'security/bekoin_security.xml',
        'views/jeune.xml',
        'views/commune.xml',
        # 'views/partenaire.xml',
        # 'views/projet.xml',
        # 'views/rehabilitation.xml',
        # 'views/inserer.xml',
        'menus/jeune.xml',
        'menus/commune.xml',
        # 'menus/projet.xml',
        # 'menus/rehabilitation.xml',
        # 'menus/inserer.xml',
        # 'menus/partenaire.xml',




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
