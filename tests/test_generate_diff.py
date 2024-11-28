import pytest
from gendiff.generate_diff import generate_diff


excepted_diff_json = 'tests/fixtures/results/plane_json_diff_result.json'
excepted_diff_yaml = 'tests/fixtures/results/plane_yaml_diff_result.yaml'

@pytest.mark.parametrize(
        'file1,file2,expected_diff',
        [
            ('tests/fixtures/json_files/plane_file1.json',
             'tests/fixtures/json_files/plane_file2.json',
             excepted_diff_json),
            ('tests/fixtures/yaml_files/plane_file1.yaml',
             'tests/fixtures/yaml_files/plane_file2.yaml',
             excepted_diff_yaml)
            ]
    )

def test_generate_diff(file1, file2, expected_diff):
    with open(expected_diff) as f:
        assert generate_diff(file1, file2) == f.read()
