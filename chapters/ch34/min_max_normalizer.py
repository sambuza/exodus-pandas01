import pandas as pd
import numpy as np

class MinMaxNormalizer:
    """
    데이터프레임의 숫자형 컬럼에 Min-Max 정규화(Normalization)를 적용하는 클래스.
    데이터를 특정 범위(기본값: 0~1)로 조정하여 스케일을 통일합니다.

    Class to apply Min-Max Normalization to numerical columns of a DataFrame.
    Scales data to a specific range (default: 0-1) to unify the scale.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_min_max_scaling(self, column: str, min_val: float = 0, max_val: float = 1) -> pd.DataFrame:
        """
        지정된 컬럼에 Min-Max 정규화를 적용합니다.

        Applies Min-Max scaling to the specified column.

        Args:
            column (str): 정규화할 숫자형 컬럼 이름.
            min_val (float): 정규화 후 데이터의 최솟값.
            max_val (float): 정규화 후 데이터의 최댓값.

        Returns:
            pd.DataFrame: 정규화된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. Min-Max 정규화를 건너뜁니다.")
            return self.df

        normalized_df = self.df.copy()
        
        original_min = normalized_df[column].min()
        original_max = normalized_df[column].max()

        if original_max == original_min: # 모든 값이 동일한 경우 0으로 처리
            normalized_df[f'{column}_minmax'] = min_val
        else:
            normalized_df[f'{column}_minmax'] = (normalized_df[column] - original_min) / (original_max - original_min) * (max_val - min_val) + min_val
        
        print(f"MinMaxNormalizer: 컬럼 '{column}'에 Min-Max 정규화 적용 완료.")
        return normalized_df

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

    normalizer = MinMaxNormalizer(sample_df)

    # 'score' 컬럼을 0-1 범위로 정규화
    normalized_score_df = normalizer.apply_min_max_scaling('score')
    print("\n'score' 컬럼 Min-Max 정규화 후:")
    print(normalized_score_df)

    # 'value' 컬럼을 0-100 범위로 정규화
    normalized_value_df = normalizer.apply_min_max_scaling('value', min_val=0, max_val=100)
    print("\n'value' 컬럼 0-100 범위로 Min-Max 정규화 후:")
    print(normalized_value_df)
