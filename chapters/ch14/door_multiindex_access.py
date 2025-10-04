
import pandas as pd
from .door_of_salvation_data import DoorOfSalvationDataGenerator

class DoorMultiIndexAccessAnalyzer:
    """
    요한복음 10장 9절의 "나는 문이니" 데이터를 `MultiIndex`를 사용하여 분석하는 클래스.
    예수님을 통한 길과 다른 길의 다층적인 의미를 구조화하고 접근합니다.

    Class to analyze "I am the door" data from John 10:9 using `MultiIndex`.
    Structures and accesses multi-layered meanings of the path through Jesus versus other paths.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = DoorOfSalvationDataGenerator()
        self.door_df = self.data_generator.generate_door_of_salvation_data()

    def create_and_access_multiindex(self):
        """
        'path_type'과 'entry_method'를 멀티인덱스로 설정하고 데이터를 접근합니다.
        Sets 'path_type' and 'entry_method' as MultiIndex and accesses data.

        - KJV: John 10:9 - "I am the door: by me if any man enter in, he shall be saved..."
        - ESV: John 10:9 - "I am the door. If anyone enters by me, he will be saved..."
        - 개역한글: 요한복음 10:9 - "내가 곧 문이니 누구든지 나로 말미암아 들어가면 구원을 얻고..."
        """
        print("\n📊 === 멀티인덱스 생성 및 접근 (MultiIndex Creation and Access) ===")
        print("'path_type'과 'entry_method'를 멀티인덱스로 설정하여 구원의 문 데이터를 분석합니다.")
        print("Analyzing the door of salvation data by setting 'path_type' and 'entry_method' as MultiIndex.")

        # MultiIndex 생성
        multi_indexed_df = self.door_df.set_index(['path_type', 'entry_method'])
        print("\n--- 멀티인덱스 DataFrame (Multi-indexed DataFrame) ---")
        print(multi_indexed_df.to_string())

        # 멀티인덱스를 사용하여 특정 데이터 접근 (예: 예수님을 통한 믿음의 길)
        print("\n--- 멀티인덱스로 특정 데이터 접근 (Accessing Data with MultiIndex - Jesus, Faith) ---")
        print(multi_indexed_df.loc[('Jesus', 'Faith')].to_string())

        print("\n💡 통찰 (Insight): `MultiIndex`는 예수님이라는 문을 통해 얻는 구원과 풍성한 삶의 다층적인 의미를 구조화하여 보여줍니다.")
        print("Insight: `MultiIndex` structures and displays the multi-layered meanings of salvation and abundant life found through Jesus, the Door.")
        return multi_indexed_df

    def analyze_multiindex_levels(self):
        """
        멀티인덱스의 특정 레벨을 기준으로 데이터를 접근하고 분석합니다.
        Accesses and analyzes data based on specific levels of the MultiIndex.

        - KJV: John 10:10 - "The thief cometh not, but for to steal, and to kill, and to destroy: I am come that they might have life, and that they might have it more abundantly."
        - ESV: John 10:10 - "The thief comes only to steal and kill and destroy. I came that they may have life and have it abundantly."
        - 개역한글: 요한복음 10:10 - "도적이 오는 것은 도적질하고 죽이고 멸망시키려는 것뿐이요 내가 온 것은 양으로 생명을 얻게 하고 더 풍성히 얻게 하려는 것이라"
        """
        print("\n📈 === 멀티인덱스 레벨별 분석 (Analysis by MultiIndex Levels) ===")
        print("멀티인덱스의 특정 레벨을 사용하여 예수님을 통한 길의 만족도와 평안 수준을 분석합니다.")
        print("Analyzing the fulfillment and peace levels of the path through Jesus using specific levels of the MultiIndex.")

        multi_indexed_df = self.door_df.set_index(['path_type', 'entry_method'])

        # 모든 예수님을 통한 길 데이터 접근
        jesus_path_data = multi_indexed_df.loc['Jesus']
        print("\n--- 모든 예수님을 통한 길 데이터 (All Jesus' Path Data) ---")
        print(jesus_path_data.to_string())

        # 예수님을 통한 길의 평균 만족도와 평안 수준
        avg_fulfillment_jesus = jesus_path_data['fulfillment_level'].mean()
        avg_peace_jesus = jesus_path_data['peace_level'].mean()
        print(f"\n예수님을 통한 길의 평균 만족도 (Average Fulfillment on Jesus' Path): {avg_fulfillment_jesus:.2f}")
        print(f"예수님을 통한 길의 평균 평안 수준 (Average Peace on Jesus' Path): {avg_peace_jesus:.2f}")

        print("\n💡 통찰 (Insight): `loc`를 통해 예수님이라는 문을 통과할 때 얻는 풍성한 삶과 평안을 데이터적으로 확인할 수 있습니다.")
        print("Insight: `loc` allows us to numerically confirm the abundant life and peace gained when passing through Jesus, the Door.")
        return jesus_path_data

    def run_all_analyses(self) -> dict:
        """
        모든 멀티인덱스 분석을 실행하고 결과를 반환합니다.
        Runs all MultiIndex analyses and returns the results.
        """
        print("\n--- 요한복음 10장: 구원의 문 멀티인덱스 분석 시작 ---")
        print("--- John Chapter 10: Door of Salvation MultiIndex Analysis Started ---")

        results = {
            'multiindex_access': self.create_and_access_multiindex(),
            'multiindex_levels_analysis': self.analyze_multiindex_levels()
        }

        print("\n--- 요한복음 10장: 구원의 문 멀티인덱스 분석 완료 ---")
        print("--- John Chapter 10: Door of Salvation MultiIndex Analysis Completed ---")
        return results

def demo_door_multiindex_access_analyzer():
    """
    DoorMultiIndexAccessAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for DoorMultiIndexAccessAnalyzer class.
    """
    print("\n=== Door MultiIndex Access Analyzer Demo ===")
    analyzer = DoorMultiIndexAccessAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_door_multiindex_access_analyzer()
