import pandas as pd
import numpy as np
from chapters.ch27.altar_data import AltarDataGenerator
from chapters.ch27.derived_variables import DerivedVariableCreator
from chapters.ch27.conditional_processing import ConditionalProcessor

class PreprocessingPipeline:
    """
    번제단 챕터의 데이터 생성, 파생변수 생성, 조건부 처리를 통합하는 파이프라인 클래스.
    데이터 전처리 과정을 효율적이고 일관되게 실행합니다.

    Pipeline class integrating data generation, derived variable creation, and conditional processing for the Altar chapter.
    Executes data preprocessing steps efficiently and consistently.
    """

    def __init__(self, initial_df: pd.DataFrame = None):
        self.initial_df = initial_df

    def run_pipeline(self) -> pd.DataFrame:
        """
        전체 전처리 파이프라인을 실행합니다.
        초기 데이터가 제공되지 않으면 AltarDataGenerator를 사용하여 생성합니다.

        Executes the entire preprocessing pipeline.
        If initial data is not provided, it generates it using AltarDataGenerator.

        Returns:
            pd.DataFrame: 모든 전처리 단계가 적용된 최종 데이터프레임.
        """
        if self.initial_df is None:
            print("PreprocessingPipeline: 초기 데이터가 없어 AltarDataGenerator를 사용하여 데이터를 생성합니다.")
            data_generator = AltarDataGenerator()
            df = data_generator.generate_altar_data()
        else:
            df = self.initial_df.copy()

        # 1. 파생변수 생성
        derived_creator = DerivedVariableCreator(df)
        df = derived_creator.create_variables()

        # 2. 조건부 처리
        conditional_processor = ConditionalProcessor(df)
        df = conditional_processor.apply_conditions()

        print("PreprocessingPipeline: 전체 파이프라인 실행 완료.")
        return df

if __name__ == "__main__":
    # 파이프라인 실행 (초기 데이터 없이)
    print("--- 초기 데이터 없이 파이프라인 실행 ---")
    pipeline = PreprocessingPipeline()
    final_df_no_initial = pipeline.run_pipeline()
    print("\n최종 데이터 (초기 데이터 없이):")
    print(final_df_no_initial)

    # 초기 데이터를 제공하여 파이프라인 실행
    print("\n--- 초기 데이터를 제공하여 파이프라인 실행 ---")
    initial_data = {
        'id': range(1, 4),
        'value1': [10, 50, 90],
        'value2': [5, 25, 45],
        'category': ['A', 'B', 'C']
    }
    initial_df = pd.DataFrame(initial_data)
    print("제공된 초기 데이터:")
    print(initial_df)

    pipeline_with_initial = PreprocessingPipeline(initial_df)
    final_df_with_initial = pipeline_with_initial.run_pipeline()
    print("\n최종 데이터 (초기 데이터 제공):")
    print(final_df_with_initial)
