{
    'name': 'Gestor de Tareas',
    'version': '1.0',
    'summary': 'Modulo para gestionar tareas',
    'description': 'Permite crear y gestionar tareas en Odoo.',
    'author': 'Alexis Xavier Cansino Rodriguez',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tarea_views.xml',
    ],
    'installable': True,
    'application': True,
}