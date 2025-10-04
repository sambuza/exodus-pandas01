
import pandas as pd
from pandas.testing import assert_frame_equal
from .truth_life_data import TruthLifeDataGenerator

class TruthAssertValidationAnalyzer:
    """
    요한복음 14장 6절의 진리 데이터를 `assert_frame_equal()`을 사용하여 분석하는 클래스.
    예수님 말씀의 절대적인 유효성을 데이터적으로 검증합니다.

    Class to analyze truth data from John 14:6 using `assert_frame_equal()`.
    Numerically validates the absolute truth of Jesus' words.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = TruthLifeDataGenerator()
        self.truth_df = self.data_generator.generate_truth_life_data()

    def validate_with_assert_frame_equal(self):
        """
        `assert_frame_equal()`을 사용하여 실제 데이터와 기대하는 진리 데이터를 비교합니다.
        Compares actual data with expected truth data using `assert_frame_equal()`.

        - KJV: John 14:6 - "Jesus saith unto him, I am the way, the truth, and the life: no man cometh unto the Father, but by me."
        - ESV: John 14:6 - "Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.'"
        - 개역한글: 요한복음 14:6 - "예수께서 가라사대 내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라"
        """
        print("\n📊 === 예수님 말씀의 진리 유효성 검증 (Validating Jesus' Words of Truth) ===")
        print("실제 데이터가 예수님 말씀의 진리 스키마에 부합하는지 `assert_frame_equal()`로 확인합니다.")
        print("Checking if actual data conforms to the truth schema of Jesus' words using `assert_frame_equal()`.")

        # 기대하는 진리 데이터프레임 (예수님을 통한 길만 구원을 얻음)
        expected_truth = pd.DataFrame({
            'path_id': [1, 2, 3, 4, 5, 6],
            'path_taken': ['Jesus', 'Jesus', 'Jesus', 'Worldly Wisdom', 'Self-effort', 'Other Religions'],
            'belief_status': ['Believe', 'Believe', 'Believe', 'Not Believe', 'Not Believe', 'Not Believe'],
            'outcome_type': ['Life', 'Life', 'Life', 'Death', 'Death', 'Death'],
            'fulfillment_level': [10, 9, 10, 3, 2, 1], # 0-10 스케일 (10: 완전한 채움)
            'peace_level': [10, 9, 10, 2, 1, 0] # 0-10 스케일 (10: 완전한 평안)
        })

        # 실제 데이터와 기대하는 진리 데이터 비교
        try:
            # 비교를 위해 컬럼 순서와 인덱스 리셋
            actual_df_sorted = self.truth_df.sort_values(by=list(self.truth_df.columns)).reset_index(drop=True)
            expected_df_sorted = expected_truth.sort_values(by=list(expected_truth.columns)).reset_index(drop=True)

            assert_frame_equal(actual_df_sorted, expected_df_sorted, check_dtype=False)
            print("✅ `assert_frame_equal`: 실제 데이터가 예수님 말씀의 진리 스키마에 부합합니다.")
            print("Actual data conforms to the truth schema of Jesus' words.")
        except AssertionError as e:
            print("❌ `assert_frame_equal`: 실제 데이터가 예수님 말씀의 진리 스키마에 부합하지 않습니다.")
            print(f"오류 내용: {e}")

        print("\n💡 통찰 (Insight): `assert_frame_equal`은 예수님이라는 절대적인 진리(스키마)에 비추어 우리의 삶이나 데이터가 유효한지 검증하는 영적 원리를 데이터적으로 보여줍니다.")
        print("Insight: `assert_frame_equal` numerically illustrates the spiritual principle of validating our lives or data against the absolute truth (schema) of Jesus.")
        return True if not e else False # Return validation status

    def run_all_analyses(self) -> dict:
        """
        모든 진리 유효성 검증 분석을 실행하고 결과를 반환합니다.
        Runs all truth validation analyses and returns the results.
        """
        print("\n--- 요한복음 14장: 진리 유효성 검증 분석 시작 ---")
        print("--- John Chapter 14: Truth Validation Analysis Started ---")

        results = {
            'validation_status': self.validate_with_assert_frame_equal()
        }

        print("\n--- 요한복음 14장: 진리 유효성 검증 분석 완료 ---")
        print("--- John Chapter 14: Truth Validation Analysis Completed ---")
        return results

def demo_truth_assert_validation_analyzer():
    """
    TruthAssertValidationAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for TruthAssertValidationAnalyzer class.
    """
    print("\n=== Truth Assert Validation Analyzer Demo ===")
    analyzer = TruthAssertValidationAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_truth_assert_validation_analyzer()
