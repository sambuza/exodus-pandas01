
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class MannaOrdinanceDataGenerator:
    """
    출애굽기 16장의 만나의 규례 데이터를 생성하는 클래스.
    매일의 만나 공급, 이스라엘의 순종/불순종을 시계열로 시뮬레이션합니다.

    Class to generate manna ordinance data from Exodus Chapter 16.
    Simulates daily manna provision and Israel's obedience/disobedience as a time series.
    """

    def __init__(self):
        self.manna_events = self._load_manna_events()

    def _load_manna_events(self):
        """
        만나 규례의 주요 사건에 대한 기본 정보를 로드합니다.
        Loads basic information about key events of the manna ordinance.
        """
        # KJV: Exodus 16:4 - "...I will rain bread from heaven for you; and the people shall go out and gather a certain rate every day..."
        # ESV: Exodus 16:4 - "...I will rain bread from heaven for you, and the people shall go out and gather a day's portion every day..."
        # 개역한글: 출애굽기 16:4 - "...하늘에서 너희를 위하여 양식을 비같이 내리리니 백성이 나가서 일용할 것을 날마다 거둘 것이라"
        return pd.DataFrame({
            'day_num': range(1, 31), # 30일간의 광야 여정 시뮬레이션
            'date': pd.to_datetime([f'2024-04-{d:02d}' for d in range(1, 31)]),
            'manna_gathered_kg': np.random.randint(100, 150, size=30), # 매일 거둔 만나 양
            'israel_obedience': np.random.randint(7, 10, size=30), # 1-10 스케일 (10: 완전 순종)
            'israel_complaint': np.random.randint(1, 4, size=30) # 1-10 스케일 (10: 극심한 불평)
        })

    def generate_manna_data(self) -> pd.DataFrame:
        """
        상세한 만나 데이터를 생성합니다.
        날짜 정보를 포함하여 시계열 데이터로 구성합니다.

        Generates detailed manna data.
        Structures it as time-series data including date information.

        Returns:
            pd.DataFrame: 상세 만나 데이터
        """
        df = self.manna_events.copy()

        # 안식일(7일째, 14일째, 21일째, 28일째)에는 만나를 거두지 않음
        # 안식일 전날(6일째, 13일째, 20일째, 27일째)에는 두 배로 거둠
        for i in range(len(df)):
            if (df.loc[i, 'day_num'] % 7) == 0: # 안식일
                df.loc[i, 'manna_gathered_kg'] = 0
                df.loc[i, 'israel_obedience'] = 10 # 안식일 규례 준수
                df.loc[i, 'israel_complaint'] = 1 # 불평 없음
            elif (df.loc[i, 'day_num'] % 7) == 6: # 안식일 전날
                df.loc[i, 'manna_gathered_kg'] *= 2
                df.loc[i, 'israel_obedience'] = 9 # 이틀치 거둠
                df.loc[i, 'israel_complaint'] = 2 # 불평 적음

        # KJV: Exodus 16:20 - "...some of them left of it till the morning, and it bred worms, and stank..."
        # ESV: Exodus 16:20 - "But they did not listen to Moses. Some left part of it till the morning, and it bred worms and stank."
        # 개역한글: 출애굽기 16:20 - "그들이 모세의 말을 청종치 아니하고 더러는 아침까지 두었더니 벌레가 생기고 냄새가 난지라"
        print("✨ 출애굽기 16장 만나 규례 데이터가 생성되었습니다.")
        print("매일의 만나 공급, 이스라엘의 순종/불순종을 시계열로 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 만나의 규례는 하나님의 매일의 공급과 순종의 중요성을 보여줍니다. 시간 데이터는 그 패턴을 드러냅니다.")
        print("Spiritual Insight: The manna ordinance reveals God's daily provision and the importance of obedience. Time data reveals its patterns.")

        return df

def demo_manna_ordinance_data_generation():
    """
    MannaOrdinanceDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for MannaOrdinanceDataGenerator class.
    """
    print("--- Manna Ordinance Data Generation Demo ---")
    print("--- 만나 규례 데이터 생성 데모 ---")
    generator = MannaOrdinanceDataGenerator()
    data = generator.generate_manna_data()
    return data

if __name__ == "__main__":
    demo_manna_ordinance_data_generation()
