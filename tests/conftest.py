MARKER = """\
unit: Mark unit tests
integration: Mark integraton tests
high: high priority
medium: medium priority
low: low priority
"""

def pytest_configure(config):
    for line in MARKER.strip().split('\n'):
        config.addinivalue_line('markers', line)