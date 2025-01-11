import pytest
from gendiff.generate_diff import generate_diff


excepted_nested_diff_json = 'tests/fixtures/results/nested_json_diff_result.json'
excepted_nested_diff_yaml = 'tests/fixtures/results/nested_yaml_diff_result.yaml'
excepted_plain_diff_json = 'tests/fixtures/results/plain_json_diff_result.json'
excepted_plain_diff_yaml = 'tests/fixtures/results/plain_yaml_diff_result.yaml'


@pytest.mark.parametrize(
        'file1,file2,expected_diff,format',
        [
            ('tests/fixtures/json_files/nested_file1.json',
             'tests/fixtures/json_files/nested_file2.json',
             excepted_nested_diff_json,
             'stylish'),
            ('tests/fixtures/yaml_files/nested_file1.yaml',
             'tests/fixtures/yaml_files/nested_file2.yaml',
             excepted_nested_diff_yaml,
             'stylish'),
            ('tests/fixtures/json_files/nested_file1.json',
             'tests/fixtures/json_files/nested_file2.json',
             excepted_plain_diff_json,
             'plain'),
            ('tests/fixtures/yaml_files/nested_file1.yaml',
             'tests/fixtures/yaml_files/nested_file2.yaml',
             excepted_plain_diff_yaml,
             'plain')
        ]
    )


def test_generate_diff(file1, file2, expected_diff, format):
    with open(expected_diff) as f:
        assert generate_diff(file1, file2, format) == f.read()
