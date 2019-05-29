import io
from file import say_hello, input_output


def test_say_hello(capsys):
    say_hello()
    output = capsys.readouterr().out.strip()
    assert output == "Hello!"

    say_hello("Jim")
    output = capsys.readouterr().out.strip()
    assert output == "Hello, Jim!"


def test_input_output(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO('my input'))
    input_output()
    output = capsys.readouterr().out.strip()
    assert output == "my input!"
