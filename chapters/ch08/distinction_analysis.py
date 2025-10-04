import pandas as pd
import numpy as np

class DistinctionAnalysis:
    """
    데이터 속에서 특정 그룹의 특징을 분석하여 구별된 통찰을 얻는 클래스.
    고센 땅의 구별처럼, 조건부 분석을 통해 데이터의 의미를 심화합니다.

    Class to analyze characteristics of specific groups in data to gain distinct insights.
    Deepens data understanding through conditional analysis, like the distinction of Goshen.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def analyze_distinctions(self, group_column: str, metric_column: str) -> pd.DataFrame:
        """
        지정된 그룹 컬럼을 기준으로 특정 지표 컬럼의 통계를 분석합니다.

        Analyzes statistics of a specific metric column based on the specified group column.

        Args:
            group_column (str): 그룹을 나눌 컬럼 이름 (예: 'region', 'is_israelite').
            metric_column (str): 분석할 지표 컬럼 이름 (예: 'plague_affected', 'water_quality_score').

        Returns:
            pd.DataFrame: 그룹별 통계 요약.
        """
        if group_column not in self.df.columns or metric_column not in self.df.columns:
            print(f"경고: 컬럼 '{group_column}' 또는 '{metric_column}'이 데이터프레임에 존재하지 않습니다. 분석을 건너뜁니다.")
            return pd.DataFrame()

        # 그룹별 평균, 합계, 개수 등 통계 분석
        distinction_summary = self.df.groupby(group_column)[metric_column].agg(['mean', 'sum', 'count'])
        print(f"DistinctionAnalysis: '{group_column}'을 기준으로 '{metric_column}' 분석 완료.")
        return distinction_summary

    def compare_groups(self, group_column: str, metric_column: str, group1_value, group2_value) -> dict:
        """
        두 그룹 간의 특정 지표를 비교합니다.

        Compares a specific metric between two groups.

        Args:
            group_column (str): 그룹을 나눌 컬럼 이름.
            metric_column (str): 비교할 지표 컬럼 이름.
            group1_value: 첫 번째 그룹의 값.
            group2_value: 두 번째 그룹의 값.

        Returns:
            dict: 두 그룹 간의 비교 결과.
        """
        if group_column not in self.df.columns or metric_column not in self.df.columns:
            print(f"경고: 컬럼 '{group_column}' 또는 '{metric_column}'이 데이터프레임에 존재하지 않습니다. 비교를 건너뜁니다.")
            return {}

        group1_data = self.df[self.df[group_column] == group1_value][metric_column]
        group2_data = self.df[self.df[group_column] == group2_value][metric_column]

        comparison_results = {
            f'{group1_value}_mean': group1_data.mean(),
            f'{group2_value}_mean': group2_data.mean(),
            f'{group1_value}_std': group1_data.std(),
            f'{group2_value}_std': group2_data.std(),
            'difference_of_means': group1_data.mean() - group2_data.mean()
        }
        print(f"DistinctionAnalysis: '{group1_value}'와 '{group2_value}' 그룹 비교 완료.")
        return comparison_results

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 11),
        'region': ['Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt', 'Goshen', 'Egypt', 'Goshen'],
        'plague_affected': [True, False, True, False, True, False, True, False, True, False],
        'water_quality_score': [1, 8, 2, 9, 3, 7, 1, 9, 2, 8],
        'is_israelite': [False, True, False, True, False, True, False, True, False, True]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    analyzer = DistinctionAnalysis(sample_df)

    # 'region'별 'plague_affected' 분석
    plague_by_region = analyzer.analyze_distinctions('region', 'plague_affected')
    print("\n'region'별 'plague_affected' 분석:")
    print(plague_by_region)

    # 'is_israelite'별 'water_quality_score' 분석
    water_by_israelite = analyzer.analyze_distinctions('is_israelite', 'water_quality_score')
    print("\n'is_israelite'별 'water_quality_score' 분석:")
    print(water_by_israelite)

    # 'Egypt'와 'Goshen'의 'water_quality_score' 비교
    water_comparison = analyzer.compare_groups('region', 'water_quality_score', 'Egypt', 'Goshen')
    print("\n'Egypt'와 'Goshen'의 'water_quality_score' 비교:")
    print(water_comparison)
