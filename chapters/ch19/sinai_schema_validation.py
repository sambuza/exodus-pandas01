
import pandas as pd
from .sinai_covenant_data import SinaiCovenantDataGenerator

class SinaiSchemaValidationAnalyzer:
    """
    출애굽기 19장의 시내산 언약 데이터를 스키마 정의와 유효성 검증을 사용하여 분석하는 클래스.
    하나님의 언약처럼 데이터의 무결성과 신뢰성을 탐구합니다.

    Class to analyze Sinai Covenant data from Exodus Chapter 19 using schema definition and validation.
    Explores data integrity and reliability, like God's covenant.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = SinaiCovenantDataGenerator()
        self.covenant_df = self.data_generator.generate_covenant_data()

        # 언약 스키마 정의
        self.covenant_schema = {
            'commandment_id': {'dtype': np.int64, 'min': 1, 'max': 12},
            'commandment_type': {'dtype': object, 'allowed_values': ['God-ward', 'Man-ward']},
            'israel_response': {'dtype': object, 'allowed_values': ['Obey', 'Disobey', 'Repent']},
            'consequence': {'dtype': object, 'allowed_values': ['Blessing', 'Curse', 'Mercy']},
            'is_valid': {'dtype': bool}
        }

    def validate_covenant_data(self):
        """
        시내산 언약 데이터를 정의된 스키마에 대해 유효성 검증합니다.
        Validates Sinai Covenant data against the defined schema.

        - KJV: Exodus 19:8 - "And all the people answered together, and said, All that the LORD hath spoken we will do..."
        - ESV: Exodus 19:8 - "All the people answered together and said, 'All that the LORD has spoken we will do.'..."
        - 개역한글: 출애굽기 19:8 - "백성이 일제히 응답하여 가로되 여호와의 명하신 대로 우리가 다 행하리이다"
        """
        print("\n📊 === 시내산 언약 데이터 유효성 검증 (Sinai Covenant Data Validation) ===")
        print("정의된 스키마에 따라 언약 데이터의 무결성을 확인합니다.")
        print("Checking the integrity of covenant data according to the defined schema.")

        errors = []
        df = self.covenant_df
        schema = self.covenant_schema

        for col, rules in schema.items():
            if col not in df.columns:
                errors.append(f"컬럼 누락: {col}")
                continue
            # dtype 검사 (object 타입은 문자열로 간주)
            if rules['dtype'] == object:
                if not (df[col].dtype == object or pd.api.types.is_string_dtype(df[col])):
                    errors.append(f"데이터 타입 불일치: {col} (기대: {rules['dtype']}, 실제: {df[col].dtype})")
            elif df[col].dtype != rules['dtype']:
                errors.append(f"데이터 타입 불일치: {col} (기대: {rules['dtype']}, 실제: {df[col].dtype})")

            if 'allowed_values' in rules:
                invalid_values = df[~df[col].isin(rules['allowed_values'])]
                if not invalid_values.empty:
                    errors.append(f"허용되지 않는 값: {col}에 {invalid_values[col].unique()} 발견")
            if 'min' in rules and (df[col] < rules['min']).any():
                errors.append(f"최소값 위반: {col}에 {rules['min']} 미만 값 발견")
            if 'max' in rules and (df[col] > rules['max']).any():
                errors.append(f"최대값 위반: {col}에 {rules['max']} 초과 값 발견")

        if errors:
            print("\n--- 데이터 유효성 검증 실패 (Data Validation Failed) ---")
            for error in errors:
                print(f"- {error}")
        else:
            print("\n--- 데이터 유효성 검증 성공 (Data Validation Succeeded) ---")
            print("언약 데이터가 스키마에 부합합니다.")

        print("\n💡 통찰 (Insight): 스키마 정의와 유효성 검증은 하나님의 언약처럼 데이터의 무결성과 신뢰성을 확보하는 데 필수적입니다.")
        print("Insight: Schema definition and validation are essential for ensuring data integrity and reliability, just like God's covenant.")
        return errors

    def run_all_analyses(self) -> dict:
        """
        모든 스키마 정의 및 유효성 검증 분석을 실행하고 결과를 반환합니다.
        Runs all schema definition and validation analyses and returns the results.
        """
        print("\n--- 출애굽기 19장: 시내산 언약 스키마/유효성 분석 시작 ---")
        print("--- Exodus Chapter 19: Sinai Covenant Schema/Validation Analysis Started ---")

        results = {
            'validation_errors': self.validate_covenant_data()
        }

        print("\n--- 출애굽기 19장: 시내산 언약 스키마/유효성 분석 완료 ---")
        print("--- Exodus Chapter 19: Sinai Covenant Schema/Validation Analysis Completed ---")
        return results

def demo_sinai_schema_validation_analyzer():
    """
    SinaiSchemaValidationAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for SinaiSchemaValidationAnalyzer class.
    """
    print("\n=== Sinai Schema Validation Analyzer Demo ===")
    analyzer = SinaiSchemaValidationAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_sinai_schema_validation_analyzer()
