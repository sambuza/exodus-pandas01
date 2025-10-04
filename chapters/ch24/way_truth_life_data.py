import pandas as pd

def get_jesus_claims_data():
    """예수님의 '길, 진리, 생명' 주장 데이터를 생성합니다."""
    data = {
        'claim': ['Way', 'Truth', 'Life', 'Light', 'Door'],
        'description': [
            'The only path to the Father',
            'The embodiment of divine reality',
            'The source of eternal existence',
            'Illuminates spiritual darkness',
            'The entrance to salvation'
        ],
        'scripture_ref': [
            'John 14:6', 'John 14:6', 'John 14:6', 'John 8:12', 'John 10:9'
        ],
        'importance_score': [10, 10, 10, 9, 9]
    }
    df = pd.DataFrame(data)
    return df

def get_believers_journey_data():
    """신자들의 영적 여정 데이터를 생성합니다."""
    data = {
        'stage': ['Seeking', 'Believing', 'Following', 'Abiding', 'Witnessing'],
        'progress_score': [6, 7, 8, 9, 8],
        'challenges': ['Doubt', 'Persecution', 'Self-will', 'Distractions', 'Fear']
    }
    df = pd.DataFrame(data)
    return df
