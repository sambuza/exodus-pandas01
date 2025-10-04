import pandas as pd
import numpy as np

class MissingValueHandler:
    """
    데이터프레임의 결측치(Missing Values)를 처리하는 클래스.
    `fillna()`와 `dropna()` 메서드를 활용하여 결측치를 채우거나 제거합니다.

    Class to handle missing values in a DataFrame.
    Fills or drops missing values using `fillna()` and `dropna()` methods.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def fill_missing_values(self, column: str, strategy: str = 'mean', fill_value=None) -> pd.DataFrame:
        """
        지정된 컬럼의 결측치를 채웁니다.

        Fills missing values in the specified column.

        Args:
            column (str): 결측치를 채울 컬럼 이름.
            strategy (str): 결측치를 채울 전략 ('mean', 'median', 'mode', 'ffill', 'bfill', 'value').
            fill_value: 'value' 전략 사용 시 채울 값.

        Returns:
            pd.DataFrame: 결측치가 채워진 데이터프레임.
        """
        if column not in self.df.columns:
            print(f"경고: 컬럼 '{column}'이 데이터프레임에 존재하지 않습니다. 결측치 채우기를 건너뜁니다.")
            return self.df

        filled_df = self.df.copy()
        if strategy == 'mean':
            filled_df[column] = filled_df[column].fillna(filled_df[column].mean())
        elif strategy == 'median':
            filled_df[column] = filled_df[column].fillna(filled_df[column].median())
        elif strategy == 'mode':
            filled_df[column] = filled_df[column].fillna(filled_df[column].mode()[0])
        elif strategy == 'ffill':
            filled_df[column] = filled_df[column].fillna(method='ffill')
        elif strategy == 'bfill':
            filled_df[column] = filled_df[column].fillna(method='bfill')
        elif strategy == 'value' and fill_value is not None:
            filled_df[column] = filled_df[column].fillna(fill_value)
        else:
            print(f"경고: 알 수 없는 전략 '{strategy}' 또는 fill_value가 지정되지 않았습니다. 결측치 채우기를 건너뜁니다.")

        print(f"MissingValueHandler: 컬럼 '{column}'의 결측치 채우기 완료 (전략: {strategy}).")
        return filled_df

    def drop_missing_values(self, subset: list = None, how: str = 'any') -> pd.DataFrame:
        """
        결측치가 있는 행이나 열을 제거합니다.

        Drops rows or columns with missing values.

        Args:
            subset (list): 결측치를 확인할 컬럼 이름 리스트.
            how (str): 'any' (하나라도 결측치 있으면 제거) 또는 'all' (모두 결측치여야 제거).

        Returns:
            pd.DataFrame: 결측치가 제거된 데이터프레임.
        """
        dropped_df = self.df.copy()
        dropped_df = dropped_df.dropna(subset=subset, how=how)
        print(f"MissingValueHandler: 결측치가 있는 행 제거 완료 (how: {how}, subset: {subset}).")
        return dropped_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, np.nan],
        'C': [1, 2, 3, np.nan, 5]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)
    print("결측치 개수:\n", sample_df.isnull().sum())

    handler = MissingValueHandler(sample_df)

    # 'A' 컬럼 결측치를 평균으로 채우기
    filled_df_mean = handler.fill_missing_values('A', strategy='mean')
    print("\n'A' 컬럼 결측치 평균으로 채운 후:")
    print(filled_df_mean)

    # 'B' 컬럼 결측치를 0으로 채우기
    filled_df_value = handler.fill_missing_values('B', strategy='value', fill_value=0)
    print("\n'B' 컬럼 결측치 0으로 채운 후:")
    print(filled_df_value)

    # 결측치가 있는 모든 행 제거
    dropped_df_any = handler.drop_missing_values()
    print("\n결측치가 있는 모든 행 제거 후:")
    print(dropped_df_any)

    # 'C' 컬럼에 결측치가 있는 행만 제거
    dropped_df_subset = handler.drop_missing_values(subset=['C'])
    print("\n'C' 컬럼에 결측치가 있는 행만 제거 후:")
    print(dropped_df_subset)
