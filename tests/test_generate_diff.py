import pytest
import json
from gendiff.generate_diff import generate_diff


json_diff_result = 'tests/fixtures/json_diff_result.json'


@pytest.mark.parametrize(
    "file1,file2,diff_result",
    [
        ('tests/fixtures/file1.json',
         'tests/fixtures/file2.json',
         json_diff_result)
    ]
)
def test_generate_diff(file1, file2, diff_result):
    with open(diff_result) as f:
        assert generate_diff(file1, file2) == f.read()