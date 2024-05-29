import argparse
import re
import inspect
import os

from typing import Union, Dict, Tuple

def get_stack() -> str:
    return inspect.stack()[2].function
class CustomParser:
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(help="command", dest="command")

    def __init__(self, subparser:argparse._SubParsersAction, cmd:str, help:str):
        self.parser:argparse.ArgumentParser = subparser.add_parser(cmd, help=help)
        self.req = self.parser.add_argument_group("required arguments")
        self.opt = self.parser.add_argument_group("optional arguments")
    
    def add_req(self, *args, **kwargs):
        '''
        add required argument
        '''
        self.req.add_argument(*args, **kwargs, required=True)
    
    def add_opt(self, *args, **kwargs):
        '''
        add optional argument
        '''
        self.opt.add_argument(*args, **kwargs, required=False)

    def add_bool(self, *args, **kwargs):
        '''
        add boolean argument (on/off)
        '''
        self.opt.add_argument(*args, **kwargs, required=False, action="store_true")
    
    @classmethod
    def parse_args(cls):
        return cls.parser.parse_args()
    
    @classmethod
    def init(cls, cmd:str, help:str):
        return cls(
            subparser=cls.subparser,
            cmd=cmd,
            help=help
        )

class Initializer:
    PATH:Dict[str, str] = {
        "python": "./Python",
        "sql": "./MySQL"
    }
    EXTENSION:Dict[str, str] = {
        "python": "py",
        "sql": "sql"
    }
    
    SAMPLE_FILE_NAME = "sample"
    
    PROGRAMMERS_URL = "https://school.programmers.co.kr/learn/courses/30/lessons"

    def __init__(self, lang:str, command:str, **kwargs):
        self.cmd_type = f"_{command}_{lang}"
        self.main(**kwargs)
    
    @property
    def path(self):
        frm = get_stack().split("_")[-1]
        return self.PATH.get(frm, None)

    @property
    def ext(self):
        frm = get_stack().split("_")[-1]
        return self.EXTENSION.get(frm, None)

    def main(self, **kwargs):
        getattr(self, self.cmd_type)(**kwargs)

    def _init_python(self, idx, name, **kwargs):
        param:Union[None, str] = kwargs['param']
        force:bool = kwargs['force']
        file_name = f"{self.path}/{idx}_{name}.{self.ext}"
        
        if not force and os.path.isfile(file_name):
            raise FileExistsError

        with open(f"{self.path}/{self.SAMPLE_FILE_NAME}.{self.ext}", "r") as f:
            lines = "".join(f.readlines())

        lines = lines.replace("@url", f" {self.PROGRAMMERS_URL}/{idx}")

        if param is not None:
            params = param.replace(",", '": None,\n\t\t"')
            lines = lines.replace("#@param", f'"{params}": None')
            lines = lines.replace("#@funcparam", param)

        with open(file_name, "w") as f:
            f.write(lines)
        

    def _init_sql(self, idx, name, **kwargs):
        force:bool = kwargs['force']
        file_name = f"{self.path}/{idx}_{name}.{self.ext}"

        lines = f"-- {self.PROGRAMMERS_URL}/{idx}\n\n"

        if not force and os.path.isfile(file_name):
            raise FileExistsError
        
        with open(file_name, "w") as f:
            f.write(lines)

    @classmethod
    def initialize(cls, **kwargs):
        return cls(**kwargs)

if __name__ == "__main__":
    parser_init = CustomParser.init("init", "initialize python file")
    parser_init.add_req("-i", "--idx", type=str, help=">> lesson index")
    parser_init.add_req("-n", "--name", type=str, help=">> lesson name")
    parser_init.add_opt("-l", "--lang", type=str, help=">> lesson language", default="python")
    parser_init.add_opt("-p", "--param", type=str, help=">> comma seperated parameter names")
    parser_init.add_bool("-f", "--force", help=">> force to overwrite the existing file")
    
    args = dict(vars(CustomParser.parse_args()))
    print(args)
    i = Initializer.initialize(**args)
    