
import pandas as pd
import numpy as np

class SongOfTheSeaDataGenerator:
    """
    출애굽기 15장의 모세와 미리암의 노래 데이터를 생성하는 클래스.
    하나님의 구원 역사를 다양한 관점에서 재구성할 데이터를 시뮬레이션합니다.

    Class to generate data for the Song of Moses and Miriam from Exodus Chapter 15.
    Simulates data to reconfigure God's salvation history from various perspectives.
    """

    def __init__(self):
        self.song_elements = self._load_song_elements()

    def _load_song_elements(self):
        """
        바다의 노래의 주요 요소에 대한 기본 정보를 로드합니다.
        Loads basic information about key elements of the Song of the Sea.
        """
        # KJV: Exodus 15:2 - "The LORD is my strength and song, and he is become my salvation..."
        # ESV: Exodus 15:2 - "The LORD is my strength and my song, and he has become my salvation..."
        # 개역한글: 출애굽기 15:2 - "여호와는 나의 힘이요 노래시며 나의 구원이시로다 그는 나의 하나님이시니 내가 그를 찬송할 것이요..."
        return pd.DataFrame({
            'event_id': [1, 2, 3, 4, 5, 6, 7, 8],
            'event_type': [
                'Praise', 'Praise', 'Judgment', 'Judgment',
                'Guidance', 'Guidance', 'Response', 'Response'
            ],
            'attribute_of_God': [
                'Strength', 'Salvation', 'Power', 'Justice',
                'Faithfulness', 'Holiness', 'None', 'None'
            ],
            'israel_response': [
                'Sing', 'Exalt', 'Fear', 'Witness',
                'Follow', 'Trust', 'Sing', 'Dance'
            ],
            'egypt_fate': [
                'None', 'None', 'Drowned', 'Destroyed',
                'None', 'None', 'None', 'None'
            ],
            'intensity': [10, 9, 8, 8, 7, 7, 9, 9], # 0-10 스케일 (0: 약함, 10: 강함)
            'time_period': ['Past', 'Past', 'Past', 'Past', 'Future', 'Future', 'Present', 'Present']
        })

    def generate_song_of_sea_data(self) -> pd.DataFrame:
        """
        상세한 바다의 노래 데이터를 생성합니다.
        하나님의 속성, 이스라엘의 반응, 애굽의 운명 등 다양한 관점을 포함합니다.

        Generates detailed Song of the Sea data.
        Includes various perspectives such as God's attributes, Israel's response, and Egypt's fate.

        Returns:
            pd.DataFrame: 상세 바다의 노래 데이터
        """
        df = self.song_elements.copy()

        # 강도에 약간의 노이즈 추가
        np.random.seed(152) # 재현성을 위해 시드 고정
        df['intensity'] = np.clip(df['intensity'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: Exodus 15:21 - "And Miriam answered them, Sing ye to the LORD, for he hath triumphed gloriously..."
        # ESV: Exodus 15:21 - "And Miriam sang to them: "Sing to the LORD, for he has triumphed gloriously..."
        # 개역한글: 출애굽기 15:21 - "미리암이 그들에게 화답하여 가로되 너희는 여호와를 찬송하라 그는 높고 영화로우시며..."
        print("✨ 출애굽기 15장 바다의 노래 데이터가 생성되었습니다.")
        print("하나님의 구원 역사를 다양한 관점에서 재구성할 데이터를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 바다의 노래는 단순한 찬양이 아니라, 하나님의 위대한 구원 역사를 다양한 관점에서 재구성하고 선포하는 것입니다.")
        print("Spiritual Insight: The Song of the Sea is not just a hymn, but a reshaping and proclamation of God's great salvation history from various perspectives.")

        return df

def demo_song_of_sea_data_generation():
    """
    SongOfTheSeaDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for SongOfTheSeaDataGenerator class.
    """
    print("--- Song of the Sea Data Generation Demo ---")
    print("--- 바다의 노래 데이터 생성 데모 ---")
    generator = SongOfTheSeaDataGenerator()
    data = generator.generate_song_of_sea_data()
    return data

if __name__ == "__main__":
    demo_song_of_sea_data_generation()
