
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class BreadOfLifeDataGenerator:
    """
    요한복음 6장의 생명의 떡 데이터를 생성하는 클래스.
    영적 갈증, 채움, 말씀 섭취를 시계열로 시뮬레이션합니다.

    Class to generate Bread of Life data from John Chapter 6.
    Simulates spiritual hunger, fulfillment, and Word intake as a time series.
    """

    def __init__(self):
        self.spiritual_journey_data = self._load_spiritual_journey_data()

    def _load_spiritual_journey_data(self):
        """
        영적 여정의 주요 지표에 대한 기본 정보를 로드합니다.
        Loads basic information about key indicators of the spiritual journey.
        """
        # KJV: John 6:35 - "...I am the bread of life: he that cometh to me shall never hunger; and he that believeth on me shall never thirst."
        # ESV: John 6:35 - "...I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst."
        # 개역한글: 요한복음 6:35 - "...내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라"
        dates = [datetime(2024, 5, 1) + timedelta(days=i) for i in range(30)]
        return pd.DataFrame({
            'date': dates,
            'spiritual_hunger': np.random.randint(1, 10, size=30), # 1-10 스케일 (10: 극심한 갈증)
            'word_intake_hours': np.random.randint(0, 2, size=30), # 말씀 섭취 시간 (시간)
            'prayer_time_minutes': np.random.randint(10, 60, size=30), # 기도 시간 (분)
            'spiritual_fulfillment': np.random.randint(1, 10, size=30) # 1-10 스케일 (10: 완전한 채움)
        })

    def generate_bread_of_life_data(self) -> pd.DataFrame:
        """
        상세한 생명의 떡 데이터를 생성합니다.
        영적 갈증, 채움, 말씀 섭취를 시계열로 구성합니다.

        Generates detailed Bread of Life data.
        Structures spiritual hunger, fulfillment, and Word intake as a time series.

        Returns:
            pd.DataFrame: 상세 생명의 떡 데이터
        """
        df = self.spiritual_journey_data.copy()

        # 말씀 섭취와 기도 시간에 따른 영적 채움 수준 조정
        df['spiritual_fulfillment'] = np.clip(
            df['spiritual_fulfillment'] + df['word_intake_hours'] * 2 + df['prayer_time_minutes'] // 15,
            1, 10
        )
        # 영적 채움이 높으면 갈증은 낮아짐
        df['spiritual_hunger'] = np.clip(11 - df['spiritual_fulfillment'] + np.random.randint(-1, 1, size=len(df)), 1, 10)

        # KJV: John 6:51 - "I am the living bread which came down from heaven: if any man eat of this bread, he shall live for ever..."
        # ESV: John 6:51 - "I am the living bread that came down from heaven. If anyone eats of this bread, he will live forever..."
        # 개역한글: 요한복음 6:51 - "나는 하늘에서 내려온 산 떡이니 사람이 이 떡을 먹으면 영생하리라..."
        print("✨ 요한복음 6장 생명의 떡 데이터가 생성되었습니다.")
        print("영적 갈증, 채움, 말씀 섭취를 시계열로 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 생명의 떡이신 예수님을 통해 영적 갈증이 해소되고 영원한 채움을 얻는 패턴을 시간 데이터로 볼 수 있습니다.")
        print("Spiritual Insight: Through Jesus, the Bread of Life, we can see a pattern of spiritual hunger being quenched and eternal fulfillment gained over time.")

        return df

def demo_bread_of_life_data_generation():
    """
    BreadOfLifeDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for BreadOfLifeDataGenerator class.
    """
    print("--- Bread of Life Data Generation Demo ---")
    print("--- 생명의 떡 데이터 생성 데모 ---")
    generator = BreadOfLifeDataGenerator()
    data = generator.generate_bread_of_life_data()
    return data

if __name__ == "__main__":
    demo_bread_of_life_data_generation()
