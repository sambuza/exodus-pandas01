

import pandas as pd
from .red_sea_crossing_data import RedSeaCrossingDataGenerator

class RedSeaDuplicatesUniqueAnalyzer:
    """
    출애굽기 14장의 홍해 사건 데이터를 `duplicated()`, `drop_duplicates()`, `unique()`, `nunique()`를 사용하여 분석하는 클래스.
    중복된 두려움과 고유한 구원의 순간을 탐구합니다.

    Class to analyze Red Sea crossing data from Exodus Chapter 14 using `duplicated()`, `drop_duplicates()`, `unique()`, `nunique()`.
    Explores duplicated fears and unique moments of salvation.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = RedSeaCrossingDataGenerator()
        self.red_sea_df = self.data_generator.generate_red_sea_event_data()

    def analyze_duplicated_emotions(self):
        """
        이스라엘 백성의 중복된 감정(두려움)을 식별합니다.
        Identifies duplicated emotions (fear) among the Israelites.

        - KJV: Exodus 14:10 - "...they were sore afraid..."
        - ESV: Exodus 14:10 - "...they were in great fear..."
        - 개역한글: 출애굽기 14:10 - "...이스라엘 자손이 심히 두려워하여"
        """
        print("\n📊 === 중복된 감정 식별 (Identifying Duplicated Emotions) ===")
        print("이스라엘 백성의 반복되는 두려움을 `duplicated()`로 찾아봅니다.")
        print("Using `duplicated()` to find recurring fears among the Israelites.")

        # 'emotion_level'이 5 이상인 'event_description_en'의 중복 여부 확인
        fear_events = self.red_sea_df[self.red_sea_df['emotion_level'] >= 5]
        duplicated_fear = fear_events['event_description_en'].duplicated()
        print(fear_events[duplicated_fear].to_string(index=False))

        print("\n💡 통찰 (Insight): `duplicated()`는 인간의 연약함과 반복되는 죄의 패턴을 데이터적으로 보여줍니다.")
        print("Insight: `duplicated()` numerically illustrates human weakness and recurring patterns of sin.")
        return fear_events[duplicated_fear]

    def analyze_unique_events(self):
        """
        홍해 사건의 고유한 전환점들을 `drop_duplicates()`로 식별합니다.
        Identifies unique turning points in the Red Sea event using `drop_duplicates()`.

        - KJV: Exodus 14:21 - "...the LORD caused the sea to go back by a strong east wind..."
        - ESV: Exodus 14:21 - "...the LORD drove the sea back by a strong east wind..."
        - 개역한글: 출애굽기 14:21 - "...여호와께서 큰 동풍으로 밤새도록 바닷물을 물러가게 하시니"
        """
        print("\n📈 === 고유한 사건 식별 (Identifying Unique Events) ===")
        print("홍해 사건의 핵심적인 고유한 전환점들을 `drop_duplicates()`로 추출합니다.")
        print("Extracting key unique turning points of the Red Sea event using `drop_duplicates()`.")

        unique_events = self.red_sea_df.drop_duplicates(subset=['event_description_en', 'group_status'])
        print(unique_events[['event_description_en', 'group_status', 'divine_intervention']].to_string(index=False))

        print("\n💡 통찰 (Insight): `drop_duplicates()`는 불필요한 노이즈를 제거하고 하나님의 유일한 구원 계획을 선명하게 드러냅니다.")
        print("Insight: `drop_duplicates()` removes unnecessary noise and clearly reveals God's unique salvation plan.")
        return unique_events

    def analyze_unique_groups_outcomes(self):
        """
        홍해 사건에 관련된 고유한 그룹과 결과의 수를 분석합니다.
        Analyzes the number of unique groups and outcomes involved in the Red Sea event.

        - KJV: Exodus 14:29 - "But the children of Israel walked upon dry land in the midst of the sea..."
        - ESV: Exodus 14:29 - "But the people of Israel walked on dry ground through the sea..."
        - 개역한글: 출애굽기 14:29 - "이스라엘 자손은 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니"
        """
        print("\n🔢 === 고유한 그룹 및 결과 분석 (Analyzing Unique Groups and Outcomes) ===")
        print("홍해 사건에 참여한 고유한 그룹과 발생한 고유한 결과의 수를 확인합니다.")
        print("Confirming the number of unique groups involved and unique outcomes that occurred in the Red Sea event.")

        unique_groups = self.red_sea_df['group_status'].unique()
        num_unique_groups = self.red_sea_df['group_status'].nunique()
        unique_outcomes = self.red_sea_df['outcome'].unique()
        num_unique_outcomes = self.red_sea_df['outcome'].nunique()

        print(f"고유한 그룹 (Unique Groups): {list(unique_groups)}")
        print(f"고유한 그룹 수 (Number of Unique Groups): {num_unique_groups}")
        print(f"고유한 결과 (Unique Outcomes): {list(unique_outcomes)}")
        print(f"고유한 결과 수 (Number of Unique Outcomes): {num_unique_outcomes}")

        print("\n💡 통찰 (Insight): `unique()`와 `nunique()`는 하나님의 구원 계획 속에서 각 그룹의 명확한 운명과 그분의 주권적인 역사를 보여줍니다.")
        print("Insight: `unique()` and `nunique()` reveal the distinct destinies of each group and God's sovereign work within His salvation plan.")
        return unique_groups, num_unique_groups, unique_outcomes, num_unique_outcomes

    def run_all_analyses(self) -> dict:
        """
        모든 중복 및 고유값 분석을 실행하고 결과를 반환합니다.
        Runs all duplicate and unique value analyses and returns the results.
        """
        print("\n--- 출애굽기 14장: 홍해 사건 중복/고유값 분석 시작 ---")
        print("--- Exodus Chapter 14: Red Sea Event Duplicates/Unique Analysis Started ---")

        results = {
            'duplicated_emotions': self.analyze_duplicated_emotions(),
            'unique_events': self.analyze_unique_events(),
            'unique_groups_outcomes': self.analyze_unique_groups_outcomes()
        }

        print("\n--- 출애굽기 14장: 홍해 사건 중복/고유값 분석 완료 ---")
        print("--- Exodus Chapter 14: Red Sea Event Duplicates/Unique Analysis Completed ---")
        return results

def demo_red_sea_duplicates_unique_analyzer():
    """
    RedSeaDuplicatesUniqueAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for RedSeaDuplicatesUniqueAnalyzer class.
    """
    print("\n=== Red Sea Duplicates/Unique Analyzer Demo ===")
    analyzer = RedSeaDuplicatesUniqueAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_red_sea_duplicates_unique_analyzer()
