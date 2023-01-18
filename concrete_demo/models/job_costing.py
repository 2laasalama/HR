# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class JobCosting(models.Model):
    _inherit = "job.costing"

    details_ids = fields.One2many('job.costing.details', 'costing_id', string='Details')


class JobCostingDetails(models.Model):
    _name = "job.costing.details"

    costing_id = fields.Many2one('job.costing')
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
