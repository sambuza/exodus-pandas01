import pandas as pd

def get_temple_body_attributes():
    """예수님의 몸된 성전의 속성 데이터를 생성합니다."""
    data = {
        'aspect': ['Divine', 'Divine', 'Human', 'Human', 'Spiritual', 'Spiritual'],
        'attribute': ['Holiness', 'Power', 'Suffering', 'Sacrifice', 'Indwelling', 'Transformation'],
        'description': [
            'Perfectly holy, without sin',
            'Authority over all creation',
            'Experienced human pain and temptation',
            'Offered Himself as a perfect sacrifice',
            'Holy Spirit dwells in believers',
            'Believers are transformed into His likeness'
        ],
        'scripture_ref': [
            'Hebrews 7:26', 'Matthew 28:18', 'Hebrews 4:15', 
            'Ephesians 5:2', '1 Corinthians 6:19', '2 Corinthians 3:18'
        ]
    }
    df = pd.DataFrame(data)
    return df

def get_believers_growth_stages():
    """성도들의 영적 성장 단계 데이터를 생성합니다."""
    data = {
        'stage': ['Infant', 'Child', 'Youth', 'Adult'],
        'characteristic': ['Needs milk', 'Learning basics', 'Strong in faith', 'Teaching others'],
        'focus': ['Self', 'Rules', 'Relationship', 'Mission']
    }
    df = pd.DataFrame(data)
    return df
