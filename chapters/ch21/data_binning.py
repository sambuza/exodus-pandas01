import pandas as pd
import numpy as np

class DataBinner:
    """
    데이터프레임의 숫자형 컬럼을 구간(bins)으로 나누어 범주화하는 클래스.
    `pd.cut()`과 `pd.qcut()`을 활용하여 데이터를 분류합니다.

    Class to categorize numerical columns of a DataFrame into bins.
    Classifies data using `pd.cut()` and `pd.qcut()`.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_cut_binning(self, column: str, bins: int = 3, labels: list = None) -> pd.DataFrame:
        """
        `pd.cut()`을 사용하여 지정된 컬럼을 고정된 구간으로 나눕니다.

        Divides the specified column into fixed bins using `pd.cut()`.

        Args:
            column (str): 구간화할 숫자형 컬럼 이름.
            bins (int): 나눌 구간의 수.
            labels (list): 각 구간에 부여할 라벨 리스트.

        Returns:
            pd.DataFrame: 구간화된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. pd.cut()을 건너뜁니다.")
            return self.df

        binned_df = self.df.copy()
        binned_df[f'{column}_cut_bin'] = pd.cut(binned_df[column], bins=bins, labels=labels)
        print(f"DataBinner: 컬럼 '{column}'에 pd.cut() 적용 완료.")
        return binned_df

    def apply_qcut_binning(self, column: str, q: int = 4, labels: list = None) -> pd.DataFrame:
        """
        `pd.qcut()`을 사용하여 지정된 컬럼을 동일한 빈도로 나눕니다.

        Divides the specified column into equal-frequency bins using `pd.qcut()`.

        Args:
            column (str): 구간화할 숫자형 컬럼 이름.
            q (int): 나눌 분위수(quantile)의 수.
            labels (list): 각 분위수에 부여할 라벨 리스트.

        Returns:
            pd.DataFrame: 분위수화된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. pd.qcut()을 건너뜁니다.")
            return self.df

        binned_df = self.df.copy()
        binned_df[f'{column}_qcut_bin'] = pd.qcut(binned_df[column], q=q, labels=labels)
        print(f"DataBinner: 컬럼 '{column}'에 pd.qcut() 적용 완료.")
        return binned_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 11),
        'score': np.random.randint(0, 100, size=10),
        'value': np.random.rand(10) * 100
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    binner = DataBinner(sample_df)

    # pd.cut 적용
    df_cut = binner.apply_cut_binning('score', bins=3, labels=['Low', 'Medium', 'High'])
    print("\npd.cut() 적용 후:")
    print(df_cut[['score', 'score_cut_bin']])

    # pd.qcut 적용
    df_qcut = binner.apply_qcut_binning('value', q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    print("\npd.qcut() 적용 후:")
    print(df_qcut[['value', 'value_qcut_bin']])
