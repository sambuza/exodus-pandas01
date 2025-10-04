import pandas as pd
import io

class DataFrameInspector:
    """
    데이터프레임의 구조와 정보를 검사하는 클래스.
    `df.info()`를 포함한 다양한 메서드를 사용하여 데이터의 특성을 파악합니다.

    Class to inspect the structure and information of a DataFrame.
    Utilizes various methods including `df.info()` to understand data characteristics.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def get_dataframe_info(self) -> str:
        """
        `df.info()` 메서드를 사용하여 데이터프레임의 요약 정보를 문자열로 반환합니다.

        Returns summary information of the DataFrame as a string using the `df.info()` method.

        Returns:
            str: `df.info()`의 출력 결과.
        """
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        info_str = buffer.getvalue()
        print("DataFrameInspector: df.info() 정보 추출 완료.")
        return info_str

    def get_column_dtypes(self) -> pd.Series:
        """
        데이터프레임의 각 컬럼 데이터 타입을 반환합니다.

        Returns the data types of each column in the DataFrame.

        Returns:
            pd.Series: 컬럼 이름과 데이터 타입을 매핑하는 Series.
        """
        print("DataFrameInspector: 컬럼 데이터 타입 정보 추출 완료.")
        return self.df.dtypes

    def get_missing_values_count(self) -> pd.Series:
        """
        데이터프레임의 각 컬럼별 결측치 개수를 반환합니다.

        Returns the count of missing values for each column in the DataFrame.

        Returns:
            pd.Series: 컬럼 이름과 결측치 개수를 매핑하는 Series.
        """
        print("DataFrameInspector: 컬럼별 결측치 개수 추출 완료.")
        return self.df.isnull().sum()

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'col1': [1, 2, 3, None, 5],
        'col2': ['A', 'B', 'C', 'D', 'E'],
        'col3': [1.1, 2.2, None, 4.4, 5.5]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    inspector = DataFrameInspector(sample_df)

    # df.info() 정보 확인
    info_output = inspector.get_dataframe_info()
    print("\n--- df.info() 출력 결과 ---")
    print(info_output)

    # 컬럼 데이터 타입 확인
    dtypes_output = inspector.get_column_dtypes()
    print("\n--- 컬럼 데이터 타입 ---")
    print(dtypes_output)

    # 결측치 개수 확인
    missing_output = inspector.get_missing_values_count()
    print("\n--- 컬럼별 결측치 개수 ---")
    print(missing_output)
