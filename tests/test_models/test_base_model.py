#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
Unit test module for the BaseModel class.
"""

class TestBaseModel(unittest.TestCase):
    ''' Unit tests for the BaseModel class '''

    def test_object_instantiation(self):
        ''' Tests class instantiation '''
        self.basemodel = BaseModel()

    def test_checking_for_docstrings(self):
        ''' Checks for the presence of docstrings in methods '''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        ''' Tests attributes of the BaseModel class '''
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "random_attr"))
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.basemodel.name = "Bob"
        self.basemodel.age = "30"
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemodel, "name"))
        delattr(self.basemodel, "age")
        self.assertFalse(hasattr(self.basemodel, "age"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def test_save_method(self):
        ''' Tests the save method '''
        self.basemodel = BaseModel()
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def test_str_method(self):
        ''' Tests the __str__ method return format of BaseModel '''
        self.basemodel = BaseModel()
        s = "[{}] ({}) {}".format(self.basemodel.__class__.__name__,
                                str(self.basemodel.id),
                                self.basemodel.__dict__)
        self.assertEqual(s, str(self.basemodel))

    def test_to_dict_method(self):
        ''' Tests the to_dict method '''
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
