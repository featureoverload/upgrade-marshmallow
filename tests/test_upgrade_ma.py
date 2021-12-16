import os

import pytest
from tests import get_sample_dir
from upgrade_marshmallow.upgrade import replace_as_metadata_kw
from upgrade_marshmallow.testing import assert_source_code_equal


SCHEMAS_FILENAME = 'schemas.py'
EXPECTED_FILENAME = 'expected.py'


@pytest.mark.parametrize('case_dir', [
    'most_common',
    'alias_fields',
    'absolute',
    'alias_absolute',
    'field_func',
    # 'comment_issue',
    # 'field_func_like',
    'default_missing',
])
def test_upgrade_field_call_expression(case_dir):
    sample_dir = os.path.join(get_sample_dir(), case_dir)

    file = os.path.join(sample_dir, SCHEMAS_FILENAME)
    result = replace_as_metadata_kw(file)

    with open(os.path.join(sample_dir, EXPECTED_FILENAME), 'r') as fp:
        expected = fp.read().splitlines()

    print(result)
    assert_source_code_equal(result.splitlines(), expected)
