import subprocess

def test_help():
    expected_output = """\
usage: Activity01.py [-h] [-c] [--repeat REPEAT] message [message ...]
Activity01.py: error: the following arguments are required: message
"""
    output = subprocess.run(
        ["python3.7", "./Activity01.py"],
        capture_output=True,
        text=True,
    )
    print(output.stderr)
    assert output.stderr == expected_output


def test_run_1():
    output = subprocess.run(
        ["python3.7", "./Activity01.py", "-c", "hello"],
        capture_output=True,
        text=True,
    )
    print(output.stdout)
    assert output.stdout == "Hello\n"


def test_run_2():
    output = subprocess.run(
        ["python3.7", "./Activity01.py", "--repeat", "2", "hello"],
        capture_output=True,
        text=True,
    )
    print(output.stdout)
    assert output.stdout == "hello\nhello\n"
