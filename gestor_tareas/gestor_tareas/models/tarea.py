from odoo import models, fields


class GestorTarea(models.Model):
    _name = 'gestor.tarea'
    _description = 'Tarea del gestor'

    name = fields.Char(string='Nombre', required=True)

    descripcion = fields.Text(string='Descripción')

    fecha_limite = fields.Date(string='Fecha límite')

    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string='Prioridad')

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('proceso', 'En proceso'),
        ('terminada', 'Terminada')
    ], string='Estado', default='pendiente')