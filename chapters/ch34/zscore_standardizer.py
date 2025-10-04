import pandas as pd
import numpy as np

class ZscoreStandardizer:
    """
    데이터프레임의 숫자형 컬럼에 Z-score 표준화(Standardization)를 적용하는 클래스.
    데이터를 평균 0, 표준편차 1을 가지도록 조정하여 분포를 통일합니다.

    Class to apply Z-score Standardization to numerical columns of a DataFrame.
    Adjusts data to have a mean of 0 and a standard deviation of 1, unifying the distribution.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_zscore_standardization(self, column: str) -> pd.DataFrame:
        """
        지정된 컬럼에 Z-score 표준화를 적용합니다.

        Applies Z-score standardization to the specified column.

        Args:
            column (str): 표준화할 숫자형 컬럼 이름.

        Returns:
            pd.DataFrame: 표준화된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. Z-score 표준화를 건너뜁니다.")
            return self.df

        standardized_df = self.df.copy()
        
        mean_val = standardized_df[column].mean()
        std_val = standardized_df[column].std()

        if std_val == 0: # 표준편차가 0인 경우 (모든 값이 동일)
            standardized_df[f'{column}_zscore'] = 0.0
        else:
            standardized_df[f'{column}_zscore'] = (standardized_df[column] - mean_val) / std_val
        
        print(f"ZscoreStandardizer: 컬럼 '{column}'에 Z-score 표준화 적용 완료.")
        return standardized_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'score': [10, 20, 30, 40, 50],
        'value': [100, 200, 50, 300, 150]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    standardizer = ZscoreStandardizer(sample_df)

    # 'score' 컬럼 Z-score 표준화
    standardized_score_df = standardizer.apply_zscore_standardization('score')
    print("\n'score' 컬럼 Z-score 표준화 후:")
    print(standardized_score_df)

    # 'value' 컬럼 Z-score 표준화
    standardized_value_df = standardizer.apply_zscore_standardization('value')
    print("\n'value' 컬럼 Z-score 표준화 후:")
    print(standardized_value_df)
