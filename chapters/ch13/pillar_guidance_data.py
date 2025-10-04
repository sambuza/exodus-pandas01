
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class PillarGuidanceDataGenerator:
    """
    출애굽기 13장의 구름기둥과 불기둥 인도 데이터를 생성하는 클래스.
    광야 여정의 시간 흐름에 따른 하나님의 인도하심을 시뮬레이션합니다.

    Class to generate data for the guidance of the pillar of cloud and fire in Exodus Chapter 13.
    Simulates God's guidance over the wilderness journey's timeline.
    """

    def __init__(self):
        self.guidance_events = self._load_guidance_events()

    def _load_guidance_events(self):
        """
        구름기둥과 불기둥 인도의 주요 사건에 대한 기본 정보를 로드합니다.
        Loads basic information about key events of the pillar guidance.
        """
        # KJV: Exodus 13:21 - "And the LORD went before them by day in a pillar of a cloud, to lead them the way; and by night in a pillar of fire, to give them light..."
        # ESV: Exodus 13:21 - "And the LORD went before them by day in a pillar of cloud to lead them along the way, and by night in a pillar of fire to give them light..."
        # 개역한글: 출애굽기 13:21 - "여호와께서 그들 앞에 행하사 낮에는 구름 기둥으로 그들의 길을 인도하시고 밤에는 불 기둥으로 그들에게 비취사 주야로 진행하게 하시니"
        return pd.DataFrame({
            'event_id': [1, 2, 3, 4, 5, 6, 7],
            'event_date': [
                '2024-03-15', '2024-03-15', '2024-03-16', '2024-03-16',
                '2024-03-17', '2024-03-17', '2024-03-18'
            ],
            'event_time': [
                '06:00', '18:00', '06:00', '18:00',
                '06:00', '18:00', '06:00'
            ],
            'guidance_type': [
                'Cloud', 'Fire', 'Cloud', 'Fire',
                'Cloud', 'Fire', 'Cloud'
            ],
            'movement_status': [
                'Moving', 'Moving', 'Resting', 'Resting',
                'Moving', 'Moving', 'Resting'
            ],
            'israel_response': [
                'Follow', 'Follow', 'Wait', 'Wait',
                'Follow', 'Follow', 'Wait'
            ]
        })

    def generate_pillar_guidance_data(self) -> pd.DataFrame:
        """
        상세한 구름기둥과 불기둥 인도 데이터를 생성합니다.
        날짜와 시간 정보를 포함하여 시계열 데이터로 구성합니다.

        Generates detailed pillar of cloud and fire guidance data.
        Structures it as time-series data including date and time information.

        Returns:
            pd.DataFrame: 상세 구름기둥/불기둥 인도 데이터
        """
        df = self.guidance_events.copy()

        # 'event_datetime' 열 생성
        df['event_datetime'] = pd.to_datetime(df['event_date'] + ' ' + df['event_time'])

        # KJV: Exodus 13:22 - "He took not away the pillar of the cloud by day, nor the pillar of fire by night, from before the people."
        # ESV: Exodus 13:22 - "The pillar of cloud by day and the pillar of fire by night did not depart from before the people."
        # 개역한글: 출애굽기 13:22 - "낮에는 구름 기둥, 밤에는 불 기둥이 백성 앞에서 떠나지 아니하니라"
        print("✨ 출애굽기 13장 구름기둥/불기둥 인도 데이터가 생성되었습니다.")
        print("광야 여정의 시간 흐름에 따른 하나님의 인도하심을 시뮬레이션합니다.")
        print(df[['event_datetime', 'guidance_type', 'movement_status', 'israel_response']].to_string(index=False))
        print("\n---")
        print("영적 통찰: 하나님은 시간의 흐름 속에서 변함없이 당신의 백성을 인도하십니다. 날짜/시간 데이터는 그 신실하심을 보여줍니다.")
        print("Spiritual Insight: God faithfully guides His people through the flow of time. Date/time data reveals His faithfulness.")

        return df

def demo_pillar_guidance_data_generation():
    """
    PillarGuidanceDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for PillarGuidanceDataGenerator class.
    """
    print("--- Pillar Guidance Data Generation Demo ---")
    print("--- 구름기둥/불기둥 인도 데이터 생성 데모 ---")
    generator = PillarGuidanceDataGenerator()
    data = generator.generate_pillar_guidance_data()
    return data

if __name__ == "__main__":
    demo_pillar_guidance_data_generation()
