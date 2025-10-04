
import pandas as pd
import numpy as np

class JethroAdviceDataGenerator:
    """
    출애굽기 18장의 이드로의 조언 데이터를 생성하는 클래스.
    모세의 재판 업무 과부하와 이드로의 조언에 따른 변화를 시뮬레이션합니다.

    Class to generate Jethro's advice data from Exodus Chapter 18.
    Simulates Moses' judicial workload and changes after Jethro's advice.
    """

    def __init__(self):
        self.jethro_events = self._load_jethro_events()

    def _load_jethro_events(self):
        """
        이드로의 조언 사건의 주요 단계에 대한 기본 정보를 로드합니다.
        Loads basic information about key stages of Jethro's advice event.
        """
        # KJV: Exodus 18:13 - "And it came to pass on the morrow, that Moses sat to judge the people: and the people stood by Moses from the morning unto the evening."
        # ESV: Exodus 18:13 - "The next day Moses sat to judge the people, and the people stood before Moses from morning till evening."
        # 개역한글: 출애굽기 18:13 - "이튿날 모세가 백성을 재판하느라고 앉았고 백성은 아침부터 저녁까지 모세 곁에 섰는지라"
        return pd.DataFrame({
            'day': range(1, 11), # 10일간의 업무 시뮬레이션
            'period': ['Before Advice'] * 5 + ['After Advice'] * 5,
            'cases_handled_moses': [10, 12, 15, 13, 16, 5, 6, 7, 5, 6], # 모세가 직접 처리한 송사 수
            'cases_handled_delegated': [0, 0, 0, 0, 0, 10, 12, 15, 13, 16], # 위임된 자들이 처리한 송사 수
            'moses_fatigue_level': [8, 9, 9, 10, 10, 4, 5, 4, 3, 3], # 1-10 스케일 (10: 극심한 피로)
            'people_satisfaction': [5, 4, 3, 3, 2, 7, 8, 8, 9, 9] # 1-10 스케일 (10: 매우 만족)
        })

    def generate_jethro_advice_data(self) -> pd.DataFrame:
        """
        상세한 이드로의 조언 데이터를 생성합니다.
        모세의 업무 과부하와 조언에 따른 변화를 시뮬레이션합니다.

        Generates detailed Jethro's advice data.
        Simulates Moses' workload and changes after the advice.

        Returns:
            pd.DataFrame: 상세 이드로의 조언 데이터
        """
        df = self.jethro_events.copy()

        # 피로도와 만족도에 약간의 노이즈 추가
        np.random.seed(1824) # 재현성을 위해 시드 고정
        df['moses_fatigue_level'] = np.clip(df['moses_fatigue_level'] + np.random.randint(-1, 1, size=len(df)), 1, 10)
        df['people_satisfaction'] = np.clip(df['people_satisfaction'] + np.random.randint(-1, 1, size=len(df)), 1, 10)

        # KJV: Exodus 18:24 - "So Moses hearkened to the voice of his father in law, and did all that he had said."
        # ESV: Exodus 18:24 - "So Moses listened to the voice of his father-in-law and did all that he had said."
        # 개역한글: 출애굽기 18:24 - "모세가 그 장인의 말을 듣고 그 말대로 하여"
        print("✨ 출애굽기 18장 이드로의 조언 데이터가 생성되었습니다.")
        print("모세의 재판 업무 과부하와 이드로의 조언에 따른 변화를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 이드로의 조언은 복잡한 작업을 효율적으로 분담하고 연결하는 지혜를 보여줍니다. 이는 데이터 처리 파이프라인과 유사합니다.")
        print("Spiritual Insight: Jethro's advice demonstrates the wisdom of efficiently delegating and connecting complex tasks, similar to data processing pipelines.")

        return df

def demo_jethro_advice_data_generation():
    """
    JethroAdviceDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for JethroAdviceDataGenerator class.
    """
    print("--- Jethro's Advice Data Generation Demo ---")
    print("--- 이드로의 조언 데이터 생성 데모 ---")
    generator = JethroAdviceDataGenerator()
    data = generator.generate_jethro_advice_data()
    return data

if __name__ == "__main__":
    demo_jethro_advice_data_generation()
