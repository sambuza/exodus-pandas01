import pandas as pd
import numpy as np

class DataVersionReverter:
    """
    데이터프레임의 변경 이력을 기반으로 특정 버전으로 되돌리는(롤백) 클래스.
    잘못된 변경 사항으로부터 데이터를 복구하는 데 활용됩니다.

    Class to revert (rollback) a DataFrame to a specific version based on its change history.
    Utilized to recover data from incorrect changes.
    """

    def __init__(self, history: list):
        self.history = history

    def revert_to_version(self, version: int) -> pd.DataFrame:
        """
        지정된 버전의 데이터프레임 상태로 되돌립니다.

        Reverts the DataFrame to the state of the specified version.

        Args:
            version (int): 되돌릴 버전 번호.

        Returns:
            pd.DataFrame: 지정된 버전의 데이터프레임.
        """
        for entry in self.history:
            if entry['version'] == version:
                print(f"DataVersionReverter: 버전 {version}으로 롤백 완료.")
                return entry['data_snapshot'].copy()
        
        print(f"경고: 버전 {version}을 찾을 수 없습니다. 롤백을 수행할 수 없습니다.")
        return pd.DataFrame()

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': range(1, 4),
        'value': [10, 20, 30],
        'status': ['A', 'B', 'C']
    }
    sample_df = pd.DataFrame(data)

    # 변경 이력 생성 (ChangeHistoryTracker와 유사)
    history = []
    current_df = sample_df.copy()
    current_df['version'] = 0
    history.append({'timestamp': pd.Timestamp.now(), 'description': 'Initial state', 'version': 0, 'data_snapshot': current_df.copy()})

    # 버전 1 변경
    current_df.loc[0, 'value'] = 15
    current_df['version'] = 1
    history.append({'timestamp': pd.Timestamp.now(), 'description': 'Changed value', 'version': 1, 'data_snapshot': current_df.copy()})

    # 버전 2 변경
    current_df.loc[1, 'status'] = 'X'
    current_df['version'] = 2
    history.append({'timestamp': pd.Timestamp.now(), 'description': 'Changed status', 'version': 2, 'data_snapshot': current_df.copy()})

    print("현재 데이터 (버전 2):")
    print(current_df)

    reverter = DataVersionReverter(history)

    # 버전 0으로 롤백
    rolled_back_df = reverter.revert_to_version(0)
    print("\n버전 0으로 롤백 후:")
    print(rolled_back_df)

    # 버전 1로 롤백
    rolled_back_df_v1 = reverter.revert_to_version(1)
    print("\n버전 1로 롤백 후:")
    print(rolled_back_df_v1)
