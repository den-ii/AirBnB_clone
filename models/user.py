#!/usr/bin/python3
"""
    User Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        [User]

        Args:
        BaseModel ([class]): [class inherited by user]
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
