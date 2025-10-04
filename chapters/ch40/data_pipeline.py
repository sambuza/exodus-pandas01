import pandas as pd

class DataPipeline:
    """
    데이터 파이프라인을 위한 클래스.
    `pipe`, `apply`, `map`을 사용하여 데이터 처리 과정을 체계적으로 구성합니다.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run_pipeline(self, *funcs):
        """
        여러 함수를 순차적으로 적용합니다.
        """
        try:
            result_df = self.df.copy() # Start with a copy
            for func, kwargs in funcs:
                result_df = func(result_df, **kwargs)
            print("DataPipeline: 파이프라인 실행 완료.")
            return result_df
        except Exception as e:
            print(f"파이프라인 실행 중 오류 발생: {e}")
            return None

    @staticmethod
    def apply_function(df, column, func):
        """
        apply를 사용하여 열에 함수를 적용합니다.
        """
        df[column] = df[column].apply(func)
        return df

    @staticmethod
    def map_values(df, column, mapping):
        """
        map을 사용하여 열의 값을 변환합니다.
        """
        df[column] = df[column].map(mapping)
        return df
