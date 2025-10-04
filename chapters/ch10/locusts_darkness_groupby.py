
import pandas as pd
from .locusts_darkness_data import LocustsDarknessDataGenerator

class LocustsDarknessGroupbyAnalyzer:
    """
    출애굽기 10장의 메뚜기 재앙과 흑암 재앙 데이터를 그룹별로 분석하는 클래스.
    애굽과 고센의 구별, 재앙별 영향 등을 `groupby()`를 활용하여 탐구합니다.

    Class to analyze the plagues of locusts and darkness from Exodus Chapter 10 by group.
    Explores the distinction between Egypt and Goshen, and plague-specific impacts using `groupby()`.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = LocustsDarknessDataGenerator()
        self.plague_df = self.data_generator.generate_plague_impact_data()

    def analyze_impact_by_location(self):
        """
        지역(애굽/고센)별 재앙의 평균 영향을 분석합니다.
        Analyzes the average impact of plagues by location (Egypt/Goshen).

        - KJV: Exodus 10:23 - "...but all the children of Israel had light in their dwellings."
        - ESV: Exodus 10:23 - "...but all the people of Israel had light in their dwellings."
        - 개역한글: 출애굽기 10:23 - "...이스라엘 자손의 거하는 곳에는 광명이 있었더라"
        """
        print("\n📊 === 지역별 재앙 평균 영향 (Average Plague Impact by Location) ===")
        print("애굽과 고센, 두 그룹에 미친 재앙의 평균적인 영향을 비교합니다.")
        print("Comparing the average impact of plagues on two groups: Egypt and Goshen.")

        impact_by_location = self.plague_df.groupby('location')['impact_score'].mean()
        print(impact_by_location)

        print("\n💡 통찰 (Insight): `groupby()`를 통해 하나님께서 당신의 백성을 어떻게 구별하여 보호하셨는지 데이터적으로 확인할 수 있습니다.")
        print("Insight: `groupby()` allows us to numerically confirm how God distinguished and protected His people.")
        return impact_by_location

    def analyze_plague_type_impact(self):
        """
        재앙 종류별(메뚜기/흑암) 애굽의 총 피해를 분석합니다.
        Analyzes the total impact on Egypt by plague type (Locusts/Darkness).

        - KJV: Exodus 10:15 - "...there remained not any green thing in all the land of Egypt..."
        - ESV: Exodus 10:15 - "...not a single green thing remained on tree or plant in all the land of Egypt."
        - 개역한글: 출애굽기 10:15 - "...애굽 온 땅에 채소나 나무의 열매는 남지 아니하였더라"
        """
        print("\n📈 === 재앙 종류별 애굽 총 피해 (Total Egypt Impact by Plague Type) ===")
        print("메뚜기 재앙과 흑암 재앙이 애굽에 각각 얼마나 큰 피해를 주었는지 합계를 계산합니다.")
        print("Calculating the total damage inflicted on Egypt by the Locusts and Darkness plagues, respectively.")

        egypt_plagues = self.plague_df[self.plague_df['location'] == 'Egypt']
        impact_by_plague_type = egypt_plagues.groupby('plague_name_en')['impact_score'].sum()
        print(impact_by_plague_type)

        print("\n💡 통찰 (Insight): `groupby()`와 `sum()`을 통해 각 재앙이 애굽에 미친 파괴적인 규모를 이해할 수 있습니다.")
        print("Insight: `groupby()` and `sum()` help understand the destructive scale of each plague on Egypt.")
        return impact_by_plague_type

    def analyze_pharaoh_response_counts(self):
        """
        파라오의 반응별 재앙 횟수를 분석합니다.
        Analyzes the count of plagues based on Pharaoh's response.

        - KJV: Exodus 10:20 - "But the LORD hardened Pharaoh's heart..."
        - ESV: Exodus 10:20 - "But the LORD hardened Pharaoh's heart..."
        - 개역한글: 출애굽기 10:20 - "그러나 여호와께서 바로의 마음을 강퍅케 하셨으므로..."
        """
        print("\n🔢 === 파라오 반응별 재앙 횟수 (Plague Counts by Pharaoh's Response) ===")
        print("파라오의 반응(일시적 회개/강퍅함)에 따라 재앙이 몇 번 발생했는지 확인합니다.")
        print("Checking how many plagues occurred based on Pharaoh's response (temporary repentance/hardened heart).")

        response_counts = self.plague_df.groupby('pharaoh_response')['plague_name_en'].nunique()
        print(response_counts)

        print("\n💡 통찰 (Insight): `groupby()`와 `nunique()`를 통해 파라오의 완악함이 재앙의 반복에 어떻게 기여했는지 엿볼 수 있습니다.")
        print("Insight: `groupby()` and `nunique()` offer a glimpse into how Pharaoh's stubbornness contributed to the repetition of plagues.")
        return response_counts

    def run_all_analyses(self) -> dict:
        """
        모든 그룹 연산 분석을 실행하고 결과를 반환합니다.
        Runs all groupby analyses and returns the results.
        """
        print("\n--- 출애굽기 10장: 그룹 연산 분석 시작 ---")
        print("--- Exodus Chapter 10: Groupby Analysis Started ---")

        results = {
            'impact_by_location': self.analyze_impact_by_location(),
            'plague_type_impact': self.analyze_plague_type_impact(),
            'pharaoh_response_counts': self.analyze_pharaoh_response_counts()
        }

        print("\n--- 출애굽기 10장: 그룹 연산 분석 완료 ---")
        print("--- Exodus Chapter 10: Groupby Analysis Completed ---")
        return results

def demo_locusts_darkness_groupby_analyzer():
    """
    LocustsDarknessGroupbyAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for LocustsDarknessGroupbyAnalyzer class.
    """
    print("\n=== Locusts and Darkness Groupby Analyzer Demo ===")
    analyzer = LocustsDarknessGroupbyAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_locusts_darkness_groupby_analyzer()
