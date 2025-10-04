import pandas as pd
import numpy as np

class VeilDataGenerator:
    """
    휘장과 덮개 챕터(ch26)를 위한 샘플 데이터를 생성하는 클래스.
    민감한 정보와 일반 정보를 포함하는 DataFrame을 생성합니다.

    Class to generate sample data for the Veil and Cover chapter (ch26).
    Generates a DataFrame with sensitive and general information.
    """

    def generate_veil_data(self) -> pd.DataFrame:
        """
        컬럼 가림/익명화에 사용될 샘플 데이터를 생성합니다.

        Generates sample data to be used for column hiding/anonymization.

        Returns:
            pd.DataFrame: 샘플 데이터
        """
        np.random.seed(26)
        data = {
            'user_id': range(1, 11),
            'username': [f'user_{i}' for i in range(1, 11)],
            'email': [f'user{i}@example.com' for i in range(1, 11)],
            'sensitive_info': np.random.randint(1000, 9999, size=10),
            'public_data': np.random.rand(10) * 100,
            'status': np.random.choice(['active', 'inactive'], size=10)
        }
        df = pd.DataFrame(data)
        print("VeilDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = VeilDataGenerator()
    df = generator.generate_veil_data()
    print(df)