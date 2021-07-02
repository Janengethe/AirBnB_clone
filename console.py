#!/usr/bin/python3
"""
Module console
contains the entry point to the command interpreter
"""


import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ command line interpreter"""
    prompt = "(hbnb) "
    all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def do_EOF(self, line):
        """ Interprets Ctrl + D
        """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        It ignores the last nonempty
        command entered and does nothing
        """
        pass

    def do_create(self, line):
        """Creates a new BaseModel instance
        Args:
            None
        Prints id of the new BaseModel instance
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        else:
            base1 = HBNBCommand.all_classes[line]()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id. Example: $ show BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id. Example: (hbnb)  destroy BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                del(all_instances[ke_y])
                storage.save()

    def do_all(self, line):
        """
        Prints the string representation of all instances
        Example: (hbnb) all BaseModel
        or (hbnb) all
        """
        obj_list = []
        all_list = []
        all_instances = storage.all()
        if line == "":
            for k, obj in all_instances.items():
                all_list.append(str(obj))
            print(all_list)
        elif line in HBNBCommand.all_classes.keys():
            for k, v in all_instances.items():
                if line == v.__class__.__name__:
                    ke_y = line + "." + str(v.id)
                    obj_list.append(all_instances[ke_y])
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: (hbnb)
        update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        elif len(a_list) == 2:
            print("** attribute name missing **")
        elif len(a_list) == 3:
            print("** value missing **")
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                setattr(obj, a_list[2], a_list[3])
                storage.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and
        returns.
        """
        if len(line) == 0:
            return
        else:
            args = line.split('.')
            class_arg = args[0]
            if class_arg in HBNBCommand.all_classes:
                if len(args) == 2:
                    if args[1] == "all()":
                        HBNBCommand.do_all(self, class_arg)
                    elif args[1] == "count()":
                        print((HBNBCommand.instance_count(self, class_arg)))
                    elif str(args[1])[:4] == "show":
                        string = args[1]
                        c_id = string[6:-2]
                        l_ine = str(class_arg) + " " + str(c_id)
                        HBNBCommand.do_show(self, l_ine)
                    elif str(args[1])[:7] == "destroy":
                        string = args[1]
                        c_id = string[9:-2]
                        l_ine = str(class_arg) + " " + str(c_id)
                        HBNBCommand.do_destroy(self, l_ine)
                    elif str(args[1])[:6] == "update":
                        a_slc = args[1][7:-1]
                        my_list = a_slc.split(", ")
                        _id = my_list[0][1:-1]
                        if type(my_list[1]) == dict:
                            for att, val in my_list[1].items():
                                l = class_arg + " " + _id + " " + att + val
                                HBNBCommand.do_update(self, l)
                        else:
                            if my_list[2][0] == '"' and my_list[2][-1] == '"':
                                val = my_list[2][1:-1]
                            else:
                                val = my_list[2]
                            if my_list[1][0] == '"' and my_list[1][-1] == '"':
                                attr = my_list[1][1:-1]
                            else:
                                attr = my_list[1]
                            l = str(class_arg + " " + _id + " " + attr +
                                    " " + val)
                            HBNBCommand.do_update(self, l)
                    else:
                        pass
                else:
                    print("Try: {}.all() or all {}".format(args[0], args[0]))
            else:
                print("*** Unknown syntax: {}".format(line))
                return

    def instance_count(self, line):
        """
        Returns a list containing string representation of instances
        """
        count = 0
        obj_list = []
        all_list = []
        all_instances = storage.all()
        if line == "":
            for k, obj in all_instances.items():
                all_list.append(str(obj))
                count = count + 1
            return(count)
        elif line in HBNBCommand.all_classes.keys():
            for k, v in all_instances.items():
                if line == v.__class__.__name__:
                    ke_y = line + "." + str(v.id)
                    obj_list.append(all_instances[ke_y])
                    count = count + 1
            return(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
