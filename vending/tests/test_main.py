import filecmp
import os
from pathlib import Path

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

num_tests = len(list(Path('data').glob('vending*.input.dat')))
test_padding = len(str(num_tests))
testdata = []
for test_id in range(1, num_tests + 1):
    input_path = f'data/vending{test_id:0{test_padding}d}.input.dat'
    output_path = f'data/vending{test_id:0{test_padding}d}.output.dat'
    stdout = f'data/vending{test_id:0{test_padding}d}.stdout'
    expected = f'data/vending{test_id:0{test_padding}d}.expected.dat'
    testdata.append((input_path, output_path, stdout, expected))


@pytest.mark.parametrize('input_path, output_path, stdout, expected', testdata)
def test_run(input_path, output_path, stdout, expected, capsys):
    main.run(input_path, output_path)
    captured = capsys.readouterr()
    assert filecmp.cmp(output_path, expected, shallow=False)
    with open(stdout, 'r') as f:
        expected_stdout = f.read()
    assert captured.out == expected_stdout
