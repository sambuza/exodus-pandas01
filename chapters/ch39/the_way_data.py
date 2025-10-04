import pandas as pd
import numpy as np

class TheWayDataGenerator:
    """
    길, 진리, 생명(ch39)을 위한 샘플 데이터를 생성하는 클래스.
    유일한 구원의 길을 시계열 데이터로 표현합니다.
    """

    def generate_the_way_data(self, num_events: int = 10) -> pd.DataFrame:
        """
        길, 진리, 생명 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(3939)
        
        event_dates = pd.to_datetime(['2023-04-03', '2023-04-05'] * (num_events // 2)) + pd.to_timedelta(np.random.randint(0, 100, size=num_events), unit='D')
        
        data = {
            'event_date': np.sort(event_dates),
            'event': ['Crucifixion', 'Resurrection'] * (num_events // 2),
            'path_to_salvation': ['The Way'] * num_events,
            'truth_revealed': [True] * num_events,
            'life_offered': [True] * num_events
        }
        df = pd.DataFrame(data)
        print("TheWayDataGenerator: 샘플 데이터 생성 완료.")
        return df
