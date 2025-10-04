import pandas as pd
import numpy as np

class TabernacleDedicationDataGenerator:
    """
    성막 봉헌(ch40)을 위한 샘플 데이터를 생성하는 클래스.
    성막의 각 부분에 대한 봉헌 상태를 데이터로 표현합니다.
    """

    def generate_dedication_data(self, num_items: int = 10) -> pd.DataFrame:
        """
        성막 봉헌 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(40)
        
        data = {
            'item': ['Ark', 'Table', 'Lampstand', 'Altar of Incense', 'Altar of Burnt Offering', 'Laver', 'Courtyard', 'Holy Garments', 'Anointing Oil', 'Incense'],
            'status': np.random.choice(['Not Consecrated', 'Consecrated'], size=num_items, p=[0.3, 0.7]),
            'consecration_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 30, size=num_items), unit='D')
        }
        df = pd.DataFrame(data)
        print("TabernacleDedicationDataGenerator: 샘플 데이터 생성 완료.")
        return df
