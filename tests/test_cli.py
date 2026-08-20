from ports.cli import main


def test_roadmap_plan_and_module(capsys):
    assert main(["roadmap"]) == 0
    out = capsys.readouterr().out
    assert "P1" in out
    assert "800" in out
    assert "8000" in out

    assert main(["plan", "--year", "2030"]) == 0
    plan_out = capsys.readouterr().out
    assert "800" in plan_out

    assert main(["module"]) == 0
    mod = capsys.readouterr().out
    assert "100" in mod
    assert "8 modules" in mod


def test_tariff_and_cooling(capsys):
    assert main(["tariff", "--it-mw", "800"]) == 0
    assert "680,000" in capsys.readouterr().out
    assert main(["cooling", "--it-mw", "800"]) == 0
