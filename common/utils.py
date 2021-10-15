import os
import toml
import yaml
import typing as t


JSONType = t.Union[str, int, float, bool, None, t.Dict[str, t.Any], t.List[t.Any]]


def get_config():
    config = toml.load(".env")
    return config


class YamlParse(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def yaml_to_json(file_name: str):
        """
        yaml file to json
        :param file_name:
        :return:
        """
        with open(file_name, 'r') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)


class FilePathTemplate(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def show_current_path() -> str:
        """ 显示当前方法所在的python执行文件所在的文件路径 """
        cur_dir = os.path.dirname(__file__)
        return cur_dir

    @staticmethod
    def show_super_path() -> str:
        """ 当前执行文件的上级文件路径 """
        super_dir = os.path.dirname(os.path.dirname(__file__))
        return super_dir


if __name__ == "__main__":
    yp = YamlParse()
    path = FilePathTemplate.show_super_path() + "/alarm_yaml/a_example.yaml"
    yp.yaml_to_json(path)
