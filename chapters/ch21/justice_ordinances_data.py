import pandas as pd
import numpy as np

class JusticeOrdinancesDataGenerator:
    """
    공의의 법도 챕터(ch21)를 위한 샘플 데이터를 생성하는 클래스.
    분류 및 범주형 분석에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Ordinances of Justice chapter (ch21).
    Generates data to be used for classification and categorical analysis.
    """

    def generate_ordinances_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        공의의 법도와 관련된 샘플 데이터를 생성합니다.
        예: 사건 유형, 피해 수준, 판단 결과 등.

        Generates sample data related to the ordinances of justice.
        E.g., incident type, damage level, judgment outcome.

        Args:
            num_records (int): 생성할 데이터 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(21)
        data = {
            'case_id': range(1, num_records + 1),
            'offense_type': np.random.choice(['Theft', 'Assault', 'Property Damage', 'Dispute'], size=num_records, p=[0.3, 0.3, 0.2, 0.2]),
            'damage_level': np.random.randint(1, 10, size=num_records), # 1-10 scale
            'witness_count': np.random.randint(0, 5, size=num_records),
            'judge_bias_score': np.random.rand(num_records) * 10, # 0-10 scale
            'judgment_outcome': np.random.choice(['Guilty', 'Not Guilty', 'Settled'], size=num_records, p=[0.4, 0.3, 0.3])
        }
        df = pd.DataFrame(data)
        print("JusticeOrdinancesDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = JusticeOrdinancesDataGenerator()
    df = generator.generate_ordinances_data()
    print(df.head())
    print(df.info())