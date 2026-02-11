import juice

def test_juice_payment(monkeypatch, capsys):
    # Simulate typing '50' twice
    user_inputs = iter(["50", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    # Run the machine
    juice.main()

    # Capture and check the output
    output = capsys.readouterr().out
    assert "Amount Due: 100" in output
    assert "Change Owed: 0" in output