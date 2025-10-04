import pandas as pd
import numpy as np

class CompensationDataGenerator:
    """
    배상과 회복 챕터(ch22)를 위한 샘플 데이터를 생성하는 클래스.
    결측치와 이상치를 포함하는 DataFrame을 생성합니다.

    Class to generate sample data for the Compensation and Restoration chapter (ch22).
    Generates a DataFrame with missing values and outliers.
    """

    def generate_compensation_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        배상과 회복과 관련된 샘플 데이터를 생성합니다.
        예: 피해액, 배상액, 겸손 점수 등.

        Generates sample data related to compensation and restoration.
        E.g., damage amount, compensation amount, humility score.

        Args:
            num_records (int): 생성할 데이터 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(22)
        data = {
            'case_id': range(1, num_records + 1),
            'damage_amount': np.random.randint(100, 1000, size=num_records),
            'compensation_amount': np.random.randint(80, 900, size=num_records),
            'humility_score': np.random.randint(1, 10, size=num_records), # 1-10 scale
            'restoration_status': np.random.choice(['Full', 'Partial', 'None'], size=num_records, p=[0.6, 0.3, 0.1])
        }
        df = pd.DataFrame(data)

        # 결측치 추가
        missing_indices = np.random.choice(df.index, size=int(num_records * 0.1), replace=False)
        df.loc[missing_indices, 'compensation_amount'] = np.nan
        missing_indices = np.random.choice(df.index, size=int(num_records * 0.05), replace=False)
        df.loc[missing_indices, 'humility_score'] = np.nan

        # 이상치 추가
        df.loc[np.random.choice(df.index, size=int(num_records * 0.02), replace=False), 'damage_amount'] = np.random.randint(2000, 5000, size=int(num_records * 0.02))
        df.loc[np.random.choice(df.index, size=int(num_records * 0.01), replace=False), 'humility_score'] = 0 # 극단적으로 낮은 겸손 점수
        df.loc[np.random.choice(df.index, size=int(num_records * 0.01), replace=False), 'humility_score'] = 100 # 극단적으로 높은 겸손 점수 (이상치)

        print("CompensationDataGenerator: 샘플 데이터 생성 완료 (결측치 및 이상치 포함).")
        return df

if __name__ == "__main__":
    generator = CompensationDataGenerator()
    df = generator.generate_compensation_data()
    print(df.head())
    print(df.info())
    print("\n결측치 개수:\n", df.isnull().sum())
    print("\ndamage_amount 기술 통계:\n", df['damage_amount'].describe())
    print("\nhumility_score 기술 통계:\n", df['humility_score'].describe())
