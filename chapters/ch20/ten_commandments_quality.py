
import pandas as pd
import numpy as np
from .ten_commandments_data import TenCommandmentsDataGenerator

class TenCommandmentsQualityAnalyzer:
    """
    출애굽기 20장의 십계명 데이터를 데이터 품질 관점(결측치, 타입, 이상치)에서 분석하는 클래스.
    십계명처럼 깨끗하고 신뢰할 수 있는 데이터를 구축하는 과정을 탐구합니다.

    Class to analyze Ten Commandments data from Exodus Chapter 20 from a data quality perspective (missing values, types, outliers).
    Explores the process of building clean and reliable data, like the Ten Commandments.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = TenCommandmentsDataGenerator()
        self.commandments_df = self.data_generator.generate_commandments_data()

    def handle_missing_values(self):
        """
        십계명 데이터의 결측치를 처리합니다.
        Handles missing values in the Ten Commandments data.

        - KJV: Exodus 20:7 - "Thou shalt not take the name of the LORD thy God in vain..."
        - ESV: Exodus 20:7 - "You shall not take the name of the LORD your God in vain..."
        - 개역한글: 출애굽기 20:7 - "너는 너의 하나님 여호와의 이름을 망령되이 일컫지 말라..."
        """
        print("\n📊 === 십계명 데이터 결측치 처리 (Handling Missing Values in Ten Commandments Data) ===")
        print("'obedience_score'와 'consequence_score'의 결측치를 처리하여 데이터의 완전성을 확보합니다.")
        print("Ensuring data completeness by handling missing values in 'obedience_score' and 'consequence_score'.")

        df_processed = self.commandments_df.copy()

        # 결측치 확인
        print("\n--- 원본 데이터 결측치 (Original Data Missing Values) ---")
        print(df_processed.isnull().sum())

        # 'obedience_score'의 결측치를 평균값으로 채우기
        df_processed['obedience_score'] = pd.to_numeric(df_processed['obedience_score'], errors='coerce') # 잘못된 타입 먼저 처리
        df_processed['obedience_score'] = df_processed['obedience_score'].fillna(df_processed['obedience_score'].mean())

        # 'consequence_score'의 결측치를 0으로 채우기
        df_processed['consequence_score'] = pd.to_numeric(df_processed['consequence_score'], errors='coerce') # 잘못된 타입 먼저 처리
        df_processed['consequence_score'] = df_processed['consequence_score'].fillna(0)

        print("\n--- 결측치 처리 후 데이터 (Data After Handling Missing Values) ---")
        print(df_processed[['commandment_id', 'obedience_score', 'consequence_score']].to_string(index=False))
        print("\n--- 결측치 처리 후 결측치 (Missing Values After Handling) ---")
        print(df_processed.isnull().sum())

        print("\n💡 통찰 (Insight): `fillna()`는 하나님의 은혜처럼 우리의 부족함을 채워 데이터의 완전성을 확보하게 합니다.")
        print("Insight: `fillna()` ensures data completeness by filling our deficiencies, much like God's grace.")
        return df_processed

    def convert_data_types(self, df_processed):
        """
        십계명 데이터의 데이터 타입을 올바르게 변환합니다.
        Converts data types in the Ten Commandments data to the correct format.

        - KJV: Exodus 20:8 - "Remember the sabbath day, to keep it holy."
        - ESV: Exodus 20:8 - "Remember the Sabbath day, to keep it holy."
        - 개역한글: 출애굽기 20:8 - "안식일을 기억하여 거룩히 지키라"
        """
        print("\n📈 === 십계명 데이터 타입 변환 (Converting Data Types in Ten Commandments Data) ===")
        print("'obedience_score'와 'consequence_score'를 숫자 타입으로, 'commandment_id'를 문자열 타입으로 변환합니다.")
        print("Converting 'obedience_score' and 'consequence_score' to numeric types, and 'commandment_id' to string type.")

        df_converted = df_processed.copy()

        # 잘못된 타입이 있는 'obedience_score'를 숫자 타입으로 변환 (errors='coerce'로 변환 불가 값은 NaN으로)
        df_converted['obedience_score'] = pd.to_numeric(df_converted['obedience_score'], errors='coerce')
        df_converted['consequence_score'] = pd.to_numeric(df_converted['consequence_score'], errors='coerce')

        # 변환 후 생긴 NaN은 다시 평균으로 채우기 (선택적)
        df_converted['obedience_score'] = df_converted['obedience_score'].fillna(df_converted['obedience_score'].mean())
        df_converted['consequence_score'] = df_converted['consequence_score'].fillna(df_converted['consequence_score'].mean())

        # 'commandment_id'를 문자열로 변환
        df_converted['commandment_id'] = df_converted['commandment_id'].astype(str)

        print("\n--- 변환 후 데이터 타입 (Data Types After Conversion) ---")
        print(df_converted.dtypes)
        print("\n--- 변환 후 데이터 (Data After Conversion) ---")
        print(df_converted[['commandment_id', 'obedience_score', 'consequence_score']].to_string(index=False))

        print("\n💡 통찰 (Insight): `astype()`은 십계명처럼 데이터가 올바른 규격에 맞는지 확인하여 분석의 유효성을 확보하게 합니다.")
        print("Insight: `astype()` ensures data conforms to correct specifications, like the Ten Commandments, securing analytical validity.")
        return df_converted

    def detect_outliers(self, df_converted):
        """
        십계명 데이터에서 이상치를 탐지합니다.
        Detects outliers in the Ten Commandments data.

        - KJV: Exodus 20:17 - "Thou shalt not covet thy neighbour's house..."
        - ESV: Exodus 20:17 - "You shall not covet your neighbor's house..."
        - 개역한글: 출애굽기 20:17 - "네 이웃의 집을 탐내지 말지니라"
        """
        print("\n📉 === 십계명 데이터 이상치 탐지 (Outlier Detection in Ten Commandments Data) ===")
        print("'obedience_score'에서 평균과 크게 벗어나는 이상치를 탐지하여 불순종의 극단적인 경우를 식별합니다.")
        print("Detecting outliers in 'obedience_score' that deviate significantly from the mean to identify extreme cases of disobedience.")

        # Z-score를 이용한 이상치 탐지
        mean_score = df_converted['obedience_score'].mean()
        std_score = df_converted['obedience_score'].std()
        df_converted['z_score_obedience'] = (df_converted['obedience_score'] - mean_score) / std_score

        # Z-score가 2 이상인 경우를 이상치로 간주
        outliers = df_converted[abs(df_converted['z_score_obedience']) > 2]

        print("\n--- 'obedience_score' 이상치 (Outliers in 'obedience_score') ---")
        print(outliers[['commandment_id', 'obedience_score', 'z_score_obedience']].to_string(index=False))

        print("\n💡 통찰 (Insight): 이상치 탐지는 십계명 준수에서 극단적인 불순종이나 과도한 순종(자기 의)을 식별하여 영적 삶의 균형을 점검하게 합니다.")
        print("Insight: Outlier detection helps identify extreme disobedience or excessive self-righteousness in keeping the Ten Commandments, prompting a check on spiritual balance.")
        return outliers

    def run_all_analyses(self) -> dict:
        """
        모든 데이터 품질 분석을 실행하고 결과를 반환합니다.
        Runs all data quality analyses and returns the results.
        """
        print("\n--- 출애굽기 20장: 십계명 데이터 품질 분석 시작 ---")
        print("--- Exodus Chapter 20: Ten Commandments Data Quality Analysis Started ---")

        df_processed_missing = self.handle_missing_values()
        df_converted_types = self.convert_data_types(df_processed_missing)
        outliers_found = self.detect_outliers(df_converted_types)

        results = {
            'processed_df': df_converted_types,
            'outliers': outliers_found
        }

        print("\n--- 출애굽기 20장: 십계명 데이터 품질 분석 완료 ---")
        print("--- Exodus Chapter 20: Ten Commandments Data Quality Analysis Completed ---")
        return results

def demo_ten_commandments_quality_analyzer():
    """
    TenCommandmentsQualityAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for TenCommandmentsQualityAnalyzer class.
    """
    print("\n=== Ten Commandments Quality Analyzer Demo ===")
    analyzer = TenCommandmentsQualityAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_ten_commandments_quality_analyzer()
