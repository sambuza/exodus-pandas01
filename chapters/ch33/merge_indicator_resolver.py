import pandas as pd

class MergeIndicatorResolver:
    """
    `pd.merge()` 메서드의 `indicator` 파라미터를 사용하여
    데이터 결합의 출처를 확인하고 데이터 불일치를 파악하는 클래스.

    Class to identify the source of data joins and detect data discrepancies
    using the `indicator` parameter of the `pd.merge()` method.
    """

    def __init__(self, left_df: pd.DataFrame, right_df: pd.DataFrame):
        self.left_df = left_df.copy()
        self.right_df = right_df.copy()

    def resolve_with_indicator(self, on: str or list, how: str = 'outer') -> pd.DataFrame:
        """
        두 데이터프레임을 결합하고 `_merge` 컬럼을 통해 각 행의 출처를 표시합니다.

        Merges two DataFrames and indicates the source of each row via the `_merge` column.

        Args:
            on (str or list): 결합 기준으로 사용할 컬럼 이름(들).
            how (str): 결합 방식 ('left', 'right', 'outer', 'inner').

        Returns:
            pd.DataFrame: `_merge` 컬럼이 추가된 결합 데이터프레임.
        """
        merged_df = pd.merge(self.left_df, self.right_df, on=on, how=how, indicator=True)
        print(f"MergeIndicatorResolver: `merge()` with `indicator=True` 적용 완료 (how='{how}').")
        return merged_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    df_left = pd.DataFrame({'id': [1, 2, 3, 4], 'value_left': [10, 20, 30, 40]})
    df_right = pd.DataFrame({'id': [3, 4, 5, 6], 'value_right': [300, 400, 500, 600]})
    
    print("Left DataFrame:")
    print(df_left)
    print("\nRight DataFrame:")
    print(df_right)

    resolver = MergeIndicatorResolver(df_left, df_right)

    # outer join with indicator
    merged_outer = resolver.resolve_with_indicator(on='id', how='outer')
    print("\nOuter Merge with Indicator:")
    print(merged_outer)
    print("\n_merge value counts:")
    print(merged_outer['_merge'].value_counts())

    # inner join with indicator
    merged_inner = resolver.resolve_with_indicator(on='id', how='inner')
    print("\nInner Merge with Indicator:")
    print(merged_inner)
