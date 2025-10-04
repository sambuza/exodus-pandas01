import pandas as pd

class IndexSorter:
    """
    데이터프레임을 인덱스(행 라벨)를 기준으로 정렬하는 클래스.
    `sort_index()` 메서드를 활용하여 데이터를 인덱스 순서에 따라 재배열합니다.

    Class to sort a DataFrame by its index (row labels).
    Rearranges data according to index order using the `sort_index()` method.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def sort_by_index(self, ascending: bool = True, level=None, sort_remaining: bool = True) -> pd.DataFrame:
        """
        데이터프레임을 인덱스 기준으로 정렬합니다.

        Sorts the DataFrame by its index.

        Args:
            ascending (bool): 오름차순(True) 또는 내림차순(False) 정렬 여부.
            level: MultiIndex의 경우, 정렬할 레벨을 지정합니다.
            sort_remaining (bool): MultiIndex의 경우, 지정된 레벨 외의 나머지 레벨도 정렬할지 여부.

        Returns:
            pd.DataFrame: 정렬된 데이터프레임.
        """
        sorted_df = self.df.sort_index(ascending=ascending, level=level, sort_remaining=sort_remaining)
        print("IndexSorter: 인덱스 기준으로 데이터 정렬 완료.")
        return sorted_df

if __name__ == "__main__":
    # 샘플 데이터 생성 (DatetimeIndex)
    dates = pd.to_datetime(['2023-01-05', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04'])
    data = {
        'value': [10, 5, 8, 7, 9]
    }
    sample_df = pd.DataFrame(data, index=dates)
    print("원본 데이터 (DatetimeIndex):")
    print(sample_df)

    sorter = IndexSorter(sample_df)

    # 인덱스 기준으로 오름차순 정렬
    sorted_by_index_asc = sorter.sort_by_index(ascending=True)
    print("\n인덱스 오름차순 정렬 후:")
    print(sorted_by_index_asc)

    # 인덱스 기준으로 내림차순 정렬
    sorted_by_index_desc = sorter.sort_by_index(ascending=False)
    print("\n인덱스 내림차순 정렬 후:")
    print(sorted_by_index_desc)

    # MultiIndex 샘플
    arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
              ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
    index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
    df_multi = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    df_multi = df_multi.sort_index(level=0, ascending=False) # 일부러 섞음
    print("\n원본 MultiIndex 데이터:")
    print(df_multi)

    multi_sorter = IndexSorter(df_multi)
    sorted_multi_df = multi_sorter.sort_by_index(level='first', ascending=True)
    print("\nMultiIndex 'first' 레벨 오름차순 정렬 후:")
    print(sorted_multi_df)
