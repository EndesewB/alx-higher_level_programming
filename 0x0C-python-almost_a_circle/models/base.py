#!/usr/bin/python3
"""This is the base class module"""
import json


class Base:
    """Base class with private attributes managing criteria"""
    __nb_objects = 0
    """private object counter"""
    def __init__(self, id=None):
        """if id is passed, it will be setted id attribute"""
        """if it is not passed it will generate a unique id attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of dicts"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json file to file objects"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_string = cls.to_json_string([ob.to_dictionary()
                                                  for ob in list_objs])
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns json strings from dictonary"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dictionary = cls.from_json_string(json_string)
                list_instances = [cls.create(**dictionary)
                                  for dictionary in list_dictionary]
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif isinstance(obj, Square):
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = Rectangle(int(row[1]), int(row[2]), int(row[3]),
                                        int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = Square(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    objs.append(obj)
                return objs
        except:
            return []
