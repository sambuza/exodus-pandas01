import pandas as pd

class ColumnConflictResolver:
    """
    `pd.merge()` 메서드의 `suffixes` 파라미터를 사용하여
    데이터 결합 시 발생하는 컬럼 이름 충돌을 해결하는 클래스.

    Class to resolve column name conflicts during data merging
    using the `suffixes` parameter of the `pd.merge()` method.
    """

    def __init__(self, left_df: pd.DataFrame, right_df: pd.DataFrame):
        self.left_df = left_df.copy()
        self.right_df = right_df.copy()

    def resolve_column_conflicts(self, on: str or list, how: str = 'inner', suffixes: tuple = ('_left', '_right')) -> pd.DataFrame:
        """
        두 데이터프레임을 결합하고 `suffixes` 파라미터를 사용하여 컬럼 이름 충돌을 해결합니다.

        Merges two DataFrames and resolves column name conflicts using the `suffixes` parameter.

        Args:
            on (str or list): 결합 기준으로 사용할 컬럼 이름(들).
            how (str): 결합 방식 ('left', 'right', 'outer', 'inner').
            suffixes (tuple): 충돌하는 컬럼 이름에 붙일 접미사 튜플 (예: ('_left', '_right')).

        Returns:
            pd.DataFrame: 컬럼 이름 충돌이 해결된 결합 데이터프레임.
        """
        merged_df = pd.merge(self.left_df, self.right_df, on=on, how=how, suffixes=suffixes)
        print(f"ColumnConflictResolver: `merge()` with `suffixes={suffixes}` 적용 완료.")
        return merged_df

if __name__ == "__main__":
    # 샘플 데이터 생성 (컬럼 이름 충돌 유발)
    df_left = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30], 'score': [100, 200, 300]})
    df_right = pd.DataFrame({'id': [3, 4, 5], 'value': [300, 400, 500], 'score': [600, 700, 800]})
    
    print("Left DataFrame:")
    print(df_left)
    print("\nRight DataFrame:")
    print(df_right)

    resolver = ColumnConflictResolver(df_left, df_right)

    # suffixes를 사용하여 컬럼 이름 충돌 해결
    merged_df = resolver.resolve_column_conflicts(on='id', how='inner', suffixes=('_df1', '_df2'))
    print("\nMerge with Suffixes:")
    print(merged_df)
