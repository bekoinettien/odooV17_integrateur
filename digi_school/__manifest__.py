{
    'name': 'Digi_school',
    'version': '0.1',
    'summary': 'Summery',
    'description': 'Description',
    'sequence': '2',
    'category': 'Category',
    'author': 'BEKOIN ETIENNE',
    'website': 'Website',
    #'license': 'License',
    'depends': ['base'],
    'data': [
             'security/groups.xml',
             'security/ir.model.access.csv',
             'views/course.xml',
             'views/session.xml'
    ],
   # 'demo': ['Demo'],
    'installable': True,
    'auto_install': False,
    'application': True
}
