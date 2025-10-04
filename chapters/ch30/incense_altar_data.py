import pandas as pd
import numpy as np

class IncenseAltarDataGenerator:
    """
    분향단과 계수 챕터(ch30)를 위한 샘플 시계열 데이터를 생성하는 클래스.
    시간 기반 데이터 분석에 사용될 데이터를 생성합니다.

    Class to generate sample time-series data for the Altar of Incense and Census chapter (ch30).
    Generates data to be used for time-based data analysis.
    """

    def generate_incense_data(self, start_date='2023-01-01', periods=100, freq='D') -> pd.DataFrame:
        """
        시계열 데이터를 생성합니다.
        예: 일별 향 소비량, 인구 계수 등.

        Generates time-series data.
        E.g., daily incense consumption, population census.

        Args:
            start_date (str): 시작 날짜.
            periods (int): 생성할 기간의 수.
            freq (str): 시간 간격 (예: 'D' for daily, 'H' for hourly).

        Returns:
            pd.DataFrame: 시계열 데이터.
        """
        np.random.seed(30)
        dates = pd.date_range(start=start_date, periods=periods, freq=freq)
        data = {
            'timestamp': dates,
            'incense_amount': np.random.randint(10, 50, size=periods) + np.random.rand(periods),
            'prayer_count': np.random.randint(50, 200, size=periods),
            'offering_value': np.random.rand(periods) * 1000
        }
        df = pd.DataFrame(data)
        df = df.set_index('timestamp')
        print("IncenseAltarDataGenerator: 샘플 시계열 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = IncenseAltarDataGenerator()
    df = generator.generate_incense_data()
    print(df.head())
    print(df.info())