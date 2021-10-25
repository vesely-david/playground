import pytest

from attr_config.attrs_example import load_config


@pytest.mark.parametrize(
    "field_name,expected_value",
    [('hdfs_server', 'hdfs://mycluster'),
     ('version', '0.1'),
     ('mlflow_uri', 'http://1.1.1.1')]
)
def test_config_attributes(field_name, expected_value):
    config = load_config('silly_config.yaml')
    field_value = getattr(config, field_name)
    assert field_value == expected_value
