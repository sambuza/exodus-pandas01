import pandas as pd
import numpy as np

class EvalQueryAccelerator:
    """
    데이터프레임에 `eval()` 및 `query()` 메서드를 적용하여 데이터 처리 속도를 가속화하는 클래스.
    복잡한 조건부 계산이나 필터링을 효율적으로 수행합니다.

    Class to accelerate data processing speed by applying `eval()` and `query()` methods to a DataFrame.
    Efficiently performs complex conditional calculations or filtering.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_eval(self, expression: str) -> pd.DataFrame:
        """
        `eval()` 메서드를 사용하여 문자열 표현식을 평가하고 새로운 컬럼을 생성합니다.

        Evaluates a string expression using the `eval()` method and creates a new column.

        Args:
            expression (str): 평가할 문자열 표현식 (예: "new_col = col1 + col2").

        Returns:
            pd.DataFrame: `eval()` 연산이 적용된 데이터프레임.
        """
        try:
            # eval()은 DataFrame의 메서드로 직접 호출하거나 pd.eval() 사용
            # 여기서는 새로운 컬럼을 추가하는 방식으로 사용
            # 예: df.eval("new_col = col1 + col2", inplace=False)
            # 또는 df.assign(new_col=df.eval("col1 + col2"))
            # 간단한 예시를 위해 새로운 컬럼을 추가하는 방식으로 구현
            # expression이 "new_col = col1 + col2" 형태라고 가정
            new_col_name = expression.split('=')[0].strip()
            eval_expression = expression.split('=')[1].strip()
            
            accelerated_df = self.df.copy()
            accelerated_df[new_col_name] = accelerated_df.eval(eval_expression)
            print(f"EvalQueryAccelerator: eval() 연산 '{expression}' 적용 완료.")
            return accelerated_df
        except Exception as e:
            print(f"❌ eval() 연산 '{expression}' 적용 중 오류 발생: {e}")
            return self.df

    def apply_query(self, query_string: str) -> pd.DataFrame:
        """
        `query()` 메서드를 사용하여 문자열 조건식으로 데이터프레임을 필터링합니다.

        Filters the DataFrame using a string conditional expression with the `query()` method.

        Args:
            query_string (str): 필터링할 조건식 (예: "column_name > 10 and another_column == 'value'").

        Returns:
            pd.DataFrame: 필터링된 데이터프레임.
        """
        try:
            filtered_df = self.df.query(query_string)
            print(f"EvalQueryAccelerator: query() 연산 '{query_string}' 적용 완료.")
            return filtered_df
        except Exception as e:
            print(f"❌ query() 연산 '{query_string}' 적용 중 오류 발생: {e}")
            return self.df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 11),
        'value1': np.random.randint(10, 100, size=10),
        'value2': np.random.rand(10) * 50,
        'category': np.random.choice(['A', 'B', 'C'], size=10)
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    accelerator = EvalQueryAccelerator(sample_df)

    # eval()을 이용한 새로운 컬럼 생성
    df_with_new_col = accelerator.apply_eval("sum_values = value1 + value2")
    print("\neval()을 이용한 'sum_values' 컬럼 생성 후:")
    print(df_with_new_col.head())

    # query()를 이용한 데이터 필터링
    filtered_df = accelerator.apply_query("value1 > 50 and category == 'A'")
    print("\nquery()를 이용한 데이터 필터링 후:")
    print(filtered_df)
