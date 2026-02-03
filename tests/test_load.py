import uuid
import pytest
import os
from dundie.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print()
    print("roda antes dos testes desse módulo\n")

def teardown_module():
    print()
    print("roda após os testes desse modulo\n")

@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    # roda antes da execução
    file_ = tmpdir.join("new_file.txt")
    file_.write("Isso é sujeira...")
    yield
    # roda após a execução
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""

    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))
    # request.addfinalizer(lambda: print("Terminou"))

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados úteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'


@pytest.mark.unit
@pytest.mark.high
def test_load2(): 
    """Test load function"""

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados úteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
    