from src.steam_personal_states import pull_steam_data
from FastAPI import TestClient
import pytest


@pytest.mark.fixture
def client():
    return TestClient()


class TestCheckingData():
    def test_getting_data(self,client):
        
        assert pull_steam_data()