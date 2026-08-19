from heartland.capacity import CampusPlan
from heartland.cooling import compare_cooling
from heartland.tariff import aep_minimum_billing_kw


def test_full_build_hits_program_target():
    snap = CampusPlan().full_build()
    assert snap.it_mw == 1122.0
    assert snap.racks > 20_000
    assert snap.site_mw > snap.facility_mw > snap.it_mw
    assert snap.progress_to_target > 0.90


def test_phase_zero_has_no_it_load():
    snap = CampusPlan().snapshot(2027)
    assert snap.it_mw == 0
    assert snap.phase_id == "P0"
    assert snap.total_capex_usd > 0


def test_phase_one_foundation_mix():
    snap = CampusPlan().snapshot(2031)
    assert snap.building_counts == {"A": 2, "B": 1, "C": 1}
    assert snap.it_mw == 48 * 2 + 120 + 18
    assert snap.phase_id == "P1"


def test_roadmap_is_monotonic():
    snaps = CampusPlan().roadmap()
    it_loads = [snap.it_mw for snap in snaps]
    assert it_loads == sorted(it_loads)
    assert it_loads[-1] > it_loads[0]


def test_aep_tariff_caps_at_85_percent_for_hyperscale():
    minimum = aep_minimum_billing_kw(240_000)
    assert minimum == 204_000


def test_aep_tariff_mid_bracket():
    # 50 MW: 15,000 + 0.85 * 25,000 = 36,250, below 85% of 50,000 (42,500)
    assert aep_minimum_billing_kw(50_000) == 36_250


def test_aep_ratchet_uses_prior_peak():
    # 50 MW contract bracket is 36,250 kW; 85% of a 48 MW peak is 40,800 kW.
    assert aep_minimum_billing_kw(50_000, highest_prior_11_month_kw=48_000) == 40_800


def test_closed_loop_saves_vast_majority_of_water():
    result = compare_cooling(1200)
    assert result.savings_ratio > 0.95
    assert result.closed_loop_million_gal < 120
    assert result.evaporative_million_gal > 400
