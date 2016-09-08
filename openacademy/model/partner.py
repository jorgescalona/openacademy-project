# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the rest partner model ....
    instructor = fields.Boolean('Instructor', default=False)

    session_ids = fields.Many2many('openacademy.session',
                                   string="Sessions as instructor", readonly=True)
