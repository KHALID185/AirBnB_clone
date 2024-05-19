#!/usr/bin/python3
"""Unit tests for the FileStorage module."""
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    '''Unit tests for the FileStorage class.'''

    def test_Instantiation(self):
        """see if the beans is type of BaseModel"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_Access(self):
        """write and read permisions of our file"""
        lr = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(lr)
        ec = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(ec)
        excu = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertFalse(excu)

    def test_new(self):
        """tests to add new object in our dir """
        inst_stor = FileStorage()
        inst_dirct = inst_stor.all()
        khalid = User()
        khalid.id = 111
        khalid.name = "khalid"
        inst_stor.new(khalid)
        ky = khalid.__class__.__name__ + "." + str(khalid.id)
        self.assertIsNotNone(inst_dirct[ky])

    def test_reload(self):
        """ test to reload objects from the file"""
        r_stor = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as fl:
            fl.write("{}")
        with open("file.json", "r") as rd:
            for ln in rd:
                self.assertEqual(ln, "{}")
        self.assertIs(r_stor.reload(), None)

    def test_funcdocs(self):
        ''' testing functions docstring '''
        for fnc in dir(FileStorage):
            self.assertTrue(len(fnc.__doc__) > 0)

    def test_save(self):
        """test to save."""
        objct = FileStorage()
        new_objct = BaseModel()
        objct.new(new_objct)
        dct1 = objct.all()
        objct.save()
        objct.reload()
        dct2 = objct.all()
        for ky in dct1:
            ky1 = ky
        for ky in dct2:
            ky2 = ky
        self.assertEqual(dct1[ky1].to_dict(), dct2[ky2].to_dict())


if __name__ == '__main__':
    unittest.main()
