
import pandas as pd
from .jesus_walks_water_data import JesusWalksWaterDataGenerator

class JesusWalksWaterDuplicatesUniqueAnalyzer:
    """
    요한복음 6장의 예수님께서 물 위를 걸으신 사건 데이터를 `duplicated()`, `drop_duplicates()`, `unique()`, `nunique()`를 사용하여 분석하는 클래스.
    제자들의 중복된 두려움과 예수님의 고유한 평안을 탐구합니다.

    Class to analyze Jesus walking on water data from John Chapter 6 using `duplicated()`, `drop_duplicates()`, `unique()`, `nunique()`.
    Explores duplicated fears of the disciples and Jesus' unique peace.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = JesusWalksWaterDataGenerator()
        self.jesus_walks_df = self.data_generator.generate_jesus_walks_water_data()

    def analyze_duplicated_emotions(self):
        """
        제자들의 중복된 감정(두려움)을 식별합니다.
        Identifies duplicated emotions (fear) among the disciples.

        - KJV: John 6:19 - "...they were afraid."
        - ESV: John 6:19 - "...they were frightened."
        - 개역한글: 요한복음 6:19 - "...두려워하는지라"
        """
        print("\n📊 === 중복된 제자들의 감정 식별 (Identifying Duplicated Disciples' Emotions) ===")
        print("제자들의 반복되는 두려움을 `duplicated()`로 찾아봅니다.")
        print("Using `duplicated()` to find recurring fears among the disciples.")

        duplicated_emotion = self.jesus_walks_df['disciple_emotion'].duplicated()
        print(self.jesus_walks_df[duplicated_emotion].to_string(index=False))

        print("\n💡 통찰 (Insight): `duplicated()`는 인간의 연약함과 반복되는 두려움의 패턴을 데이터적으로 보여줍니다.")
        print("Insight: `duplicated()` numerically illustrates human weakness and recurring patterns of fear.")
        return self.jesus_walks_df[duplicated_emotion]

    def analyze_unique_emotions_events(self):
        """
        제자들의 고유한 감정과 사건의 고유한 유형을 분석합니다.
        Analyzes unique emotions of the disciples and unique types of events.

        - KJV: John 6:20 - "But he saith unto them, It is I; be not afraid."
        - ESV: John 6:20 - "But he said to them, 'It is I; do not be afraid.'"
        - 개역한글: 요한복음 6:20 - "예수께서 곧 그들에게 말씀하여 가라사대 안심하라 내니 두려워 말라 하신대"
        """
        print("\n📈 === 고유한 감정 및 사건 유형 분석 (Analyzing Unique Emotions and Event Types) ===")
        print("제자들이 보인 고유한 감정과 사건의 고유한 유형을 `unique()`와 `nunique()`로 추출합니다.")
        print("Extracting unique emotions shown by disciples and unique event types using `unique()` and `nunique()`.")

        unique_emotions = self.jesus_walks_df['disciple_emotion'].unique()
        num_unique_emotions = self.jesus_walks_df['disciple_emotion'].nunique()
        unique_event_types = self.jesus_walks_df['event_type'].unique()
        num_unique_event_types = self.jesus_walks_df['event_type'].nunique()

        print(f"고유한 감정 (Unique Emotions): {list(unique_emotions)}")
        print(f"고유한 감정 수 (Number of Unique Emotions): {num_unique_emotions}")
        print(f"고유한 사건 유형 (Unique Event Types): {list(unique_event_types)}")
        print(f"고유한 사건 유형 수 (Number of Unique Event Types): {num_unique_event_types}")

        print("\n💡 통찰 (Insight): `unique()`와 `nunique()`는 세상의 혼란 속에서도 예수님만이 주실 수 있는 고유한 평안과 그분의 유일한 현현을 보여줍니다.")
        print("Insight: `unique()` and `nunique()` reveal the unique peace only Jesus can give amidst worldly chaos, and His singular appearance.")
        return unique_emotions, num_unique_emotions, unique_event_types, num_unique_event_types

    def run_all_analyses(self) -> dict:
        """
        모든 중복 및 고유값 분석을 실행하고 결과를 반환합니다.
        Runs all duplicate and unique value analyses and returns the results.
        """
        print("\n--- 요한복음 6장: 물 위를 걸으신 사건 중복/고유값 분석 시작 ---")
        print("--- John Chapter 6: Jesus Walks on Water Duplicates/Unique Analysis Started ---")

        results = {
            'duplicated_emotions': self.analyze_duplicated_emotions(),
            'unique_emotions_events': self.analyze_unique_emotions_events()
        }

        print("\n--- 요한복음 6장: 물 위를 걸으신 사건 중복/고유값 분석 완료 ---")
        print("--- John Chapter 6: Jesus Walks on Water Duplicates/Unique Analysis Completed ---")
        return results

def demo_jesus_walks_water_duplicates_unique_analyzer():
    """
    JesusWalksWaterDuplicatesUniqueAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for JesusWalksWaterDuplicatesUniqueAnalyzer class.
    """
    print("\n=== Jesus Walks on Water Duplicates/Unique Analyzer Demo ===")
    analyzer = JesusWalksWaterDuplicatesUniqueAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_jesus_walks_water_duplicates_unique_analyzer()
