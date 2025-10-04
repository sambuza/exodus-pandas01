
import pandas as pd
import numpy as np

class RedSeaCrossingDataGenerator:
    """
    출애굽기 14장의 홍해를 건너는 사건 데이터를 생성하는 클래스.
    이스라엘 백성과 애굽 군대의 상황, 감정, 결과를 시뮬레이션합니다.

    Class to generate data for the crossing of the Red Sea in Exodus Chapter 14.
    Simulates the situations, emotions, and outcomes for the Israelites and Egyptian army.
    """

    def __init__(self):
        self.events_info = self._load_events_info()

    def _load_events_info(self):
        """
        홍해 사건의 주요 단계에 대한 기본 정보를 로드합니다.
        Loads basic information about the key stages of the Red Sea event.
        """
        # KJV: Exodus 14:10 - "...the children of Israel lifted up their eyes, and, behold, the Egyptians marched after them; and they were sore afraid..."
        # ESV: Exodus 14:10 - "...the people of Israel lifted up their eyes, and behold, the Egyptians were marching after them, and they were in great fear..."
        # 개역한글: 출애굽기 14:10 - "바로가 가까이 올 때에 이스라엘 자손이 눈을 들어 본즉 애굽 사람들이 자기 뒤에 미친지라 이스라엘 자손이 심히 두려워하여"
        return pd.DataFrame({
            'event_id': [1, 2, 3, 4, 5, 6, 7],
            'event_time': ['Before', 'Before', 'During', 'During', 'During', 'After', 'After'],
            'event_description_kr': [
                '애굽 군대 추격', '이스라엘의 두려움', '홍해 갈라짐', 
                '이스라엘 통과', '애굽 군대 추격', '애굽 군대 수장', '이스라엘의 구원'
            ],
            'event_description_en': [
                'Egyptians pursue', 'Israelites\' fear', 'Red Sea parts', 
                'Israelites cross', 'Egyptians pursue', 'Egyptians drowned', 'Israelites saved'
            ],
            'group_status': [
                'Egyptians', 'Israelites', 'Israelites', 'Israelites', 
                'Egyptians', 'Egyptians', 'Israelites'
            ],
            'emotion_level': [0, 8, 5, 2, 0, 0, 9], # 0-10 스케일 (0: 평온, 10: 극심한 두려움/기쁨)
            'divine_intervention': [False, False, True, True, False, True, True]
        })

    def generate_red_sea_event_data(self) -> pd.DataFrame:
        """
        상세한 홍해 사건 데이터를 생성합니다.
        이스라엘과 애굽 군대의 상황을 포함합니다.

        Generates detailed Red Sea event data.
        Includes situations for Israelites and Egyptian army.

        Returns:
            pd.DataFrame: 상세 홍해 사건 데이터
        """
        df = self.events_info.copy()

        # 감정 수준에 약간의 노이즈 추가
        np.random.seed(14) # 재현성을 위해 시드 고정
        df['emotion_level'] = np.clip(df['emotion_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: Exodus 14:29 - "But the children of Israel walked upon dry land in the midst of the sea..."
        # ESV: Exodus 14:29 - "But the people of Israel walked on dry ground through the sea..."
        # 개역한글: 출애굽기 14:29 - "이스라엘 자손은 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니"
        print("✨ 출애굽기 14장 홍해 사건 데이터가 생성되었습니다.")
        print("이스라엘 백성과 애굽 군대의 상황, 감정, 결과를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 홍해 사건은 하나님의 유일한 구원과 애굽의 중복된 완악함을 극명하게 보여줍니다.")
        print("Spiritual Insight: The Red Sea event vividly demonstrates God's unique salvation and Egypt's persistent stubbornness.")

        return df

def demo_red_sea_crossing_data_generation():
    """
    RedSeaCrossingDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for RedSeaCrossingDataGenerator class.
    """
    print("--- Red Sea Crossing Data Generation Demo ---")
    print("--- 홍해 도하 데이터 생성 데모 ---")
    generator = RedSeaCrossingDataGenerator()
    data = generator.generate_red_sea_event_data()
    return data

if __name__ == "__main__":
    demo_red_sea_crossing_data_generation()
