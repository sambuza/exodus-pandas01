import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class TrainTestSplitter:
    """
    데이터프레임을 훈련 세트와 테스트 세트로 분할하는 클래스.
    머신러닝 모델 학습 및 평가를 위한 기본적인 데이터 분할을 수행합니다.

    Class to split a DataFrame into training and testing sets.
    Performs basic data partitioning for machine learning model training and evaluation.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def split_data(self, test_size: float = 0.2, random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        데이터프레임을 훈련 세트와 테스트 세트로 분할합니다.

        Splits the DataFrame into training and testing sets.

        Args:
            test_size (float): 테스트 세트의 비율 (0.0 ~ 1.0).
            random_state (int): 재현 가능한 분할을 위한 시드.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame]: (훈련 세트, 테스트 세트)
        """
        # 예시를 위해 간단히 모든 컬럼을 특성으로 사용
        X = self.df
        # 실제 사용 시에는 타겟 변수(y)를 분리해야 함
        # 여기서는 분할 기능 자체에 초점을 맞춤
        
        train_df, test_df = train_test_split(X, test_size=test_size, random_state=random_state)

        print(f"TrainTestSplitter: 훈련 세트 {len(train_df)}개, 테스트 세트 {len(test_df)}개로 분할 완료.")
        return train_df, test_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'feature1': np.random.rand(100),
        'feature2': np.random.randint(0, 100, size=100),
        'target': np.random.choice([0, 1], size=100)
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터 (일부):")
    print(sample_df.head())

    splitter = TrainTestSplitter(sample_df)
    train_df, test_df = splitter.split_data(test_size=0.3)
    print("\n훈련 세트 (일부):")
    print(train_df.head())
    print("\n테스트 세트 (일부):")
    print(test_df.head())
