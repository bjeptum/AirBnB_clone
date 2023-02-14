#!/usr/bin/python3


"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
"""

import unitest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        mod = BaseModel()
        self.asserIsInstance(mod, BaseModel)

        self.assertIsInstance(mod, BaseModel)
        self.assertEqual(type(mod), BaseModel)

    def test_unique_id(self):
        mod = BaseModel()
        mod1 = BaseModel()

        self.assertEqual(mod.id, mod1.id)

    def test_instance_save(self):
        mod = BaseModel()
        md = mod.to_dict()

    def test_attributes(self):
        mod = BaseModel()

        self.assertTrue(mod.id)
        self.assertTrue(mod.created_at)
        self.assertTrue(mod.updated_at)

if __name__ = "__main__":
    unittest.main()
