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
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    # Method of test startswitch 'def test_*(self):'
    @mute_logger('openerp.sql_db')
    def test_10_same_name_description(self):
        '''
        Test create a course with a same name & description.
        To raise constraint of name different to description.
        '''
        # Error raised expected with message expected.

        # Mute error openerp sql_db to don't to avoid in log
        with self.assertRaisesRegexp(
            IntegrityError,
            'new row for relation "openacademy_course" violates'
            ' check constraint "openacademy_course_name_description_check"'
        ):
            # create a course with same name & description to raise error
            self.create_course('test', 'test', None)

    @mute_logger('openerp.sql_db')
    def test_20_two_course_same_name(self):
        '''
        Test for create two course same name.
        To raise constraint of unique name.
        '''
        self.create_course('test1', 'test_description', None)
        # print "new_id: ", new_id
        with self.assertRaisesRegexp(
            IntegrityError,
            'duplicate key value violates unique constraint'
            ' "openacademy_course_name_unique"'
        ):
            self.create_course('test1', 'test_description', None)

    def test_15_duplicate_course(self):
        '''
        Test to duplicate course & check that work fine!
        '''
        course = self.env.ref('openacademy.course0')
        course.copy()
