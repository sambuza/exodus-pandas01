
import pandas as pd
import numpy as np

class JesusWalksWaterDataGenerator:
    """
    요한복음 6장의 예수님께서 물 위를 걸으신 사건 데이터를 생성하는 클래스.
    제자들의 감정 변화와 예수님의 현현을 시뮬레이션합니다.

    Class to generate data for Jesus walking on water in John Chapter 6.
    Simulates the disciples' emotional changes and Jesus' appearance.
    """

    def __init__(self):
        self.events_info = self._load_events_info()

    def _load_events_info(self):
        """
        물 위를 걸으신 사건의 주요 단계에 대한 기본 정보를 로드합니다.
        Loads basic information about the key stages of Jesus walking on water.
        """
        # KJV: John 6:19 - "...they see Jesus walking on the sea, and drawing nigh unto the ship: and they were afraid."
        # ESV: John 6:19 - "...they saw Jesus walking on the sea and coming near the boat, and they were frightened."
        # 개역한글: 요한복음 6:19 - "제자들이 노를 저어 십여 리쯤 가다가 예수께서 바다 위로 걸어 배에 가까이 오심을 보고 두려워하는지라"
        return pd.DataFrame({
            'event_id': [1, 2, 3, 4, 5, 6],
            'event_time': ['Evening', 'Night', 'Night', 'Night', 'Night', 'Dawn'],
            'event_type': ['Departure', 'Storm', 'Jesus Appears', 'Disciples\' Fear', 'Jesus Speaks', 'Arrival'],
            'disciple_name': ['Peter', 'Andrew', 'James', 'John', 'All', 'All'],
            'disciple_emotion': ['Normal', 'Fear', 'Fear', 'Fear', 'Peace', 'Joy'],
            'wind_strength': [1, 8, 8, 8, 1, 0], # 0-10 스케일 (0: 잔잔, 10: 폭풍)
            'jesus_presence': [False, False, True, True, True, True]
        })

    def generate_jesus_walks_water_data(self) -> pd.DataFrame:
        """
        상세한 예수님께서 물 위를 걸으신 사건 데이터를 생성합니다.
        제자들의 감정 변화와 사건의 흐름을 포함합니다.

        Generates detailed data for Jesus walking on water.
        Includes disciples' emotional changes and the flow of events.

        Returns:
            pd.DataFrame: 상세 사건 데이터
        """
        df = self.events_info.copy()

        # 감정 수준에 약간의 노이즈 추가
        np.random.seed(620) # 재현성을 위해 시드 고정
        df['wind_strength'] = np.clip(df['wind_strength'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: John 6:21 - "Then they willingly received him into the ship: and immediately the ship was at the land whither they went."
        # ESV: John 6:21 - "Then they were glad to take him into the boat, and immediately the boat was at the land to which they were going."
        # 개역한글: 요한복음 6:21 - "이에 기뻐서 배로 영접하니 배가 곧 그들의 가려던 땅에 이르더라"
        print("✨ 요한복음 6장 예수님께서 물 위를 걸으신 사건 데이터가 생성되었습니다.")
        print("제자들의 감정 변화와 예수님의 현현을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 세상의 반복되는 두려움 속에서도 예수님은 유일한 평안과 구원을 주십니다.")
        print("Spiritual Insight: Even amidst the world's recurring fears, Jesus alone provides unique peace and salvation.")

        return df

def demo_jesus_walks_water_data_generation():
    """
    JesusWalksWaterDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for JesusWalksWaterDataGenerator class.
    """
    print("--- Jesus Walks on Water Data Generation Demo ---")
    print("--- 예수님 물 위를 걸으신 데이터 생성 데모 ---")
    generator = JesusWalksWaterDataGenerator()
    data = generator.generate_jesus_walks_water_data()
    return data

if __name__ == "__main__":
    demo_jesus_walks_water_data_generation()
