
import pandas as pd
import numpy as np

class LocustsDarknessDataGenerator:
    """
    출애굽기 10장의 메뚜기 재앙과 흑암 재앙 데이터를 생성하는 클래스.
    애굽과 고센에 미친 재앙의 영향을 그룹별로 시뮬레이션합니다.

    Class to generate data for the plagues of locusts and darkness from Exodus Chapter 10.
    Simulates the impact of these plagues on Egypt and Goshen by group.
    """

    def __init__(self):
        self.plagues_info = self._load_plagues_info()

    def _load_plagues_info(self):
        """
        메뚜기 재앙과 흑암 재앙에 대한 기본 정보를 로드합니다.
        Loads basic information about the plagues of locusts and darkness.
        """
        # KJV: Exodus 10:15 - "...there remained not any green thing in all the land of Egypt..."
        # ESV: Exodus 10:15 - "...not a single green thing remained on tree or plant in all the land of Egypt."
        # 개역한글: 출애굽기 10:15 - "...애굽 온 땅에 채소나 나무의 열매는 남지 아니하였더라"
        # KJV: Exodus 10:23 - "...but all the children of Israel had light in their dwellings."
        # ESV: Exodus 10:23 - "...but all the people of Israel had light in their dwellings."
        # 개역한글: 출애굽기 10:23 - "...이스라엘 자손의 거하는 곳에는 광명이 있었더라"
        return pd.DataFrame({
            'plague_order': [8, 9],
            'plague_name_kr': ['메뚜기 재앙', '흑암 재앙'],
            'plague_name_en': ['Locusts', 'Darkness'],
            'target_kr': ['채소, 나무', '온 땅, 사람'],
            'target_en': ['Vegetation, Trees', 'All Land, People'],
            'duration_days': [1, 3], # 재앙 지속 일수
            'pharaoh_response_kr': ['회개(일시적)', '강퍅함'],
            'pharaoh_response_en': ['Repentance(temporary)', 'Hardened']
        })

    def generate_plague_impact_data(self) -> pd.DataFrame:
        """
        상세한 재앙 영향 데이터를 생성합니다.
        애굽과 고센에 미친 영향을 그룹별로 시뮬레이션합니다.

        Generates detailed plague impact data.
        Simulates the impact on Egypt and Goshen by group.

        Returns:
            pd.DataFrame: 상세 재앙 영향 데이터
        """
        df = self.plagues_info.copy()

        # 애굽과 고센의 피해 시뮬레이션
        np.random.seed(10) # 재현성을 위해 시드 고정
        egypt_impact = []
        goshen_impact = []
        location = []
        plague_name = []
        plague_name_en = []
        pharaoh_response = []

        for _, row in df.iterrows():
            # 애굽 데이터
            egypt_impact.append(row['duration_days'] * np.random.randint(20, 40))
            goshen_impact.append(np.random.randint(0, 5)) # 고센은 피해가 적거나 없음
            location.append('Egypt')
            plague_name.append(row['plague_name_kr'])
            plague_name_en.append(row['plague_name_en'])
            pharaoh_response.append(row['pharaoh_response_kr'])

            # 고센 데이터
            egypt_impact.append(np.random.randint(0, 5)) # 고센 데이터에서는 애굽 피해는 무의미
            goshen_impact.append(np.random.randint(0, 5)) # 고센은 피해가 적거나 없음
            location.append('Goshen')
            plague_name.append(row['plague_name_kr'])
            plague_name_en.append(row['plague_name_en'])
            pharaoh_response.append(row['pharaoh_response_kr'])

        impact_df = pd.DataFrame({
            'plague_name_kr': plague_name,
            'plague_name_en': plague_name_en,
            'location': location,
            'impact_score': egypt_impact if location[0] == 'Egypt' else goshen_impact, # 실제 피해 점수
            'pharaoh_response': pharaoh_response
        })

        # impact_score를 location에 따라 올바르게 할당
        impact_df['impact_score'] = impact_df.apply(lambda x: x['impact_score'] if x['location'] == 'Egypt' else np.random.randint(0, 5), axis=1)

        # KJV: Exodus 10:23 - "...but all the children of Israel had light in their dwellings."
        # ESV: Exodus 10:23 - "...but all the people of Israel had light in their dwellings."
        # 개역한글: 출애굽기 10:23 - "...이스라엘 자손의 거하는 곳에는 광명이 있었더라"
        print("✨ 출애굽기 10장 재앙 영향 데이터가 생성되었습니다.")
        print("메뚜기 재앙과 흑암 재앙이 애굽과 고센에 미친 영향을 시뮬레이션합니다.")
        print(impact_df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 하나님은 재앙 속에서도 당신의 백성을 명확히 구분하고 보호하셨습니다.")
        print("Spiritual Insight: God clearly distinguished and protected His people even amidst the plagues.")

        return impact_df

def demo_locusts_darkness_data_generation():
    """
    LocustsDarknessDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for LocustsDarknessDataGenerator class.
    """
    print("--- Locusts and Darkness Data Generation Demo ---")
    print("--- 메뚜기 및 흑암 재앙 데이터 생성 데모 ---")
    generator = LocustsDarknessDataGenerator()
    data = generator.generate_plague_impact_data()
    return data

if __name__ == "__main__":
    demo_locusts_darkness_data_generation()
