
import pandas as pd
import numpy as np
from .new_commandment_data import NewCommandmentDataGenerator

class NewCommandmentQualityAnalyzer:
    """
    요한복음 13장의 새 계명(사랑) 데이터를 데이터 품질 관점(결측치, 타입, 이상치)에서 분석하는 클래스.
    사랑이라는 최상의 품질 기준으로 깨끗하고 신뢰할 수 있는 데이터를 구축하는 과정을 탐구합니다.

    Class to analyze New Commandment (love) data from John Chapter 13 from a data quality perspective (missing values, types, outliers).
    Explores the process of building clean and reliable data based on love as the highest quality standard.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = NewCommandmentDataGenerator()
        self.new_commandment_df = self.data_generator.generate_new_commandment_data()

    def handle_missing_values(self):
        """
        새 계명 데이터의 결측치를 처리합니다.
        Handles missing values in the New Commandment data.

        - KJV: John 13:34 - "A new commandment I give unto you, That ye love one another..."
        - ESV: John 13:34 - "A new commandment I give to you, that you love one another..."
        - 개역한글: 요한복음 13:34 - "새 계명을 너희에게 주노니 서로 사랑하라..."
        """
        print("\n📊 === 새 계명 데이터 결측치 처리 (Handling Missing Values in New Commandment Data) ===")
        print("'love_level'과 'spiritual_impact_score'의 결측치를 처리하여 데이터의 완전성을 확보합니다.")
        print("Ensuring data completeness by handling missing values in 'love_level' and 'spiritual_impact_score'.")

        df_processed = self.new_commandment_df.copy()

        # 결측치 확인
        print("\n--- 원본 데이터 결측치 (Original Data Missing Values) ---")
        print(df_processed.isnull().sum())

        # 'love_level'의 결측치를 중앙값으로 채우기
        df_processed['love_level'] = pd.to_numeric(df_processed['love_level'], errors='coerce') # 잘못된 타입 먼저 처리
        df_processed['love_level'] = df_processed['love_level'].fillna(df_processed['love_level'].median())

        # 'spiritual_impact_score'의 결측치를 0으로 채우기
        df_processed['spiritual_impact_score'] = pd.to_numeric(df_processed['spiritual_impact_score'], errors='coerce') # 잘못된 타입 먼저 처리
        df_processed['spiritual_impact_score'] = df_processed['spiritual_impact_score'].fillna(0)

        print("\n--- 결측치 처리 후 데이터 (Data After Handling Missing Values) ---")
        print(df_processed[['action_id', 'love_level', 'spiritual_impact_score']].to_string(index=False))
        print("\n--- 결측치 처리 후 결측치 (Missing Values After Handling) ---")
        print(df_processed.isnull().sum())

        print("\n💡 통찰 (Insight): `fillna()`는 사랑이라는 새 계명 실천에서 우리의 부족함을 채워 데이터의 완전성을 확보하게 합니다.")
        print("Insight: `fillna()` ensures data completeness by filling our deficiencies in practicing the New Commandment of love.")
        return df_processed

    def convert_data_types(self, df_processed):
        """
        새 계명 데이터의 데이터 타입을 올바르게 변환합니다.
        Converts data types in the New Commandment data to the correct format.

        - KJV: John 13:35 - "By this shall all men know that ye are my disciples, if ye have love one to another."
        - ESV: John 13:35 - "By this all people will know that you are my disciples, if you have love for one another."
        - 개역한글: 요한복음 13:35 - "너희가 서로 사랑하면 이로써 모든 사람이 너희가 내 제자인 줄 알리라"
        """
        print("\n📈 === 새 계명 데이터 타입 변환 (Converting Data Types in New Commandment Data) ===")
        print("'love_level'과 'spiritual_impact_score'를 숫자 타입으로 변환합니다.")
        print("Converting 'love_level' and 'spiritual_impact_score' to numeric types.")

        df_converted = df_processed.copy()

        # 잘못된 타입이 있는 'love_level'을 숫자 타입으로 변환 (errors='coerce'로 변환 불가 값은 NaN으로)
        df_converted['love_level'] = pd.to_numeric(df_converted['love_level'], errors='coerce')
        df_converted['spiritual_impact_score'] = pd.to_numeric(df_converted['spiritual_impact_score'], errors='coerce')

        # 변환 후 생긴 NaN은 다시 중앙값으로 채우기 (선택적)
        df_converted['love_level'] = df_converted['love_level'].fillna(df_converted['love_level'].median())
        df_converted['spiritual_impact_score'] = df_converted['spiritual_impact_score'].fillna(df_converted['spiritual_impact_score'].median())

        # 정수 타입으로 변환
        df_converted['love_level'] = df_converted['love_level'].astype(int)
        df_converted['spiritual_impact_score'] = df_converted['spiritual_impact_score'].astype(int)

        print("\n--- 변환 후 데이터 타입 (Data Types After Conversion) ---")
        print(df_converted.dtypes)
        print("\n--- 변환 후 데이터 (Data After Conversion) ---")
        print(df_converted[['action_id', 'love_level', 'spiritual_impact_score']].to_string(index=False))

        print("\n💡 통찰 (Insight): `astype()`은 사랑이라는 새 계명 실천이 가져오는 영적 영향력을 정확하게 측정하여 분석의 유효성을 확보하게 합니다.")
        print("Insight: `astype()` ensures the validity of analysis by accurately measuring the spiritual impact of practicing the New Commandment of love.")
        return df_converted

    def detect_outliers(self, df_converted):
        """
        새 계명 데이터에서 이상치를 탐지합니다.
        Detects outliers in the New Commandment data.

        - KJV: John 15:12 - "This is my commandment, That ye love one another, as I have loved you."
        - ESV: John 15:12 - "This is my commandment, that you love one another as I have loved you."
        - 개역한글: 요한복음 15:12 - "내 계명은 곧 내가 너희를 사랑한 것같이 너희도 서로 사랑하라 하는 이것이니라"
        """
        print("\n📉 === 새 계명 데이터 이상치 탐지 (Outlier Detection in New Commandment Data) ===")
        print("'love_level'에서 평균과 크게 벗어나는 이상치를 탐지하여 사랑 부족의 극단적인 경우를 식별합니다.")
        print("Detecting outliers in 'love_level' that deviate significantly from the mean to identify extreme cases of lack of love.")

        # IQR을 이용한 이상치 탐지
        Q1 = df_converted['love_level'].quantile(0.25)
        Q3 = df_converted['love_level'].quantile(0.75)
        IQR = Q3 - Q1
        outlier_threshold_lower = Q1 - 1.5 * IQR
        outlier_threshold_upper = Q3 + 1.5 * IQR

        outliers = df_converted[(df_converted['love_level'] < outlier_threshold_lower) |
                                  (df_converted['love_level'] > outlier_threshold_upper)]

        print("\n--- 'love_level' 이상치 (Outliers in 'love_level') ---")
        print(outliers[['action_id', 'action_type', 'love_level']].to_string(index=False))

        print("\n💡 통찰 (Insight): 이상치 탐지는 사랑 실천에서 극단적인 부족이나 과도한 자기희생을 식별하여 영적 삶의 균형을 점검하게 합니다.")
        print("Insight: Outlier detection helps identify extreme deficiencies or excessive self-sacrifice in practicing love, prompting a check on spiritual balance.")
        return outliers

    def run_all_analyses(self) -> dict:
        """
        모든 데이터 품질 분석을 실행하고 결과를 반환합니다.
        Runs all data quality analyses and returns the results.
        """
        print("\n--- 요한복음 13장: 새 계명 데이터 품질 분석 시작 ---")
        print("--- John Chapter 13: New Commandment Data Quality Analysis Started ---")

        df_processed_missing = self.handle_missing_values()
        df_converted_types = self.convert_data_types(df_processed_missing)
        outliers_found = self.detect_outliers(df_converted_types)

        results = {
            'processed_df': df_converted_types,
            'outliers': outliers_found
        }

        print("\n--- 요한복음 13장: 새 계명 데이터 품질 분석 완료 ---")
        print("--- John Chapter 13: New Commandment Data Quality Analysis Completed ---")
        return results

def demo_new_commandment_quality_analyzer():
    """
    NewCommandmentQualityAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for NewCommandmentQualityAnalyzer class.
    """
    print("\n=== New Commandment Quality Analyzer Demo ===")
    analyzer = NewCommandmentQualityAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_new_commandment_quality_analyzer()
