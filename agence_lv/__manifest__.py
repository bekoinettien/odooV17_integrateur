{
    'name': 'Agence de location de vehicule',
    'sequence': '1',
    'version': '0.1',
    'summary': 'Summery',
    'description': 'Description',
    'category': 'Category',
    'author': 'BEKOIN ETTIEN',
    'website': 'Website',
    #'license': 'License',
    'depends': ['base'],
    'data': [
        #'Data'
        #'security/groups.xml',
        'security/ir.model.access.csv',
        'views/agence_vehicule.xml',
        'views/marque.xml',
        #'views/conducteur.xml'
    ],
    'demo': ['Demo'],
    'installable': True,
    'auto_install': False,
    'application': True
}
