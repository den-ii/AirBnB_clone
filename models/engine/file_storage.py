#!/usr/bin/python3
"""[FileStorage class]
"""
from os import path
import json
from models.base_model import BaseModel


class FileStorage():
    """[FileStorage]
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """[all]
        Returns:
            [dict]: [dictionnary containing objects]
        """
        return FileStorage.__objects

    def new(self, obj):
        """[new]
        Args:
            obj ([object]): [object to be created]
        """
        _id = obj.id
        key = str(obj.__class__.__name__) + "." + _id
        FileStorage.__objects[key] = obj

    def save(self):
        """[save]
        """
        dct = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            for k, v in FileStorage.__objects.items():
                dct[k] = v.to_dict()
            json.dump(dct, f, indent=4)

    def reload(self):
        """[reload]
        """
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj = json.load(f)
                dct = {}
                for k, v in obj.items():
                    dct[k] = self.classes[v["__class__"]](**v)
                FileStorage.__objects = dct
        else:
            return
