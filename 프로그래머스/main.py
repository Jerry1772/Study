import argparse
import re

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

    def __init__(self, lang:str, command:str, **kwargs):
        self.cmd_type = f"_{command}_{lang}"
        self.main(**kwargs)
    
    def main(self, **kwargs):
        getattr(self, self.cmd_type)(**kwargs)

    def _init_python(self, idx, name, **kwargs):
        with open("./Python/sample.py", "r") as f:
            lines = "".join(f.readlines())

        lines = lines.replace("@url", f" https://school.programmers.co.kr/learn/courses/30/lessons/{idx}")
        
        if "param" in kwargs:
            params = kwargs['param'].replace(",", '": None,\n\t\t"')
            
            lines = lines.replace("#@param", f'"{params}": None')

        with open(f"./Python/{idx}_{name}.py", "w") as f:
            f.write(lines)
        

    def _init_sql(self):
        pass

    @classmethod
    def initialize(cls, **kwargs):
        return cls(**kwargs)

if __name__ == "__main__":
    parser_init = CustomParser.init("init", "initialize python file")
    parser_init.add_req("-i", "--idx", type=str, help=">> problem index")
    parser_init.add_req("-n", "--name", type=str, help=">> problem name")
    parser_init.add_req("-l", "--lang", type=str, help=">> problem language")
    parser_init.add_opt("-p", "--param", type=str, help=">> comma seperated parameter names")
    
    args = dict(vars(CustomParser.parse_args()))
    i = Initializer.initialize(**args)
    