
import pandas as pd
import numpy as np

class PassoverPreparationDataGenerator:
    """
    출애굽기 11장의 열 번째 재앙 예고와 유월절 준비 데이터를 생성하는 클래스.
    애굽의 심판과 이스라엘의 구원이라는 두 사건을 시뮬레이션합니다.

    Class to generate data for the announcement of the tenth plague and Passover preparations from Exodus Chapter 11.
    Simulates the two events: judgment on Egypt and salvation of Israel.
    """

    def __init__(self):
        self.events_info = self._load_events_info()

    def _load_events_info(self):
        """
        열 번째 재앙 예고와 유월절 규례에 대한 기본 정보를 로드합니다.
        Loads basic information about the announcement of the tenth plague and Passover ordinances.
        """
        # KJV: Exodus 11:7 - "But against any of the children of Israel shall not a dog move his tongue..."
        # ESV: Exodus 11:7 - "But against any of the people of Israel, not a dog shall growl..."
        # 개역한글: 출애굽기 11:7 - "이스라엘 자손에게는 사람에게나 짐승에게나 개 한 마리도 그 혀를 움직이지 아니하리니"
        return pd.DataFrame({
            'event_id': [1, 2, 3, 4],
            'event_type': ['Plague Announcement', 'Passover Command', 'Blood Application', 'Eating Lamb'],
            'description_kr': ['장자 죽음 예고', '어린 양 준비 명령', '문설주에 피 바르기', '무교병과 쓴 나물 먹기'],
            'description_en': ['Firstborn Death Announced', 'Lamb Preparation Command', 'Blood on Doorposts', 'Eating Unleavened Bread'],
            'target_group': ['Egypt & Israel', 'Israel', 'Israel', 'Israel'],
            'divine_protection': [True, True, True, True] # 유월절 규례를 지키면 보호받음
        })

    def generate_detailed_passover_data(self) -> (pd.DataFrame, pd.DataFrame):
        """
        상세한 유월절 데이터를 생성합니다.
        재앙 예고와 유월절 규례 데이터를 분리하여 반환합니다.

        Generates detailed Passover data.
        Returns separate DataFrames for plague announcement and Passover ordinances.

        Returns:
            tuple: (pd.DataFrame, pd.DataFrame) - (plague_announcement_df, passover_rules_df)
        """
        df = self.events_info.copy()

        # 재앙 예고 데이터
        plague_announcement_df = df[df['event_type'] == 'Plague Announcement'].copy()
        plague_announcement_df['impact_egypt'] = 100 # 애굽의 모든 장자 죽음
        plague_announcement_df['impact_israel'] = 0 # 이스라엘은 보호

        # 유월절 규례 데이터
        passover_rules_df = df[df['event_type'] != 'Plague Announcement'].copy()
        passover_rules_df['obedience_level'] = np.random.randint(80, 100, size=len(passover_rules_df)) # 순종 수준 시뮬레이션

        # KJV: Exodus 12:13 - "And the blood shall be to you for a token upon the houses where ye are..."
        # ESV: Exodus 12:13 - "The blood shall be a sign for you, on the houses where you are..."
        # 개역한글: 출애굽기 12:13 - "내가 애굽 땅을 칠 때에 그 피가 너희의 거하는 집에 대하여 표적이 되어"
        print("✨ 출애굽기 11장 유월절 준비 데이터가 생성되었습니다.")
        print("열 번째 재앙 예고와 유월절 규례 데이터를 분리하여 시뮬레이션합니다.")
        print("\n--- 재앙 예고 데이터 (Plague Announcement Data) ---")
        print(plague_announcement_df.to_string(index=False))
        print("\n--- 유월절 규례 데이터 (Passover Rules Data) ---")
        print(passover_rules_df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 유월절 어린 양의 피는 심판과 구원을 연결하는 핵심 키입니다.")
        print("Spiritual Insight: The blood of the Passover lamb is the key connecting judgment and salvation.")

        return plague_announcement_df, passover_rules_df

def demo_passover_preparation_data_generation():
    """
    PassoverPreparationDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for PassoverPreparationDataGenerator class.
    """
    print("--- Passover Preparation Data Generation Demo ---")
    print("--- 유월절 준비 데이터 생성 데모 ---")
    generator = PassoverPreparationDataGenerator()
    plague_announce_df, passover_rules_df = generator.generate_detailed_passover_data()
    return plague_announce_df, passover_rules_df

if __name__ == "__main__":
    demo_passover_preparation_data_generation()
