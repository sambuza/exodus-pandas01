import pandas as pd
import numpy as np

class AltarDataGenerator:
    """
    번제단 챕터(ch27)를 위한 샘플 데이터를 생성하는 클래스.
    파생변수 생성 및 전처리에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Altar chapter (ch27).
    Generates data to be used for derived variable creation and preprocessing.
    """

    def generate_altar_data(self) -> pd.DataFrame:
        """
        파생변수 생성 및 전처리에 사용될 샘플 데이터를 생성합니다.

        Generates sample data to be used for derived variable creation and preprocessing.

        Returns:
            pd.DataFrame: 샘플 데이터
        """
        np.random.seed(27)
        data = {
            'id': range(1, 11),
            'value1': np.random.randint(10, 100, size=10),
            'value2': np.random.rand(10) * 50,
            'category': np.random.choice(['A', 'B', 'C'], size=10),
            'timestamp': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.arange(10), unit='D')
        }
        df = pd.DataFrame(data)
        print("AltarDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = AltarDataGenerator()
    df = generator.generate_altar_data()
    print(df)