import pytest
from dev2il_devops_app.mountains import highest_mountain

def test_highest_mountain():
    mountains = [
        {'name': 'Kilimanjaro', 'height': 5895},
        {'name': 'Everest', 'height': 8848},
        {'name': 'K2', 'height': 8611}
    ]
    assert highest_mountain(mountains) == {'name': 'Everest', 'height': 8848}
    
def test_highest_mountain_empty():
    mountains = []
    assert highest_mountain(mountains) is None