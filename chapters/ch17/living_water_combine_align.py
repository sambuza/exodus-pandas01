
import pandas as pd
from datetime import datetime, timedelta
from .living_water_flow_data import LivingWaterFlowDataGenerator

class LivingWaterCombineAlignAnalyzer:
    """
    요한복음 7장의 생수의 강 데이터를 `align()`과 `merge_asof()`를 사용하여 분석하는 클래스.
    말씀 섭취와 기도 강도 데이터를 결합하여 영적 흐름을 통합적으로 탐구합니다.

    Class to analyze living water data from John Chapter 7 using `align()` and `merge_asof()`.
    Integratively explores spiritual flow by combining Word intake and prayer intensity data.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = LivingWaterFlowDataGenerator()
        self.living_water_df = self.data_generator.generate_living_water_flow_data()
        self.living_water_df = self.living_water_df.set_index('timestamp') # 날짜를 인덱스로 설정

    def analyze_align_data(self):
        """
        서로 다른 영적 활동 데이터를 `align()`으로 정렬하고 결합합니다.
        Aligns and combines different spiritual activity data using `align()`.

        - KJV: John 7:37 - "...If any man thirst, let him come unto me, and drink."
        - ESV: John 7:37 - "...If anyone thirsts, let him come to me and drink."
        - 개역한글: 요한복음 7:37 - "...누구든지 목마르거든 내게로 와서 마시라"
        """
        print("\n📊 === 영적 활동 데이터 정렬 (Aligning Spiritual Activity Data) ===")
        print("말씀 섭취와 기도 강도 데이터를 `align()`으로 정렬하여 영적 흐름을 통합적으로 파악합니다.")
        print("Aligning Word intake and prayer intensity data with `align()` to integratively understand spiritual flow.")

        # 말씀 섭취 데이터와 기도 강도 데이터를 분리
        word_intake_df = self.living_water_df[['word_intake_score']].copy()
        prayer_intensity_df = self.living_water_df[['prayer_intensity_score']].copy()

        # 일부러 데이터 누락 시뮬레이션
        word_intake_df.loc[word_intake_df.index[5:10], 'word_intake_score'] = np.nan
        prayer_intensity_df.loc[prayer_intensity_df.index[15:20], 'prayer_intensity_score'] = np.nan

        # 두 데이터프레임을 시간 인덱스에 맞춰 정렬 (outer join)
        aligned_word, aligned_prayer = word_intake_df.align(prayer_intensity_df, join='outer')
        combined_aligned_df = pd.DataFrame({
            'word_intake_score': aligned_word['word_intake_score'],
            'prayer_intensity_score': aligned_prayer['prayer_intensity_score']
        })
        print(combined_aligned_df.head(20).to_string())

        print("\n💡 통찰 (Insight): `align()`은 서로 다른 영적 활동들이 시간적으로 어떻게 상호작용하는지 통합적으로 이해하는 데 도움을 줍니다.")
        print("Insight: `align()` helps integratively understand how different spiritual activities interact over time.")
        return combined_aligned_df

    def analyze_merge_asof(self):
        """
        `merge_asof()`를 사용하여 시간적으로 근접한 영적 흐름 데이터를 결합합니다.
        Combines time-proximate spiritual flow data using `merge_asof()`.

        - KJV: John 7:38 - "He that believeth on me, as the scripture hath said, out of his belly shall flow rivers of living water."
        - ESV: John 7:38 - "Whoever believes in me, as the Scripture has said, 'Out of his heart will flow rivers of living water.'"
        - 개역한글: 요한복음 7:38 - "나를 믿는 자는 성경에 이름과 같이 그 배에서 생수의 강이 흘러나리라 하시니"
        """
        print("\n📈 === `merge_asof()`를 사용한 시간 기반 결합 (Time-based Merge with `merge_asof()`) ===")
        print("말씀 섭취와 영적 흐름 속도 데이터를 `merge_asof()`로 결합하여 시간적 인과 관계를 분석합니다.")
        print("Combining Word intake and spiritual flow rate data with `merge_asof()` to analyze temporal causality.")

        # 예시를 위해 인덱스를 리셋하고 시간 열을 기준으로 정렬
        df_word_reset = self.living_water_df[['word_intake_score']].reset_index().sort_values('timestamp')
        df_flow_reset = self.living_water_df[['spiritual_flow_rate']].reset_index().sort_values('timestamp')

        # `merge_asof`는 시간적으로 가장 가까운 이전 값을 기준으로 병합
        merged_asof_df = pd.merge_asof(df_flow_reset, df_word_reset, on='timestamp', direction='nearest', suffixes=('_flow', '_word'))
        print(merged_asof_df.head(20).to_string(index=False))

        print("\n💡 통찰 (Insight): `merge_asof()`는 말씀 섭취가 영적 흐름에 미치는 시간적 영향을 분석하여 생수의 강이 흐르는 패턴을 보여줍니다.")
        print("Insight: `merge_asof()` analyzes the temporal impact of Word intake on spiritual flow, revealing the pattern of living water flowing.")
        return merged_asof_df

    def run_all_analyses(self) -> dict:
        """
        모든 결합 및 정렬 분석을 실행하고 결과를 반환합니다.
        Runs all combine and align analyses and returns the results.
        """
        print("\n--- 요한복음 7장: 생수의 강 결합/정렬 분석 시작 ---")
        print("--- John Chapter 7: Living Water Combine/Align Analysis Started ---")

        results = {
            'aligned_data': self.analyze_align_data(),
            'merged_asof_data': self.analyze_merge_asof()
        }

        print("\n--- 요한복음 7장: 생수의 강 결합/정렬 분석 완료 ---")
        print("--- John Chapter 7: Living Water Combine/Align Analysis Completed ---")
        return results

def demo_living_water_combine_align_analyzer():
    """
    LivingWaterCombineAlignAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for LivingWaterCombineAlignAnalyzer class.
    """
    print("\n=== Living Water Combine/Align Analyzer Demo ===")
    analyzer = LivingWaterCombineAlignAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_living_water_combine_align_analyzer()
