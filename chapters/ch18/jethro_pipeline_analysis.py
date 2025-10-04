
import pandas as pd
from .jethro_advice_data import JethroAdviceDataGenerator

class JethroPipelineAnalyzer:
    """
    출애굽기 18장의 이드로의 조언 데이터를 `assign()`과 `pipe()`를 사용하여 분석하는 클래스.
    모세의 업무 효율성 변화를 함수형 파이프라인으로 탐구합니다.

    Class to analyze Jethro's advice data from Exodus Chapter 18 using `assign()` and `pipe()`.
    Explores changes in Moses' work efficiency through functional pipelines.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = JethroAdviceDataGenerator()
        self.jethro_df = self.data_generator.generate_jethro_advice_data()

    def analyze_with_assign_chaining(self):
        """
        `assign()`과 메서드 체이닝을 사용하여 새로운 컬럼을 추가하고 데이터를 처리합니다.
        Adds new columns and processes data using `assign()` and method chaining.

        - KJV: Exodus 18:18 - "Thou wilt surely wear away, both thou, and this people that is with thee: for this thing is too heavy for thee; thou art not able to perform it thyself alone."
        - ESV: Exodus 18:18 - "You and the people with you will certainly wear yourselves out, for the thing is too heavy for you. You are not able to do it alone."
        - 개역한글: 출애굽기 18:18 - "너와 또 너와 함께한 이 백성이 필연 기력이 쇠하리니 이 일이 네게 너무 중함이라 네가 혼자 할 수 없으리라"
        """
        print("\n📊 === assign()과 메서드 체이닝을 사용한 데이터 처리 (Data Processing with assign() & Method Chaining) ===")
        print("모세의 업무 부담과 효율성을 새로운 지표로 계산합니다.")
        print("Calculating Moses' workload and efficiency with new metrics.")

        processed_df = self.jethro_df \
            .assign(total_cases = lambda x: x['cases_handled_moses'] + x['cases_handled_delegated']) \
            .assign(moses_load_ratio = lambda x: x['cases_handled_moses'] / x['total_cases']) \
            .assign(efficiency_score = lambda x: x['total_cases'] / (x['moses_fatigue_level'] + 1)) \
            .sort_values('day')
        print(processed_df.to_string(index=False))

        print("\n💡 통찰 (Insight): `assign()`과 메서드 체이닝은 복잡한 데이터 처리 과정을 간결하고 가독성 높게 연결하여 이드로의 조언이 가져온 변화를 명확히 보여줍니다.")
        print("Insight: `assign()` and method chaining concisely and readably connect complex data processing steps, clearly showing the changes brought by Jethro's advice.")
        return processed_df

    def analyze_with_pipe(self):
        """
        `pipe()`를 사용하여 함수형 파이프라인을 구축하고 데이터를 처리합니다.
        Builds a functional pipeline and processes data using `pipe()`.

        - KJV: Exodus 18:24 - "So Moses hearkened to the voice of his father in law, and did all that he had said."
        - ESV: Exodus 18:24 - "So Moses listened to the voice of his father-in-law and did all that he had said."
        - 개역한글: 출애굽기 18:24 - "모세가 그 장인의 말을 듣고 그 말대로 하여"
        """
        print("\n📈 === pipe()를 사용한 함수형 파이프라인 (Functional Pipeline with pipe()) ===")
        print("이드로의 조언을 받아들인 후 모세의 업무 효율성 변화를 `pipe()`로 분석합니다.")
        print("Analyzing changes in Moses' work efficiency after accepting Jethro's advice using `pipe()`.")

        def calculate_efficiency_metrics(df):
            # 총 송사 처리 건수 계산
            df = df.assign(total_cases = lambda x: x['cases_handled_moses'] + x['cases_handled_delegated'])
            # 모세의 업무 부담 비율
            df = df.assign(moses_load_ratio = lambda x: x['cases_handled_moses'] / x['total_cases'])
            # 효율성 점수 (총 처리 건수 / (모세 피로도 + 1))
            df = df.assign(efficiency_score = lambda x: x['total_cases'] / (x['moses_fatigue_level'] + 1))
            return df

        def filter_and_sort_by_period(df, period_type):
            return df.query(f'period == "{period_type}"').sort_values('efficiency_score', ascending=False)

        # 파이프라인 적용
        pipeline_result_before = self.jethro_df.pipe(calculate_efficiency_metrics).pipe(filter_and_sort_by_period, 'Before Advice')
        pipeline_result_after = self.jethro_df.pipe(calculate_efficiency_metrics).pipe(filter_and_sort_by_period, 'After Advice')

        print("\n--- 조언 전 효율성 (Efficiency Before Advice) ---")
        print(pipeline_result_before.to_string(index=False))
        print("\n--- 조언 후 효율성 (Efficiency After Advice) ---")
        print(pipeline_result_after.to_string(index=False))

        print("\n💡 통찰 (Insight): `pipe()`는 복잡한 데이터 처리 로직을 여러 함수로 나누어 가독성과 재사용성을 높이며, 이드로의 조언이 가져온 효율성 증대를 명확히 보여줍니다.")
        print("Insight: `pipe()` enhances readability and reusability by dividing complex data processing logic into multiple functions, clearly demonstrating the efficiency gains from Jethro's advice.")
        return pipeline_result_before, pipeline_result_after

    def run_all_analyses(self) -> dict:
        """
        모든 함수형 파이프라인 분석을 실행하고 결과를 반환합니다.
        Runs all functional pipeline analyses and returns the results.
        """
        print("\n--- 출애굽기 18장: 이드로의 조언 함수형 파이프라인 분석 시작 ---")
        print("--- Exodus Chapter 18: Jethro's Advice Functional Pipeline Analysis Started ---")

        results = {
            'assign_chaining_result': self.analyze_with_assign_chaining(),
            'pipe_result': self.analyze_with_pipe()
        }

        print("\n--- 출애굽기 18장: 이드로의 조언 함수형 파이프라인 분석 완료 ---")
        print("--- Exodus Chapter 18: Jethro's Advice Functional Pipeline Analysis Completed ---")
        return results

def demo_jethro_pipeline_analyzer():
    """
    JethroPipelineAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for JethroPipelineAnalyzer class.
    """
    print("\n=== Jethro Pipeline Analyzer Demo ===")
    analyzer = JethroPipelineAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_jethro_pipeline_analyzer()
