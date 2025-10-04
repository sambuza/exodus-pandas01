import pandas as pd
import numpy as np
from scipy.stats import zscore

class OutlierRemediator:
    """
    데이터프레임의 숫자형 컬럼에서 탐지된 이상치(Outliers)를 처리하는 클래스.
    이상치 제거, 대체, 변환 등의 방법을 제공합니다.

    Class to handle detected outliers in numerical columns of a DataFrame.
    Provides methods for outlier removal, replacement, and transformation.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def remove_outliers_iqr(self, column: str, threshold: float = 1.5) -> pd.DataFrame:
        """
        IQR 방법을 사용하여 지정된 컬럼의 이상치를 제거합니다.

        Removes outliers from the specified column using the IQR method.

        Args:
            column (str): 이상치를 제거할 숫자형 컬럼 이름.
            threshold (float): IQR 곱셈 계수 (일반적으로 1.5).

        Returns:
            pd.DataFrame: 이상치가 제거된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. IQR 이상치 제거를 건너뜁니다.")
            return self.df

        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        df_cleaned = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        print(f"OutlierRemediator: 컬럼 '{column}'에서 IQR 이상치 제거 완료 ({len(self.df) - len(df_cleaned)}개 제거).")
        return df_cleaned

    def replace_outliers_zscore(self, column: str, threshold: float = 3.0, replacement_value='median') -> pd.DataFrame:
        """
        Z-score 방법을 사용하여 지정된 컬럼의 이상치를 대체합니다.

        Replaces outliers in the specified column using the Z-score method.

        Args:
            column (str): 이상치를 대체할 숫자형 컬럼 이름.
            threshold (float): Z-score 임계값.
            replacement_value: 이상치를 대체할 값 ('mean', 'median', 'mode' 또는 특정 숫자).

        Returns:
            pd.DataFrame: 이상치가 대체된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. Z-score 이상치 대체를 건너뜁니다.")
            return self.df

        df_remediated = self.df.copy() 
        
        # Z-score 계산 (결측치 제외)
        col_series = df_remediated[column].dropna()
        z_scores = np.abs(zscore(col_series))
        
        # 이상치 인덱스
        outlier_indices = col_series[z_scores > threshold].index

        if replacement_value == 'mean':
            value = col_series.mean()
        elif replacement_value == 'median':
            value = col_series.median()
        elif replacement_value == 'mode':
            value = col_series.mode()[0]
        else:
            value = replacement_value # 특정 값으로 대체

        df_remediated.loc[outlier_indices, column] = value
        print(f"OutlierRemediator: 컬럼 '{column}'에서 Z-score 이상치 대체 완료 ({len(outlier_indices)}개 대체).")
        return df_remediated

    def transform_outliers_log(self, column: str) -> pd.DataFrame:
        """
        지정된 컬럼에 로그 변환을 적용하여 이상치의 영향을 줄입니다.
        (양수 값에만 적용 가능)

        Applies log transformation to the specified column to reduce outlier impact.
        (Applicable only to positive values)

        Args:
            column (str): 로그 변환할 숫자형 컬럼 이름.

        Returns:
            pd.DataFrame: 로그 변환된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. 로그 변환을 건너뜁니다.")
            return self.df
        
        if (self.df[column] <= 0).any():
            print(f"경고: 컬럼 '{column}'에 0 또는 음수 값이 있어 로그 변환을 적용할 수 없습니다. 건너뜁니다.")
            return self.df

        df_transformed = self.df.copy()
        df_transformed[f'{column}_log'] = np.log(df_transformed[column])
        print(f"OutlierRemediator: 컬럼 '{column}'에 로그 변환 적용 완료.")
        return df_transformed

if __name__ == "__main__":
    # 샘플 데이터 생성 (이상치 포함)
    data = {
        'id': range(1, 11),
        'value': [10, 12, 11, 15, 13, 100, 14, 12, 11, 5], # 100은 이상치
        'score': [50, 55, 52, 58, 53, 51, 54, 56, 57, 200] # 200은 이상치
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    remediator = OutlierRemediator(sample_df)

    # 'value' 컬럼에서 IQR 이상치 제거
    df_removed = remediator.remove_outliers_iqr('value')
    print("\n'value' 컬럼 IQR 이상치 제거 후:")
    print(df_removed)

    # 'score' 컬럼에서 Z-score 이상치 중앙값으로 대체
    df_replaced = remediator.replace_outliers_zscore('score', replacement_value='median')
    print("\n'score' 컬럼 Z-score 이상치 중앙값으로 대체 후:")
    print(df_replaced)

    # 'value' 컬럼 로그 변환
    df_transformed = remediator.transform_outliers_log('value')
    print("\n'value' 컬럼 로그 변환 후:")
    print(df_transformed)
