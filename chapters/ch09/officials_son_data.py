import pandas as pd
import numpy as np

class OfficialsSonDataGenerator:
    """
    요한복음 4장의 왕의 신하의 아들 치유 데이터를 생성하는 클래스.
    신하의 믿음 여정과 아들의 병세 변화를 시뮬레이션합니다.

    Class to generate data for the healing of the royal official's son in John 4.
    Simulates the official's journey of faith and the son's health changes.
    """

    def __init__(self):
        self.healing_events_info = self._load_healing_events_info()

    def _load_healing_events_info(self):
        """
        치유 사건에 대한 기본 정보를 로드합니다.
        Loads basic information about the healing events.
        """
        # KJV: John 4:50 - "Jesus saith unto him, Go thy way; thy son liveth. And the man believed the word..."
        # ESV: John 4:50 - "Jesus said to him, 'Go; your son will live.' The man believed the word..."
        # 개역한글: 요한복음 4:50 - "예수께서 가라사대 가라 네 아들이 살았다 하신대 그 사람이 예수의 하신 말씀을 믿고 가더니"
        return pd.DataFrame({
            'event_order': [1, 2, 3, 4, 5],
            'event_name_kr': ['간청', '예수님 말씀', '믿고 돌아감', '종들의 보고', '완치 확인'],
            'event_name_en': ['Plea', 'Jesus', 'Word', 'Believed & Departed', 'Servants', 'Report', 'Healing Confirmed'],
            'time_elapsed_hours': [0, 0.5, 1, 23, 24], # 예수님 말씀 시점부터 경과 시간
            'son_fever_level': [40.0, 40.0, 39.5, 36.5, 36.5], # 아들의 열 수준 (섭씨)
            'officials_faith_level': [70, 85, 95, 100, 100] # 신하의 믿음 수준 (0-100)
        })

    def generate_detailed_healing_data(self) -> pd.DataFrame:
        """
        상세한 치유 여정 데이터를 생성합니다.
        Generates detailed healing journey data.

        Returns:
            pd.DataFrame: 상세 치유 여정 데이터
        """
        df = self.healing_events_info.copy()

        # 믿음 수준에 약간의 노이즈 추가 (시뮬레이션)
        np.random.seed(43) # 재현성을 위해 시드 고정
        df['officials_faith_level'] = np.clip(df['officials_faith_level'] + np.random.randint(-3, 3, size=len(df)), 0, 100)

        # KJV: John 4:53 - "So the father knew that it was at the same hour... and himself believed, and his whole house."
        # ESV: John 4:53 - "The father knew that was the hour... And he himself believed, and all his household."
        # 개역한글: 요한복음 4:53 - "아비가 예수께서 네 아들이 살았다 하신 그 시각인 줄 알고 자기와 그 온 집이 다 믿으니라"
        print("✨ 요한복음 4장 왕의 신하의 아들 치유 데이터가 생성되었습니다.")
        print("신하의 믿음 여정과 아들의 병세 변화를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 예수님의 말씀은 시공간을 초월하여 역사하며, 믿음은 그 말씀을 통해 자라납니다.")
        print("Spiritual Insight: Jesus' word transcends time and space, and faith grows through that word.")

        return df

def demo_officials_son_data_generation():
    """
    OfficialsSonDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for OfficialsSonDataGenerator class.
    """
    print("--- Royal Official's Son Healing Data Generation Demo ---")
    print("--- 왕의 신하의 아들 치유 데이터 생성 데모 ---")
    generator = OfficialsSonDataGenerator()
    data = generator.generate_detailed_healing_data()
    return data

if __name__ == "__main__":
    demo_officials_son_data_generation()