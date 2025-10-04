
import pandas as pd
import numpy as np

class NewCommandmentDataGenerator:
    """
    요한복음 13장의 새 계명(사랑) 데이터를 생성하는 클래스.
    사랑 실천 수준, 행동 유형, 영적 영향력, 데이터 품질 문제(결측치, 이상치)를 시뮬레이션합니다.

    Class to generate New Commandment (love) data from John Chapter 13.
    Simulates love practice levels, action types, spiritual impact, and data quality issues (missing values, outliers).
    """

    def __init__(self):
        self.love_actions_info = self._load_love_actions_info()

    def _load_love_actions_info(self):
        """
        새 계명(사랑) 실천의 주요 요소에 대한 기본 정보를 로드합니다.
        Loads basic information about key elements of practicing the New Commandment (love).
        """
        # KJV: John 13:34 - "A new commandment I give unto you, That ye love one another; as I have loved you, that ye also love one another."
        # ESV: John 13:34 - "A new commandment I give to you, that you love one another: just as I have loved you, you also are to love one another."
        # 개역한글: 요한복음 13:34 - "새 계명을 너희에게 주노니 서로 사랑하라 내가 너희를 사랑한 것같이 너희도 서로 사랑하라"
        return pd.DataFrame({
            'action_id': range(1, 11),
            'action_type': [
                '봉사', '용서', '나눔', '비판', '격려',
                '희생', '무관심', '기도', '정죄', '섬김'
            ],
            'love_level': [9, 8, 7, 2, 8, 10, 1, 9, 3, 9], # 1-10 스케일 (10: 완전한 사랑)
            'spiritual_impact_score': [9, 8, 7, 1, 8, 10, 0, 9, 2, 9], # 0-10 스케일 (10: 매우 긍정적 영향)
            'is_disciple_like': [True, True, True, False, True, True, False, True, False, True]
        })

    def generate_new_commandment_data(self) -> pd.DataFrame:
        """
        상세한 새 계명(사랑) 데이터를 생성합니다.
        사랑 실천 수준, 행동 유형, 영적 영향력, 데이터 품질 문제를 포함합니다.

        Generates detailed New Commandment (love) data.
        Includes love practice levels, action types, spiritual impact, and data quality issues.

        Returns:
            pd.DataFrame: 상세 새 계명 데이터
        """
        df = self.love_actions_info.copy()

        # 데이터 품질 문제 시뮬레이션
        np.random.seed(1334) # 재현성을 위해 시드 고정
        # 결측치 추가
        df.loc[3, 'love_level'] = np.nan # 4번째 행동 (비판) 사랑 수준 누락
        df.loc[6, 'spiritual_impact_score'] = np.nan # 7번째 행동 (무관심) 영적 영향력 누락
        # 잘못된 타입 추가
        df.loc[1, 'love_level'] = 8 # 2번째 행동 (용서) 잘못된 타입
        # 이상치 추가
        df.loc[2, 'love_level'] = 1 # 3번째 행동 (나눔) 극단적으로 낮은 점수

        # KJV: John 13:35 - "By this shall all men know that ye are my disciples, if ye have love one to another."
        # ESV: John 13:35 - "By this all people will know that you are my disciples, if you have love for one another."
        # 개역한글: 요한복음 13:35 - "너희가 서로 사랑하면 이로써 모든 사람이 너희가 내 제자인 줄 알리라"
        print("✨ 요한복음 13장 새 계명(사랑) 데이터가 생성되었습니다.")
        print("사랑 실천 수준, 행동 유형, 영적 영향력, 데이터 품질 문제를 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 새 계명인 사랑은 모든 율법을 아우르는 최상의 품질 기준이자, 제자됨의 유효성 검증 기준이 됩니다.")
        print("Spiritual Insight: The New Commandment of love is the highest quality standard encompassing all laws, and a validation criterion for discipleship.")

        return df

def demo_new_commandment_data_generation():
    """
    NewCommandmentDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for NewCommandmentDataGenerator class.
    """
    print("--- New Commandment Data Generation Demo ---")
    print("--- 새 계명 데이터 생성 데모 ---")
    generator = NewCommandmentDataGenerator()
    data = generator.generate_new_commandment_data()
    return data

if __name__ == "__main__":
    demo_new_commandment_data_generation()
