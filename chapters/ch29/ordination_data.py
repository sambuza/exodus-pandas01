import pandas as pd
import numpy as np

class OrdinationDataGenerator:
    """
    위임식 챕터(ch29)를 위한 샘플 데이터를 생성하는 클래스.
    데이터 샘플링 및 훈련/테스트 분할에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Ordination chapter (ch29).
    Generates data to be used for data sampling and train/test splitting.
    """

    def generate_ordination_data(self) -> pd.DataFrame:
        """
        데이터 샘플링 및 훈련/테스트 분할에 사용될 샘플 데이터를 생성합니다.

        Generates sample data to be used for data sampling and train/test splitting.

        Returns:
            pd.DataFrame: 샘플 데이터
        """
        np.random.seed(29)
        data = {
            'disciple_id': range(1, 101),
            'faith_score': np.random.randint(50, 100, size=100),
            'service_hours': np.random.randint(10, 100, size=100),
            'calling_type': np.random.choice(['Apostle', 'Prophet', 'Evangelist', 'Pastor', 'Teacher'], size=100),
            'is_ordained': np.random.choice([True, False], p=[0.3, 0.7], size=100)
        }
        df = pd.DataFrame(data)
        print("OrdinationDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = OrdinationDataGenerator()
    df = generator.generate_ordination_data()
    print(df.head())
    print(df.info())