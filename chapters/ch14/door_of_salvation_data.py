
import pandas as pd
import numpy as np

class DoorOfSalvationDataGenerator:
    """
    요한복음 10장 9절의 "나는 문이니" 말씀을 기반으로 구원의 문 데이터를 생성하는 클래스.
    예수님을 통한 길과 다른 길의 결과, 그리고 접근 방식을 시뮬레이션합니다.

    Class to generate data for the door of salvation based on John 10:9, "I am the door."
    Simulates the outcomes and approaches of the path through Jesus versus other paths.
    """

    def __init__(self):
        self.paths_info = self._load_paths_info()

    def _load_paths_info(self):
        """
        구원의 문과 관련된 길에 대한 기본 정보를 로드합니다.
        Loads basic information about paths related to the door of salvation.
        """
        # KJV: John 10:9 - "I am the door: by me if any man enter in, he shall be saved, and shall go in and out, and find pasture."
        # ESV: John 10:9 - "I am the door. If anyone enters by me, he will be saved and will go in and out and find pasture."
        # 개역한글: 요한복음 10:9 - "내가 곧 문이니 누구든지 나로 말미암아 들어가면 구원을 얻고 또는 들어가며 나오며 꼴을 얻으리라"
        return pd.DataFrame({
            'path_id': [1, 2, 3, 4, 5, 6],
            'path_type': ['Jesus', 'Jesus', 'Jesus', 'World', 'World', 'World'],
            'entry_method': ['Faith', 'Obedience', 'Grace', 'Works', 'Philosophy', 'Self-effort'],
            'outcome_kr': ['구원', '풍성한 삶', '영생', '혼란', '좌절', '허무'],
            'outcome_en': ['Salvation', 'Abundant Life', 'Eternal Life', 'Confusion', 'Frustration', 'Emptiness'],
            'fulfillment_level': [10, 9, 10, 3, 2, 1], # 0-10 스케일 (10: 완전한 채움)
            'peace_level': [10, 9, 10, 2, 1, 0] # 0-10 스케일 (10: 완전한 평안)
        })

    def generate_door_of_salvation_data(self) -> pd.DataFrame:
        """
        상세한 구원의 문 데이터를 생성합니다.
        예수님을 통한 길과 다른 길의 결과 및 접근 방식을 포함합니다.

        Generates detailed data for the door of salvation.
        Includes outcomes and approaches of the path through Jesus versus other paths.

        Returns:
            pd.DataFrame: 상세 구원의 문 데이터
        """
        df = self.paths_info.copy()

        # 만족도 수준에 약간의 노이즈 추가
        np.random.seed(109) # 재현성을 위해 시드 고정
        df['fulfillment_level'] = np.clip(df['fulfillment_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)
        df['peace_level'] = np.clip(df['peace_level'] + np.random.randint(-1, 1, size=len(df)), 0, 10)

        # KJV: John 14:6 - "I am the way, the truth, and the life: no man cometh unto the Father, but by me."
        # ESV: John 14:6 - "Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.'"
        # 개역한글: 요한복음 14:6 - "예수께서 가라사대 내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라"
        print("✨ 요한복음 10장 9절 기반 구원의 문 데이터가 생성되었습니다.")
        print("예수님을 통한 길과 다른 길의 결과 및 접근 방식을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 예수님은 구원과 풍성한 삶으로 들어가는 유일한 문입니다. 다른 길은 혼란과 허무를 가져옵니다.")
        print("Spiritual Insight: Jesus is the only door to salvation and abundant life. Other paths lead to confusion and emptiness.")

        return df

def demo_door_of_salvation_data_generation():
    """
    DoorOfSalvationDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for DoorOfSalvationDataGenerator class.
    """
    print("--- Door of Salvation Data Generation Demo ---")
    print("--- 구원의 문 데이터 생성 데모 ---")
    generator = DoorOfSalvationDataGenerator()
    data = generator.generate_door_of_salvation_data()
    return data

if __name__ == "__main__":
    demo_door_of_salvation_data_generation()
