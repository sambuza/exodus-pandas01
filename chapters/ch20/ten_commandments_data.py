
import pandas as pd
import numpy as np

class TenCommandmentsDataGenerator:
    """
    출애굽기 20장의 십계명 데이터를 생성하는 클래스.
    십계명 준수 수준, 결과, 데이터 품질 문제(결측치, 잘못된 타입, 이상치)를 시뮬레이션합니다.

    Class to generate Ten Commandments data from Exodus Chapter 20.
    Simulates commandment obedience levels, outcomes, and data quality issues (missing values, incorrect types, outliers).
    """

    def __init__(self):
        self.commandments_info = self._load_commandments_info()

    def _load_commandments_info(self):
        """
        십계명에 대한 기본 정보를 로드합니다.
        Loads basic information about the Ten Commandments.
        """
        # KJV: Exodus 20:3 - "Thou shalt have no other gods before me."
        # ESV: Exodus 20:3 - "You shall have no other gods before me."
        # 개역한글: 출애굽기 20:3 - "너는 나 외에는 다른 신들을 네게 있게 말지니라"
        return pd.DataFrame({
            'commandment_id': range(1, 11),
            'commandment_text_kr': [
                '다른 신을 두지 말라', '우상을 만들지 말라', '이름을 망령되이 일컫지 말라', '안식일을 기억하라',
                '부모를 공경하라', '살인하지 말라', '간음하지 말라', '도적질하지 말라',
                '거짓 증거하지 말라', '탐내지 말라'
            ],
            'commandment_text_en': [
                'No other gods', 'No idols', 'Do not misuse God\'s name', 'Keep the Sabbath holy',
                'Honor your father and mother', 'Do not murder', 'Do not commit adultery', 'Do not steal',
                'Do not give false testimony', 'Do not covet'
            ],
            'obedience_score': [9, 8, 7, 6, 9, 10, 8, 7, 5, 4], # 1-10 스케일 (10: 완전 준수)
            'consequence_score': [1, 2, 3, 4, 1, 0, 2, 3, 5, 6], # 1-10 스케일 (10: 심각한 결과)
            'israel_response_type': [
                'Obedience', 'Obedience', 'Disobedience', 'Partial Obedience',
                'Obedience', 'Obedience', 'Partial Obedience', 'Disobedience',
                'Disobedience', 'Disobedience'
            ]
        })

    def generate_commandments_data(self) -> pd.DataFrame:
        """
        상세한 십계명 데이터를 생성합니다.
        준수 수준, 결과, 데이터 품질 문제(결측치, 잘못된 타입, 이상치)를 포함합니다.

        Generates detailed Ten Commandments data.
        Includes obedience levels, outcomes, and data quality issues (missing values, incorrect types, outliers).

        Returns:
            pd.DataFrame: 상세 십계명 데이터
        """
        df = self.commandments_info.copy()

        # 데이터 품질 문제 시뮬레이션
        np.random.seed(2003) # 재현성을 위해 시드 고정
        # 결측치 추가
        df.loc[2, 'obedience_score'] = np.nan # 3번째 계명 (이름 망령되이) 누락
        df.loc[5, 'consequence_score'] = np.nan # 6번째 계명 (살인) 결과 누락
        # 잘못된 타입 추가
        df.loc[3, 'obedience_score'] = 'six' # 4번째 계명 (안식일) 잘못된 타입
        # 이상치 추가
        df.loc[8, 'obedience_score'] = 1 # 9번째 계명 (거짓 증거) 극단적으로 낮은 점수

        # KJV: Exodus 20:17 - "Thou shalt not covet thy neighbour's house..."
        # ESV: Exodus 20:17 - "You shall not covet your neighbor's house..."
        # 개역한글: 출애굽기 20:17 - "네 이웃의 집을 탐내지 말지니라"
        print("✨ 출애굽기 20장 십계명 데이터가 생성되었습니다.")
        print("십계명 준수 수준, 결과, 데이터 품질 문제(결측치, 잘못된 타입, 이상치)를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 십계명은 하나님의 백성으로서 지켜야 할 근본적인 규약이자 삶의 표준입니다. 이는 데이터 품질 규약과 같습니다.")
        print("Spiritual Insight: The Ten Commandments are fundamental standards for God's people, akin to data quality standards.")

        return df

def demo_ten_commandments_data_generation():
    """
    TenCommandmentsDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for TenCommandmentsDataGenerator class.
    """
    print("--- Ten Commandments Data Generation Demo ---")
    print("--- 십계명 데이터 생성 데모 ---")
    generator = TenCommandmentsDataGenerator()
    data = generator.generate_commandments_data()
    return data

if __name__ == "__main__":
    demo_ten_commandments_data_generation()
