
import pandas as pd
from .living_water_data import LivingWaterDataGenerator

class LivingWaterResampleAnalyzer:
    """
    요한복음 7장의 생수의 강 데이터를 `resample()`을 사용하여 분석하는 클래스.
    영적 갈증과 채움의 변화를 시간 간격별로 탐구합니다.

    Class to analyze living water data from John Chapter 7 using `resample()`.
    Explores changes in spiritual thirst and fulfillment over time intervals.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = LivingWaterDataGenerator()
        self.living_water_df = self.data_generator.generate_living_water_data()
        self.living_water_df = self.living_water_df.set_index('event_datetime') # DatetimeIndex 설정

    def analyze_daily_resample(self):
        """
        일별로 데이터를 재표본화하여 영적 갈증과 채움의 일일 평균을 분석합니다.
        Resamples data daily to analyze daily averages of spiritual thirst and fulfillment.

        - KJV: John 7:37 - "...If any man thirst, let him come unto me, and drink."
        - ESV: John 7:37 - "...If anyone thirsts, let him come to me and drink."
        - 개역한글: 요한복음 7:37 - "...누구든지 목마르거든 내게로 와서 마시라"
        """
        print("\n📊 === 일별 영적 상태 재표본화 (Daily Spiritual State Resampling) ===")
        print("일별로 영적 갈증과 채움의 평균을 계산하여 일일 변화를 파악합니다.")
        print("Calculating daily averages of spiritual thirst and fulfillment to understand daily changes.")

        daily_avg = self.living_water_df[['thirst_level', 'fulfillment_level']].resample('D').mean()
        print(daily_avg.to_string())

        print("\n💡 통찰 (Insight): `resample('D').mean()`은 매일매일 말씀으로 채워지는 삶의 패턴을 보여주며, 영적 갈증이 해소되는 과정을 시계열적으로 이해하게 합니다.")
        print("Insight: `resample('D').mean()` shows the daily pattern of a life filled with the Word, helping to understand the process of spiritual thirst being quenched over time.")
        return daily_avg

    def analyze_event_counts_by_day(self):
        """
        일별 사건 발생 횟수를 분석합니다.
        Analyzes the count of events occurring daily.

        - KJV: John 7:38 - "He that believeth on me, as the scripture hath said, out of his belly shall flow rivers of living water."
        - ESV: John 7:38 - "Whoever believes in me, as the Scripture has said, 'Out of his heart will flow rivers of living water.'"
        - 개역한글: 요한복음 7:38 - "나를 믿는 자는 성경에 이름과 같이 그 배에서 생수의 강이 흘러나리라 하시니"
        """
        print("\n📈 === 일별 사건 발생 횟수 (Daily Event Counts) ===")
        print("일별로 발생한 영적 사건들의 횟수를 계산하여 활동 빈도를 파악합니다.")
        print("Calculating the daily count of spiritual events to understand activity frequency.")

        daily_counts = self.living_water_df['event_type'].resample('D').count()
        print(daily_counts.to_string())

        print("\n💡 통찰 (Insight): `resample('D').count()`는 영적 활동의 꾸준함과 말씀에 대한 반응의 빈도를 보여줍니다.")
        print("Insight: `resample('D').count()` reveals the consistency of spiritual activities and the frequency of response to the Word.")
        return daily_counts

    def run_all_analyses(self) -> dict:
        """
        모든 재표본화 분석을 실행하고 결과를 반환합니다.
        Runs all resampling analyses and returns the results.
        """
        print("\n--- 요한복음 7장: 생수의 강 재표본화 분석 시작 ---")
        print("--- John Chapter 7: Living Water Resampling Analysis Started ---")

        results = {
            'daily_resample_avg': self.analyze_daily_resample(),
            'daily_event_counts': self.analyze_event_counts_by_day()
        }

        print("\n--- 요한복음 7장: 생수의 강 재표본화 분석 완료 ---")
        print("--- John Chapter 7: Living Water Resampling Analysis Completed ---")
        return results

def demo_living_water_resample_analyzer():
    """
    LivingWaterResampleAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for LivingWaterResampleAnalyzer class.
    """
    print("\n=== Living Water Resampling Analyzer Demo ===")
    analyzer = LivingWaterResampleAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_living_water_resample_analyzer()
