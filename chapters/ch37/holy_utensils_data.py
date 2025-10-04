import pandas as pd
import numpy as np

class HolyUtensilsDataGenerator:
    """
    성막 기구(ch37)를 위한 샘플 데이터를 생성하는 클래스.
    언약궤, 속죄소, 등잔대 등의 제작에 사용된 재료와 무게를 데이터로 표현합니다.
    """

    def generate_utensils_data(self, num_records: int = 10) -> pd.DataFrame:
        """
        성막 기구 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(37)
        
        data = {
            'utensil': ['Ark', 'Mercy Seat', 'Table', 'Lampstand', 'Altar of Incense'] * (num_records // 5),
            'material': np.random.choice(['Gold', 'Acacia Wood', 'Silver'], size=num_records),
            'weight_kg': np.random.uniform(10, 100, size=num_records),
            'purity_percentage': np.random.uniform(90, 100, size=num_records)
        }
        df = pd.DataFrame(data)
        print("HolyUtensilsDataGenerator: 샘플 데이터 생성 완료.")
        return df
