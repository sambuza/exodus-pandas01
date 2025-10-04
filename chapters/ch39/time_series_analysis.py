import pandas as pd

class TimeSeriesAnalysis:
    """
    시계열 분석을 위한 클래스.
    `resample`, `rolling` 등을 사용하여 시계열 데이터를 분석합니다.
    """

    def __init__(self, df: pd.DataFrame, date_column: str):
        self.df = df
        self.date_column = date_column
        self.df[self.date_column] = pd.to_datetime(self.df[self.date_column])
        self.df = self.df.set_index(self.date_column)

    def resample_data(self, rule, agg_func):
        """
        데이터를 리샘플링합니다.
        """
        try:
            resampled_df = self.df.resample(rule).agg(agg_func)
            print(f"TimeSeriesAnalysis: 데이터 리샘플링 완료 (rule={rule}).")
            return resampled_df
        except Exception as e:
            print(f"데이터 리샘플링 중 오류 발생: {e}")
            return None

    def rolling_average(self, window, column):
        """
        이동 평균을 계산합니다.
        """
        try:
            rolling_avg = self.df[column].rolling(window=window).mean()
            print(f"TimeSeriesAnalysis: 이동 평균 계산 완료 (window={window}).")
            return rolling_avg
        except Exception as e:
            print(f"이동 평균 계산 중 오류 발생: {e}")
            return None
