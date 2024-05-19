mport cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime

""" console for the command promt module"""


class HBNBCommand(cmd.Cmd):
    """ definition of console class"""
    prompt = "(hbnb)"

    Classes_dct = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_EOF(self, arg):
        ''' class to quit the console'''
        print("")
        return True

    def do_quit(self, arg):
        '''this is also for quit console'''
        return True

    def do_nothing(self, arg):
        ''' this fct has no effect'''
        pass

    def emptyline(self):
        '''the fct command for empty line'''
        pass

    def do_create(self, args):
        '''this fct for create an instance of our module'''
        if args == "":
            print("** class name missing **")
            return
        argmt = shlex.split(args)
        if argmt[0] not in HBNBCommand.Classes_dct:
            print("** class doesn't exist **")
            return
        new_inst = HBNBCommand.Classes_dct[argmt[0]]()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, args):
        """this is print the name and id command"""
        argmt = shlex.split(args)
        if len(argmt) == 0:
            print("** class name missing **")
            return
        if argmt[0] not in HBNBCommand.Classes_dct:
            print("** class doesn't exist **")
            return
        if len(argmt) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        objct = storage.all()
        objct_key = argmt[0] + "." + argmt[1]
        if objct_key in objct:
            print(str(objct[objct_key]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        '''this command for destroy instance in our module'''
        argmt = shlex.split(args)
        if len(argmt) == 0:
            print("** class name missing **")
            return
        if argmt[0] not in HBNBCommand.Classes_dct:
            print("** class doesn't exist **")
            return
        if len(argmt) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        objct = storage.all()
        objct_key = argmt[0] + "." + argmt[1]
        if objct_key in objct:
            del objct[objct_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ this function tell the command to do all constructions"""
        storage.reload()
        json_dctr = []
        objct_dictr = storage.all()
        if args == "":
            for key, val in objct_dictr.items():
                json_dctr.append(str(val))
            print(json.dumps(json_dctr))
            return
        arg = shlex.split(args)
        if arg[0] in HBNBCommand.Classes_dct.keys():
            for key, val in objct_dictr.items():
                if arg[0] in key:
                    json_dctr.append(str(val))
            print(json.dumps(json_dctr))
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ first update of our module base"""

        if not args:
            print("** class name missing **")
            return
        argmt = shlex.split(args)
        storage.reload()
        objct = storage.all()
        if argmt[0] not in HBNBCommand.Classes_dct.keys():
            print("** class doesn't exist **")
            return
        if len(argmt) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = argmt[0] + "." + argmt[1]
            objct[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(argmt) == 2):
            print("** attribute name missing **")
            return
        if (len(argmt) == 3):
            print("** value missing **")
            return
        obj_dict = objct[obj_key].__dict__
        if argmt[2] in obj_dict.keys():
            d_type = type(obj_dict[argmt[2]])
            print(d_type)
            obj_dict[argmt[2]] = type(obj_dict[argmt[2]])(argmt[3])
        else:
            obj_dict[argmt[2]] = argmt[3]
        storage.save()

    def do_update2(self, args):
        """the second update"""
        if not args:
            print("** class name missing **")
            return
        dict_mine = "{" + args.split("{")[1]
        argmt = shlex.split(args)
        storage.reload()
        objct = storage.all()
        if argmt[0] not in HBNBCommand.Classes_dct.keys():
            print("** class doesn't exist **")
            return
        if len(argmt) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = argmt[0] + "." + argmt[1]
            objct[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (dict_mine == "{"):
            print("** attribute name missing **")
            return
        dict_mine = dict_mine.replace("\'", "\"")
        dict_mine = json.loads(dict_mine)
        objct_inst = objct[obj_key]
        for k in dict_mine:
            if hasattr(objct_inst, k):
                d_type = type(getattr(objct_inst, k))
                setattr(objct_inst, k, dict_mine[k])
            else:
                setattr(objct_inst, k, dict_mine[k])
        storage.save()

    def do_count(self, args):
        """this calculute the instance create of our module"""
        objct = storage.all()
        counter = 0
        for ky in objct:
            if (args in ky):
                counter += 1
        print(counter)

    def default(self, args):
        """the default function if none of our fct above traite"""
        cmmd = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            }
        argmt = args.strip()
        val = argmt.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, argmt)
            return
        cls_name = val[0]
        command = val[1].split("(")[0]
        line = ""
        if (command == "update" and val[1].split("(")[1][-2] == "}"):
            inputs = val[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = cls_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = val[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
            line = cls_name + line
            if (command in cmmd.keys()):
                cmmd[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
