import pandas as pd
import unicodedata

class StringNormalizer:
    """
    데이터프레임의 문자열 컬럼에 유니코드 정규화(`unicodedata.normalize`)를 적용하는 클래스.
    텍스트 데이터의 다양한 표현을 통일하여 분석의 일관성을 확보합니다.

    Class to apply Unicode normalization (`unicodedata.normalize`) to string columns of a DataFrame.
    Ensures consistency in text analysis by unifying various representations of text data.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_string_normalization(self, column: str, form: str = 'NFKC') -> pd.DataFrame:
        """
        지정된 문자열 컬럼에 유니코드 정규화를 적용합니다.

        Applies Unicode normalization to the specified string column.

        Args:
            column (str): 정규화할 문자열 컬럼 이름.
            form (str): 유니코드 정규화 형식 ('NFC', 'NFKC', 'NFD', 'NFKD').

        Returns:
            pd.DataFrame: 문자열이 정규화된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_string_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 문자열 타입이 아닙니다. 문자열 정규화를 건너뜁니다.")
            return self.df

        normalized_df = self.df.copy()
        normalized_df[f'{column}_normalized'] = normalized_df[column].apply(lambda x: unicodedata.normalize(form, str(x)) if pd.notna(x) else x)
        print(f"StringNormalizer: 컬럼 '{column}'에 문자열 정규화 적용 완료 (형식: {form}).")
        return normalized_df

    def apply_text_cleaning(self, column: str) -> pd.DataFrame:
        """
        지정된 문자열 컬럼에 기본적인 텍스트 클리닝(소문자 변환, 공백 제거)을 적용합니다.

        Applies basic text cleaning (lowercase conversion, whitespace removal) to the specified string column.

        Args:
            column (str): 클리닝할 문자열 컬럼 이름.

        Returns:
            pd.DataFrame: 텍스트 클리닝이 적용된 컬럼이 추가된 데이터프레임.
        """
        if column not in self.df.columns or not pd.api.types.is_string_dtype(self.df[column]):
            print(f"경고: 컬럼 '{column}'이 존재하지 않거나 문자열 타입이 아닙니다. 텍스트 클리닝을 건너뜁니다.")
            return self.df

        cleaned_df = self.df.copy()
        cleaned_df[f'{column}_cleaned'] = normalized_df[column].apply(lambda x: str(x).strip().lower() if pd.notna(x) else x)
        print(f"StringNormalizer: 컬럼 '{column}'에 텍스트 클리닝 적용 완료.")
        return cleaned_df

if __name__ == "__main__":
    # 샘플 데이터 생성 (다양한 문자열 표현 포함)
    data = {
        'id': range(1, 6),
        'text_col': ['Hello World', 'hello world!', 'HELLO WORLD', 'Hello  World', 'Héllö Wörld']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    normalizer = StringNormalizer(sample_df)

    # 유니코드 정규화 (NFKC) 적용
    normalized_unicode_df = normalizer.apply_string_normalization('text_col', form='NFKC')
    print("\n유니코드 정규화 (NFKC) 후:")
    print(normalized_unicode_df)

    # 텍스트 클리닝 적용
    cleaned_text_df = normalizer.apply_text_cleaning('text_col')
    print("\n텍스트 클리닝 후:")
    print(cleaned_text_df)
