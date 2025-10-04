
import pandas as pd
import numpy as np

class LightOfTheWorldDataGenerator:
    """
    요한복음 8장 12절의 "나는 세상의 빛이니" 말씀을 기반으로 빛과 어둠의 데이터를 생성하는 클래스.
    빛을 따르는 삶과 어둠에 거하는 삶의 특성을 시뮬레이션합니다.

    Class to generate light and darkness data based on John 8:12, "I am the light of the world."
    Simulates the characteristics of lives following the light versus those dwelling in darkness.
    """

    def __init__(self):
        self.concepts_info = self._load_concepts_info()

    def _load_concepts_info(self):
        """
        빛과 어둠 관련 개념에 대한 기본 정보를 로드합니다.
        Loads basic information about concepts related to light and darkness.
        """
        # KJV: John 8:12 - "...he that followeth me shall not walk in darkness, but shall have the light of life."
        # ESV: John 8:12 - "...whoever follows me will not walk in darkness, but will have the light of life."
        # 개역한글: 요한복음 8:12 - "...나를 따르는 자는 어두움에 다니지 아니하고 생명의 빛을 얻으리라"
        return pd.DataFrame({
            'concept_name_kr': ['생명의 빛', '진리', '사랑', '평안', '어둠', '죄', '두려움', '혼돈'],
            'concept_name_en': ['Light of Life', 'Truth', 'Love', 'Peace', 'Darkness', 'Sin', 'Fear', 'Chaos'],
            'category': ['Light', 'Light', 'Light', 'Light', 'Darkness', 'Darkness', 'Darkness', 'Darkness'],
            'impact_on_life': [10, 9, 9, 8, -10, -9, -8, -7], # 삶에 미치는 영향 (긍정/부정)
            'spiritual_growth_factor': [5, 4, 4, 3, -5, -4, -4, -3] # 영적 성장에 기여하는 정도
        })

    def generate_light_darkness_data(self) -> pd.DataFrame:
        """
        상세한 빛과 어둠 데이터를 생성합니다.
        각 개념이 삶과 영적 성장에 미치는 영향을 시뮬레이션합니다.

        Generates detailed light and darkness data.
        Simulates the impact of each concept on life and spiritual growth.

        Returns:
            pd.DataFrame: 상세 빛과 어둠 데이터
        """
        df = self.concepts_info.copy()

        # 데이터에 약간의 변동성 추가
        np.random.seed(812) # 재현성을 위해 시드 고정
        df['impact_on_life'] = np.clip(df['impact_on_life'] + np.random.randint(-2, 2, size=len(df)), -10, 10)
        df['spiritual_growth_factor'] = np.clip(df['spiritual_growth_factor'] + np.random.randint(-1, 1, size=len(df)), -5, 5)

        # KJV: John 1:5 - "And the light shineth in darkness; and the darkness comprehended it not."
        # ESV: John 1:5 - "The light shines in the darkness, and the darkness has not overcome it."
        # 개역한글: 요한복음 1:5 - "빛이 어두움에 비취되 어두움이 깨닫지 못하더라"
        print("✨ 요한복음 8장 12절 기반 빛과 어둠 데이터가 생성되었습니다.")
        print("각 개념이 삶과 영적 성장에 미치는 영향을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 빛과 어둠은 삶과 영적 성장에 극명하게 다른 영향을 미칩니다. 예수님은 생명의 빛이십니다.")
        print("Spiritual Insight: Light and darkness have distinctly different impacts on life and spiritual growth. Jesus is the Light of Life.")

        return df

def demo_light_of_the_world_data_generation():
    """
    LightOfTheWorldDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for LightOfTheWorldDataGenerator class.
    """
    print("--- Light of the World Data Generation Demo ---")
    print("--- 세상의 빛 데이터 생성 데모 ---")
    generator = LightOfTheWorldDataGenerator()
    data = generator.generate_light_darkness_data()
    return data

if __name__ == "__main__":
    demo_light_of_the_world_data_generation()
