import pandas as pd

class MergeValidator:
    """
    `pd.merge()` 메서드의 `validate` 파라미터를 사용하여
    데이터 결합의 유효성을 검사하고 잘못된 결합을 방지하는 클래스.

    Class to validate data joins and prevent incorrect merges
    using the `validate` parameter of the `pd.merge()` method.
    """

    def __init__(self, left_df: pd.DataFrame, right_df: pd.DataFrame):
        self.left_df = left_df.copy()
        self.right_df = right_df.copy()

    def validate_merge(self, on: str or list, how: str = 'inner', validate: str = 'one_to_one') -> pd.DataFrame:
        """
        두 데이터프레임을 결합하고 `validate` 파라미터를 사용하여 결합의 유효성을 검사합니다.

        Merges two DataFrames and validates the join using the `validate` parameter.

        Args:
            on (str or list): 결합 기준으로 사용할 컬럼 이름(들).
            how (str): 결합 방식 ('left', 'right', 'outer', 'inner').
            validate (str): 결합 키의 관계를 검사하는 방법 ('one_to_one', 'one_to_many', 'many_to_one', 'many_to_many').

        Returns:
            pd.DataFrame: 유효성 검사를 통과한 결합 데이터프레임.
        """
        try:
            merged_df = pd.merge(self.left_df, self.right_df, on=on, how=how, validate=validate)
            print(f"MergeValidator: `merge()` with `validate='{validate}'` 적용 완료.")
            return merged_df
        except Exception as e:
            print(f"❌ `merge()` with `validate='{validate}'` 적용 중 오류 발생: {e}")
            return pd.DataFrame()

if __name__ == "__main__":
    # 샘플 데이터 생성
    df_left = pd.DataFrame({'id': [1, 2, 3], 'value_left': [10, 20, 30]})
    df_right = pd.DataFrame({'id': [3, 4, 5], 'value_right': [300, 400, 500]})
    
    print("Left DataFrame:")
    print(df_left)
    print("\nRight DataFrame:")
    print(df_right)

    validator = MergeValidator(df_left, df_right)

    # one_to_one 유효성 검사 (성공)
    merged_one_to_one = validator.validate_merge(on='id', how='inner', validate='one_to_one')
    print("\nOne-to-One Validated Merge (Success):")
    print(merged_one_to_one)

    # one_to_one 유효성 검사 (실패 시뮬레이션)
    df_left_duplicate = pd.DataFrame({'id': [1, 2, 3, 3], 'value_left': [10, 20, 30, 35]})
    validator_duplicate = MergeValidator(df_left_duplicate, df_right)
    print("\nOne-to-One Validated Merge (Failure expected due to duplicate in left):")
    merged_one_to_one_fail = validator_duplicate.validate_merge(on='id', how='inner', validate='one_to_one')
    print(merged_one_to_one_fail)
