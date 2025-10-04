import pandas as pd
import numpy as np

class MetadataManager:
    """
    데이터프레임에 메타데이터 컬럼을 추가하고 관리하는 클래스.
    데이터에 대한 부가적인 정보를 제공하여 데이터의 이해도를 높입니다.

    Class to add and manage metadata columns in a DataFrame.
    Provides additional information about the data to enhance data understanding.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def add_metadata_columns(self, metadata_dict: dict) -> pd.DataFrame:
        """
        데이터프레임에 메타데이터 컬럼을 추가합니다.

        Adds metadata columns to the DataFrame.

        Args:
            metadata_dict (dict): 추가할 메타데이터 컬럼 이름과 값을 매핑하는 딕셔너리.
                                  예: {'source': 'Tabernacle Design', 'last_updated': pd.Timestamp.now()}

        Returns:
            pd.DataFrame: 메타데이터 컬럼이 추가된 데이터프레임.
        """
        for col, value in metadata_dict.items():
            self.df[col] = value
        print("MetadataManager: 메타데이터 컬럼 추가 완료.")
        return self.df

    def get_metadata_info(self) -> pd.DataFrame:
        """
        데이터프레임의 메타데이터 컬럼 정보를 반환합니다.
        (여기서는 메타데이터로 추가된 컬럼들을 보여주는 것으로 가정)

        Returns metadata column information of the DataFrame.
        (Assumes showing columns added as metadata here)

        Returns:
            pd.DataFrame: 메타데이터 컬럼을 포함하는 데이터프레임.
        """
        # 실제 메타데이터는 별도의 시스템에서 관리될 수 있으나, 여기서는 컬럼으로 추가된 것을 보여줌
        metadata_cols = [col for col in self.df.columns if col.startswith('meta_') or col in ['source', 'last_updated', 'description']]
        if not metadata_cols:
            print("경고: 메타데이터 컬럼이 데이터프레임에 없습니다.")
            return pd.DataFrame()
        
        print("MetadataManager: 메타데이터 컬럼 정보 반환 완료.")
        return self.df[metadata_cols]

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'component': ['Ark', 'Table', 'Lampstand'],
        'material': ['Gold', 'Acacia Wood', 'Gold'],
        'length_cubits': [2.5, 2.0, 1.5]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    manager = MetadataManager(sample_df)

    # 메타데이터 컬럼 추가
    metadata_to_add = {
        'source': 'Exodus 25',
        'last_updated': pd.Timestamp.now(),
        'description': '성막 주요 구성 요소'
    }
    df_with_metadata = manager.add_metadata_columns(metadata_to_add)
    print("\n메타데이터 컬럼 추가 후:")
    print(df_with_metadata)

    # 메타데이터 정보 확인
    metadata_info = manager.get_metadata_info()
    print("\n메타데이터 정보:")
    print(metadata_info)
