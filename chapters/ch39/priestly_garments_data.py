import pandas as pd
import numpy as np

class PriestlyGarmentsDataGenerator:
    """
    제사장의 옷(ch39)을 위한 샘플 데이터를 생성하는 클래스.
    에봇, 흉패 등의 제작 과정을 시계열 데이터로 표현합니다.
    """

    def generate_garments_data(self, num_days: int = 30) -> pd.DataFrame:
        """
        제사장의 옷 제작 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(39)
        
        dates = pd.date_range(start='2023-01-01', periods=num_days, freq='D')
        
        data = {
            'date': dates,
            'garment_part': np.random.choice(['Ephod', 'Breastplate', 'Robe', 'Tunic'], size=num_days),
            'progress_percentage': np.sort(np.random.uniform(0, 100, size=num_days)),
            'workers_assigned': np.random.randint(10, 51, size=num_days)
        }
        df = pd.DataFrame(data)
        print("PriestlyGarmentsDataGenerator: 샘플 데이터 생성 완료.")
        return df
