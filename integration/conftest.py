MARKER = """\
unit: Mark unit tests
integration: Mark integraton tests
high: high priority
medium: medium priority
low: low priority
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers', line), MARKER.split())    
    
    