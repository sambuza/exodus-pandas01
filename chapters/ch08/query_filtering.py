import pandas as pd

class QueryFiltering:
    """
    데이터프레임에 `query()` 메서드를 사용하여 데이터를 필터링하는 클래스.
    복잡한 조건식을 문자열로 전달하여 데이터를 선택합니다.

    Class to filter data in a DataFrame using the `query()` method.
    Selects data by passing complex conditional expressions as strings.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_query(self, query_string: str) -> pd.DataFrame:
        """
        지정된 쿼리 문자열을 사용하여 데이터프레임을 필터링합니다.

        Filters the DataFrame using the specified query string.

        Args:
            query_string (str): 필터링할 조건식 (예: "column_name > 10 and another_column == 'value'").

        Returns:
            pd.DataFrame: 필터링된 데이터프레임.
        """
        try:
            filtered_df = self.df.query(query_string)
            print(f"QueryFiltering: 쿼리 '{query_string}' 적용 완료.")
            return filtered_df
        except Exception as e:
            print(f"❌ 쿼리 '{query_string}' 적용 중 오류 발생: {e}")
            return pd.DataFrame()

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 11),
        'region': ['Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt', 'Goshen'],
        'population_density': [800, 300, 900, 400, 700, 200, 1000, 500, 600, 150],
        'plague_affected': [True, False, True, False, True, False, True, False, True, False]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    query_filter = QueryFiltering(sample_df)

    # 'region'이 'Goshen'이고 'population_density'가 300 이상인 데이터 필터링
    filtered_goshen = query_filter.apply_query("region == 'Goshen' and population_density >= 300")
    print("\n'region'이 'Goshen'이고 'population_density'가 300 이상인 데이터:")
    print(filtered_goshen)

    # 'plague_affected'가 True이고 'population_density'가 700 이상인 데이터 필터링
    filtered_plague = query_filter.apply_query("plague_affected == True and population_density >= 700")
    print("\n'plague_affected'가 True이고 'population_density'가 700 이상인 데이터:")
    print(filtered_plague)
