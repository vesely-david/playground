import attr
import cattr
import yaml


@attr.s
class MyConfig(object):
    version = attr.ib(str)
    hdfs_server = attr.ib(str)
    mlflow_uri = attr.ib(str)


def load_config(path):
    with open(path) as config_f:
        config = yaml.safe_load(config_f)
    return cattr.structure(config, MyConfig)
