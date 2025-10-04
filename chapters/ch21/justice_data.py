
import pandas as pd
import numpy as np

class JusticeDataGenerator:
    """
    출애굽기 21-23장의 공의의 법도 데이터를 생성하는 클래스.
    사건 유형, 판결, 배상 수준 등을 시뮬레이션합니다.

    Class to generate Ordinances of Justice data from Exodus Chapters 21-23.
    Simulates case types, judgments, compensation levels, etc.
    """

    def __init__(self, num_cases=100):
        self.num_cases = num_cases

    def generate_justice_data(self) -> pd.DataFrame:
        """
        공의의 법도 데이터를 생성합니다.
        
        Generates the Ordinances of Justice data.

        Returns:
            pd.DataFrame: 공의의 법도 데이터
        """
        np.random.seed(2123)
        
        categories = ['폭행', '절도', '재산 피해', '소유주 책임', '공정한 재판']
        judgments = ['배상', '태형', '무죄', '추방', '사형']
        
        data = {
            'case_id': range(1, self.num_cases + 1),
            'category': np.random.choice(categories, self.num_cases, p=[0.3, 0.2, 0.2, 0.2, 0.1]),
            'victim_status': np.random.choice(['종', '자유인', '외국인'], self.num_cases, p=[0.3, 0.5, 0.2]),
            'offender_status': np.random.choice(['종', '자유인', '외국인'], self.num_cases, p=[0.4, 0.5, 0.1]),
            'compensation_amount': np.random.randint(0, 500, self.num_cases) * 10,
            'judgment': np.random.choice(judgments, self.num_cases, p=[0.5, 0.1, 0.2, 0.1, 0.1])
        }
        
        df = pd.DataFrame(data)

        # 데이터 품질 문제 추가
        df.loc[df.sample(frac=0.1, random_state=1).index, 'compensation_amount'] = np.nan
        df.loc[df.sample(frac=0.05, random_state=2).index, 'judgment'] = '알 수 없음'

        print("✨ 출애굽기 21-23장 공의의 법도 데이터가 생성되었습니다.")
        print(f"{self.num_cases}개의 재판 사례를 시뮬레이션합니다.")
        print(df.head().to_string())
        print("\n---")
        print("영적 통찰: 공의의 법도는 공동체의 질서와 정의를 유지하기 위한 하나님의 구체적인 지침입니다.")
        print("Spiritual Insight: The ordinances of justice are God's specific guidelines for maintaining order and justice in the community.")

        return df

def demo_justice_data_generation():
    """
    JusticeDataGenerator 클래스의 데모 실행 함수.
    """
    print("--- Justice Data Generation Demo ---")
    generator = JusticeDataGenerator()
    data = generator.generate_justice_data()
    return data

if __name__ == "__main__":
    demo_justice_data_generation()
