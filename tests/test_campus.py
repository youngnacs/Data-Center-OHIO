from ports.capacity import CampusPlan
from ports.cooling import compare_cooling
from ports.tariff import aep_minimum_billing_kw


def test_compute_module_is_one_hundred_mw():
    cm = CampusPlan().types["CM"]
    assert cm.it_mw == 100
    assert cm.racks == 1000


def test_phase_one_is_eight_modules():
    snap = CampusPlan().snapshot(2030)
    assert snap.building_counts == {"CM": 8}
    assert snap.it_mw == 800
    assert snap.phase_id == "P1"


def test_full_build_is_eight_gw_it():
    snap = CampusPlan().full_build()
    assert snap.it_mw == 8000
    assert snap.building_counts["CM"] == 80
    assert snap.btm_mw > snap.grid_mw
    assert snap.progress_to_target == 1.0


def test_phase_zero_has_no_it_load():
    snap = CampusPlan().snapshot(2027)
    assert snap.it_mw == 0
    assert snap.phase_id == "P0"


def test_roadmap_is_monotonic():
    it_loads = [snap.it_mw for snap in CampusPlan().roadmap()]
    assert it_loads == sorted(it_loads)
    assert it_loads == [0, 800, 2400, 4800, 8000]


def test_aep_tariff_caps_at_85_percent_for_hyperscale():
    assert aep_minimum_billing_kw(800_000) == 680_000


def test_aep_tariff_mid_bracket():
    assert aep_minimum_billing_kw(50_000) == 36_250


def test_aep_ratchet_uses_prior_peak():
    assert aep_minimum_billing_kw(50_000, highest_prior_11_month_kw=48_000) == 40_800


def test_closed_loop_saves_vast_majority_of_water():
    result = compare_cooling(800)
    assert result.savings_ratio > 0.95
    assert result.closed_loop_million_gal < 120
    assert result.evaporative_million_gal > 400
