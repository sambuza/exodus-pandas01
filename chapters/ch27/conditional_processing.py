import pandas as pd
import numpy as np

class ConditionalProcessor:
    """
    데이터프레임에 조건부 처리를 적용하는 클래스.
    `np.where`를 활용하여 특정 조건에 따라 값을 변경하거나 새로운 컬럼을 생성합니다.

    Class to apply conditional processing to a DataFrame.
    Uses `np.where` to change values or create new columns based on specific conditions.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_conditions(self) -> pd.DataFrame:
        """
        데이터프레임에 조건부 로직을 적용합니다.
        예: 'value1'이 특정 값 이상이면 'high', 아니면 'low'로 분류.

        Applies conditional logic to the DataFrame.
        E.g., classifies 'value1' as 'high' if above a certain threshold, else 'low'.

        Returns:
            pd.DataFrame: 조건부 처리가 적용된 데이터프레임.
        """
        processed_df = self.df.copy()
        processed_df['value1_level'] = np.where(
            processed_df['value1'] >= processed_df['value1'].mean(),
            'high',
            'low'
        )
        processed_df['adjusted_value2'] = np.where(
            processed_df['category'] == 'A',
            processed_df['value2'] * 1.5,
            processed_df['value2']
        )
        print("ConditionalProcessor: 조건부 처리 적용 완료.")
        return processed_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'value1': np.random.randint(10, 100, size=5),
        'value2': np.random.rand(5) * 50,
        'category': np.random.choice(['A', 'B', 'C'], size=5)
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    processor = ConditionalProcessor(sample_df)
    processed_df = processor.apply_conditions()
    print("\n조건부 처리된 데이터:")
    print(processed_df)
