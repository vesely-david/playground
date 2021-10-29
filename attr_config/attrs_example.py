import attr
import cattr
import yaml


@attr.define(auto_attribs=True, frozen=True)
class MyConfig:
    version: str
    hdfs_server: str
    mlflow_uri: str


def load_config(path):
    with open(path) as config_f:
        config = yaml.safe_load(config_f)
    return cattr.structure(config, MyConfig)
