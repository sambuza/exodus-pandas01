import pandas as pd
from .officials_son_data import OfficialsSonDataGenerator

class OfficialsSonAggregationAnalyzer:
    """
    요한복음 4장의 왕의 신하의 아들 치유 데이터를 집계하여 분석하는 클래스.
    신하의 믿음 성장과 예수님 말씀의 능력을 통계적으로 탐구합니다.

    Class to analyze the healing data of the royal official's son in John 4 using aggregation.
    Statistically explores the official's growth in faith and the power of Jesus' word.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = OfficialsSonDataGenerator()
        self.healing_df = self.data_generator.generate_detailed_healing_data()

    def analyze_faith_level_summary(self):
        """
        신하의 믿음 수준에 대한 요약 통계를 분석합니다.
        Analyzes summary statistics for the official's faith level.

        - KJV: John 4:50 - "...the man believed the word that Jesus had spoken unto him..."
        - ESV: John 4:50 - "...The man believed the word that Jesus spoke to him..."
        - 개역한글: 요한복음 4:50 - "...그 사람이 예수의 하신 말씀을 믿고 가더니"
        """
        print("\n📊 === 신하의 믿음 수준 요약 통계 (Official's Faith Level Summary Statistics) ===")
        print("왕의 신하의 믿음 수준 변화를 숫자로 요약합니다.")
        print("Summarizing the changes in the royal official's faith level numerically.")

        summary = self.healing_df['officials_faith_level'].describe()
        print(summary)

        print("\n💡 통찰 (Insight): `describe()`는 믿음이 예수님의 말씀을 통해 어떻게 성장하고 확신에 이르는지 보여줍니다.")
        print("Insight: `describe()` shows how faith grows and leads to conviction through Jesus' word.")
        return summary

    def analyze_average_faith_and_healing_time(self):
        """
        평균 믿음 수준과 치유까지 걸린 평균 시간을 분석합니다.
        Analyzes the average faith level and average time taken for healing.

        - KJV: John 4:53 - "...at the same hour, in the which Jesus said unto him, Thy son liveth..."
        - ESV: John 4:53 - "...that was the hour when Jesus had said to him, 'Your son will live.'..."
        - 개역한글: 요한복음 4:53 - "...예수께서 네 아들이 살았다 하신 그 시각인 줄 알고..."
        """
        print("\n📈 === 평균 믿음 수준 및 치유 시간 (Average Faith Level & Healing Time) ===")
        print("신하의 평균 믿음 수준과 아들이 치유되기까지 걸린 평균 시간을 알아봅니다.")
        print("Investigating the official's average faith level and the average time until his son's healing.")

        average_faith = self.healing_df['officials_faith_level'].mean()
        average_time_to_healing = self.healing_df['time_elapsed_hours'].max() # 마지막 이벤트까지의 시간

        print(f"평균 신하의 믿음 수준 (Average Official's Faith Level): {average_faith:.2f}")
        print(f"치유까지 경과된 시간 (Time Elapsed until Healing): {average_time_to_healing} 시간")

        print("\n💡 통찰 (Insight): `mean()`과 `max()`를 통해 믿음의 여정과 말씀의 즉각적인 효력을 이해할 수 있습니다.")
        print("Insight: `mean()` and `max()` help understand the journey of faith and the immediate effect of the Word.")
        return average_faith, average_time_to_healing

    def analyze_event_counts(self):
        """
        치유 여정의 주요 사건들의 수를 분석합니다.
        Analyzes the count of key events in the healing journey.

        - KJV: John 4:51 - "And as he was now going down, his servants met him..."
        - ESV: John 4:51 - "As he was going down, his servants met him..."
        - 개역한글: 요한복음 4:51 - "내려가는 길에서 그 종들이 오다가 만나서..."
        """
        print("\n🔢 === 치유 여정 사건 수 (Count of Healing Journey Events) ===")
        print("왕의 신하의 아들 치유 여정에서 발생한 주요 사건들의 횟수를 확인합니다.")
        print("Confirming the number of key events that occurred during the healing journey of the royal official's son.")

        event_count = self.healing_df['event_name_en'].count()
        print(f"기록된 치유 여정 사건의 총 수 (Total Count of Recorded Healing Events): {event_count}")

        # 열이 'High'였던 사건 수
        high_fever_events = self.healing_df[self.healing_df['son_fever_level'] >= 39.0]['event_name_en'].count()
        print(f"고열 상태 사건 수 (Count of High Fever Events): {high_fever_events}")

        print("\n💡 통찰 (Insight): `count()`는 믿음의 여정에서 각 단계의 중요성과 말씀의 성취 과정을 보여줍니다.")
        print("Insight: `count()` shows the importance of each stage in the journey of faith and the fulfillment of the Word.")
        return event_count, high_fever_events

    def run_all_analyses(self) -> dict:
        """
        모든 집계 분석을 실행하고 결과를 반환합니다.
        Runs all aggregation analyses and returns the results.
        """
        print("\n--- 요한복음 4장: 치유와 믿음 집계 분석 시작 ---")
        print("--- John Chapter 4: Healing and Faith Aggregation Analysis Started ---")

        results = {
            'faith_level_summary': self.analyze_faith_level_summary(),
            'average_faith_and_time': self.analyze_average_faith_and_healing_time(),
            'event_counts': self.analyze_event_counts()
        }

        print("\n--- 요한복음 4장: 치유와 믿음 집계 분석 완료 ---")
        print("--- John Chapter 4: Healing and Faith Aggregation Analysis Completed ---")
        return results

def demo_officials_son_aggregation_analyzer():
    """
    OfficialsSonAggregationAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for OfficialsSonAggregationAnalyzer class.
    """
    print("\n=== Royal Official's Son Aggregation Analyzer Demo ===")
    analyzer = OfficialsSonAggregationAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_officials_son_aggregation_analyzer()