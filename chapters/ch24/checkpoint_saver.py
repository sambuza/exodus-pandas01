import pandas as pd
import os

class CheckpointSaver:
    """
    데이터프레임을 CSV 또는 Parquet 파일로 체크포인트 저장하는 클래스.
    데이터의 무결성과 재현성을 보장하는 데 활용됩니다.

    Class to save DataFrame checkpoints to CSV or Parquet files.
    Utilized to ensure data integrity and reproducibility.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def save_checkpoint(self, filename: str, file_format: str = 'csv', index: bool = False) -> str:
        """
        데이터프레임을 지정된 형식의 파일로 저장합니다.

        Saves the DataFrame to a file in the specified format.

        Args:
            filename (str): 저장할 파일 이름 (확장자 포함).
            file_format (str): 'csv' 또는 'parquet'.
            index (bool): DataFrame 인덱스를 파일에 쓸지 여부.

        Returns:
            str: 저장된 파일의 전체 경로.
        """
        full_path = os.path.join(os.getcwd(), filename) # 현재 작업 디렉토리에 저장

        if file_format == 'csv':
            self.df.to_csv(full_path, index=index)
            print(f"CheckpointSaver: CSV 체크포인트 '{filename}' 저장 완료.")
        elif file_format == 'parquet':
            self.df.to_parquet(full_path, index=index)
            print(f"CheckpointSaver: Parquet 체크포인트 '{filename}' 저장 완료.")
        else:
            print(f"경고: 지원하지 않는 파일 형식 '{file_format}'입니다. 저장을 건너뜁니다.")
            return ""
        return full_path

    def load_checkpoint(self, filename: str, file_format: str = 'csv') -> pd.DataFrame:
        """
        지정된 형식의 체크포인트 파일을 불러옵니다.

        Loads a checkpoint file in the specified format.

        Args:
            filename (str): 불러올 파일 이름 (확장자 포함).
            file_format (str): 'csv' 또는 'parquet'.

        Returns:
            pd.DataFrame: 불러온 데이터프레임.
        """
        full_path = os.path.join(os.getcwd(), filename)

        if not os.path.exists(full_path):
            print(f"경고: 파일 '{filename}'을 찾을 수 없습니다.")
            return pd.DataFrame()

        if file_format == 'csv':
            loaded_df = pd.read_csv(full_path)
            print(f"CheckpointSaver: CSV 체크포인트 '{filename}' 불러오기 완료.")
        elif file_format == 'parquet':
            loaded_df = pd.read_parquet(full_path)
            print(f"CheckpointSaver: Parquet 체크포인트 '{filename}' 불러오기 완료.")
        else:
            print(f"경고: 지원하지 않는 파일 형식 '{file_format}'입니다. 불러오기를 건너뜁니다.")
            return pd.DataFrame()
        return loaded_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'value': [10, 20, 30, 40, 50],
        'status': ['A', 'B', 'C', 'D', 'E']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    saver = CheckpointSaver(sample_df)

    # CSV로 저장
    csv_file = "test_checkpoint.csv"
    saver.save_checkpoint(csv_file, file_format='csv')

    # Parquet으로 저장
    parquet_file = "test_checkpoint.parquet"
    saver.save_checkpoint(parquet_file, file_format='parquet')

    # 저장된 파일 불러오기
    loaded_csv_df = saver.load_checkpoint(csv_file, file_format='csv')
    print("\nCSV에서 불러온 데이터:")
    print(loaded_csv_df)

    loaded_parquet_df = saver.load_checkpoint(parquet_file, file_format='parquet')
    print("\nParquet에서 불러온 데이터:")
    print(loaded_parquet_df)

    # 생성된 파일 삭제 (정리)
    if os.path.exists(csv_file):
        os.remove(csv_file)
    if os.path.exists(parquet_file):
        os.remove(parquet_file)
