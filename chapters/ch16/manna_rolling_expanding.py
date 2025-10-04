
import pandas as pd
from .manna_ordinance_data import MannaOrdinanceDataGenerator

class MannaRollingExpandingAnalyzer:
    """
    출애굽기 16장의 만나 데이터를 `rolling()`과 `expanding()`을 사용하여 분석하는 클래스.
    만나 공급의 주기적 패턴과 이스라엘의 누적된 불평을 탐구합니다.

    Class to analyze manna data from Exodus Chapter 16 using `rolling()` and `expanding()`.
    Explores periodic patterns of manna provision and Israel's accumulated complaints.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = MannaOrdinanceDataGenerator()
        self.manna_df = self.data_generator.generate_manna_data()
        self.manna_df = self.manna_df.set_index('date') # 날짜를 인덱스로 설정

    def analyze_rolling_mean_manna(self):
        """
        7일 `rolling mean`을 사용하여 만나 수확량의 주간 평균을 분석합니다.
        Analyzes the weekly average of manna gathered using a 7-day `rolling mean`.

        - KJV: Exodus 16:22 - "...on the sixth day they gathered twice as much bread..."
        - ESV: Exodus 16:22 - "...on the sixth day they gathered twice as much bread..."
        - 개역한글: 출애굽기 16:22 - "제 육일에는 각 사람이 갑절의 식물 곧 한 사람에 두 오멜씩 거둔지라..."
        """
        print("\n📊 === 7일 이동 평균 만나 수확량 (7-Day Rolling Mean Manna Gathered) ===")
        print("만나 수확량의 7일 이동 평균을 계산하여 주간 패턴을 파악합니다.")
        print("Calculating the 7-day rolling mean of manna gathered to identify weekly patterns.")

        self.manna_df['rolling_mean_manna'] = self.manna_df['manna_gathered_kg'].rolling(window=7, min_periods=1).mean()
        print(self.manna_df[['manna_gathered_kg', 'rolling_mean_manna']].to_string())

        print("\n💡 통찰 (Insight): `rolling().mean()`은 안식일 규례로 인한 만나 공급의 주기적인 패턴을 보여주며, 하나님의 세밀한 공급 계획을 드러냅니다.")
        print("Insight: `rolling().mean()` reveals the periodic pattern of manna provision due to the Sabbath ordinance, showcasing God's meticulous provision plan.")
        return self.manna_df['rolling_mean_manna']

    def analyze_expanding_sum_complaint(self):
        """
        `expanding sum`을 사용하여 이스라엘의 누적된 불평을 분석합니다.
        Analyzes Israel's accumulated complaints using `expanding sum`.

        - KJV: Exodus 16:2 - "And the whole congregation of the children of Israel murmured against Moses and Aaron in the wilderness."
        - ESV: Exodus 16:2 - "And the whole congregation of the people of Israel grumbled against Moses and Aaron in the wilderness."
        - 개역한글: 출애굽기 16:2 - "이스라엘 자손 온 회중이 그 광야에서 모세와 아론을 원망하여"
        """
        print("\n📈 === 누적 불평 지수 (Expanding Sum of Complaint Index) ===")
        print("광야 여정 전체에 걸쳐 이스라엘 백성의 누적된 불평을 `expanding().sum()`으로 계산합니다.")
        print("Calculating the accumulated complaints of the Israelites over the entire wilderness journey using `expanding().sum()`.")

        self.manna_df['expanding_sum_complaint'] = self.manna_df['israel_complaint'].expanding(min_periods=1).sum()
        print(self.manna_df[['israel_complaint', 'expanding_sum_complaint']].to_string())

        print("\n💡 통찰 (Insight): `expanding().sum()`은 인간의 연약함과 불순종이 시간이 지남에 따라 어떻게 쌓여가는지 데이터적으로 보여줍니다.")
        print("Insight: `expanding().sum()` numerically illustrates how human weakness and disobedience accumulate over time.")
        return self.manna_df['expanding_sum_complaint']

    def run_all_analyses(self) -> dict:
        """
        모든 롤링 및 익스팬딩 분석을 실행하고 결과를 반환합니다.
        Runs all rolling and expanding analyses and returns the results.
        """
        print("\n--- 출애굽기 16장: 만나 롤링/익스팬딩 분석 시작 ---")
        print("--- Exodus Chapter 16: Manna Rolling/Expanding Analysis Started ---")

        results = {
            'rolling_mean_manna': self.analyze_rolling_mean_manna(),
            'expanding_sum_complaint': self.analyze_expanding_sum_complaint()
        }

        print("\n--- 출애굽기 16장: 만나 롤링/익스팬딩 분석 완료 ---")
        print("--- Exodus Chapter 16: Manna Rolling/Expanding Analysis Completed ---")
        return results

def demo_manna_rolling_expanding_analyzer():
    """
    MannaRollingExpandingAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for MannaRollingExpandingAnalyzer class.
    """
    print("\n=== Manna Rolling/Expanding Analyzer Demo ===")
    analyzer = MannaRollingExpandingAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_manna_rolling_expanding_analyzer()
