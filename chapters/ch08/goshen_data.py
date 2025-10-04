import pandas as pd
import numpy as np

class GoshenDataGenerator:
    """
    고센과 마스킹 챕터(ch08)를 위한 샘플 데이터를 생성하는 클래스.
    재앙 속 구별과 마스킹 연산에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Goshen and Masking chapter (ch08).
    Generates data to be used for distinction in plagues and masking operations.
    """

    def generate_goshen_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        고센 땅의 구별과 관련된 샘플 데이터를 생성합니다.
        예: 지역, 재앙 영향 여부, 인구 밀도 등.

        Generates sample data related to the distinction of Goshen.
        E.g., region, plague affected status, population density.

        Args:
            num_records (int): 생성할 데이터 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(8)
        regions = np.random.choice(['Goshen', 'Egypt'], size=num_records, p=[0.3, 0.7])
        
        data = {
            'location_id': range(1, num_records + 1),
            'region': regions,
            'population_density': np.random.randint(100, 1000, size=num_records),
            'plague_affected': np.where(regions == 'Egypt', np.random.choice([True, False], size=num_records, p=[0.8, 0.2]), False),
            'is_israelite': np.where(regions == 'Goshen', True, False),
            'water_quality_score': np.random.randint(1, 10, size=num_records) # 사마리아 여인과 생수 관련
        }
        df = pd.DataFrame(data)
        print("GoshenDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = GoshenDataGenerator()
    df = generator.generate_goshen_data()
    print(df.head())
    print(df.info())