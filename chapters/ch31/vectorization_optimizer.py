import pandas as pd
import numpy as np

class VectorizationOptimizer:
    """
    데이터프레임에 벡터화 연산을 적용하여 성능을 최적화하는 클래스.
    파이썬 루프 대신 NumPy 및 Pandas의 내장 함수를 활용합니다.

    Class to optimize performance by applying vectorized operations to a DataFrame.
    Utilizes NumPy and Pandas built-in functions instead of Python loops.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate_total_time_vectorized(self) -> pd.DataFrame:
        """
        'time_spent_minutes'와 'material_cost'를 사용하여 총 비용을 벡터화하여 계산합니다.
        (예시: 간단한 벡터화 연산)

        Calculates total cost using 'time_spent_minutes' and 'material_cost' in a vectorized manner.
        (Example: simple vectorized operation)

        Returns:
            pd.DataFrame: 총 비용 컬럼이 추가된 데이터프레임.
        """
        if 'time_spent_minutes' not in self.df.columns or 'material_cost' not in self.df.columns:
            print("경고: 'time_spent_minutes' 또는 'material_cost' 컬럼이 없습니다. 벡터화 연산을 건너뜁니다.")
            return self.df

        optimized_df = self.df.copy()
        # 벡터화 연산: 각 작업의 총 비용 (시간 * 재료비 계수)
        optimized_df['total_cost'] = optimized_df['time_spent_minutes'] * (optimized_df['material_cost'] / 100)
        print("VectorizationOptimizer: 총 비용 벡터화 연산 완료.")
        return optimized_df

    def apply_complex_vectorization(self) -> pd.DataFrame:
        """
        더 복잡한 벡터화 연산을 적용합니다.
        (예: 조건부 벡터화 연산)

        Applies more complex vectorized operations.
        (Example: conditional vectorized operation)

        Returns:
            pd.DataFrame: 복잡한 벡터화 연산이 적용된 데이터프레임.
        """
        if 'quality_score' not in self.df.columns:
            print("경고: 'quality_score' 컬럼이 없습니다. 복잡한 벡터화 연산을 건너뜁니다.")
            return self.df

        optimized_df = self.df.copy()
        # 품질 점수에 따라 보너스 점수 부여 (벡터화된 np.where 사용)
        optimized_df['bonus_score'] = np.where(optimized_df['quality_score'] > 90, 10, 0)
        print("VectorizationOptimizer: 복잡한 벡터화 연산 완료 (bonus_score).")
        return optimized_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'task_id': range(1, 11),
        'time_spent_minutes': np.random.randint(10, 300, size=10),
        'material_cost': np.random.rand(10) * 1000 + 50,
        'quality_score': np.random.randint(70, 100, size=10)
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    optimizer = VectorizationOptimizer(sample_df)

    # 총 비용 벡터화 연산
    df_with_cost = optimizer.calculate_total_time_vectorized()
    print("\n총 비용 벡터화 연산 후:")
    print(df_with_cost.head())

    # 복잡한 벡터화 연산 (보너스 점수)
    df_with_bonus = optimizer.apply_complex_vectorization()
    print("\n복잡한 벡터화 연산 (보너스 점수) 후:")
    print(df_with_bonus.head())
