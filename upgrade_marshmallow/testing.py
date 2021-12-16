def assert_source_code_equal(left, right):
    assert len(left) == len(right), (f"left line count {len(left)} != {len(right)} right line count")

    for lineno, (left_line, right_line) in enumerate(zip(left, right)):
        assert left_line == right_line, (f'line number: {lineno + 1}\n'
                                         f'left line: "{left_line}"\n'
                                         f'right line: "{right_line}"')
