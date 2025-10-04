import pandas as pd
import numpy as np
from scipy.stats import zscore

class OutlierDetector:
    """
    데이터프레임의 숫자형 컬럼에서 이상치(Outliers)를 탐지하는 클래스.
    IQR(사분위 범위)과 Z-score(표준점수) 방법을 활용합니다.

    Class to detect outliers in numerical columns of a DataFrame.
    Utilizes IQR (Interquartile Range) and Z-score methods.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def detect_outliers_iqr(self, column: str, threshold: float = 1.5) -> pd.DataFrame:
        """
        IQR 방법을 사용하여 지정된 컬럼에서 이상치를 탐지합니다.

        Detects outliers in the specified column using the IQR method.

        Args:
            column (str): 이상치를 탐지할 숫자형 컬럼 이름.
            threshold (float): IQR 곱셈 계수 (일반적으로 1.5).

        Returns:
            pd.DataFrame: 탐지된 이상치들을 포함하는 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. IQR 이상치 탐지를 건너뜁니다.")
            return pd.DataFrame()

        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        outliers = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
        print(f"OutlierDetector: 컬럼 '{column}'에서 IQR 이상치 탐지 완료 ({len(outliers)}개).")
        return outliers

    def detect_outliers_zscore(self, column: str, threshold: float = 3.0) -> pd.DataFrame:
        """
        Z-score 방법을 사용하여 지정된 컬럼에서 이상치를 탐지합니다.

        Detects outliers in the specified column using the Z-score method.

        Args:
            column (str): 이상치를 탐지할 숫자형 컬럼 이름.
            threshold (float): Z-score 임계값 (일반적으로 2.0 또는 3.0).

        Returns:
            pd.DataFrame: 탐지된 이상치들을 포함하는 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 숫자형이 아닙니다. Z-score 이상치 탐지를 건너뜁니다.")
            return pd.DataFrame()

        # 결측치 제외하고 Z-score 계산
        z_scores = np.abs(zscore(self.df[column].dropna()))
        outliers = self.df[z_scores > threshold]
        print(f"OutlierDetector: 컬럼 '{column}'에서 Z-score 이상치 탐지 완료 ({len(outliers)}개).")
        return outliers

if __name__ == "__main__":
    # 샘플 데이터 생성 (이상치 포함)
    data = {
        'id': range(1, 11),
        'value': [10, 12, 11, 15, 13, 100, 14, 12, 11, -5], # 100과 -5는 이상치
        'score': [50, 55, 52, 58, 53, 51, 54, 56, 57, 200] # 200은 이상치
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    detector = OutlierDetector(sample_df)

    # 'value' 컬럼에서 IQR 이상치 탐지
    iqr_outliers_value = detector.detect_outliers_iqr('value')
    print("\n'value' 컬럼 IQR 이상치:")
    print(iqr_outliers_value)

    # 'score' 컬럼에서 Z-score 이상치 탐지
    zscore_outliers_score = detector.detect_outliers_zscore('score')
    print("\n'score' 컬럼 Z-score 이상치:")
    print(zscore_outliers_score)
