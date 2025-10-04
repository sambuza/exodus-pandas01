import pandas as pd
import numpy as np

class DataSnapshotter:
    """
    데이터프레임의 특정 시점 상태를 스냅샷으로 기록하고 관리하는 클래스.
    데이터의 무결성과 재현성을 보장하는 데 활용됩니다.

    Class to record and manage the state of a DataFrame at specific points in time as snapshots.
    Utilized to ensure data integrity and reproducibility.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.snapshots = {}

    def create_snapshot(self, snapshot_name: str = None) -> pd.DataFrame:
        """
        현재 데이터프레임의 스냅샷을 생성하고 저장합니다.

        Creates and stores a snapshot of the current DataFrame.

        Args:
            snapshot_name (str): 스냅샷의 이름. 지정하지 않으면 타임스탬프가 사용됩니다.

        Returns:
            pd.DataFrame: 생성된 스냅샷 데이터프레임.
        """
        snapshot_df = self.df.copy()
        if snapshot_name is None:
            snapshot_name = pd.Timestamp.now().strftime("snapshot_%Y%m%d_%H%M%S")
        
        snapshot_df['snapshot_name'] = snapshot_name
        snapshot_df['snapshot_timestamp'] = pd.Timestamp.now()
        self.snapshots[snapshot_name] = snapshot_df
        
        print(f"DataSnapshotter: 스냅샷 '{snapshot_name}' 생성 완료.")
        return snapshot_df

    def get_snapshot(self, snapshot_name: str) -> pd.DataFrame:
        """
        지정된 이름의 스냅샷을 반환합니다.

        Returns the snapshot DataFrame with the specified name.

        Args:
            snapshot_name (str): 가져올 스냅샷의 이름.

        Returns:
            pd.DataFrame: 요청된 스냅샷 데이터프레임.
        """
        if snapshot_name in self.snapshots:
            print(f"DataSnapshotter: 스냅샷 '{snapshot_name}' 불러오기 완료.")
            return self.snapshots[snapshot_name].copy()
        else:
            print(f"경고: 스냅샷 '{snapshot_name}'을 찾을 수 없습니다.")
            return pd.DataFrame()

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 6),
        'value': [10, 20, 30, 40, 50],
        'status': ['active', 'inactive', 'active', 'pending', 'active']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    snapshotter = DataSnapshotter(sample_df)

    # 첫 번째 스냅샷 생성
    snapshot1 = snapshotter.create_snapshot("initial_state")
    print("\n첫 번째 스냅샷:")
    print(snapshot1)

    # 데이터 변경
    sample_df.loc[0, 'value'] = 15
    sample_df.loc[1, 'status'] = 'active'
    snapshotter.df = sample_df # 내부 데이터 업데이트

    # 두 번째 스냅샷 생성
    snapshot2 = snapshotter.create_snapshot("after_changes")
    print("\n두 번째 스냅샷:")
    print(snapshot2)

    # 스냅샷 불러오기
    loaded_snapshot = snapshotter.get_snapshot("initial_state")
    print("\n불러온 'initial_state' 스냅샷:")
    print(loaded_snapshot)
