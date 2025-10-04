import pandas as pd
import numpy as np

class TimeSeriesAnalyzer:
    """
    시계열 데이터에 대한 기본적인 분석을 수행하는 클래스.
    이동 평균, 추세, 계절성 등의 패턴을 탐색합니다.

    Class to perform basic analysis on time-series data.
    Explores patterns such as moving averages, trends, and seasonality.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        if not isinstance(self.df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame must have a DatetimeIndex for time series analysis.")

    def perform_analysis(self, column: str = 'incense_amount', window: int = 7) -> dict:
        """
        지정된 컬럼에 대해 기본적인 시계열 분석을 수행합니다.
        이동 평균, 총합, 평균 등을 계산합니다.

        Performs basic time-series analysis on the specified column.
        Calculates moving averages, total sums, means, etc.

        Args:
            column (str): 분석할 시계열 컬럼 이름.
            window (int): 이동 평균 계산을 위한 윈도우 크기.

        Returns:
            dict: 분석 결과를 담은 딕셔너리.
        """
        if column not in self.df.columns:
            raise ValueError(f"컬럼 '{column}'이 데이터프레임에 존재하지 않습니다.")

        analysis_results = {}

        # 이동 평균
        self.df[f'{column}_rolling_mean'] = self.df[column].rolling(window=window).mean()
        analysis_results['rolling_mean_head'] = self.df[f'{column}_rolling_mean'].head().to_dict()
        analysis_results['rolling_mean_tail'] = self.df[f'{column}_rolling_mean'].tail().to_dict()

        # 총합
        analysis_results['total_sum'] = self.df[column].sum()

        # 평균
        analysis_results['average'] = self.df[column].mean()

        print("TimeSeriesAnalyzer: 시계열 분석 완료.")
        return analysis_results

if __name__ == "__main__":
    # 샘플 시계열 데이터 생성
    dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
    data = {
        'incense_amount': np.random.randint(10, 50, size=30) + np.random.rand(30),
        'prayer_count': np.random.randint(50, 200, size=30)
    }
    sample_df = pd.DataFrame(data, index=dates)
    print("원본 시계열 데이터 (일부):")
    print(sample_df.head())

    analyzer = TimeSeriesAnalyzer(sample_df)
    results = analyzer.perform_analysis(column='incense_amount')
    print("\n시계열 분석 결과:")
    print(results)
