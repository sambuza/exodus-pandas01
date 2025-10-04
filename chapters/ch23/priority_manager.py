import pandas as pd
import numpy as np

class PriorityManager:
    """
    데이터프레임에 다중키 정렬 및 안정 정렬 개념을 적용하는 클래스.
    여러 기준에 따라 데이터를 정렬하고, 동일한 값의 순서를 유지하는 정렬을 시연합니다.

    Class to apply multi-key sorting and stable sort concepts to a DataFrame.
    Sorts data by multiple criteria and demonstrates stable sorting for preserving order of equal values.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_multi_key_sort(self, by_columns: list, ascending: list = None, kind: str = 'quicksort') -> pd.DataFrame:
        """
        여러 컬럼을 기준으로 데이터프레임을 정렬합니다.

        Sorts the DataFrame by multiple columns.

        Args:
            by_columns (list): 정렬 기준으로 사용할 컬럼 이름 리스트.
            ascending (list): 각 컬럼에 대한 오름차순(True) 또는 내림차순(False) 정렬 여부.
                              `by_columns`와 길이가 같아야 합니다.
            kind (str): 정렬 알고리즘 ('quicksort', 'mergesort', 'heapsort', 'stable').

        Returns:
            pd.DataFrame: 다중키 정렬된 데이터프레임.
        """
        if ascending is None:
            ascending = [True] * len(by_columns)

        multi_sorted_df = self.df.sort_values(by=by_columns, ascending=ascending, kind=kind)
        print(f"PriorityManager: 컬럼 '{by_columns}'을 기준으로 다중키 정렬 완료.")
        return multi_sorted_df

    def apply_stable_sort(self, by_column: str, ascending: bool = True) -> pd.DataFrame:
        """
        지정된 컬럼을 기준으로 안정 정렬을 적용합니다.
        동일한 값을 가진 요소들의 원래 순서를 유지합니다.

        Applies stable sort based on the specified column.
        Preserves the original order of elements with equal values.

        Args:
            by_column (str): 안정 정렬 기준으로 사용할 컬럼 이름.
            ascending (bool): 오름차순(True) 또는 내림차순(False) 정렬 여부.

        Returns:
            pd.DataFrame: 안정 정렬된 데이터프레임.
        """
        if by_column not in self.df.columns:
            print(f"경고: 컬럼 '{by_column}'이 데이터프레임에 존재하지 않습니다. 안정 정렬을 건너뜁니다.")
            return self.df

        stable_sorted_df = self.df.sort_values(by=by_column, ascending=ascending, kind='stable')
        print(f"PriorityManager: 컬럼 '{by_column}'을 기준으로 안정 정렬 완료.")
        return stable_sorted_df

if __name__ == "__main__":
    # 샘플 데이터 생성 (안정 정렬 시연을 위해 일부러 중복 값 포함)
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
        'score': [90, 85, 90, 70, 85, 95, 70, 80],
        'sub_score': [10, 20, 15, 5, 25, 12, 8, 22] # score가 같을 때 원래 순서 확인용
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    manager = PriorityManager(sample_df)

    # 'category' 오름차순, 'score' 내림차순으로 다중키 정렬
    multi_sorted_df = manager.apply_multi_key_sort(by_columns=['category', 'score'], ascending=[True, False])
    print("\n다중키 정렬 (category 오름차순, score 내림차순) 후:")
    print(multi_sorted_df)

    # 'score'를 기준으로 안정 정렬 (score가 90인 두 행의 원래 순서 확인: id 1 -> id 3)
    stable_sorted_df = manager.apply_stable_sort(by_column='score', ascending=False)
    print("\n'score' 내림차순 안정 정렬 후:")
    print(stable_sorted_df)
