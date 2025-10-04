import pandas as pd
import numpy as np

class LightOfWorldDataGenerator:
    """
    세상의 빛(ch37)을 위한 샘플 데이터를 생성하는 클래스.
    빛과 어둠의 대비를 데이터로 표현합니다.
    """

    def generate_light_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        빛과 어둠 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(3737)
        
        data = {
            'event_id': range(1, num_records + 1),
            'event_type': np.random.choice(['Light', 'Darkness'], size=num_records, p=[0.7, 0.3]),
            'intensity': np.random.uniform(0, 100, size=num_records),
            'duration_hours': np.random.uniform(1, 12, size=num_records)
        }
        df = pd.DataFrame(data)
        print("LightOfWorldDataGenerator: 샘플 데이터 생성 완료.")
        return df
