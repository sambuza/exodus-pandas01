import pandas as pd

def get_heavenly_throne_data():
    """하늘 보좌와 어린양 데이터를 생성합니다."""
    data = {
        'entity': ['God', 'Lamb', '24 Elders', 'Four Living Creatures', 'Angels'],
        'role': ['Sovereign', 'Redeemer', 'Worshippers', 'Guardians', 'Servants'],
        'worship_activity': ['Receives Glory', 'Receives Praise', 'Cast Crowns', 'Ceaseless Worship', 'Proclaim Holiness'],
        'revelation_ref': ['Rev 4:2', 'Rev 5:6', 'Rev 4:4', 'Rev 4:6-8', 'Rev 5:11']
    }
    df = pd.DataFrame(data)
    return df

def get_worship_elements_data():
    """천상 예배 요소 데이터를 생성합니다."""
    data = {
        'element': ['Glory', 'Honor', 'Thanksgiving', 'Power', 'Strength'],
        'source': ['Creation', 'Redemption', 'Provision', 'Sovereignty', 'Victory']
    }
    df = pd.DataFrame(data)
    return df
