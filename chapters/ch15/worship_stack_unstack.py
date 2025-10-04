
import pandas as pd
from .worship_spirit_truth_data import WorshipSpiritTruthDataGenerator

class WorshipStackUnstackAnalyzer:
    """
    요한복음 4장의 예배 데이터를 `stack()`과 `unstack()`을 사용하여 분석하는 클래스.
    예배의 본질과 다양한 형태를 인덱스와 컬럼 간에 전환하며 탐구합니다.

    Class to analyze worship data from John Chapter 4 using `stack()` and `unstack()`.
    Explores the essence and various forms of worship by pivoting between index and columns.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = WorshipSpiritTruthDataGenerator()
        self.worship_df = self.data_generator.generate_worship_data()

    def analyze_stack_unstack(self):
        """
        `stack()`과 `unstack()`을 사용하여 예배 데이터를 인덱스와 컬럼 간에 전환합니다.
        예배의 본질과 표현 수준을 다각도로 분석합니다.

        Uses `stack()` and `unstack()` to pivot worship data between index and columns.
        Analyzes the essence and expression levels of worship from multiple angles.

        - KJV: John 4:24 - "God is a Spirit: and they that worship him must worship him in spirit and in truth."
        - ESV: John 4:24 - "God is spirit, and those who worship him must worship in spirit and truth."
        - 개역한글: 요한복음 4:24 - "하나님은 영이시니 예배하는 자가 신령과 진정으로 예배할지니라"
        """
        print("\n📊 === 예배 데이터 Stack/Unstack 분석 (Worship Data Stack/Unstack Analysis) ===")
        print("예배의 본질과 표현 수준을 `stack()`과 `unstack()`으로 전환하며 다각도로 분석합니다.")
        print("Analyzing the essence and expression levels of worship from multiple angles by pivoting with `stack()` and `unstack()`.")

        # 'worship_type'과 'element_en'을 멀티인덱스로 설정
        multi_indexed_worship = self.worship_df.set_index(['worship_type', 'element_en'])
        print("\n--- 멀티인덱스 DataFrame (Multi-indexed DataFrame) ---")
        print(multi_indexed_worship.to_string())

        # 멀티인덱스를 stack하여 컬럼을 인덱스 레벨로 변환
        print("\n--- 데이터 Stack (Stacking Data) ---")
        stacked_worship = multi_indexed_worship[['essence_level', 'expression_level']].stack()
        print(stacked_worship.head().to_string())

        # stack된 데이터를 unstack하여 인덱스 레벨을 컬럼으로 변환
        print("\n--- 데이터 Unstack (Unstacking Data) ---")
        unstacked_worship = stacked_worship.unstack()
        print(unstacked_worship.head().to_string())

        print("\n💡 통찰 (Insight): `stack()`과 `unstack()`은 예배의 본질과 외적 표현이 어떻게 상호작용하는지 다층적으로 이해하게 합니다.")
        print("Insight: `stack()` and `unstack()` help understand how the essence and outward expression of worship interact in a multi-layered way.")
        return stacked_worship, unstacked_worship

    def run_all_analyses(self) -> dict:
        """
        모든 스택/언스택 분석을 실행하고 결과를 반환합니다.
        Runs all stack/unstack analyses and returns the results.
        """
        print("\n--- 요한복음 4장: 예배 스택/언스택 분석 시작 ---")
        print("--- John Chapter 4: Worship Stack/Unstack Analysis Started ---")

        results = {
            'stack_unstack_results': self.analyze_stack_unstack()
        }

        print("\n--- 요한복음 4장: 예배 스택/언스택 분석 완료 ---")
        print("--- John Chapter 4: Worship Stack/Unstack Analysis Completed ---")
        return results

def demo_worship_stack_unstack_analyzer():
    """
    WorshipStackUnstackAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for WorshipStackUnstackAnalyzer class.
    """
    print("\n=== Worship Stack/Unstack Analyzer Demo ===")
    analyzer = WorshipStackUnstackAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_worship_stack_unstack_analyzer()
