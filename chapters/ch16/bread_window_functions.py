
import pandas as pd
from .bread_of_life_data import BreadOfLifeDataGenerator

class BreadWindowFunctionsAnalyzer:
    """
    요한복음 6장의 생명의 떡 데이터를 윈도우 함수를 사용하여 분석하는 클래스.
    영적 갈증과 채움의 변화 추세를 `rolling()` 연산으로 탐구합니다.

    Class to analyze Bread of Life data from John Chapter 6 using window functions.
    Explores trends in spiritual hunger and fulfillment using `rolling()` operations.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = BreadOfLifeDataGenerator()
        self.bread_df = self.data_generator.generate_bread_of_life_data()
        self.bread_df = self.bread_df.set_index('date') # 날짜를 인덱스로 설정

    def analyze_rolling_mean_fulfillment(self):
        """
        7일 `rolling mean`을 사용하여 영적 채움 수준의 주간 평균을 분석합니다.
        Analyzes the weekly average of spiritual fulfillment using a 7-day `rolling mean`.

        - KJV: John 6:35 - "...he that cometh to me shall never hunger; and he that believeth on me shall never thirst."
        - ESV: John 6:35 - "...whoever comes to me shall not hunger, and whoever believes in me shall never thirst."
        - 개역한글: 요한복음 6:35 - "...내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라"
        """
        print("\n📊 === 7일 이동 평균 영적 채움 (7-Day Rolling Mean Spiritual Fulfillment) ===")
        print("영적 채움 수준의 7일 이동 평균을 계산하여 영적 상태의 주간 추세를 파악합니다.")
        print("Calculating the 7-day rolling mean of spiritual fulfillment to identify weekly trends in spiritual state.")

        self.bread_df['rolling_mean_fulfillment'] = self.bread_df['spiritual_fulfillment'].rolling(window=7, min_periods=1).mean()
        print(self.bread_df[['spiritual_fulfillment', 'rolling_mean_fulfillment']].to_string())

        print("\n💡 통찰 (Insight): `rolling().mean()`은 생명의 떡이신 예수님을 통해 영적 채움이 지속적으로 유지되는 패턴을 보여줍니다.")
        print("Insight: `rolling().mean()` reveals the pattern of continuous spiritual fulfillment maintained through Jesus, the Bread of Life.")
        return self.bread_df['rolling_mean_fulfillment']

    def analyze_rolling_std_hunger(self):
        """
        5일 `rolling standard deviation`을 사용하여 영적 갈증 수준의 변동성을 분석합니다.
        Analyzes the variability of spiritual hunger using a 5-day `rolling standard deviation`.

        - KJV: John 6:27 - "Labour not for the meat which perisheth, but for that meat which endureth unto everlasting life..."
        - ESV: John 6:27 - "Do not labor for the food that perishes, but for the food that endures to eternal life..."
        # 개역한글: 요한복음 6:27 - "썩을 양식을 위하여 일하지 말고 영생하도록 있는 양식을 위하여 하라..."
        """
        print("\n📈 === 5일 이동 표준편차 영적 갈증 (5-Day Rolling Std Spiritual Hunger) ===")
        print("영적 갈증 수준의 5일 이동 표준편차를 계산하여 영적 상태의 변동성을 파악합니다.")
        print("Calculating the 5-day rolling standard deviation of spiritual hunger to identify variability in spiritual state.")

        self.bread_df['rolling_std_hunger'] = self.bread_df['spiritual_hunger'].rolling(window=5, min_periods=1).std()
        print(self.bread_df[['spiritual_hunger', 'rolling_std_hunger']].to_string())

        print("\n💡 통찰 (Insight): `rolling().std()`는 말씀 섭취와 기도 생활을 통해 영적 갈증의 변동성이 줄어들고 안정적인 상태에 이르는 과정을 보여줍니다.")
        print("Insight: `rolling().std()` shows how the variability of spiritual hunger decreases and a stable state is reached through Word intake and prayer life.")
        return self.bread_df['rolling_std_hunger']

    def run_all_analyses(self) -> dict:
        """
        모든 윈도우 함수 분석을 실행하고 결과를 반환합니다.
        Runs all window function analyses and returns the results.
        """
        print("\n--- 요한복음 6장: 생명의 떡 윈도우 함수 분석 시작 ---")
        print("--- John Chapter 6: Bread of Life Window Functions Analysis Started ---")

        results = {
            'rolling_mean_fulfillment': self.analyze_rolling_mean_fulfillment(),
            'rolling_std_hunger': self.analyze_rolling_std_hunger()
        }

        print("\n--- 요한복음 6장: 생명의 떡 윈도우 함수 분석 완료 ---")
        print("--- John Chapter 6: Bread of Life Window Functions Analysis Completed ---")
        return results

def demo_bread_window_functions_analyzer():
    """
    BreadWindowFunctionsAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for BreadWindowFunctionsAnalyzer class.
    """
    print("\n=== Bread of Life Window Functions Analyzer Demo ===")
    analyzer = BreadWindowFunctionsAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_bread_window_functions_analyzer()
