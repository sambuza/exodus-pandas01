import pandas as pd
import numpy as np

class MaskingOperations:
    """
    데이터프레임에 `mask()`와 `where()` 연산을 적용하는 클래스.
    특정 조건에 따라 데이터를 가리거나 선택적으로 값을 변경합니다.

    Class to apply `mask()` and `where()` operations to a DataFrame.
    Hides data or selectively changes values based on specific conditions.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_masking(self, column: str, condition_value, mask_value) -> pd.DataFrame:
        """
        `mask()` 메서드를 사용하여 지정된 컬럼의 특정 조건에 맞는 값을 가립니다.

        Hides values in the specified column that meet a certain condition using the `mask()` method.

        Args:
            column (str): 마스킹할 컬럼 이름.
            condition_value: 마스킹할 조건 값.
            mask_value: 마스킹할 값 (예: np.nan, 'Masked').

        Returns:
            pd.DataFrame: 마스킹이 적용된 데이터프레임.
        """
        if column not in self.df.columns:
            print(f"경고: 컬럼 '{column}'이 데이터프레임에 존재하지 않습니다. 마스킹을 건너뜁니다.")
            return self.df

        masked_df = self.df.copy()
        masked_df[column] = masked_df[column].mask(masked_df[column] == condition_value, mask_value)
        print(f"MaskingOperations: 컬럼 '{column}'에 mask() 적용 완료.")
        return masked_df

    def apply_where(self, column: str, condition_value, where_value) -> pd.DataFrame:
        """
        `where()` 메서드를 사용하여 지정된 컬럼의 특정 조건에 맞지 않는 값을 변경합니다.

        Changes values in the specified column that do not meet a certain condition using the `where()` method.

        Args:
            column (str): 값을 변경할 컬럼 이름.
            condition_value: 값을 변경하지 않을 조건 값.
            where_value: 조건에 맞지 않을 때 변경할 값.

        Returns:
            pd.DataFrame: `where()` 연산이 적용된 데이터프레임.
        """
        if column not in self.df.columns:
            print(f"경고: 컬럼 '{column}'이 데이터프레임에 존재하지 않습니다. where()를 건너뜁니다.")
            return self.df

        where_df = self.df.copy()
        where_df[column] = where_df[column].where(where_df[column] == condition_value, where_value)
        print(f"MaskingOperations: 컬럼 '{column}'에 where() 적용 완료.")
        return where_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'region': ['Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt'],
        'plague_affected': [True, False, True, False, True],
        'population': [1000, 500, 1200, 600, 1100]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    masker = MaskingOperations(sample_df)

    # 'plague_affected'가 True인 경우 'population'을 0으로 마스킹
    masked_population_df = masker.apply_masking('population', condition_value=1000, mask_value=0)
    print("\n'population' 컬럼 마스킹 후 (plague_affected가 True인 경우):")
    print(masked_population_df)

    # 'region'이 'Goshen'이 아닌 경우 'plague_affected'를 True로 변경
    where_plague_df = masker.apply_where('plague_affected', condition_value=False, where_value=True)
    print("\n'plague_affected' 컬럼 where() 적용 후 (region이 'Goshen'이 아닌 경우):")
    print(where_plague_df)
