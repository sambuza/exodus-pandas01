import pandas as pd
import numpy as np

class OfferingDataGenerator:
    """
    자원 봉헌 챕터(ch35)를 위한 샘플 데이터를 생성하는 클래스.
    다양한 형식의 데이터 입출력(IO)에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Offering of Resources chapter (ch35).
    Generates data to be used for various data input/output (IO) operations.
    """

    def generate_offering_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        자원 봉헌과 관련된 샘플 데이터를 생성합니다.
        예: 봉헌자 ID, 예물 종류, 수량, 가치 등.

        Generates sample data related to voluntary offerings.
        E.g., offerer ID, type of offering, quantity, value.

        Args:
            num_records (int): 생성할 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(35)
        
        data = {
            'offerer_id': range(1, num_records + 1),
            'offering_type': np.random.choice(['Gold', 'Silver', 'Bronze', 'Fine Linen', 'Acacia Wood', 'Gemstone'], size=num_records, p=[0.2, 0.15, 0.15, 0.2, 0.15, 0.15]),
            'quantity': np.random.randint(1, 100, size=num_records),
            'value_shekels': np.random.rand(num_records) * 1000 + 10,
            'voluntary': np.random.choice([True, False], size=num_records, p=[0.8, 0.2]),
            'offering_date': pd.to_datetime('1446-01-01') + pd.to_timedelta(np.random.randint(0, 365, size=num_records), unit='D')
        }
        df = pd.DataFrame(data)

        # 오병이어 관련 데이터 추가 (예시)
        df['loaves'] = np.random.randint(0, 5, size=num_records)
        df['fishes'] = np.random.randint(0, 2, size=num_records)

        print("OfferingDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = OfferingDataGenerator()
    df = generator.generate_offering_data()
    print(df.head())
    print(df.info())