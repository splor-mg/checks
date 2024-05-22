from src.checks.requirements import parse_requirement

def test_parse_requirement():

    assert parse_requirement('pandas') == {"pandas": None}
    assert parse_requirement('tensorflow== 2.11.0 ') == {'tensorflow': '2.11.0'}
    assert parse_requirement('frictionless[excel]') == {'frictionless': None}
    assert parse_requirement('requests[security] ==2.6.2') == {'requests': '2.6.2'}
    assert parse_requirement('frictionless[excel,pandas]') == {'frictionless': None}
    assert parse_requirement('frictionless[excel,pandas]==1.1.3') == {'frictionless': '1.1.3'}
    assert parse_requirement('dpm @ git+https://github.com/splor-mg/dpm.git@main') == {'dpm': None}



