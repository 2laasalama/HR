# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    sizes_ids = fields.One2many('project.task.sizes', 'task_id', string='Sizes')


class ProjectTaskSizes(models.Model):
    _name = "project.task.sizes"

    task_id = fields.Many2one('project.task')
    size = fields.Selection([('small', 'Small'),
                             ('medium', 'Medium'),
                             ('large', 'Large'),
                             ('x', 'X-Large'),
                             ('2x', '2X-Large'),
                             ('3x', '3X-Large'),
                             ('4x', '4X-Large'),
                             ('5x', '5X-Large'),
                             ('6x', '6X-Large')], default='small')
    amount = fields.Integer()
