import pandas as pd

class CategoricalConverter:
    """
    데이터프레임의 특정 컬럼을 범주형(category) 데이터 타입으로 변환하는 클래스.
    메모리 효율성을 높이고 범주형 데이터에 특화된 연산을 가능하게 합니다.

    Class to convert specific columns of a DataFrame to categorical (category) data type.
    Enhances memory efficiency and enables operations specialized for categorical data.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def convert_to_category(self, columns_to_convert: list = None) -> pd.DataFrame:
        """
        지정된 컬럼들을 `category` dtype으로 변환합니다.

        Converts specified columns to `category` dtype.

        Args:
            columns_to_convert (list): `category` dtype으로 변환할 컬럼 이름 리스트.
                                       기본값은 ['offense_type', 'judgment_outcome'].

        Returns:
            pd.DataFrame: `category` dtype으로 변환된 컬럼을 포함하는 데이터프레임.
        """
        if columns_to_convert is None:
            columns_to_convert = ['offense_type', 'judgment_outcome']

        converted_df = self.df.copy()

        for col in columns_to_convert:
            if col in converted_df.columns:
                converted_df[col] = converted_df[col].astype('category')
            else:
                print(f"경고: 컬럼 '{col}'이 데이터프레임에 존재하지 않습니다.")

        print("CategoricalConverter: 컬럼을 category dtype으로 변환 완료.")
        return converted_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'offense_type': ['Theft', 'Assault', 'Theft', 'Dispute', 'Assault'],
        'damage_level': [5, 8, 6, 3, 7],
        'judgment_outcome': ['Guilty', 'Guilty', 'Not Guilty', 'Settled', 'Guilty']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)
    print(sample_df.dtypes)

    converter = CategoricalConverter(sample_df)
    converted_df = converter.convert_to_category()
    print("\n변환된 데이터:")
    print(converted_df)
    print(converted_df.dtypes)
