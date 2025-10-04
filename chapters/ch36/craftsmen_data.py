import pandas as pd
import numpy as np

class CraftsmenDataGenerator:
    """
    성막 건축 장인(ch36)을 위한 샘플 데이터를 생성하는 클래스.
    브살렐과 오홀리압과 같은 장인들의 기술, 헌신, 역할을 데이터로 표현합니다.
    """

    def generate_craftsmen_data(self, num_records: int = 10) -> pd.DataFrame:
        """
        장인 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(36)
        
        data = {
            'craftsman_id': range(1, num_records + 1),
            'name': ['Bezalel', 'Oholiab'] + [f'Craftsman_{i}' for i in range(num_records - 2)],
            'skill': np.random.choice(['Goldwork', 'Weaving', 'Woodwork', 'Engraving', 'Stonework'], size=num_records),
            'wisdom_score': np.random.randint(80, 101, size=num_records),
            'dedication_hours': np.random.randint(40, 81, size=num_records)
        }
        df = pd.DataFrame(data)
        print("CraftsmenDataGenerator: 샘플 데이터 생성 완료.")
        return df
