"""This module creates a base model class
"""
import uuid
from datetime import datetime


class BaseModel:
    """This is the base class"""

    def __init__(self):
        """initializes an instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string"""

        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updated the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the __dict__
        instance
        """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
