
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class LivingWaterFlowDataGenerator:
    """
    요한복음 7장의 생수의 강 흐름 데이터를 생성하는 클래스.
    말씀 섭취, 기도 강도, 영적 흐름 속도를 시계열로 시뮬레이션합니다.

    Class to generate living water flow data from John Chapter 7.
    Simulates Word intake, prayer intensity, and spiritual flow rate as a time series.
    """

    def __init__(self):
        self.flow_events = self._load_flow_events()

    def _load_flow_events(self):
        """
        생수의 강 흐름의 주요 지표에 대한 기본 정보를 로드합니다.
        Loads basic information about key indicators of the living water flow.
        """
        # KJV: John 7:38 - "He that believeth on me, as the scripture hath said, out of his belly shall flow rivers of living water."
        # ESV: John 7:38 - "Whoever believes in me, as the Scripture has said, 'Out of his heart will flow rivers of living water.'"
        # 개역한글: 요한복음 7:38 - "나를 믿는 자는 성경에 이름과 같이 그 배에서 생수의 강이 흘러나리라 하시니"
        dates = [datetime(2024, 7, 1) + timedelta(hours=i) for i in range(24 * 5)] # 5일간의 데이터
        return pd.DataFrame({
            'timestamp': dates,
            'word_intake_score': np.random.randint(1, 10, size=len(dates)), # 1-10 스케일 (10: 말씀 섭취 높음)
            'prayer_intensity_score': np.random.randint(1, 10, size=len(dates)), # 1-10 스케일 (10: 기도 강도 높음)
            'spiritual_flow_rate': np.random.randint(1, 10, size=len(dates)) # 1-10 스케일 (10: 영적 흐름 풍성)
        })

    def generate_living_water_flow_data(self) -> pd.DataFrame:
        """
        상세한 생수의 강 흐름 데이터를 생성합니다.
        말씀 섭취, 기도 강도, 영적 흐름 속도를 시계열로 구성합니다.

        Generates detailed living water flow data.
        Structures Word intake, prayer intensity, and spiritual flow rate as a time series.

        Returns:
            pd.DataFrame: 상세 생수의 강 흐름 데이터
        """
        df = self.flow_events.copy()

        # 말씀 섭취와 기도 강도에 따른 영적 흐름 속도 조정
        df['spiritual_flow_rate'] = np.clip(
            df['spiritual_flow_rate'] + (df['word_intake_score'] + df['prayer_intensity_score']) // 2 - 5,
            1, 10
        )

        # KJV: John 7:39 - "(But this spake he of the Spirit, which they that believe on him should receive...)"
        # ESV: John 7:39 - "(Now this he said about the Spirit, whom those who believed in him were to receive...)"
        # 개역한글: 요한복음 7:39 - "이는 저를 믿는 자의 받을 성령을 가리켜 말씀하신 것이라..."
        print("✨ 요한복음 7장 생수의 강 흐름 데이터가 생성되었습니다.")
        print("말씀 섭취, 기도 강도, 영적 흐름 속도를 시계열로 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 생수의 강은 말씀 섭취와 기도 생활을 통해 지속적으로 흐르며, 영적 흐름의 패턴을 시간 데이터로 볼 수 있습니다.")
        print("Spiritual Insight: The river of living water flows continuously through Word intake and prayer life, and its patterns can be seen in time-series data.")

        return df

def demo_living_water_flow_data_generation():
    """
    LivingWaterFlowDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for LivingWaterFlowDataGenerator class.
    """
    print("--- Living Water Flow Data Generation Demo ---")
    print("--- 생수의 강 흐름 데이터 생성 데모 ---")
    generator = LivingWaterFlowDataGenerator()
    data = generator.generate_living_water_flow_data()
    return data

if __name__ == "__main__":
    demo_living_water_flow_data_generation()
