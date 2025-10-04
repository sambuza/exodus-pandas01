import pandas as pd
import numpy as np

class ChangeHistoryTracker:
    """
    데이터프레임의 변경 이력을 추적하고 관리하는 클래스.
    'version' 컬럼을 추가하고 데이터 변경 시 버전을 업데이트하며,
    이전 버전의 데이터를 저장합니다.

    Class to track and manage the change history of a DataFrame.
    Adds a 'version' column, updates the version upon data modification, and
    stores previous versions of the data.
    """

    def __init__(self, initial_df: pd.DataFrame):
        self.history = []
        self.current_df = initial_df.copy()
        if 'version' not in self.current_df.columns:
            self.current_df['version'] = 0
        self._record_current_state("Initial state")

    def _record_current_state(self, description: str) -> None:
        """내부적으로 현재 데이터프레임 상태를 이력에 기록합니다."""
        self.history.append({
            'timestamp': pd.Timestamp.now(),
            'description': description,
            'version': self.current_df['version'].max(),
            'data_snapshot': self.current_df.copy()
        })

    def add_change(self, new_df: pd.DataFrame, description: str = "Data modified") -> pd.DataFrame:
        """
        데이터프레임을 업데이트하고 'version' 컬럼을 증가시킵니다.
        이전 상태를 기록한 후 새로운 상태를 저장합니다.

        Updates the DataFrame and increments the 'version' column.
        Records the previous state before saving the new state.

        Args:
            new_df (pd.DataFrame): 업데이트된 새로운 데이터프레임.
            description (str): 변경 내용에 대한 설명.

        Returns:
            pd.DataFrame: 버전이 업데이트된 데이터프레임.
        """
        # 현재 버전을 기록
        current_version = self.current_df['version'].max()
        
        # 새로운 데이터프레임에 버전 업데이트
        updated_df = new_df.copy()
        updated_df['version'] = current_version + 1
        
        self.current_df = updated_df # 내부 데이터프레임 업데이트
        self._record_current_state(description) # 새로운 상태 기록
        
        print(f"ChangeHistoryTracker: 데이터 버전 업데이트 완료 (새 버전: {self.current_df['version'].max()}).")
        return self.current_df

    def get_current_data(self) -> pd.DataFrame:
        """현재 데이터프레임 상태를 반환합니다."""
        return self.current_df.copy()

    def get_history(self) -> list:
        """기록된 변경 이력을 반환합니다."""
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

    tracker = ChangeHistoryTracker(sample_df)
    print("\n초기 데이터 (버전 0):")
    print(tracker.get_current_data())

    # 데이터 변경 및 버전 업데이트
    modified_df = sample_df.copy()
    modified_df.loc[0, 'value'] = 15
    modified_df.loc[1, 'status'] = 'X'
    tracker.add_change(modified_df, "Changed value and status")
    print("\n데이터 변경 후 (버전 1):")
    print(tracker.get_current_data())

    # 또 다른 변경
    another_modified_df = tracker.get_current_data().copy()
    another_modified_df.loc[2, 'value'] = 35
    tracker.add_change(another_modified_df, "Changed another value")
    print("\n데이터 변경 후 (버전 2):")
    print(tracker.get_current_data())

    print("\n변경 이력:")
    for entry in tracker.get_history():
        print(f"- {entry['timestamp']} (버전 {entry['version']}): {entry['description']}")
        # print(entry['data_snapshot']) # 스냅샷 데이터도 확인 가능
