import pandas as pd
import numpy as np

class SalvationSacrificesDataGenerator:
    """
    구원의 희생(ch38)을 위한 샘플 데이터를 생성하는 클래스.
    예수님의 희생과 구원의 완성을 데이터로 표현합니다.
    """

    def generate_sacrifices_data(self, num_records: int = 20) -> pd.DataFrame:
        """
        구원의 희생 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(3838)
        
        data = {
            'sacrifice_type': ['Jesus Christ'] * num_records,
            'cost': [np.inf] * num_records,
            'souls_saved': [np.inf] * num_records,
            'completion_status': ['Finished'] * num_records
        }
        df = pd.DataFrame(data)
        print("SalvationSacrificesDataGenerator: 샘플 데이터 생성 완료.")
        return df
