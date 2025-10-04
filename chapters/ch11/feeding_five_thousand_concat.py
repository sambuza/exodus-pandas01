
import pandas as pd
from .feeding_five_thousand_data import FeedingFiveThousandDataGenerator

class FeedingFiveThousandConcatAnalyzer:
    """
    요한복음 6장의 오병이어 기적 데이터를 `concat()`을 사용하여 분석하는 클래스.
    초기 자원과 기적 후 남은 조각을 연결하여 예수님의 능력을 탐구합니다.

    Class to analyze the miracle of feeding the five thousand from John Chapter 6 using `concat()`.
    Explores Jesus' power by concatenating initial resources and leftover fragments after the miracle.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = FeedingFiveThousandDataGenerator()
        self.initial_resources_df, self.after_miracle_df = self.data_generator.generate_miracle_data()

    def analyze_concatenation_vertical(self):
        """
        초기 자원과 기적 후 남은 조각 데이터를 수직으로 연결합니다.
        자원의 변화를 한눈에 파악합니다.

        Vertically concatenates initial resources and leftover fragments after the miracle.
        Provides an at-a-glance view of resource changes.

        - KJV: John 6:13 - "Therefore they gathered them together, and filled twelve baskets with the fragments..."
        - ESV: John 6:13 - "So they gathered them up and filled twelve baskets with fragments..."
        - 개역한글: 요한복음 6:13 - "이에 거두니 보리떡 다섯 개로 먹고 남은 조각이 열두 바구니에 찼더라"
        """
        print("\n📊 === 초기 자원과 남은 조각 수직 연결 (Vertical Concatenation of Initial & Leftover Resources) ===")
        print("기적 전후의 자원 데이터를 수직으로 연결하여 전체 자원의 변화를 확인합니다.")
        print("Connecting pre- and post-miracle resource data vertically to observe the overall resource change.")

        concatenated_df = pd.concat([self.initial_resources_df, self.after_miracle_df], ignore_index=True)
        print(concatenated_df.to_string(index=False))

        print("\n💡 통찰 (Insight): `concat()`을 통해 예수님의 능력으로 자원이 얼마나 증폭되었는지 한눈에 시각적으로 확인할 수 있습니다.")
        print("Insight: `concat()` visually demonstrates how resources were amplified by Jesus' power.")
        return concatenated_df

    def analyze_concatenation_horizontal(self):
        """
        (예시) 다른 종류의 데이터를 수평으로 연결합니다.
        (Example) Horizontally concatenates different types of data.

        - KJV: John 6:10 - "...the men sat down, in number about five thousand."
        - ESV: John 6:10 - "...the people sat down, about five thousand in number."
        - 개역한글: 요한복음 6:10 - "...사람들이 앉으니 수효가 오천 명쯤 되더라"
        """
        print("\n📈 === 자원과 사람 수 수평 연결 (Horizontal Concatenation of Resources & People Count) ===")
        print("자원 데이터와 사람 수 데이터를 수평으로 연결하여 기적의 규모를 다각도로 살펴봅니다.")
        print("Connecting resource data and people count data horizontally to examine the miracle's scale from various angles.")

        # 가상의 사람 수 데이터프레임 생성
        people_count_df = pd.DataFrame({
            'resource_type': ['bread', 'fish', 'leftover'],
            'people_fed': [5000, 5000, 0] # 남은 조각은 이미 배부른 사람들을 위한 것
        })

        # resource_type을 인덱스로 설정하여 concat (axis=1)
        # initial_resources_df와 people_count_df를 resource_type을 기준으로 합치기 위해
        # 먼저 resource_type을 인덱스로 설정하고, 그 다음 concat을 사용합니다.
        # 이 예시에서는 merge가 더 적합할 수 있으나, concat의 활용을 보여주기 위함입니다.
        combined_df = pd.concat([
            self.initial_resources_df.groupby('resource_type')['quantity_initial'].sum().reset_index(),
            people_count_df
        ], axis=1)
        print(combined_df.to_string(index=False))

        print("\n💡 통찰 (Insight): `concat(axis=1)`은 서로 다른 관점의 데이터를 나란히 놓고 비교할 때 유용합니다.")
        print("Insight: `concat(axis=1)` is useful for comparing data from different perspectives side-by-side.")
        return combined_df

    def run_all_analyses(self) -> dict:
        """
        모든 연결 분석을 실행하고 결과를 반환합니다.
        Runs all concatenation analyses and returns the results.
        """
        print("\n--- 요한복음 6장: 오병이어 연결 분석 시작 ---")
        print("--- John Chapter 6: Feeding Five Thousand Concatenation Analysis Started ---")

        results = {
            'vertical_concat_result': self.analyze_concatenation_vertical(),
            'horizontal_concat_result': self.analyze_concatenation_horizontal()
        }

        print("\n--- 요한복음 6장: 오병이어 연결 분석 완료 ---")
        print("--- John Chapter 6: Feeding Five Thousand Concatenation Analysis Completed ---")
        return results

def demo_feeding_five_thousand_concat_analyzer():
    """
    FeedingFiveThousandConcatAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for FeedingFiveThousandConcatAnalyzer class.
    """
    print("\n=== Feeding Five Thousand Concatenation Analyzer Demo ===")
    analyzer = FeedingFiveThousandConcatAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_feeding_five_thousand_concat_analyzer()
