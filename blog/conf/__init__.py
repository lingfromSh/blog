import importlib

PythonPath = str


class LazyConfig:
    def from_object(self, config: object):
        def is_dunder_name(name: str):
            return name.startswith("__") and name.endswith("__")

        for attr_name in dir(config):
            if not is_dunder_name(attr_name):
                setattr(self, attr_name, getattr(config, attr_name))


def set_project_config(file: PythonPath):
    global settings
    obj = importlib.import_module(file)
    settings.from_object(obj)

settings = LazyConfig()
