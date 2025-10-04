
import pandas as pd
import numpy as np

class SinaiCovenantDataGenerator:
    """
    출애굽기 19장의 시내산 언약 데이터를 생성하는 클래스.
    언약의 규례, 이스라엘의 반응, 결과 등을 시뮬레이션합니다.

    Class to generate Sinai Covenant data from Exodus Chapter 19.
    Simulates covenant ordinances, Israel's responses, and outcomes.
    """

    def __init__(self):
        self.covenant_elements = self._load_covenant_elements()

    def _load_covenant_elements(self):
        """
        시내산 언약의 주요 요소에 대한 기본 정보를 로드합니다.
        Loads basic information about key elements of the Sinai Covenant.
        """
        # KJV: Exodus 19:5 - "Now therefore, if ye will obey my voice indeed, and keep my covenant, then ye shall be a peculiar treasure unto me above all people..."
        # ESV: Exodus 19:5 - "Now therefore, if you will indeed obey my voice and keep my covenant, you shall be my treasured possession among all peoples..."
        # 개역한글: 출애굽기 19:5 - "세계가 다 내게 속하였나니 너희가 내 말을 잘 듣고 내 언약을 지키면 너희는 열국 중에서 내 소유가 되겠고"
        return pd.DataFrame({
            'commandment_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], # 십계명 및 추가 규례
            'commandment_type': [
                'God-ward', 'God-ward', 'God-ward', 'God-ward',
                'Man-ward', 'Man-ward', 'Man-ward', 'Man-ward',
                'Man-ward', 'Man-ward', 'Man-ward', 'Man-ward'
            ],
            'israel_response': [
                'Obey', 'Obey', 'Disobey', 'Obey',
                'Obey', 'Disobey', 'Obey', 'Obey',
                'Disobey', 'Obey', 'Obey', 'Disobey'
            ],
            'consequence': [
                'Blessing', 'Blessing', 'Curse', 'Blessing',
                'Blessing', 'Curse', 'Blessing', 'Blessing',
                'Curse', 'Blessing', 'Blessing', 'Curse'
            ],
            'is_valid': [True, True, False, True, True, False, True, True, False, True, True, False] # 언약 준수 여부
        })

    def generate_covenant_data(self) -> pd.DataFrame:
        """
        상세한 시내산 언약 데이터를 생성합니다.
        언약의 규례, 이스라엘의 반응, 결과 등을 포함합니다.

        Generates detailed Sinai Covenant data.
        Includes covenant ordinances, Israel's responses, and outcomes.

        Returns:
            pd.DataFrame: 상세 시내산 언약 데이터
        """
        df = self.covenant_elements.copy()

        # KJV: Exodus 19:8 - "And all the people answered together, and said, All that the LORD hath spoken we will do..."
        # ESV: Exodus 19:8 - "All the people answered together and said, 'All that the LORD has spoken we will do.'..."
        # 개역한글: 출애굽기 19:8 - "백성이 일제히 응답하여 가로되 여호와의 명하신 대로 우리가 다 행하리이다"
        print("✨ 출애굽기 19장 시내산 언약 데이터가 생성되었습니다.")
        print("언약의 규례, 이스라엘의 반응, 결과 등을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 시내산 언약은 하나님의 백성으로서 지켜야 할 명확한 규례(스키마)와 그에 따른 결과(유효성)를 보여줍니다.")
        print("Spiritual Insight: The Sinai Covenant reveals clear ordinances (schema) for God's people and corresponding outcomes (validation).")

        return df

def demo_sinai_covenant_data_generation():
    """
    SinaiCovenantDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for SinaiCovenantDataGenerator class.
    """
    print("--- Sinai Covenant Data Generation Demo ---")
    print("--- 시내산 언약 데이터 생성 데모 ---")
    generator = SinaiCovenantDataGenerator()
    data = generator.generate_covenant_data()
    return data

if __name__ == "__main__":
    demo_sinai_covenant_data_generation()
