import pandas as pd
import os

class ExcelIOHandler:
    """
    데이터프레임을 Excel 파일로 읽고 쓰는 클래스.
    `to_excel()`와 `read_excel()` 메서드를 활용하여 Excel 파일 입출력을 처리합니다.

    Class to read and write DataFrames to/from Excel files.
    Handles Excel file input/output using `to_excel()` and `read_excel()` methods.
    """

    def __init__(self, df: pd.DataFrame = None):
        self.df = df

    def save_data(self, filename: str, index: bool = False, **kwargs) -> str:
        """
        데이터프레임을 Excel 파일로 저장합니다.

        Saves the DataFrame to an Excel file.

        Args:
            filename (str): 저장할 파일 이름.
            index (bool): DataFrame 인덱스를 파일에 쓸지 여부.
            **kwargs: `pd.DataFrame.to_excel()`에 전달할 추가 인자.

        Returns:
            str: 저장된 파일의 전체 경로.
        """
        if self.df is None:
            print("경고: 저장할 데이터프레임이 없습니다. 저장을 건너뜁니다.")
            return ""
        
        full_path = os.path.join(os.getcwd(), filename)
        self.df.to_excel(full_path, index=index, **kwargs)
        print(f"ExcelIOHandler: Excel 파일 '{filename}' 저장 완료.")
        return full_path

    def load_data(self, filename: str, **kwargs) -> pd.DataFrame:
        """
        Excel 파일에서 데이터를 불러와 데이터프레임으로 반환합니다.

        Loads data from an Excel file and returns it as a DataFrame.

        Args:
            filename (str): 불러올 파일 이름.
            **kwargs: `pd.read_excel()`에 전달할 추가 인자.

        Returns:
            pd.DataFrame: 불러온 데이터프레임.
        """
        full_path = os.path.join(os.getcwd(), filename)
        if not os.path.exists(full_path):
            print(f"경고: 파일 '{filename}'을 찾을 수 없습니다. 빈 데이터프레임을 반환합니다.")
            return pd.DataFrame()

        loaded_df = pd.read_excel(full_path, **kwargs)
        print(f"ExcelIOHandler: Excel 파일 '{filename}' 불러오기 완료.")
        return loaded_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'score': [85, 92, 78, 92, 85]
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    handler = ExcelIOHandler(sample_df)

    # Excel로 저장
    excel_file = "test_data.xlsx"
    saved_path = handler.save_data(excel_file)

    # Excel에서 불러오기
    loaded_df = handler.load_data(excel_file)
    print("\nExcel에서 불러온 데이터:")
    print(loaded_df)

    # 생성된 파일 삭제 (정리)
    if os.path.exists(saved_path):
        os.remove(saved_path)
