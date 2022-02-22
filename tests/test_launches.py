from spacex_api import launches

def get_launches():
    got_launches, _ = launches.get_launches()
    return got_launches

def get_launches_by_query():
    got_launches, _ = launches.get_launches(site_id="ksc_lc_39a")
    return got_launches

def test_get_launches():
    assert type(get_launches()) is list

def test_get_launches_by_query():
    assert type(get_launches_by_query()) is list
