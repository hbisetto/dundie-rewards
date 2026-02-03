import pytest

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


@pytest.fixture(autouse=True) # fixture == pré requisitos para os testes
def go_to_tmpdir(request): # injeção de dependências
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield # faz o que tem que fazer, e retorna a função