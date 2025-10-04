import pandas as pd
import numpy as np

class CovenantDataGenerator:
    """
    피의 언약 챕터(ch24)를 위한 샘플 데이터를 생성하는 클래스.
    데이터 스냅샷 및 버전 관리에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Covenant of Blood chapter (ch24).
    Generates data to be used for data snapshotting and version control.
    """

    def generate_covenant_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        피의 언약과 관련된 샘플 데이터를 생성합니다.
        예: 언약 이벤트, 참여자 수, 순종 지수 등.

        Generates sample data related to the covenant of blood.
        E.g., covenant events, number of participants, obedience score.

        Args:
            num_records (int): 생성할 데이터 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(24)
        dates = pd.date_range(start='1446-01-01', periods=num_records, freq='D') # Exodus era
        data = {
            'event_date': dates,
            'event_type': np.random.choice(['Law Proclaimed', 'Blood Sprinkled', 'Feast', 'Disobedience', 'Repentance'], size=num_records, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
            'participants': np.random.randint(1000, 10000, size=num_records),
            'obedience_score': np.random.randint(1, 10, size=num_records), # 1-10 scale
            'divine_favor': np.random.rand(num_records)
        }
        df = pd.DataFrame(data)
        print("CovenantDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = CovenantDataGenerator()
    df = generator.generate_covenant_data()
    print(df.head())
    print(df.info())