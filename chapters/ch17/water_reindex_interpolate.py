
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from .water_from_rock_data import WaterFromRockDataGenerator

class WaterReindexInterpolateAnalyzer:
    """
    출애굽기 17장의 반석에서 난 물 데이터를 `reindex()`와 `interpolate()`를 사용하여 분석하는 클래스.
    누락된 시간대를 채우고 갈증 수준을 보간하여 하나님의 공급을 탐구합니다.

    Class to analyze water from the rock data from Exodus Chapter 17 using `reindex()` and `interpolate()`.
    Explores God's provision by filling missing timestamps and interpolating thirst levels.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = WaterFromRockDataGenerator()
        self.water_df = self.data_generator.generate_water_from_rock_data()
        self.water_df = self.water_df.set_index('timestamp') # 날짜를 인덱스로 설정

    def analyze_reindex_and_interpolate(self):
        """
        누락된 시간대를 `reindex()`로 채우고, `thirst_level`을 `interpolate()`로 보간합니다.
        Fills missing timestamps with `reindex()` and interpolates `thirst_level` with `interpolate()`.

        - KJV: Exodus 17:3 - "...the people thirsted there for water; and the people murmured against Moses..."
        - ESV: Exodus 17:3 - "...the people thirsted there for water, and the people grumbled against Moses..."
        - 개역한글: 출애굽기 17:3 - "거기서 백성이 물이 없으므로 모세를 대하여 원망하여 가로되..."
        """
        print("\n📊 === 누락된 시간대 재색인 및 갈증 수준 보간 (Reindexing & Interpolating Thirst Level) ===")
        print("누락된 시간대를 채우고 갈증 수준을 보간하여 이스라엘의 고통과 하나님의 공급을 연속적으로 파악합니다.")
        print("Filling missing timestamps and interpolating thirst levels to continuously understand Israel's suffering and God's provision.")

        # 데이터프레임에서 일부 데이터 누락 시뮬레이션
        df_sparse = self.water_df.copy()
        df_sparse.loc[df_sparse.index[10:20], 'thirst_level'] = np.nan # 일부러 누락
        df_sparse.loc[df_sparse.index[30:40], 'israel_complaint_level'] = np.nan # 일부러 누락

        # 1시간 간격으로 인덱스 재설정
        full_hourly_range = pd.date_range(start=df_sparse.index.min(), end=df_sparse.index.max(), freq='H')
        reindexed_df = df_sparse.reindex(full_hourly_range)

        # 누락된 'thirst_level' 데이터 선형 보간
        reindexed_df['thirst_level_interpolated'] = reindexed_df['thirst_level'].interpolate(method='linear')
        # 누락된 'israel_complaint_level' 데이터 선형 보간
        reindexed_df['complaint_level_interpolated'] = reindexed_df['israel_complaint_level'].interpolate(method='linear')

        print("\n--- 원본 데이터 (일부 누락) ---")
        print(df_sparse[['thirst_level', 'israel_complaint_level']].head(20).to_string())
        print("\n--- 재색인 및 보간된 데이터 (Reindexed & Interpolated Data) ---")
        print(reindexed_df[['thirst_level', 'thirst_level_interpolated', 'israel_complaint_level', 'complaint_level_interpolated']].head(20).to_string())

        print("\n💡 통찰 (Insight): `reindex()`와 `interpolate()`는 파편화된 정보 속에서도 하나님의 신실한 인도하심이 끊이지 않았음을 연속적인 흐름으로 보여줍니다.")
        print("Insight: `reindex()` and `interpolate()` show that God's faithful guidance was continuous, even amidst fragmented information.")
        return reindexed_df

    def run_all_analyses(self) -> dict:
        """
        모든 재색인 및 보간 분석을 실행하고 결과를 반환합니다.
        Runs all reindex and interpolation analyses and returns the results.
        """
        print("\n--- 출애굽기 17장: 반석에서 난 물 재색인/보간 분석 시작 ---")
        print("--- Exodus Chapter 17: Water from Rock Reindex/Interpolate Analysis Started ---")

        results = {
            'reindex_interpolate_result': self.analyze_reindex_and_interpolate()
        }

        print("\n--- 출애굽기 17장: 반석에서 난 물 재색인/보간 분석 완료 ---")
        print("--- Exodus Chapter 17: Water from Rock Reindex/Interpolate Analysis Completed ---")
        return results

def demo_water_reindex_interpolate_analyzer():
    """
    WaterReindexInterpolateAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for WaterReindexInterpolateAnalyzer class.
    """
    print("\n=== Water Reindex/Interpolate Analyzer Demo ===")
    analyzer = WaterReindexInterpolateAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_water_reindex_interpolate_analyzer()
