
import pandas as pd
from .red_sea_path_data import RedSeaPathDataGenerator

class RedSeaMultiIndexAnalyzer:
    """
    출애굽기 14장의 홍해 길 데이터를 `MultiIndex`를 사용하여 분석하는 클래스.
    시간, 그룹, 길의 상태 등 다층적인 정보를 구조화하고 접근합니다.

    Class to analyze Red Sea path data from Exodus Chapter 14 using `MultiIndex`.
    Structures and accesses multi-layered information such as time, group, and path condition.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = RedSeaPathDataGenerator()
        self.red_sea_df = self.data_generator.generate_red_sea_path_data()

    def create_and_access_multiindex(self):
        """
        'time_of_day'와 'group_status'를 멀티인덱스로 설정하고 데이터를 접근합니다.
        Sets 'time_of_day' and 'group_status' as MultiIndex and accesses data.

        - KJV: Exodus 14:20 - "...so that the one came not near the other all the night."
        - ESV: Exodus 14:20 - "...so that one did not come near the other all night."
        - 개역한글: 출애굽기 14:20 - "...밤새도록 이 편에 가까이 못하게 하시니"
        """
        print("\n📊 === 멀티인덱스 생성 및 접근 (MultiIndex Creation and Access) ===")
        print("'time_of_day'와 'group_status'를 멀티인덱스로 설정하여 홍해 길의 다층적 구조를 분석합니다.")
        print("Analyzing the multi-layered structure of the Red Sea path by setting 'time_of_day' and 'group_status' as MultiIndex.")

        # MultiIndex 생성
        multi_indexed_df = self.red_sea_df.set_index(['time_of_day', 'group_status'])
        print("\n--- 멀티인덱스 DataFrame (Multi-indexed DataFrame) ---")
        print(multi_indexed_df.to_string())

        # 멀티인덱스를 사용하여 특정 데이터 접근 (예: Night 시간의 Israelites 데이터)
        print("\n--- 멀티인덱스로 특정 데이터 접근 (Accessing Data with MultiIndex - Night, Israelites) ---")
        print(multi_indexed_df.loc[('Night', 'Israelites')].to_string())

        print("\n💡 통찰 (Insight): `MultiIndex`는 하나님의 인도하심이 시간과 대상에 따라 어떻게 세밀하게 구별되었는지 보여줍니다.")
        print("Insight: `MultiIndex` reveals how God's guidance was meticulously distinguished by time and target.")
        return multi_indexed_df

    def analyze_multiindex_levels(self):
        """
        멀티인덱스의 특정 레벨을 기준으로 데이터를 접근하고 분석합니다.
        Accesses and analyzes data based on specific levels of the MultiIndex.

        - KJV: Exodus 14:29 - "But the children of Israel walked upon dry land in the midst of the sea..."
        - ESV: Exodus 14:29 - "But the people of Israel walked on dry ground through the sea..."
        - 개역한글: 출애굽기 14:29 - "이스라엘 자손은 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니"
        """
        print("\n📈 === 멀티인덱스 레벨별 분석 (Analysis by MultiIndex Levels) ===")
        print("멀티인덱스의 특정 레벨을 사용하여 이스라엘 백성의 안전 수준을 분석합니다.")
        print("Analyzing the safety level of the Israelites using specific levels of the MultiIndex.")

        multi_indexed_df = self.red_sea_df.set_index(['time_of_day', 'group_status'])

        # 모든 이스라엘 백성 데이터 접근
        israelites_data = multi_indexed_df.loc[(slice(None), 'Israelites'), :]
        print("\n--- 모든 이스라엘 백성 데이터 (All Israelites Data) ---")
        print(israelites_data.to_string())

        # 이스라엘 백성의 평균 안전 수준
        avg_safety_israelites = israelites_data['safety_level'].mean()
        print(f"\n이스라엘 백성의 평균 안전 수준 (Average Safety Level for Israelites): {avg_safety_israelites:.2f}")

        print("\n💡 통찰 (Insight): `loc`와 `slice(None)`을 통해 특정 그룹의 여정을 추적하며 하나님의 보호하심을 데이터적으로 확인할 수 있습니다.")
        print("Insight: `loc` and `slice(None)` allow us to track the journey of a specific group, numerically confirming God's protection.")
        return israelites_data

    def run_all_analyses(self) -> dict:
        """
        모든 멀티인덱스 분석을 실행하고 결과를 반환합니다.
        Runs all MultiIndex analyses and returns the results.
        """
        print("\n--- 출애굽기 14장: 홍해 길 멀티인덱스 분석 시작 ---")
        print("--- Exodus Chapter 14: Red Sea Path MultiIndex Analysis Started ---")

        results = {
            'multiindex_access': self.create_and_access_multiindex(),
            'multiindex_levels_analysis': self.analyze_multiindex_levels()
        }

        print("\n--- 출애굽기 14장: 홍해 길 멀티인덱스 분석 완료 ---")
        print("--- Exodus Chapter 14: Red Sea Path MultiIndex Analysis Completed ---")
        return results

def demo_red_sea_multiindex_analyzer():
    """
    RedSeaMultiIndexAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for RedSeaMultiIndexAnalyzer class.
    """
    print("\n=== Red Sea MultiIndex Analyzer Demo ===")
    analyzer = RedSeaMultiIndexAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_red_sea_multiindex_analyzer()
