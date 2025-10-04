import pandas as pd
import numpy as np
import hashlib

class AnonymizationTechniques:
    """
    데이터프레임에 다양한 익명화 기법을 적용하는 클래스.
    해싱, 일반화(generalization) 등의 기법을 포함합니다.

    Class to apply various anonymization techniques to a DataFrame.
    Includes techniques like hashing and generalization.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_anonymization(self, columns_to_anonymize: list = None) -> pd.DataFrame:
        """
        지정된 컬럼에 익명화 기법을 적용합니다.

        Applies anonymization techniques to specified columns.

        Args:
            columns_to_anonymize (list): 익명화할 컬럼 이름 리스트. 기본값은 ['email', 'username'].

        Returns:
            pd.DataFrame: 익명화가 적용된 데이터프레임.
        """
        if columns_to_anonymize is None:
            columns_to_anonymize = ['email', 'username']

        anonymized_df = self.df.copy()

        for col in columns_to_anonymize:
            if col in anonymized_df.columns:
                if pd.api.types.is_string_dtype(anonymized_df[col]):
                    # 해싱을 통한 익명화
                    anonymized_df[col] = anonymized_df[col].apply(
                        lambda x: hashlib.sha256(x.encode()).hexdigest()
                    )
                elif pd.api.types.is_numeric_dtype(anonymized_df[col]):
                    # 일반화 (예: 범주화)
                    # 여기서는 간단히 평균값으로 대체하거나 범주화할 수 있음
                    # 예시: 1000단위로 묶기
                    anonymized_df[col] = (anonymized_df[col] // 1000) * 1000
            else:
                print(f"경고: 컬럼 '{col}'이 데이터프레임에 존재하지 않습니다.")

        print("AnonymizationTechniques: 익명화 기법 적용 완료.")
        return anonymized_df

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

    anonymizer = AnonymizationTechniques(sample_df)
    anonymized_df = anonymizer.apply_anonymization(columns_to_anonymize=['email', 'sensitive_info'])
    print("\n익명화된 데이터:")
    print(anonymized_df)
