import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class ReproducibleSplitter:
    """
    재현 가능한 훈련/테스트 데이터 분할을 시연하는 클래스.
    `random_state`를 고정하여 동일한 분할 결과를 보장합니다.

    Class to demonstrate reproducible train/test data splitting.
    Ensures identical split results by fixing `random_state`.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def split_data_reproducibly(self, test_size: float = 0.2, random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        고정된 `random_state`를 사용하여 데이터프레임을 훈련 세트와 테스트 세트로 분할합니다.

        Splits the DataFrame into training and testing sets using a fixed `random_state`.

        Args:
            test_size (float): 테스트 세트의 비율 (0.0 ~ 1.0).
            random_state (int): 재현 가능한 분할을 위한 시드.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame]: (훈련 세트, 테스트 세트)
        """
        train_df, test_df = train_test_split(self.df, test_size=test_size, random_state=random_state)

        print(f"ReproducibleSplitter: 고정된 random_state({random_state})로 훈련 세트 {len(train_df)}개, 테스트 세트 {len(test_df)}개로 분할 완료.")
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

    splitter1 = ReproducibleSplitter(sample_df)
    train_df1, test_df1 = splitter1.split_data_reproducibly(test_size=0.3, random_state=123)
    print("\n첫 번째 재현 가능한 분할 (random_state=123) - 훈련 세트 헤드:")
    print(train_df1.head())

    splitter2 = ReproducibleSplitter(sample_df)
    train_df2, test_df2 = splitter2.split_data_reproducibly(test_size=0.3, random_state=123)
    print("\n두 번째 재현 가능한 분할 (random_state=123) - 훈련 세트 헤드:")
    print(train_df2.head())

    # 두 분할 결과가 동일한지 확인
    print("\n두 훈련 세트가 동일한가요?", train_df1.equals(train_df2))