import pandas as pd
import numpy as np

class TabernacleConstructionDataGenerator:
    """
    성막 건축(ch36)을 위한 샘플 데이터를 생성하는 클래스.
    성막의 각 부분, 필요한 재료, 담당 장인 등의 정보를 데이터로 표현합니다.
    """

    def generate_construction_data(self, num_records: int = 20) -> pd.DataFrame:
        """
        성막 건축 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(3636)
        
        data = {
            'task_id': range(1, num_records + 1),
            'component': np.random.choice(['Ark', 'Table', 'Lampstand', 'Altar', 'Curtains', 'Pillars'], size=num_records),
            'material': np.random.choice(['Gold', 'Silver', 'Bronze', 'Acacia Wood', 'Fine Linen'], size=num_records),
            'quantity_needed': np.random.randint(1, 100, size=num_records),
            'assigned_craftsman_id': np.random.randint(1, 11, size=num_records)
        }
        df = pd.DataFrame(data)
        print("TabernacleConstructionDataGenerator: 샘플 데이터 생성 완료.")
        return df
