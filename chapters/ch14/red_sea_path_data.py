
import pandas as pd
import numpy as np

class RedSeaPathDataGenerator:
    """
    출애굽기 14장의 홍해 길 데이터를 생성하는 클래스.
    홍해를 건너는 길의 다층적인 상황과 그룹별 경험을 시뮬레이션합니다.

    Class to generate Red Sea path data from Exodus Chapter 14.
    Simulates the multi-layered situations and group-specific experiences of crossing the Red Sea.
    """

    def __init__(self):
        self.path_events = self._load_path_events()

    def _load_path_events(self):
        """
        홍해 길의 주요 사건에 대한 기본 정보를 로드합니다.
        Loads basic information about key events of the Red Sea path.
        """
        # KJV: Exodus 14:22 - "And the children of Israel went into the midst of the sea upon the dry ground..."
        # ESV: Exodus 14:22 - "The people of Israel went into the midst of the sea on dry ground..."
        # 개역한글: 출애굽기 14:22 - "이스라엘 자손이 바다 가운데 육지로 행하고..."
        return pd.DataFrame({
            'segment_id': [1, 2, 3, 4, 5, 6, 7, 8],
            'time_of_day': ['Night', 'Night', 'Night', 'Night', 'Dawn', 'Dawn', 'Day', 'Day'],
            'group_status': [
                'Israelites', 'Israelites', 'Israelites', 'Israelites',
                'Egyptians', 'Egyptians', 'Israelites', 'Egyptians'
            ],
            'path_condition': [
                'Dry Ground', 'Dry Ground', 'Dry Ground', 'Dry Ground',
                'Dry Ground', 'Muddy', 'Dry Ground', 'Water Returns'
            ],
            'guidance_type': [
                'Fire Pillar', 'Fire Pillar', 'Fire Pillar', 'Fire Pillar',
                'Cloud Pillar', 'Cloud Pillar', 'Cloud Pillar', 'None'
            ],
            'safety_level': [9, 9, 9, 9, 5, 3, 9, 0], # 0-10 스케일 (0: 위험, 10: 안전)
            'progress_km': [1, 2, 3, 4, 1, 2, 5, 0] # 진행 거리
        })

    def generate_red_sea_path_data(self) -> pd.DataFrame:
        """
        상세한 홍해 길 데이터를 생성합니다.
        시간, 그룹, 길의 상태 등 다층적인 정보를 포함합니다.

        Generates detailed Red Sea path data.
        Includes multi-layered information such as time, group, and path condition.

        Returns:
            pd.DataFrame: 상세 홍해 길 데이터
        """
        df = self.path_events.copy()

        # 안전 수준에 약간의 노이즈 추가
        np.random.seed(1429) # 재현성을 위해 시드 고정
        df['safety_level'] = np.clip(df['safety_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: Exodus 14:29 - "But the children of Israel walked upon dry land in the midst of the sea..."
        # ESV: Exodus 14:29 - "But the people of Israel walked on dry ground through the sea..."
        # 개역한글: 출애굽기 14:29 - "이스라엘 자손은 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니"
        print("✨ 출애굽기 14장 홍해 길 데이터가 생성되었습니다.")
        print("홍해를 건너는 길의 다층적인 상황과 그룹별 경험을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 홍해의 길은 단순한 길이 아니라, 하나님의 세밀한 인도와 구별된 보호가 담긴 다층적인 길입니다.")
        print("Spiritual Insight: The Red Sea path is not just a road, but a multi-layered path containing God's meticulous guidance and distinct protection.")

        return df

def demo_red_sea_path_data_generation():
    """
    RedSeaPathDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for RedSeaPathDataGenerator class.
    """
    print("--- Red Sea Path Data Generation Demo ---")
    print("--- 홍해 길 데이터 생성 데모 ---")
    generator = RedSeaPathDataGenerator()
    data = generator.generate_red_sea_path_data()
    return data

if __name__ == "__main__":
    demo_red_sea_path_data_generation()
