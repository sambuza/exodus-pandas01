
import pandas as pd
from .passover_preparation_data import PassoverPreparationDataGenerator

class PassoverMergeJoinAnalyzer:
    """
    출애굽기 11장의 유월절 데이터를 `merge()`와 `join()`을 사용하여 분석하는 클래스.
    재앙 예고와 유월절 규례를 병합하여 하나님의 구원 계획을 탐구합니다.

    Class to analyze Passover data from Exodus Chapter 11 using `merge()` and `join()`.
    Explores God's salvation plan by merging plague announcements and Passover ordinances.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = PassoverPreparationDataGenerator()
        self.plague_announce_df, self.passover_rules_df = self.data_generator.generate_detailed_passover_data()

    def analyze_inner_merge(self):
        """
        `inner merge`를 사용하여 재앙 예고와 유월절 규례를 병합합니다.
        애굽의 심판과 이스라엘의 구원이 어떻게 연결되는지 보여줍니다.

        Uses `inner merge` to combine plague announcements and Passover ordinances.
        Shows how Egypt's judgment and Israel's salvation are connected.

        - KJV: Exodus 12:13 - "And the blood shall be to you for a token upon the houses where ye are..."
        - ESV: Exodus 12:13 - "The blood shall be a sign for you, on the houses where you are..."
        - 개역한글: 출애굽기 12:13 - "내가 애굽 땅을 칠 때에 그 피가 너희의 거하는 집에 대하여 표적이 되어"
        """
        print("\n📊 === 재앙 예고와 유월절 규례 Inner Merge (Plague Announcement & Passover Rules Inner Merge) ===")
        print("'event_id'를 키로 사용하여 애굽의 심판과 이스라엘의 구원 계획을 연결합니다.")
        print("Connecting Egypt's judgment and Israel's salvation plan using 'event_id' as the key.")

        # event_id를 키로 사용하여 inner merge
        merged_df = pd.merge(self.plague_announce_df, self.passover_rules_df, on='event_id', how='inner')
        print(merged_df.to_string(index=False))

        print("\n💡 통찰 (Insight): `inner merge`는 유월절 어린 양의 피라는 '키'를 통해 심판과 구원이 동시에 일어나는 하나님의 완벽한 계획을 보여줍니다.")
        print("Insight: `inner merge` reveals God's perfect plan where judgment and salvation occur simultaneously through the 'key' of the Passover lamb's blood.")
        return merged_df

    def analyze_left_join(self):
        """
        `left join`을 사용하여 유월절 규례를 기준으로 재앙 예고 정보를 연결합니다.
        이스라엘의 관점에서 유월절 준비와 그 의미를 탐구합니다.

        Uses `left join` to connect plague announcement information based on Passover ordinances.
        Explores Passover preparations and their meaning from Israel's perspective.

        - KJV: Exodus 12:26 - "...what mean ye by this service?"
        - ESV: Exodus 12:26 - "...What do you mean by this service?"
        - 개역한글: 출애굽기 12:26 - "...이 예식이 무슨 뜻이냐 하거든"
        """
        print("\n📈 === 유월절 규례 Left Join (Passover Rules Left Join) ===")
        print("유월절 규례를 중심으로 재앙 예고 정보를 연결하여 이스라엘의 관점에서 사건을 분석합니다.")
        print("Analyzing events from Israel's perspective by joining plague announcement info with Passover rules.")

        # event_type을 인덱스로 설정하여 left join
        # join은 기본적으로 인덱스를 기준으로 동작
        joined_df = self.passover_rules_df.set_index('event_id').join(
            self.plague_announce_df.set_index('event_id'),
            lsuffix='_rule', rsuffix='_announce',
            how='left'
        )
        print(joined_df.to_string())

        print("\n💡 통찰 (Insight): `left join`은 이스라엘 백성이 지켜야 할 규례를 중심으로 하나님의 구원 계획이 어떻게 펼쳐졌는지 이해하는 데 도움을 줍니다.")
        print("Insight: `left join` helps understand how God's salvation plan unfolded, centered on the ordinances Israel had to observe.")
        return joined_df

    def run_all_analyses(self) -> dict:
        """
        모든 병합 및 연결 분석을 실행하고 결과를 반환합니다.
        Runs all merge and join analyses and returns the results.
        """
        print("\n--- 출애굽기 11장: 유월절 병합/연결 분석 시작 ---")
        print("--- Exodus Chapter 11: Passover Merge/Join Analysis Started ---")

        results = {
            'inner_merge_result': self.analyze_inner_merge(),
            'left_join_result': self.analyze_left_join()
        }

        print("\n--- 출애굽기 11장: 유월절 병합/연결 분석 완료 ---")
        print("--- Exodus Chapter 11: Passover Merge/Join Analysis Completed ---")
        return results

def demo_passover_merge_join_analyzer():
    """
    PassoverMergeJoinAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for PassoverMergeJoinAnalyzer class.
    """
    print("\n=== Passover Merge/Join Analyzer Demo ===")
    analyzer = PassoverMergeJoinAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_passover_merge_join_analyzer()
