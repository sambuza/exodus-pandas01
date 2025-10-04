import pandas as pd
import numpy as np

class DtypeTuner:
    """
    데이터프레임의 데이터 타입(`dtype`)을 최적화하여 메모리 사용량을 줄이고
    데이터 처리 속도를 개선하는 클래스.

    Class to optimize a DataFrame's data types (`dtype`) to reduce memory usage and
    improve data processing speed.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def optimize_dtypes(self) -> pd.DataFrame:
        """
        데이터프레임의 숫자형 컬럼을 더 효율적인 `dtype`으로 변환하고,
        객체형 컬럼을 `category` dtype으로 변환하여 메모리를 최적화합니다.

        Converts numerical columns of the DataFrame to more efficient `dtype`s and
        object-type columns to `category` dtype to optimize memory.

        Returns:
            pd.DataFrame: 데이터 타입이 최적화된 데이터프레임.
        """
        optimized_df = self.df.copy()
        original_memory_usage = optimized_df.memory_usage(deep=True).sum()
        
        for col in optimized_df.columns:
            col_type = optimized_df[col].dtype

            if str(col_type)[:3] == 'int':
                # 정수형 최적화
                min_val = optimized_df[col].min()
                max_val = optimized_df[col].max()
                if min_val >= np.iinfo(np.int8).min and max_val <= np.iinfo(np.int8).max:
                    optimized_df[col] = optimized_df[col].astype(np.int8)
                elif min_val >= np.iinfo(np.int16).min and max_val <= np.iinfo(np.int16).max:
                    optimized_df[col] = optimized_df[col].astype(np.int16)
                elif min_val >= np.iinfo(np.int32).min and max_val <= np.iinfo(np.int32).max:
                    optimized_df[col] = optimized_df[col].astype(np.int32)
            elif str(col_type)[:5] == 'float':
                # 실수형 최적화 (float32로 다운캐스팅)
                optimized_df[col] = optimized_df[col].astype(np.float32)
            elif col_type == 'object':
                # 문자열 컬럼을 category로 변환 (고유값이 적을 경우)
                num_unique_values = len(optimized_df[col].unique())
                num_total_values = len(optimized_df[col])
                if num_unique_values / num_total_values < 0.5: # 고유값 비율이 50% 미만일 때 category로 변환
                    optimized_df[col] = optimized_df[col].astype('category')
        
        new_memory_usage = optimized_df.memory_usage(deep=True).sum()
        print(f"DtypeTuner: 데이터 타입 최적화 완료. 메모리 절감율: {(1 - new_memory_usage / original_memory_usage) * 100:.2f}%")
        return optimized_df

if __name__ == "__main__":
    # 샘플 데이터 생성 (다양한 데이터 타입 포함)
    data = {
        'int_col': np.random.randint(0, 200, size=1000), # int8 범위 초과
        'small_int_col': np.random.randint(0, 100, size=1000), # int8 범위
        'float_col': np.random.rand(1000) * 1000,
        'object_col': np.random.choice(['A', 'B', 'C', 'D'], size=1000),
        'bool_col': np.random.choice([True, False], size=1000)
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터 정보:")
    sample_df.info(memory_usage='deep')

    tuner = DtypeTuner(sample_df)
    optimized_df = tuner.optimize_dtypes()

    print("\n최적화된 데이터 정보:")
    optimized_df.info(memory_usage='deep')
