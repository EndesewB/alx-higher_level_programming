#!/usr/bin/python3
"""The module which adds all the arguments to the python list"""
import sys

if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    """importing save_to_json_ file from previous method"""
    load_json = __import__('6-load_from_json_file').load_from_json_file
    """importing load_from_json_file from previous method"""
    try:
        items = load_json("add_item.json")
    except FileNotFoundError:
        items = []
        """initializing the list to empty"""
    items.extend(sys.argv[1:])
    """appending files to the existing filename"""
    save_json(items, "add_item.json")
