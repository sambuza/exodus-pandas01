import pandas as pd

class AdvancedReshaping:
    """
    데이터 재구성(reshaping)을 위한 클래스.
    `wide_to_long`, `pivot_table` 등을 사용하여 데이터 구조를 변환합니다.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def reshape_wide_to_long(self, stubnames, i, j):
        """
        wide_to_long을 사용하여 데이터를 넓은 형식에서 긴 형식으로 변환합니다.
        """
        try:
            long_df = pd.wide_to_long(self.df, stubnames=stubnames, i=i, j=j)
            print("AdvancedReshaping: wide_to_long 변환 완료.")
            return long_df
        except Exception as e:
            print(f"wide_to_long 변환 중 오류 발생: {e}")
            return None

    def create_pivot_table(self, values, index, columns, aggfunc):
        """
        pivot_table을 생성합니다.
        """
        try:
            pivot_df = self.df.pivot_table(values=values, index=index, columns=columns, aggfunc=aggfunc)
            print("AdvancedReshaping: pivot_table 생성 완료.")
            return pivot_df
        except Exception as e:
            print(f"pivot_table 생성 중 오류 발생: {e}")
            return None
