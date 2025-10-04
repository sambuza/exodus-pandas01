
import pandas as pd
from .pillar_guidance_data import PillarGuidanceDataGenerator

class PillarDatetimeAnalyzer:
    """
    출애굽기 13장의 구름기둥과 불기둥 인도 데이터를 날짜/시간 기능을 사용하여 분석하는 클래스.
    하나님의 인도하심의 패턴과 시간성을 탐구합니다.

    Class to analyze pillar guidance data from Exodus Chapter 13 using date/time functionalities.
    Explores the patterns and temporality of God's guidance.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = PillarGuidanceDataGenerator()
        self.guidance_df = self.data_generator.generate_pillar_guidance_data()

    def convert_to_datetime(self):
        """
        문자열 날짜/시간 열을 `datetime` 객체로 변환합니다.
        Converts string date/time columns to `datetime` objects.

        - KJV: Exodus 13:21 - "...by day in a pillar of a cloud... and by night in a pillar of fire..."
        - ESV: Exodus 13:21 - "...by day in a pillar of cloud... and by night in a pillar of fire..."
        - 개역한글: 출애굽기 13:21 - "낮에는 구름 기둥으로... 밤에는 불 기둥으로..."
        """
        print("\n📊 === 날짜/시간 데이터 변환 (Converting Date/Time Data) ===")
        print("'event_date'와 'event_time'을 결합하여 `datetime` 객체로 변환합니다.")
        print("Combining 'event_date' and 'event_time' to convert them into `datetime` objects.")

        # 이미 generate_pillar_guidance_data에서 'event_datetime'을 생성했으므로, 여기서는 확인만 합니다.
        # If 'event_datetime' is already created in generate_pillar_guidance_data, we just verify it here.
        print(self.guidance_df[['event_date', 'event_time', 'event_datetime']].head().to_string(index=False))
        print(f"\n'event_datetime' 열의 데이터 타입: {self.guidance_df['event_datetime'].dtype}")

        print("\n💡 통찰 (Insight): `pd.to_datetime()`은 시간의 흐름을 정확하게 기록하여 하나님의 인도하심의 연속성을 파악하게 합니다.")
        print("Insight: `pd.to_datetime()` accurately records the flow of time, allowing us to understand the continuity of God's guidance.")
        return self.guidance_df

    def set_datetime_index(self):
        """
        `event_datetime` 열을 `DatetimeIndex`로 설정하여 시계열 분석의 기반을 마련합니다.
        Sets the `event_datetime` column as `DatetimeIndex` to prepare for time-series analysis.

        - KJV: Exodus 13:22 - "He took not away the pillar of the cloud by day, nor the pillar of fire by night..."
        - ESV: Exodus 13:22 - "The pillar of cloud by day and the pillar of fire by night did not depart..."
        - 개역한글: 출애굽기 13:22 - "낮에는 구름 기둥, 밤에는 불 기둥이 백성 앞에서 떠나지 아니하니라"
        """
        print("\n📈 === DatetimeIndex 설정 (Setting DatetimeIndex) ===")
        print("'event_datetime'을 인덱스로 설정하여 시간 기반 데이터 접근을 용이하게 합니다.")
        print("Setting 'event_datetime' as the index facilitates time-based data access.")

        df_indexed = self.guidance_df.set_index('event_datetime')
        print(df_indexed.head().to_string())
        print(f"\n인덱스의 데이터 타입: {df_indexed.index.dtype}")

        print("\n💡 통찰 (Insight): `DatetimeIndex`는 하나님의 인도하심이 특정 시점에 국한되지 않고 지속적이었음을 보여주는 시간의 척도가 됩니다.")
        print("Insight: `DatetimeIndex` serves as a temporal measure, showing that God's guidance was continuous, not limited to specific moments.")
        return df_indexed

    def analyze_guidance_frequency(self):
        """
        시간대별(낮/밤) 인도 유형의 빈도를 분석합니다.
        Analyzes the frequency of guidance types by time of day (day/night).

        - KJV: Exodus 13:21 - "...by day in a pillar of a cloud... and by night in a pillar of fire..."
        - ESV: Exodus 13:21 - "...by day in a pillar of cloud... and by night in a pillar of fire..."
        - 개역한글: 출애굽기 13:21 - "낮에는 구름 기둥으로... 밤에는 불 기둥으로..."
        """
        print("\n🔢 === 시간대별 인도 유형 빈도 (Guidance Type Frequency by Time of Day) ===")
        print("낮과 밤에 나타난 구름 기둥과 불기둥의 빈도를 확인합니다.")
        print("Checking the frequency of the pillar of cloud by day and the pillar of fire by night.")

        # 시간대 추출 (낮: 06:00-17:59, 밤: 18:00-05:59)
        self.guidance_df['time_of_day_category'] = self.guidance_df['event_datetime'].dt.hour.apply(
            lambda x: 'Day' if 6 <= x < 18 else 'Night'
        )
        frequency = self.guidance_df.groupby(['time_of_day_category', 'guidance_type']).size().unstack(fill_value=0)
        print(frequency)

        print("\n💡 통찰 (Insight): `dt.hour`와 `groupby()`를 통해 하나님의 인도하심이 낮과 밤, 모든 시간에 걸쳐 세밀하게 이루어졌음을 알 수 있습니다.")
        print("Insight: `dt.hour` and `groupby()` reveal that God's guidance was meticulously provided throughout both day and night.")
        return frequency

    def run_all_analyses(self) -> dict:
        """
        모든 날짜/시간 분석을 실행하고 결과를 반환합니다.
        Runs all date/time analyses and returns the results.
        """
        print("\n--- 출애굽기 13장: 구름기둥/불기둥 날짜/시간 분석 시작 ---")
        print("--- Exodus Chapter 13: Pillar Guidance Date/Time Analysis Started ---")

        results = {
            'datetime_conversion': self.convert_to_datetime(),
            'datetime_index_set': self.set_datetime_index(),
            'guidance_frequency': self.analyze_guidance_frequency()
        }

        print("\n--- 출애굽기 13장: 구름기둥/불기둥 날짜/시간 분석 완료 ---")
        print("--- Exodus Chapter 13: Pillar Guidance Date/Time Analysis Completed ---")
        return results

def demo_pillar_datetime_analyzer():
    """
    PillarDatetimeAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for PillarDatetimeAnalyzer class.
    """
    print("\n=== Pillar Datetime Analyzer Demo ===")
    analyzer = PillarDatetimeAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_pillar_datetime_analyzer()
