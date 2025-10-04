
import pandas as pd
import numpy as np

class TruthLifeDataGenerator:
    """
    요한복음 14장 6절의 "나는 길이요 진리요 생명이니" 말씀을 기반으로 데이터를 생성하는 클래스.
    다양한 삶의 길과 그에 따른 결과를 시뮬레이션합니다.

    Class to generate data based on John 14:6, "I am the way, the truth, and the life."
    Simulates various life paths and their corresponding outcomes.
    """

    def __init__(self):
        self.path_elements = self._load_path_elements()

    def _load_path_elements(self):
        """
        예수님 말씀의 진리와 관련된 길의 주요 요소에 대한 기본 정보를 로드합니다.
        Loads basic information about key elements of paths related to Jesus' truth.
        """
        # KJV: John 14:6 - "Jesus saith unto him, I am the way, the truth, and the life: no man cometh unto the Father, but by me."
        # ESV: John 14:6 - "Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.'"
        # 개역한글: 요한복음 14:6 - "예수께서 가라사대 내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라"
        return pd.DataFrame({
            'path_id': [1, 2, 3, 4, 5, 6],
            'path_taken': ['Jesus', 'Jesus', 'Jesus', 'Worldly Wisdom', 'Self-effort', 'Other Religions'],
            'belief_status': ['Believe', 'Believe', 'Believe', 'Not Believe', 'Not Believe', 'Not Believe'],
            'outcome_type': ['Life', 'Life', 'Life', 'Death', 'Death', 'Death'],
            'fulfillment_level': [10, 9, 10, 3, 2, 1], # 0-10 스케일 (10: 완전한 채움)
            'peace_level': [10, 9, 10, 2, 1, 0] # 0-10 스케일 (10: 완전한 평안)
        })

    def generate_truth_life_data(self) -> pd.DataFrame:
        """
        상세한 예수님 말씀의 진리 데이터를 생성합니다.
        다양한 삶의 길과 그에 따른 결과를 포함합니다.

        Generates detailed data for Jesus' words of truth and life.
        Includes various life paths and their corresponding outcomes.

        Returns:
            pd.DataFrame: 상세 예수님 말씀의 진리 데이터
        """
        df = self.path_elements.copy()

        # 만족도 수준에 약간의 노이즈 추가
        np.random.seed(146) # 재현성을 위해 시드 고정
        df['fulfillment_level'] = np.clip(df['fulfillment_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)
        df['peace_level'] = np.clip(df['peace_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: John 8:32 - "And ye shall know the truth, and the truth shall make you free."
        # ESV: John 8:32 - "and you will know the truth, and the truth will set you free."
        # 개역한글: 요한복음 8:32 - "진리를 알지니 진리가 너희를 자유케 하리라"
        print("✨ 요한복음 14장 6절 기반 진리 데이터가 생성되었습니다.")
        print("다양한 삶의 길과 그에 따른 결과를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 예수님은 구원과 영원한 생명으로 이끄는 유일한 길이요 진리입니다. 다른 길은 혼란과 사망을 가져옵니다.")
        print("Spiritual Insight: Jesus is the only way and truth leading to salvation and eternal life. Other paths bring confusion and death.")

        return df

def demo_truth_life_data_generation():
    """
    TruthLifeDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for TruthLifeDataGenerator class.
    """
    print("--- Truth and Life Data Generation Demo ---")
    print("--- 진리와 생명 데이터 생성 데모 ---")
    generator = TruthLifeDataGenerator()
    data = generator.generate_truth_life_data()
    return data

if __name__ == "__main__":
    demo_truth_life_data_generation()
