import pandas as pd

class PeriodConverter:
    """
    시계열 데이터를 `Period` 객체로 변환하고 빈도를 변경하는 클래스.
    시간 기반 데이터의 주기성을 분석하는 데 활용됩니다.

    Class to convert time-series data to `Period` objects and change frequency.
    Used for analyzing periodicity in time-based data.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def convert_to_period(self, freq: str = 'M') -> pd.DataFrame:
        """
        데이터프레임의 DatetimeIndex를 PeriodIndex로 변환하고,
        지정된 빈도로 데이터를 리샘플링합니다.

        Converts the DataFrame's DatetimeIndex to PeriodIndex and
        resamples the data to the specified frequency.

        Args:
            freq (str): 변환할 주기 빈도 (예: 'M' for monthly, 'Q' for quarterly).

        Returns:
            pd.DataFrame: PeriodIndex로 변환되고 리샘플링된 데이터프레임.
        """
        if not isinstance(self.df.index, pd.DatetimeIndex):
            print("경고: 데이터프레임 인덱스가 DatetimeIndex가 아닙니다. 변환을 건너뜁니다.")
            return self.df

        # DatetimeIndex를 PeriodIndex로 변환
        period_df = self.df.copy()
        period_df.index = period_df.index.to_period(freq=freq)

        # PeriodIndex를 기준으로 리샘플링 (예: 월별 합계)
        resampled_df = period_df.resample(freq).sum()

        print(f"PeriodConverter: DatetimeIndex를 {freq} PeriodIndex로 변환 및 리샘플링 완료.")
        return resampled_df

if __name__ == "__main__":
    # 샘플 시계열 데이터 생성
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    data = {
        'value': np.random.randint(1, 100, size=100)
    }
    sample_df = pd.DataFrame(data, index=dates)
    print("원본 시계열 데이터 (일부):")
    print(sample_df.head())

    converter = PeriodConverter(sample_df)
    converted_df = converter.convert_to_period(freq='M')
    print("\n월별 PeriodIndex로 변환 및 리샘플링된 데이터:")
    print(converted_df)
