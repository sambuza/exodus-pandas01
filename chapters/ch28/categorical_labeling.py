import pandas as pd

class CategoricalLabeler:
    """
    데이터프레임의 특정 컬럼에 범주형 라벨링을 적용하는 클래스.
    데이터의 의미를 명확히 하고 효율적인 분석을 돕습니다.

    Class to apply categorical labeling to specific columns of a DataFrame.
    Clarifies data meaning and aids efficient analysis.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def apply_categorical_labels(self, columns_to_label: list = None) -> pd.DataFrame:
        """
        지정된 컬럼들을 범주형(Categorical) 데이터 타입으로 변환합니다.

        Converts specified columns to Categorical data type.

        Args:
            columns_to_label (list): 범주형으로 변환할 컬럼 이름 리스트. 기본값은 ['garment_type', 'status'].

        Returns:
            pd.DataFrame: 범주형 라벨링이 적용된 데이터프레임.
        """
        if columns_to_label is None:
            columns_to_label = ['garment_type', 'status']

        labeled_df = self.df.copy()

        for col in columns_to_label:
            if col in labeled_df.columns:
                labeled_df[col] = labeled_df[col].astype('category')
            else:
                print(f"경고: 컬럼 '{col}'이 데이터프레임에 존재하지 않습니다.")

        print("CategoricalLabeler: 범주형 라벨링 적용 완료.")
        return labeled_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'priest_id': range(1, 6),
        'garment_type': ['Ephod', 'Robe', 'Ephod', 'Tunic', 'Robe'],
        'material_quality': [7, 8, 6, 9, 7],
        'status': ['Clean', 'Worn', 'New', 'Clean', 'Worn']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)
    print(sample_df.dtypes)

    labeler = CategoricalLabeler(sample_df)
    labeled_df = labeler.apply_categorical_labels()
    print("\n범주형 라벨링 적용된 데이터:")
    print(labeled_df)
    print(labeled_df.dtypes)
