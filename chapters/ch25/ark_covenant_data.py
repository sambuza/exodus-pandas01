import pandas as pd

def get_ark_covenant_components():
    """언약궤 구성 요소 데이터를 생성합니다."""
    data = {
        'component': ['Ark', 'Mercy Seat', 'Cherubim', 'Tablets of Law', 'Jar of Manna', 'Aaron\'s Staff'],
        'material': ['Acacia Wood overlaid with Gold', 'Pure Gold', 'Pure Gold', 'Stone', 'Gold', 'Almond Wood'],
        'symbolism': ['God\'s Presence', 'Atonement', 'Guardianship', 'God\'s Law', 'God\'s Provision', 'God\'s Authority'],
        'location': ['Most Holy Place', 'Most Holy Place', 'Most Holy Place', 'Inside Ark', 'Inside Ark', 'Inside Ark']
    }
    df = pd.DataFrame(data)
    return df

def get_tabernacle_sections():
    """성막의 구역 데이터를 생성합니다."""
    data = {
        'section_name': ['Outer Court', 'Holy Place', 'Most Holy Place'],
        'access_level': ['All Israelites', 'Priests only', 'High Priest only'],
        'purpose': ['Sacrifice, Cleansing', 'Daily Service', 'Atonement, God\'s Presence']
    }
    df = pd.DataFrame(data)
    return df
