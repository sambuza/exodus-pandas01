import pandas as pd
import numpy as np

class PlaguesDataGenerator:
    """
    출애굽기 9장의 재앙 데이터를 생성하는 클래스.
    이집트와 이스라엘(고센)에 미친 재앙의 영향을 시뮬레이션합니다.

    Class to generate plague data from Exodus Chapter 9.
    Simulates the impact of plagues on Egypt and Israel (Goshen).
    """

    def __init__(self):
        self.plagues_info = self._load_plagues_info()

    def _load_plagues_info(self):
        """
        재앙에 대한 기본 정보를 로드합니다.
        Loads basic information about the plagues.
        """
        # KJV: Exodus 9:3 - "Behold, the hand of the LORD is upon thy cattle which is in the field..."
        # ESV: Exodus 9:3 - "Behold, the hand of the LORD will fall with a very severe plague upon your livestock..."
        # 개역한글: 출애굽기 9:3 - "여호와의 손이 들에 있는 네 생축에게 더하리니... 심한 악질이 있을 것이며"
        return pd.DataFrame({
            'plague_order': [5, 6, 7],
            'plague_name_kr': ['악질', '독종', '우박'],
            'plague_name_en': ['Livestock', 'Boils', 'Hail'],
            'target_kr': ['생축', '사람과 짐승', '사람, 짐승, 채소'],
            'target_en': ['Livestock', 'People & Animals', 'People, Animals & Crops'],
            'severity_egypt_initial': [90, 70, 80], # 초기 심각도 (100점 만점)
            'severity_goshen_initial': [0, 10, 0], # 고센 초기 심각도 (100점 만점)
            'pharaoh_heart_hardening': [True, True, True] # 파라오 마음 견고해짐 여부
        })

    def generate_detailed_plague_data(self) -> pd.DataFrame:
        """
        상세한 재앙 데이터를 생성합니다.
        Generates detailed plague data.

        Returns:
            pd.DataFrame: 상세 재앙 데이터
        """
        df = self.plagues_info.copy()

        # 재앙별 실제 피해율 (시뮬레이션)
        np.random.seed(42) # 재현성을 위해 시드 고정
        df['actual_damage_egypt'] = df['severity_egypt_initial'] + np.random.randint(-10, 10, size=len(df))
        df['actual_damage_goshen'] = df['severity_goshen_initial'] + np.random.randint(-5, 5, size=len(df))

        # 피해율은 0-100 사이로 조정
        df['actual_damage_egypt'] = np.clip(df['actual_damage_egypt'], 0, 100)
        df['actual_damage_goshen'] = np.clip(df['actual_damage_goshen'], 0, 100)

        # 고센 보호 여부 (실제 피해가 10 미만이면 보호된 것으로 간주)
        df['is_goshen_protected'] = df['actual_damage_goshen'] < 10

        # KJV: Exodus 9:7 - "And Pharaoh sent, and, behold, there was not one of the cattle of the Israelites dead."
        # ESV: Exodus 9:7 - "And Pharaoh sent, and behold, not one of the livestock of Israel had died."
        # 개역한글: 출애굽기 9:7 - "바로가 보내어 본즉 이스라엘의 생축은 하나도 죽지 아니하였더라"
        print("✨ 출애굽기 9장 재앙 데이터가 생성되었습니다.")
        print("각 재앙이 애굽과 고센에 미친 영향을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 하나님은 재앙 속에서도 당신의 백성을 명확히 구분하고 보호하셨습니다.")
        print("Spiritual Insight: God clearly distinguished and protected His people even amidst the plagues.")

        return df

def demo_plagues_data_generation():
    """
    PlaguesDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for PlaguesDataGenerator class.
    """
    print("--- Plagues Data Generation Demo ---")
    print("--- 재앙 데이터 생성 데모 ---")
    generator = PlaguesDataGenerator()
    data = generator.generate_detailed_plague_data()
    return data

if __name__ == "__main__":
    demo_plagues_data_generation()