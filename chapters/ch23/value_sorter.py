import pandas as pd

class ValueSorter:
    """
    데이터프레임을 하나 이상의 컬럼 값을 기준으로 정렬하는 클래스.
    `sort_values()` 메서드를 활용하여 데이터를 특정 기준에 따라 재배열합니다.

    Class to sort a DataFrame by one or more column values.
    Rearranges data according to specific criteria using the `sort_values()` method.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def sort_by_values(self, by_columns: str or list, ascending: bool or list = True, kind: str = 'quicksort') -> pd.DataFrame:
        """
        지정된 컬럼(들)의 값을 기준으로 데이터프레임을 정렬합니다.

        Sorts the DataFrame by the values of the specified column(s).

        Args:
            by_columns (str or list): 정렬 기준으로 사용할 컬럼 이름(들).
            ascending (bool or list): 오름차순(True) 또는 내림차순(False) 정렬 여부.
                                      리스트인 경우 `by_columns`와 길이가 같아야 합니다.
            kind (str): 정렬 알고리즘 ('quicksort', 'mergesort', 'heapsort', 'stable').
                        'stable'은 mergesort를 사용합니다.

        Returns:
            pd.DataFrame: 정렬된 데이터프레임.
        """
        sorted_df = self.df.sort_values(by=by_columns, ascending=ascending, kind=kind)
        print(f"ValueSorter: 컬럼 '{by_columns}'을 기준으로 데이터 정렬 완료.")
        return sorted_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'score': [85, 92, 78, 92, 85],
        'grade': ['B', 'A', 'C', 'A', 'B']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    sorter = ValueSorter(sample_df)

    # 'score' 컬럼을 기준으로 내림차순 정렬
    sorted_by_score = sorter.sort_by_values(by_columns='score', ascending=False)
    print("\n'score' 내림차순 정렬 후:")
    print(sorted_by_score)

    # 'grade' 오름차순, 'score' 내림차순으로 다중키 정렬
    multi_sorted_df = sorter.sort_by_values(by_columns=['grade', 'score'], ascending=[True, False])
    print("\n'grade' 오름차순, 'score' 내림차순 다중키 정렬 후:")
    print(multi_sorted_df)
