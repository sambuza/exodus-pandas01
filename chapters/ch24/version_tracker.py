import pandas as pd
import numpy as np

class VersionTracker:
    """
    데이터프레임의 변경 이력을 추적하고 버전 관리하는 클래스.
    'version' 컬럼을 추가하고 데이터 변경 시 버전을 업데이트합니다.

    Class to track and manage the change history of a DataFrame.
    Adds a 'version' column and updates the version upon data modification.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        if 'version' not in self.df.columns:
            self.df['version'] = 0 # 초기 버전
        self.history = [] # 변경 이력 저장

    def record_change(self, description: str = "Data modified") -> None:
        """
        현재 데이터프레임의 상태와 변경 내용을 이력에 기록합니다.

        Records the current state of the DataFrame and the change description in history.

        Args:
            description (str): 변경 내용에 대한 설명.
        """
        self.history.append({
            'timestamp': pd.Timestamp.now(),
            'description': description,
            'version': self.df['version'].max() if not self.df.empty else 0,
            'data_snapshot': self.df.copy() # 변경 전 데이터 스냅샷
        })
        print(f"VersionTracker: 변경 이력 기록 완료 - '{description}' (버전: {self.df['version'].max() if not self.df.empty else 0}).")

    def update_version(self, new_df: pd.DataFrame, description: str = "Data updated") -> pd.DataFrame:
        """
        데이터프레임을 업데이트하고 'version' 컬럼을 증가시킵니다.

        Updates the DataFrame and increments the 'version' column.

        Args:
            new_df (pd.DataFrame): 업데이트된 새로운 데이터프레임.
            description (str): 변경 내용에 대한 설명.

        Returns:
            pd.DataFrame: 버전이 업데이트된 데이터프레임.
        """
        self.record_change(f"Before update: {description}") # 변경 전 상태 기록
        
        current_version = self.df['version'].max() if not self.df.empty else 0
        updated_df = new_df.copy()
        updated_df['version'] = current_version + 1
        self.df = updated_df # 내부 데이터프레임 업데이트
        
        self.record_change(f"After update: {description}") # 변경 후 상태 기록
        print(f"VersionTracker: 데이터 버전 업데이트 완료 (새 버전: {self.df['version'].max()}).")
        return self.df

    def get_history(self) -> list:
        """
        기록된 변경 이력을 반환합니다.

        Returns the recorded change history.

        Returns:
            list: 변경 이력 리스트.
        """
        return self.history

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 4),
        'value': [10, 20, 30],
        'status': ['A', 'B', 'C']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    tracker = VersionTracker(sample_df)
    print("\n초기 데이터 (버전 0):")
    print(tracker.df)

    # 데이터 변경 및 버전 업데이트
    modified_df = sample_df.copy()
    modified_df.loc[0, 'value'] = 15
    modified_df.loc[1, 'status'] = 'X'
    tracker.update_version(modified_df, "Changed value and status")
    print("\n데이터 변경 후 (버전 1):")
    print(tracker.df)

    # 또 다른 변경
    another_modified_df = tracker.df.copy()
    another_modified_df.loc[2, 'value'] = 35
    tracker.update_version(another_modified_df, "Changed another value")
    print("\n데이터 변경 후 (버전 2):")
    print(tracker.df)

    print("\n변경 이력:")
    for entry in tracker.get_history():
        print(f"- {entry['timestamp']} (버전 {entry['version']}): {entry['description']}")
        # print(entry['data_snapshot']) # 스냅샷 데이터도 확인 가능
