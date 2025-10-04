import pandas as pd
import numpy as np

class ConstructionCostsDataGenerator:
    """
    성막 건축 비용(ch38)을 위한 샘플 데이터를 생성하는 클래스.
    놋제단, 성막 뜰 등의 건축 비용을 데이터로 표현합니다.
    """

    def generate_costs_data(self, num_records: int = 50) -> pd.DataFrame:
        """
        성막 건축 비용 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(38)
        
        data = {
            'item': np.random.choice(['Bronze Altar', 'Courtyard Pillars', 'Bronze Basin', 'Silver Sockets', 'Gold Hooks'], size=num_records),
            'material': np.random.choice(['Bronze', 'Silver', 'Gold', 'Acacia Wood'], size=num_records),
            'cost_shekels': np.random.uniform(100, 5000, size=num_records),
            'quantity': np.random.randint(1, 100, size=num_records)
        }
        df = pd.DataFrame(data)
        print("ConstructionCostsDataGenerator: 샘플 데이터 생성 완료.")
        return df
