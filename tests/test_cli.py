"""CLI smoke tests."""

from heartland.cli import main


def test_roadmap_and_plan_exit_zero(capsys):
    assert main(["roadmap"]) == 0
    out = capsys.readouterr().out
    assert "P1" in out
    assert "1122" in out or "1,122" in out or "    1122" in out

    assert main(["plan", "--year", "2031"]) == 0
    plan_out = capsys.readouterr().out
    assert "234" in plan_out


def test_tariff_and_cooling(capsys):
    assert main(["tariff", "--it-mw", "240"]) == 0
    assert "204,000" in capsys.readouterr().out
    assert main(["cooling", "--it-mw", "1200"]) == 0
