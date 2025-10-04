import pandas as pd
import numpy as np

def get_tabernacle_glory_events():
    """성막 봉헌 시 하나님의 영광 임재 데이터를 생성합니다."""
    data = {
        'event_id': [1, 2, 3, 4, 5],
        'event_description': [
            'Cloud covered the Tent of Meeting',
            'Glory of the Lord filled the Tabernacle',
            'Moses could not enter the Tent',
            'Fire came out from before the Lord',
            'Consumed the burnt offering and the fat'
        ],
        'intensity_score': [9, 10, 8, 9, 7],
        'divine_presence': [True, True, True, True, True],
        'chapter_verse': ['Exodus 40:34', 'Exodus 40:34', 'Exodus 40:35', 'Leviticus 9:24', 'Leviticus 9:24']
    }
    df = pd.DataFrame(data)
    return df

def get_israel_response_data():
    """이스라엘 백성의 반응 데이터를 생성합니다."""
    data = {
        'response_id': [1, 2, 3, 4, 5],
        'event_id': [1, 2, 3, 4, 5],
        'response_type': ['Awe', 'Worship', 'Fear', 'Shout', 'Fell on faces'],
        'emotional_level': [8, 9, 7, 8, 9]
    }
    df = pd.DataFrame(data)
    return df
