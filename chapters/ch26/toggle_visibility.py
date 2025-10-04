import pandas as pd

class VisibilityToggler:
    """
    데이터프레임의 컬럼 표시/비표시를 토글하는 클래스.
    실제 데이터 삭제 없이 뷰를 조작하는 것을 시뮬레이션합니다.

    Class to toggle the visibility of columns in a DataFrame.
    Simulates manipulating the view without actually deleting data.
    """

    def __init__(self, df: pd.DataFrame):
        self.original_df = df.copy()
        self.current_df = df.copy()

    def hide_columns(self, columns_to_hide: list) -> pd.DataFrame:
        """
        지정된 컬럼들을 숨깁니다.

        Hides the specified columns.

        Args:
            columns_to_hide (list): 숨길 컬럼 이름 리스트.

        Returns:
            pd.DataFrame: 지정된 컬럼들이 숨겨진 데이터프레임.
        """
        hidden_df = self.current_df.drop(columns=columns_to_hide, errors='ignore')
        print(f"VisibilityToggler: 컬럼 {columns_to_hide} 숨김.")
        return hidden_df

    def show_columns(self, columns_to_show: list) -> pd.DataFrame:
        """
        지정된 컬럼들을 다시 표시합니다 (원본 데이터프레임에서 복원).

        Shows the specified columns again (restoring from the original DataFrame).

        Args:
            columns_to_show (list): 표시할 컬럼 이름 리스트.

        Returns:
            pd.DataFrame: 지정된 컬럼들이 표시된 데이터프레임.
        """
        # 원본 데이터프레임에서 해당 컬럼들을 가져와 현재 데이터프레임에 추가
        for col in columns_to_show:
            if col in self.original_df.columns and col not in self.current_df.columns:
                self.current_df[col] = self.original_df[col]
        print(f"VisibilityToggler: 컬럼 {columns_to_show} 표시.")
        return self.current_df

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

    toggler = VisibilityToggler(sample_df)
    hidden_df = toggler.hide_columns(['email', 'sensitive_info'])
    print("\n일부 컬럼 숨김:")
    print(hidden_df)

    shown_df = toggler.show_columns(['email'])
    print("\n'email' 컬럼 다시 표시:")
    print(shown_df)
