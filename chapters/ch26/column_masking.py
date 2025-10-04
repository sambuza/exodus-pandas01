import pandas as pd
import numpy as np

class ColumnMaskingProcessor:
    """
    데이터프레임의 특정 컬럼을 마스킹하는 클래스.
    민감한 정보를 부분적으로 가리거나 대체합니다.

    Class to mask specific columns of a DataFrame.
    Partially hides or replaces sensitive information.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_masking(self, columns_to_mask: list = None, mask_char: str = '*', num_chars_to_show: int = 4) -> pd.DataFrame:
        """
        지정된 컬럼에 마스킹을 적용합니다.

        Applies masking to specified columns.

        Args:
            columns_to_mask (list): 마스킹할 컬럼 이름 리스트. 기본값은 ['email', 'sensitive_info'].
            mask_char (str): 마스킹에 사용할 문자.
            num_chars_to_show (int): 마스킹되지 않고 보여줄 문자의 수 (문자열 컬럼의 경우).

        Returns:
            pd.DataFrame: 마스킹이 적용된 데이터프레임.
        """
        if columns_to_mask is None:
            columns_to_mask = ['email', 'sensitive_info']

        masked_df = self.df.copy()

        for col in columns_to_mask:
            if col in masked_df.columns:
                if pd.api.types.is_string_dtype(masked_df[col]):
                    masked_df[col] = masked_df[col].apply(
                        lambda x: x[:num_chars_to_show] + mask_char * (len(x) - num_chars_to_show) if len(x) > num_chars_to_show else mask_char * len(x)
                    )
                elif pd.api.types.is_numeric_dtype(masked_df[col]):
                    # 숫자형 컬럼은 단순히 0으로 대체하거나 특정 값으로 마스킹
                    masked_df[col] = masked_df[col].apply(lambda x: 0 if not pd.isna(x) else np.nan)
            else:
                print(f"경고: 컬럼 '{col}'이 데이터프레임에 존재하지 않습니다.")

        print("ColumnMaskingProcessor: 컬럼 마스킹 적용 완료.")
        return masked_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'user_id': range(1, 6),
        'username': [f'user_{i}' for i in range(1, 6)],
        'email': [f'user{i}@example.com' for i in range(1, 6)],
        'sensitive_info': np.random.randint(1000, 9999, size=5),
        'public_data': np.random.rand(5) * 100
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    processor = ColumnMaskingProcessor(sample_df)
    masked_df = processor.apply_masking(columns_to_mask=['email', 'sensitive_info'])
    print("\n마스킹된 데이터:")
    print(masked_df)
