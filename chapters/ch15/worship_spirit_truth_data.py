
import pandas as pd
import numpy as np

class WorshipSpiritTruthDataGenerator:
    """
    요한복음 4장의 신령과 진정으로 드리는 예배 데이터를 생성하는 클래스.
    예배의 본질과 다양한 형태를 시뮬레이션합니다.

    Class to generate data for worship in spirit and truth from John Chapter 4.
    Simulates the essence and various forms of worship.
    """

    def __init__(self):
        self.worship_elements = self._load_worship_elements()

    def _load_worship_elements(self):
        """
        예배의 주요 요소에 대한 기본 정보를 로드합니다.
        Loads basic information about key elements of worship.
        """
        # KJV: John 4:23 - "...the true worshippers shall worship the Father in spirit and in truth..."
        # ESV: John 4:23 - "...the true worshipers will worship the Father in spirit and truth..."
        # 개역한글: 요한복음 4:23 - "...아버지께 참으로 예배하는 자들은 신령과 진정으로 예배할 때가 오나니 곧 이때라..."
        return pd.DataFrame({
            'worship_id': [1, 2, 3, 4, 5, 6, 7, 8],
            'worship_type': [
                'Spirit', 'Spirit', 'Truth', 'Truth',
                'Form', 'Form', 'Heart', 'Heart'
            ],
            'element_kr': [
                '영적 교감', '성령의 인도', '말씀 순종', '진실된 고백',
                '찬양', '기도', '감사', '헌신'
            ],
            'element_en': [
                'Spiritual Communion', 'Guidance of Spirit', 'Obedience to Word', 'True Confession',
                'Praise', 'Prayer', 'Thanksgiving', 'Dedication'
            ],
            'essence_level': [10, 9, 9, 8, 6, 7, 8, 9], # 0-10 스케일 (10: 본질에 가까움)
            'expression_level': [7, 8, 7, 8, 10, 9, 8, 9], # 0-10 스케일 (10: 외적 표현 강함)
            'divine_acceptance': [True, True, True, True, False, False, True, True] # 하나님이 받으시는 예배 여부
        })

    def generate_worship_data(self) -> pd.DataFrame:
        """
        상세한 예배 데이터를 생성합니다.
        예배의 본질과 다양한 형태를 포함합니다.

        Generates detailed worship data.
        Includes the essence and various forms of worship.

        Returns:
            pd.DataFrame: 상세 예배 데이터
        """
        df = self.worship_elements.copy()

        # 수준에 약간의 노이즈 추가
        np.random.seed(424) # 재현성을 위해 시드 고정
        df['essence_level'] = np.clip(df['essence_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)
        df['expression_level'] = np.clip(df['expression_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: John 4:24 - "God is a Spirit: and they that worship him must worship him in spirit and in truth."
        # ESV: John 4:24 - "God is spirit, and those who worship him must worship in spirit and truth."
        # 개역한글: 요한복음 4:24 - "하나님은 영이시니 예배하는 자가 신령과 진정으로 예배할지니라"
        print("✨ 요한복음 4장 신령과 진정으로 드리는 예배 데이터가 생성되었습니다.")
        print("예배의 본질과 다양한 형태를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 예배는 단순히 외적인 행위가 아니라, 영적인 상태와 진실된 마음이라는 다층적인 요소를 포함합니다.")
        print("Spiritual Insight: Worship includes multi-layered elements of spiritual state and sincere heart, not just outward actions.")

        return df

def demo_worship_spirit_truth_data_generation():
    """
    WorshipSpiritTruthDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for WorshipSpiritTruthDataGenerator class.
    """
    print("--- Worship in Spirit and Truth Data Generation Demo ---")
    print("--- 신령과 진정으로 드리는 예배 데이터 생성 데모 ---")
    generator = WorshipSpiritTruthDataGenerator()
    data = generator.generate_worship_data()
    return data

if __name__ == "__main__":
    demo_worship_spirit_truth_data_generation()
