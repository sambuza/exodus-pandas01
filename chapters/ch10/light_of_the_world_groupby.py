
import pandas as pd
from .light_of_the_world_data import LightOfTheWorldDataGenerator

class LightOfTheWorldGroupbyAnalyzer:
    """
    요한복음 8장 12절의 "나는 세상의 빛이니" 말씀을 기반으로 빛과 어둠의 데이터를 그룹별로 분석하는 클래스.
    빛을 따르는 삶과 어둠에 거하는 삶의 영적 특성을 `groupby()`를 활용하여 탐구합니다.

    Class to analyze light and darkness data based on John 8:12, "I am the light of the world," using groupby.
    Explores the spiritual characteristics of lives following the light versus those dwelling in darkness using `groupby()`.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = LightOfTheWorldDataGenerator()
        self.light_dark_df = self.data_generator.generate_light_darkness_data()

    def analyze_impact_by_category(self):
        """
        카테고리(빛/어둠)별 삶에 미치는 평균 영향을 분석합니다.
        Analyzes the average impact on life by category (Light/Darkness).

        - KJV: John 8:12 - "...he that followeth me shall not walk in darkness, but shall have the light of life."
        - ESV: John 8:12 - "...whoever follows me will not walk in darkness, but will have the light of life."
        - 개역한글: 요한복음 8:12 - "...나를 따르는 자는 어두움에 다니지 아니하고 생명의 빛을 얻으리라"
        """
        print("\n📊 === 카테고리별 삶에 미치는 평균 영향 (Average Impact on Life by Category) ===")
        print("빛과 어둠, 두 그룹이 삶에 미치는 평균적인 영향을 비교합니다.")
        print("Comparing the average impact on life of two groups: Light and Darkness.")

        impact_by_category = self.light_dark_df.groupby('category')['impact_on_life'].mean()
        print(impact_by_category)

        print("\n💡 통찰 (Insight): `groupby()`를 통해 빛을 따르는 삶이 훨씬 긍정적인 영향을 미침을 데이터적으로 확인할 수 있습니다.")
        print("Insight: `groupby()` allows us to numerically confirm that a life following the light has a significantly more positive impact.")
        return impact_by_category

    def analyze_spiritual_growth_by_category(self):
        """
        카테고리(빛/어둠)별 영적 성장에 기여하는 정도를 분석합니다.
        Analyzes the contribution to spiritual growth by category (Light/Darkness).

        - KJV: John 1:5 - "And the light shineth in darkness; and the darkness comprehended it not."
        - ESV: John 1:5 - "The light shines in the darkness, and the darkness has not overcome it."
        - 개역한글: 요한복음 1:5 - "빛이 어두움에 비취되 어두움이 깨닫지 못하더라"
        """
        print("\n📈 === 카테고리별 영적 성장 기여도 (Spiritual Growth Contribution by Category) ===")
        print("빛과 어둠의 개념들이 영적 성장에 각각 얼마나 기여하는지 합계를 계산합니다.")
        print("Calculating the total contribution of light and darkness concepts to spiritual growth.")

        growth_by_category = self.light_dark_df.groupby('category')['spiritual_growth_factor'].sum()
        print(growth_by_category)

        print("\n💡 통찰 (Insight): `groupby()`와 `sum()`을 통해 빛의 개념들이 영적 성장에 필수적임을 이해할 수 있습니다.")
        print("Insight: `groupby()` and `sum()` help understand that concepts of light are essential for spiritual growth.")
        return growth_by_category

    def analyze_concept_counts(self):
        """
        개념별 출현 횟수를 분석합니다.
        Analyzes the count of each concept.

        - KJV: John 3:19 - "...men loved darkness rather than light..."
        - ESV: John 3:19 - "...people loved the darkness rather than the light..."
        - 개역한글: 요한복음 3:19 - "...사람들이 빛보다 어두움을 더 사랑한 것이니라"
        """
        print("\n🔢 === 개념별 출현 횟수 (Count of Concepts) ===")
        print("각 빛과 어둠 관련 개념들이 데이터에 몇 번 나타나는지 확인합니다.")
        print("Confirming how many times each light and darkness concept appears in the data.")

        concept_counts = self.light_dark_df.groupby('concept_name_en')['category'].count()
        print(concept_counts)

        print("\n💡 통찰 (Insight): `groupby()`와 `count()`를 통해 어떤 개념이 더 자주 언급되는지 파악하여 영적 중요도를 엿볼 수 있습니다.")
        print("Insight: `groupby()` and `count()` help gauge spiritual importance by identifying which concepts are mentioned more frequently.")
        return concept_counts

    def run_all_analyses(self) -> dict:
        """
        모든 그룹 연산 분석을 실행하고 결과를 반환합니다.
        Runs all groupby analyses and returns the results.
        """
        print("\n--- 요한복음 8장: 빛과 어둠 그룹 분석 시작 ---")
        print("--- John Chapter 8: Light and Darkness Group Analysis Started ---")

        results = {
            'impact_by_category': self.analyze_impact_by_category(),
            'spiritual_growth_by_category': self.analyze_spiritual_growth_by_category(),
            'concept_counts': self.analyze_concept_counts()
        }

        print("\n--- 요한복음 8장: 빛과 어둠 그룹 분석 완료 ---")
        print("--- John Chapter 8: Light and Darkness Group Analysis Completed ---")
        return results

def demo_light_of_the_world_groupby_analyzer():
    """
    LightOfTheWorldGroupbyAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for LightOfTheWorldGroupbyAnalyzer class.
    """
    print("\n=== Light of the World Groupby Analyzer Demo ===")
    analyzer = LightOfTheWorldGroupbyAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_light_of_the_world_groupby_analyzer()
