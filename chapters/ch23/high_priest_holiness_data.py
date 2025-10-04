import pandas as pd

def get_jesus_attributes_data():
    """대제사장 예수님의 속성 데이터를 생성합니다."""
    data = {
        'attribute': ['Holy', 'Blameless', 'Undefiled', 'Separated from sinners', 'Exalted above the heavens'],
        'description': [
            'Perfectly holy, without sin',
            'Without fault or imperfection',
            'Pure and uncorrupted',
            'Distinct from sinful humanity',
            'Superior to all creation'
        ],
        'scripture_ref': [
            'Hebrews 7:26', 'Hebrews 7:26', 'Hebrews 7:26', 'Hebrews 7:26', 'Hebrews 7:26'
        ]
    }
    df = pd.DataFrame(data)
    return df

def get_sin_offering_data():
    """죄 사함 제물 데이터를 생성합니다."""
    data = {
        'offering_type': ['Old Covenant', 'Old Covenant', 'New Covenant'],
        'priest': ['Aaron', 'Levitical Priests', 'Jesus'],
        'frequency': ['Annually', 'Daily', 'Once for all'],
        'effectiveness': ['Temporary', 'Temporary', 'Eternal']
    }
    df = pd.DataFrame(data)
    return df
