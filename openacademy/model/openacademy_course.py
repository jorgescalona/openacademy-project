# -*- coding: utf-8 -*-
'''
This module create model of Course
'''

from openerp import models, fields, api


class Course(models.Model):
    '''
    This class create model Course
    '''
    _name = 'openacademy.course'  # Model odoo name

    name = fields.Char(string='Title', required=True)
    # field reserved to identified rec_name
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible",
                                     index=True)
    session_ids = fields.One2many('openacademy.session',
                                  'course_id', string="Sessions")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique', 'UNIQUE(name)',
         "The course title must be unique"),
    ]
