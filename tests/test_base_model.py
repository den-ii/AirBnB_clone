#!/usr/bin/python3
"""
    TestBaseModel module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        Tests base model class
    """

    def test_instance_creation_of_base_model(self):
        """
            Tests instance creation of BaseModel
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_avoid_id_duplication_for_instance(self):
        """
            Tests avoid ID duplication
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_assignment_of_created_attribute(self):
        """
            Tests created_at_attributr

        """
        bm = BaseModel()
        c_at = bm.created_at
        self.assertIsInstance(c_at, datetime)

    def test_assignment_of_updated_at_attribute(self):
        """
            Tests updated_at attribute
        """
        bm = BaseModel()
        u_at = bm.updated_at
        self.assertIsInstance(u_at, datetime)

    def test_save_method(self):
        """
            Tests save method
        """
        bm = BaseModel()
        update_in_create = bm.updated_at
        bm.save()
        update_in_save = bm.updated_at
        self.assertNotEqual(update_in_create, update_in_save)

    def test_str(self):
        """
            Test __str__method
        """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

