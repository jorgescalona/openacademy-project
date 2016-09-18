#/usr/bin/env python
# -*- coding:utf-8 -*-

from psycopg2 import IntegrityError
from openerp.tests.common import TransactionCase
from openerp.tools import mute_logger

class GlobalOpenacademyCourse(TransactionCase):

    '''
    Global test to openacademy course model.
    Test create courses and trigger constraints.
    '''
    def setUp(self):
        # define global variables to test methods
        super(GlobalOpenacademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    # Method of class that don't is test
    def create_course(self, course_name, course_description,
                      course_responsible_id):
        # create a course with parameters receiver
        course_id = self.course.create({
            'name' : course_name,
            'description' : course_description,
            'responsible_id' : course_responsible_id,
        })
        return course_id

    # Method of test startswitch 'def test_*(self):'
    @mute_logger('openerp.sql_db')
    def test_01_same_name_description(self):
        '''
        Test create a course with a same name & description.
        To test constraint of name different to description.
        '''
        # Error raised expected with message expected.

        # Mute error openerp sql_db to don't to avoid in log
        with self.assertRaisesRegexp(
            IntegrityError,
            'new row for relation "openacademy_course" violates'
            ' check constraint "openacademy_course_name_description_check"'
        ):
            # create a course with same name & description to raise error
            self.create_course('test','test', None)

