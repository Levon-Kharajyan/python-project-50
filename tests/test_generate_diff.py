import pytest
from gendiff.generate_diff import generate_diff


expected_nested_diff_json = 'tests/fixtures/results/nested_json_diff_result.json'
expected_nested_diff_yaml = 'tests/fixtures/results/nested_yaml_diff_result.yaml'
expected_plain_diff_json = 'tests/fixtures/results/plain_json_diff_result.json'
expected_plain_diff_yaml = 'tests/fixtures/results/plain_yaml_diff_result.yaml'
expected_json_form_diff = 'tests/fixtures/results/json_form_diff_result.json'


@pytest.mark.parametrize(
        'file1,file2,expected_diff,format',
        [
            ('tests/fixtures/json_files/nested_file1.json',
             'tests/fixtures/json_files/nested_file2.json',
             expected_nested_diff_json,
             'stylish'),
            ('tests/fixtures/yaml_files/nested_file1.yaml',
             'tests/fixtures/yaml_files/nested_file2.yaml',
             expected_nested_diff_yaml,
             'stylish'),
            ('tests/fixtures/json_files/nested_file1.json',
             'tests/fixtures/json_files/nested_file2.json',
             expected_plain_diff_json,
             'plain'),
            ('tests/fixtures/yaml_files/nested_file1.yaml',
             'tests/fixtures/yaml_files/nested_file2.yaml',
             expected_plain_diff_yaml,
             'plain'),
            ('tests/fixtures/json_files/nested_file1.json',
             'tests/fixtures/json_files/nested_file2.json',
             expected_json_form_diff,
             'json'),
            ('tests/fixtures/yaml_files/nested_file1.yaml',
             'tests/fixtures/yaml_files/nested_file2.yaml',
             expected_json_form_diff,
             'json')
        ]
    )


def test_generate_diff(file1, file2, expected_diff, format):
    with open(expected_diff) as f:
        assert generate_diff(file1, file2, format) == f.read()
