# coding: utf-8


# imports
import os
import copy
from json import loads, dumps


class Conection(object):
    """
    Generic class. Create a conection with a json file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    name = "conection.json"
    data = {}
    
    def __init__(self):    
        # setting the full path to json file.
        self.name = os.path.join(self.current_dir, self.name)
        # checking the permissions.
        self.write_permission = os.access(self.current_dir, os.W_OK)
        self.read_permission = os.access(self.current_dir, os.R_OK)
        # trying load the json file.
        self.load()
    
    def load(self):
        """
        Check if exists a file with the same name that self.name,
        if exists will set the content in self.data,
        else will create.
        """
        if self.read_permission:
            file_name = os.path.basename(self.name)
            if file_name in os.listdir(self.current_dir):
                with open(self.name, "r", encoding="utf-8") as f:
                    self.data = loads(f.read())
            else:
                self.save()
        else:
            print("No read permissions.")
    
    def save(self):
        """
        Create a json file with current values in self.data.
        """
        if self.write_permission:
            with open(self.name, "w", encoding="utf-8") as f:
                f.write(dumps(self.data, indent=4, ensure_ascii=False))
            return True
        else:
            print("No write permissions.")
            return False
    
    def get_write_permission(self):
        """
        Returns:
            True: can write files.
            False: can't write files.
        """
        return self.write_permission
    
    def get_read_permission(self):
        """
        Returns:
            True: can read files.
            False: can't read files.
        """
        return self.read_permission
    
    def get_name(self):
        """Return full path to json file.
        """
        return self.name
    
    def get_data(self):
        """Return a copy from data.
        """
        return copy.deepcopy(self.data)
    
    def set_data(self, data):
        """Define data attribute.
        """
        self.data = data


class FazentechConection(Conection):
    name = "fazentech.json"
    data = {"funcionários":{},
            "animais":{},
            "ordenhas":{}}


class StyleConection(Conection):
    name = "style.json"
    data = {"label":{"background":"#fff",
                     "foreground":"#000",
                     "font":["Geogia", 8, "normal"]},
                     
            "button":{"background":"#fff",
                      "foreground":"#000",
                      "font":["Georgia", 8, "normal"]},
                       
            "entry":{"background":"#fff",
                     "foreground":"#000",
                     "font":["Georgia", 8, "normal"]},
                       
            "window":{"background":"#fff"}}


if __name__ == "__main__":
    #fazentech_conection = FazentechConection()
    style_conection = StyleConection()
    
