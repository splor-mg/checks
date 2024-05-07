from src.checks.requirements import parse_requirement

def test_parse_requirement():
    input = [
        'pandas',
        'tensorflow== 2.11.0 ',  # intentional spaces
        'frictionless[excel]',
        'requests[security] ==2.6.2',
        'dpm @ git+https://github.com/splor-mg/dpm.git@main',
    ]

    expected_result = {'pandas': None, 'requests': '2.6.2', 'frictionless': None, 'tensorflow': '2.11.0', 'dpm': None}

    result = {package: version for dep in input for package, version in parse_requirement(dep).items()}

    assert result == expected_result


test_parse_requirement()