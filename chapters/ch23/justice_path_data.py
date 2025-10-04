import pandas as pd
import numpy as np

class JusticePathDataGenerator:
    """
    정의의 길 챕터(ch23)를 위한 샘플 데이터를 생성하는 클래스.
    정렬 및 우선순위 전략에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Path of Justice chapter (ch23).
    Generates data to be used for sorting and priority strategies.
    """

    def generate_justice_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        정의의 길과 관련된 샘플 데이터를 생성합니다.
        예: 사건 유형, 심각도, 처리 시급성, 약자 보호 여부 등.

        Generates sample data related to the path of justice.
        E.g., incident type, severity, urgency of processing, protection for the vulnerable.

        Args:
            num_records (int): 생성할 데이터 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(23)
        data = {
            'case_id': range(1, num_records + 1),
            'offense_type': np.random.choice(['Theft', 'Assault', 'Fraud', 'Dispute', 'Property Damage'], size=num_records, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
            'severity': np.random.randint(1, 10, size=num_records), # 1-10 scale (10 is most severe)
            'urgency': np.random.randint(1, 10, size=num_records), # 1-10 scale (10 is most urgent)
            'vulnerable_party': np.random.choice([True, False], size=num_records, p=[0.3, 0.7]),
            'filing_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, size=num_records), unit='D')
        }
        df = pd.DataFrame(data)
        print("JusticePathDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = JusticePathDataGenerator()
    df = generator.generate_justice_data()
    print(df.head())
    print(df.info())