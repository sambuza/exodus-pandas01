import pandas as pd
import numpy as np

class AuditLogger:
    """
    데이터 변경 이력을 기록하는 감사 로그(Audit Log)를 생성하고 관리하는 클래스.
    데이터의 투명성을 확보하고 문제 발생 시 원인을 추적하는 데 활용됩니다.

    Class to create and manage audit logs that record data change history.
    Utilized to ensure data transparency and track the root cause of issues.
    """

    def __init__(self):
        self.logs = []

    def log_action(self, user: str, action: str, description: str, data_state_info: any = None) -> None:
        """
        데이터 변경 또는 중요한 작업에 대한 로그를 기록합니다.

        Records a log for data changes or important actions.

        Args:
            user (str): 작업을 수행한 사용자.
            action (str): 수행된 작업 (예: 'Data_Update', 'Data_Delete', 'Data_Load').
            description (str): 작업에 대한 상세 설명.
            data_state_info (any): 작업 당시 데이터의 상태 정보 (예: DataFrame.shape, version).
        """
        self.logs.append({
            'timestamp': pd.Timestamp.now(),
            'user': user,
            'action': action,
            'description': description,
            'data_state_info': str(data_state_info) # 문자열로 저장
        })
        print(f"AuditLogger: 로그 기록 완료 - 사용자: {user}, 작업: {action}, 설명: {description}.")

    def get_logs(self) -> pd.DataFrame:
        """
        기록된 모든 감사 로그를 데이터프레임 형태로 반환합니다.

        Returns all recorded audit logs as a DataFrame.

        Returns:
            pd.DataFrame: 감사 로그 데이터프레임.
        """
        if not self.logs:
            return pd.DataFrame(columns=['timestamp', 'user', 'action', 'description', 'data_state_info'])
        return pd.DataFrame(self.logs)

if __name__ == "__main__":
    # 감사 로그 초기화
    audit_logger = AuditLogger()

    # 샘플 데이터 변경 시뮬레이션 및 로그 기록
    audit_logger.log_action('Admin', 'Data_Load', 'Initial dataset loaded', {'shape': (100, 5), 'version': 0})
    audit_logger.log_action('User_A', 'Data_Update', 'Updated user profile for ID 123', {'user_id': 123, 'field': 'email'})
    audit_logger.log_action('System', 'Data_Backup', 'Daily backup completed', {'status': 'success'})

    # 감사 로그 확인
    logs_df = audit_logger.get_logs()
    print("\n--- 감사 로그 기록 ---\n")
    print(logs_df)
