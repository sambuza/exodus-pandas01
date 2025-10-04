
import pandas as pd
from .true_vine_data import TrueVineDataGenerator

class TrueVineChainingAnalyzer:
    """
    요한복음 15장의 참 포도나무 데이터를 메서드 체이닝을 사용하여 분석하는 클래스.
    가지의 연결 상태, 가지치기 여부, 열매 수확량 등을 간결하게 탐구합니다.

    Class to analyze True Vine data from John Chapter 15 using method chaining.
    Concise exploration of branch connection status, pruning status, fruit yield, etc.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = TrueVineDataGenerator()
        self.vine_df = self.data_generator.generate_true_vine_data()

    def analyze_fruitful_branches(self):
        """
        메서드 체이닝을 사용하여 열매 맺는 가지들을 필터링하고 분석합니다.
        Filters and analyzes fruitful branches using method chaining.

        - KJV: John 15:2 - "Every branch in me that beareth not fruit he taketh away: and every branch that beareth fruit, he purgeth it, that it may bring forth more fruit."
        - ESV: John 15:2 - "Every branch in me that does not bear fruit he takes away, and every branch that does bear fruit he prunes, that it may bear more fruit."
        - 개역한글: 요한복음 15:2 - "무릇 내게 있어 과실을 맺지 아니하는 가지는 아버지께서 이를 제해 버리시고 무릇 과실을 맺는 가지는 더 많은 과실을 맺게 하려 하여 이를 깨끗케 하시느니라"
        """
        print("\n📊 === 열매 맺는 가지 분석 (Analysis of Fruitful Branches) ===")
        print("메서드 체이닝을 사용하여 예수님께 잘 붙어 있고 열매를 많이 맺는 가지들을 필터링합니다.")
        print("Filtering branches that are well-connected to Jesus and bear much fruit using method chaining.")

        fruitful_branches = self.vine_df \
            .query('connection_to_vine == "Strong" and fruit_yield > 0') \
            .assign(fruitfulness_score = lambda x: x['fruit_yield'] * x['spiritual_health']) \
            .sort_values('fruitfulness_score', ascending=False)
        print(fruitful_branches.to_string(index=False))

        print("\n💡 통찰 (Insight): 메서드 체이닝은 열매 맺는 삶의 여러 영적 조건(연결, 열매, 건강)을 간결하게 연결하여 분석하게 합니다.")
        print("Insight: Method chaining concisely connects various spiritual conditions (connection, fruit, health) of a fruitful life for analysis.")
        return fruitful_branches

    def analyze_pruning_effect(self):
        """
        메서드 체이닝을 사용하여 가지치기의 효과를 분석합니다.
        Analyzes the effect of pruning using method chaining.

        - KJV: John 15:3 - "Now ye are clean through the word which I have spoken unto you."
        - ESV: John 15:3 - "Already you are clean because of the word that I have spoken to you."
        - 개역한글: 요한복음 15:3 - "너희는 내가 일러준 말로 이미 깨끗하였으니"
        """
        print("\n📈 === 가지치기 효과 분석 (Analysis of Pruning Effect) ===")
        print("가지치기 전후의 열매 수확량 변화를 메서드 체이닝으로 분석합니다.")
        print("Analyzing changes in fruit yield before and after pruning using method chaining.")

        pruning_effect_df = self.vine_df \
            .assign(pruning_factor = lambda x: x['pruning_status'].apply(lambda s: 1.5 if s == 'Pruned' else 1.0)) \
            .assign(adjusted_fruit_yield = lambda x: x['fruit_yield'] * x['pruning_factor']) \
            .sort_values('adjusted_fruit_yield', ascending=False)
        print(pruning_effect_df[['branch_id', 'pruning_status', 'fruit_yield', 'adjusted_fruit_yield']].to_string(index=False))

        print("\n💡 통찰 (Insight): 메서드 체이닝은 가지치기라는 영적 과정을 데이터적으로 모델링하여 더 많은 열매를 맺게 하는 하나님의 섭리를 보여줍니다.")
        print("Insight: Method chaining models the spiritual process of pruning, revealing God's providence in bearing more fruit.")
        return pruning_effect_df

    def run_all_analyses(self) -> dict:
        """
        모든 메서드 체이닝 분석을 실행하고 결과를 반환합니다.
        Runs all method chaining analyses and returns the results.
        """
        print("\n--- 요한복음 15장: 참 포도나무 메서드 체이닝 분석 시작 ---")
        print("--- John Chapter 15: True Vine Method Chaining Analysis Started ---")

        results = {
            'fruitful_branches': self.analyze_fruitful_branches(),
            'pruning_effect': self.analyze_pruning_effect()
        }

        print("\n--- 요한복음 15장: 참 포도나무 메서드 체이닝 분석 완료 ---")
        print("--- John Chapter 15: True Vine Method Chaining Analysis Completed ---")
        return results

def demo_true_vine_chaining_analyzer():
    """
    TrueVineChainingAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for TrueVineChainingAnalyzer class.
    """
    print("\n=== True Vine Chaining Analyzer Demo ===")
    analyzer = TrueVineChainingAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_true_vine_chaining_analyzer()
