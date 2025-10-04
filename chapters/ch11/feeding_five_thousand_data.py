
import pandas as pd
import numpy as np

class FeedingFiveThousandDataGenerator:
    """
    요한복음 6장의 오병이어 기적 데이터를 생성하는 클래스.
    초기 자원과 기적 후 남은 조각 데이터를 시뮬레이션합니다.

    Class to generate data for the miracle of feeding the five thousand from John Chapter 6.
    Simulates initial resources and leftover fragments after the miracle.
    """

    def __init__(self):
        self.resources_info = self._load_resources_info()

    def _load_resources_info(self):
        """
        오병이어 기적의 자원에 대한 기본 정보를 로드합니다.
        Loads basic information about the resources in the miracle of feeding the five thousand.
        """
        # KJV: John 6:9 - "There is a lad here, which hath five barley loaves, and two small fishes..."
        # ESV: John 6:9 - "There is a boy here who has five barley loaves and two fish..."
        # 개역한글: 요한복음 6:9 - "여기 한 아이가 있어 보리떡 다섯 개와 물고기 두 마리를 가졌나이다"
        return pd.DataFrame({
            'resource_id': [1, 2, 3, 4, 5, 6, 7],
            'resource_type': ['bread', 'bread', 'bread', 'bread', 'bread', 'fish', 'fish'],
            'quantity_initial': [1, 1, 1, 1, 1, 1, 1], # 각 자원의 초기 수량
            'source': ['boy', 'boy', 'boy', 'boy', 'boy', 'boy', 'boy'],
            'description_kr': ['보리떡', '보리떡', '보리떡', '보리떡', '보리떡', '물고기', '물고기'],
            'description_en': ['Barley Loaf', 'Barley Loaf', 'Barley Loaf', 'Barley Loaf', 'Barley Loaf', 'Fish', 'Fish']
        })

    def generate_miracle_data(self) -> (pd.DataFrame, pd.DataFrame):
        """
        상세한 오병이어 기적 데이터를 생성합니다.
        초기 자원 데이터와 기적 후 남은 조각 데이터를 분리하여 반환합니다.

        Generates detailed data for the miracle of feeding the five thousand.
        Returns separate DataFrames for initial resources and leftover fragments after the miracle.

        Returns:
            tuple: (pd.DataFrame, pd.DataFrame) - (initial_resources_df, after_miracle_df)
        """
        initial_resources_df = self.resources_info.copy()

        # 기적 후 남은 조각 데이터 시뮬레이션
        after_miracle_data = {
            'resource_id': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            'resource_type': ['leftover'] * 12,
            'quantity_initial': [1] * 12, # 각 바구니에 남은 조각
            'source': ['basket'] * 12,
            'description_kr': ['남은 조각'] * 12,
            'description_en': ['Leftover Fragment'] * 12
        }
        after_miracle_df = pd.DataFrame(after_miracle_data)

        # KJV: John 6:13 - "Therefore they gathered them together, and filled twelve baskets with the fragments..."
        # ESV: John 6:13 - "So they gathered them up and filled twelve baskets with fragments..."
        # 개역한글: 요한복음 6:13 - "이에 거두니 보리떡 다섯 개로 먹고 남은 조각이 열두 바구니에 찼더라"
        print("✨ 요한복음 6장 오병이어 기적 데이터가 생성되었습니다.")
        print("초기 자원과 기적 후 남은 조각 데이터를 분리하여 시뮬레이션합니다.")
        print("\n--- 초기 자원 데이터 (Initial Resources Data) ---")
        print(initial_resources_df.to_string(index=False))
        print("\n--- 기적 후 남은 조각 데이터 (Leftover Fragments Data) ---")
        print(after_miracle_df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 예수님의 능력은 작은 것을 통해 풍성함을 만드십니다. 부족함이 아닌 가능성을 보십니다.")
        print("Spiritual Insight: Jesus' power creates abundance from scarcity. He sees potential, not lack.")

        return initial_resources_df, after_miracle_df

def demo_feeding_five_thousand_data_generation():
    """
    FeedingFiveThousandDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for FeedingFiveThousandDataGenerator class.
    """
    print("--- Feeding Five Thousand Data Generation Demo ---")
    print("--- 오병이어 기적 데이터 생성 데모 ---")
    generator = FeedingFiveThousandDataGenerator()
    initial_df, after_df = generator.generate_miracle_data()
    return initial_df, after_df

if __name__ == "__main__":
    demo_feeding_five_thousand_data_generation()
