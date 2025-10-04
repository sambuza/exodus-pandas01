import pandas as pd
import numpy as np

class DataSampler:
    """
    데이터프레임에서 데이터를 샘플링하는 클래스.
    `sample` 메서드를 활용하여 데이터의 일부를 추출합니다.

    Class to sample data from a DataFrame.
    Extracts a subset of data using the `sample` method.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def perform_sampling(self, fraction: float = 0.5, n_samples: int = None, random_state: int = 42) -> pd.DataFrame:
        """
        데이터프레임에서 샘플링을 수행합니다.
        `fraction` 또는 `n_samples` 중 하나를 지정하여 샘플 크기를 결정합니다.

        Performs sampling from the DataFrame.
        Determines sample size by specifying either `fraction` or `n_samples`.

        Args:
            fraction (float): 원본 데이터프레임에서 추출할 비율 (0.0 ~ 1.0).
            n_samples (int): 추출할 샘플의 개수. `fraction`과 함께 사용될 수 없습니다.
            random_state (int): 재현 가능한 샘플링을 위한 시드.

        Returns:
            pd.DataFrame: 샘플링된 데이터프레임.
        """
        if n_samples is not None and not (0.0 <= fraction <= 1.0):
            sampled_df = self.df.sample(n=n_samples, random_state=random_state)
        else:
            sampled_df = self.df.sample(frac=fraction, random_state=random_state)

        print(f"DataSampler: {len(sampled_df)}개의 샘플 데이터 추출 완료.")
        return sampled_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 21),
        'value': np.random.randint(1, 100, size=20),
        'group': np.random.choice(['A', 'B'], size=20)
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터 (일부):")
    print(sample_df.head())

    sampler = DataSampler(sample_df)
    sampled_df_frac = sampler.perform_sampling(fraction=0.3)
    print("\n비율(0.3)로 샘플링된 데이터:")
    print(sampled_df_frac)

    sampled_df_n = sampler.perform_sampling(n_samples=5)
    print("\n개수(5개)로 샘플링된 데이터:")
    print(sampled_df_n)
