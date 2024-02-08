import pytest
import json
from gendiff.generate_diff import generate_diff


json_1 = '/home/kharajyan/python-project-50/tests/fixtures/file1.json'
json_2 = '/home/kharajyan/python-project-50/tests/fixtures/file2.json'
json_diff_result = '/home/kharajyan/python-project-50/tests/fixtures/json_diff_result.json'


@pytest.fixture
def test_generate_diff(json_1, json_2, json_diff_result):
    actual = generate_diff(json_1, json_2)
    expected_result = json.load(open(json_diff_result))
    assert actual == expected_result
