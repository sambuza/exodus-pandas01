import pandas as pd
import numpy as np

class DerivedVariableCreator:
    """
    데이터프레임에 파생변수를 생성하는 클래스.
    `assign` 메서드를 활용하여 새로운 컬럼을 추가합니다.

    Class to create derived variables in a DataFrame.
    Adds new columns using the `assign` method.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def create_variables(self) -> pd.DataFrame:
        """
        기존 컬럼을 기반으로 새로운 파생변수를 생성합니다.
        예: 'value1'과 'value2'를 이용한 'sum_values', 'ratio_values' 등.

        Creates new derived variables based on existing columns.
        E.g., 'sum_values', 'ratio_values' using 'value1' and 'value2'.

        Returns:
            pd.DataFrame: 파생변수가 추가된 데이터프레임.
        """
        derived_df = self.df.assign(
            sum_values=lambda x: x['value1'] + x['value2'],
            ratio_values=lambda x: x['value1'] / (x['value2'] + 1e-6), # 0으로 나누는 오류 방지
            is_high_value1=lambda x: x['value1'] > x['value1'].mean()
        )
        print("DerivedVariableCreator: 파생변수 생성 완료.")
        return derived_df

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

    creator = DerivedVariableCreator(sample_df)
    derived_df = creator.create_variables()
    print("\n파생변수 추가된 데이터:")
    print(derived_df)
