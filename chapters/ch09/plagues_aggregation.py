import pandas as pd
from .plagues_data import PlaguesDataGenerator

class PlaguesAggregationAnalyzer:
    """
    출애굽기 9장의 재앙 데이터를 집계하여 분석하는 클래스.
    파라오의 견고한 마음과 하나님의 권능을 통계적으로 탐구합니다.

    Class to analyze plague data from Exodus Chapter 9 using aggregation.
    Statistically explores Pharaoh's hardened heart and God's power.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = PlaguesDataGenerator()
        self.plague_df = self.data_generator.generate_detailed_plague_data()

    def analyze_summary_statistics(self):
        """
        재앙의 심각도에 대한 요약 통계를 분석합니다.
        Analyzes summary statistics for plague severity.

        - KJV: Exodus 9:14 - "For I will at this time send all my plagues upon thine heart..."
        - ESV: Exodus 9:14 - "For this time I will send all my plagues upon your heart..."
        - 개역한글: 출애굽기 9:14 - "내가 이번에는 모든 재앙을 너와 네 신하와 네 백성에게 내려..."
        """
        print("\n📊 === 재앙 심각도 요약 통계 (Plague Severity Summary Statistics) ===")
        print("애굽에 임한 재앙의 심각도를 숫자로 요약합니다.")
        print("Summarizing the severity of plagues in Egypt numerically.")

        summary = self.plague_df['actual_damage_egypt'].describe()
        print(summary)

        print("\n💡 통찰 (Insight): `describe()`는 재앙의 평균적인 심각도, 최소/최대 피해 범위 등을 한눈에 보여줍니다.")
        print("Insight: `describe()` provides an at-a-glance summary of average severity, min/max damage range, etc.")
        return summary

    def analyze_total_impact(self):
        """
        재앙의 총체적인 영향을 분석합니다.
        Analyzes the total cumulative impact of the plagues.

        - KJV: Exodus 9:6 - "...all the livestock of Egypt died..."
        - ESV: Exodus 9:6 - "...all the livestock of Egypt died..."
        - 개역한글: 출애굽기 9:6 - "...애굽의 모든 생축이 죽으니..."
        """ 
        print("\n📈 === 재앙의 총체적 영향 (Total Impact of Plagues) ===")
        print("애굽이 받은 총 피해의 합계를 계산합니다.")
        print("Calculating the sum of total damage inflicted upon Egypt.")

        total_damage = self.plague_df['actual_damage_egypt'].sum()
        print(f"총 애굽 피해 심각도 합계 (Total Egypt Damage Severity Sum): {total_damage}")

        print("\n💡 통찰 (Insight): `sum()`은 파라오의 견고한 마음이 애굽에 가져온 총체적인 고통을 보여줍니다.")
        print("Insight: `sum()` reveals the cumulative suffering brought upon Egypt by Pharaoh's hardened heart.")
        return total_damage

    def analyze_average_severity(self):
        """
        재앙의 평균 심각도를 분석합니다.
        Analyzes the average severity of the plagues.

        - KJV: Exodus 9:24 - "...there was hail, and fire mingled with the hail, very grievous..."
        - ESV: Exodus 9:24 - "...there was hail and fire flashing continually amid the hail, very severe..."
        - 개역한글: 출애굽기 9:24 - "...우박이 내리니 불덩이가 우박에 섞여 내림이 심히 맹렬하여..."
        """
        print("\n📉 === 재앙의 평균 심각도 (Average Severity of Plagues) ===")
        print("각 재앙이 평균적으로 얼마나 심각했는지 알아봅니다.")
        print("Investigating the average severity of each plague.")

        average_severity = self.plague_df['actual_damage_egypt'].mean()
        print(f"평균 애굽 피해 심각도 (Average Egypt Damage Severity): {average_severity:.2f}")

        print("\n💡 통찰 (Insight): `mean()`은 개별 재앙의 강도를 평균적인 관점에서 이해하는 데 도움을 줍니다.")
        print("Insight: `mean()` helps understand the intensity of individual plagues from an average perspective.")
        return average_severity

    def analyze_plague_count(self):
        """
        기록된 재앙의 수를 분석합니다.
        Analyzes the count of recorded plagues.

        - KJV: Exodus 9:12 - "And the LORD hardened the heart of Pharaoh..."
        - ESV: Exodus 9:12 - "But the LORD hardened the heart of Pharaoh..."
        - 개역한글: 출애굽기 9:12 - "여호와께서 바로의 마음을 강퍅케 하셨으므로..."
        """
        print("\n🔢 === 기록된 재앙의 수 (Count of Recorded Plagues) ===")
        print("하나님께서 애굽에 내리신 재앙의 횟수를 확인합니다.")
        print("Confirming the number of plagues God inflicted upon Egypt.")

        plague_count = self.plague_df['plague_name_en'].count()
        print(f"기록된 재앙의 총 수 (Total Count of Recorded Plagues): {plague_count}")

        protected_count = self.plague_df[self.plague_df['is_goshen_protected'] == True]['plague_name_en'].count()
        print(f"고센이 보호받은 재앙의 수 (Count of Plagues where Goshen was Protected): {protected_count}")

        print("\n💡 통찰 (Insight): `count()`는 하나님의 심판의 횟수와 그 속에서 백성을 보호하시는 하나님의 신실하심을 보여줍니다.")
        print("Insight: `count()` reveals the number of God's judgments and His faithfulness in protecting His people within them.")
        return plague_count, protected_count

    def run_all_analyses(self) -> dict:
        """
        모든 집계 분석을 실행하고 결과를 반환합니다.
        Runs all aggregation analyses and returns the results.
        """
        print("\n--- 출애굽기 9장: 재앙 집계 분석 시작 ---")
        print("--- Exodus Chapter 9: Plagues Aggregation Analysis Started ---")

        results = {
            'summary_statistics': self.analyze_summary_statistics(),
            'total_impact': self.analyze_total_impact(),
            'average_severity': self.analyze_average_severity(),
            'plague_counts': self.analyze_plague_count()
        }

        print("\n--- 출애굽기 9장: 재앙 집계 분석 완료 ---")
        print("--- Exodus Chapter 9: Plagues Aggregation Analysis Completed ---")
        return results

def demo_plagues_aggregation_analyzer():
    """
    PlaguesAggregationAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for PlaguesAggregationAnalyzer class.
    """
    print("\n=== Plagues Aggregation Analyzer Demo ===")
    analyzer = PlaguesAggregationAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_plagues_aggregation_analyzer()