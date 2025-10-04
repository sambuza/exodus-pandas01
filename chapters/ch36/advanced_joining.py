import pandas as pd

class AdvancedJoining:
    """
    고급 데이터 조인(joining)을 위한 클래스.
    `merge`를 사용하여 여러 데이터프레임을 결합합니다.
    """

    def __init__(self, df1: pd.DataFrame, df2: pd.DataFrame):
        self.df1 = df1
        self.df2 = df2

    def merge_dataframes(self, on=None, how='inner', **kwargs):
        """
        두 데이터프레임을 병합합니다.
        """
        try:
            merged_df = pd.merge(self.df1, self.df2, on=on, how=how, **kwargs)
            print(f"AdvancedJoining: 데이터프레임 병합 완료 (how={how}).")
            return merged_df
        except Exception as e:
            print(f"데이터프레임 병합 중 오류 발생: {e}")
            return None
