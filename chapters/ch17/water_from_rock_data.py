
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class WaterFromRockDataGenerator:
    """
    출애굽기 17장의 반석에서 난 물 데이터를 생성하는 클래스.
    이스라엘의 갈증, 불평, 그리고 하나님의 기적적인 공급을 시계열로 시뮬레이션합니다.

    Class to generate water from the rock data from Exodus Chapter 17.
    Simulates Israel's thirst, complaints, and God's miraculous provision as a time series.
    """

    def __init__(self):
        self.rock_events = self._load_rock_events()

    def _load_rock_events(self):
        """
        반석에서 난 물 사건의 주요 단계에 대한 기본 정보를 로드합니다.
        Loads basic information about key stages of the water from the rock event.
        """
        # KJV: Exodus 17:3 - "And the people thirsted there for water; and the people murmured against Moses..."
        # ESV: Exodus 17:3 - "But the people thirsted there for water, and the people grumbled against Moses..."
        # 개역한글: 출애굽기 17:3 - "거기서 백성이 물이 없으므로 모세를 대하여 원망하여 가로되..."
        dates = [datetime(2024, 6, 1) + timedelta(hours=i) for i in range(24 * 5)] # 5일간의 데이터
        return pd.DataFrame({
            'timestamp': dates,
            'thirst_level': np.random.randint(5, 10, size=len(dates)), # 1-10 스케일 (10: 극심한 갈증)
            'israel_complaint_level': np.random.randint(1, 5, size=len(dates)), # 1-10 스케일 (10: 극심한 불평)
            'water_supply_status': ['None'] * len(dates) # 초기에는 물 공급 없음
        })

    def generate_water_from_rock_data(self) -> pd.DataFrame:
        """
        상세한 반석에서 난 물 데이터를 생성합니다.
        갈증, 불평, 물 공급 상태를 시계열로 구성합니다.

        Generates detailed water from the rock data.
        Structures thirst, complaints, and water supply status as a time series.

        Returns:
            pd.DataFrame: 상세 반석에서 난 물 데이터
        """
        df = self.rock_events.copy()

        # 특정 시점에 물 공급 발생 시뮬레이션
        # 3일째 12시에 물 공급 시작
        supply_start_time = datetime(2024, 6, 3, 12, 0)
        df.loc[df['timestamp'] >= supply_start_time, 'water_supply_status'] = 'Flowing'
        df.loc[df['timestamp'] >= supply_start_time, 'thirst_level'] = np.clip(df['thirst_level'] - np.random.randint(5, 8), 1, 10)
        df.loc[df['timestamp'] >= supply_start_time, 'israel_complaint_level'] = np.clip(df['israel_complaint_level'] - np.random.randint(2, 4), 1, 10)

        # KJV: Exodus 17:6 - "...thou shalt smite the rock, and there shall come water out of it, that the people may drink..."
        # ESV: Exodus 17:6 - "...you shall strike the rock, and water shall come out of it, and the people will drink."
        # 개역한글: 출애굽기 17:6 - "...네가 반석을 치라 그리하면 그곳에서 물이 나리니 백성이 마시리라"
        print("✨ 출애굽기 17장 반석에서 난 물 데이터가 생성되었습니다.")
        print("이스라엘의 갈증, 불평, 하나님의 기적적인 공급을 시계열로 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 하나님의 공급은 인간의 불평 속에서도 기적적으로 나타나며, 시간의 흐름 속에서 그 신실하심을 보여줍니다.")
        print("Spiritual Insight: God's provision miraculously appears even amidst human complaints, demonstrating His faithfulness over time.")

        return df

def demo_water_from_rock_data_generation():
    """
    WaterFromRockDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for WaterFromRockDataGenerator class.
    """
    print("--- Water From Rock Data Generation Demo ---")
    print("--- 반석에서 난 물 데이터 생성 데모 ---")
    generator = WaterFromRockDataGenerator()
    data = generator.generate_water_from_rock_data()
    return data

if __name__ == "__main__":
    demo_water_from_rock_data_generation()
