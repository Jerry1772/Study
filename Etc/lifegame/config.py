from abc import ABCMeta, abstractmethod
import json

class BaseConfig(metaclass=ABCMeta):
    
    @classmethod
    @abstractmethod
    def _from_json(cls, config_json: dict):
        raise NotImplementedError

    def to_dict(self):
        result = {}
        for key, value in vars(self).items():
            if key[0] == "_":
                continue
            if isinstance(value, BaseConfig):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                if isinstance(value[0], BaseConfig):
                    result[key] = [x.to_dict() for x in value]
                else:
                    result[key] = value
            else:
                result[key] = value
        return result
    
    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

class Config(BaseConfig):
    def __init__(self, sleep_time:int, board_size:int, 
                point_x:list[int], point_y:list[int],
                print_iter:int, char_alive:str, char_dead:str):
        self.sleep_time = sleep_time
        self.board_size = board_size
        self.point_x = point_x
        self.point_y = point_y
        self.print_iter = print_iter
        self.char_alive = char_alive
        self.char_dead = char_dead
    
    @classmethod
    def _from_json(cls, config_json: dict):
        return cls(
            sleep_time=config_json["sleep_time"],
            board_size=config_json["board_size"],
            point_x=config_json["point_x"],
            point_y=config_json["point_y"],
            print_iter=config_json["print_iter"],
            char_alive=config_json["alive_char"],
            char_dead=config_json["dead_char"]
        )
        #cls.from_json 을 통해 객체 초기화
        # => 객체 초기화해놓고, from_json 으로 self.var 추가해나가는 방식은?
        #    똑같긴 할듯.. (from_json을 classmethod 로 지정하지 않고, self.var 에다가 config_json[""] 할당해나가는 방식
    
    @classmethod
    def from_path(cls, config_file_path: str):
        with open(config_file_path) as f:
            config_json = json.load(f)
        return cls._from_json(config_json)

    # @classmethod
    # def from_server(cls, url: str):
    #     #url get 해서 data 가져오고, 가공해서 json형식으로 바꿈
    #     #json 받은걸 cls.from_json(json) 호출해서 객체 초기화 가능
    #     pass