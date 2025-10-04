import pandas as pd
import numpy as np

class GraceDataGenerator:
    """
    다시 만난 은혜 챕터(ch33)를 위한 샘플 데이터를 생성하는 클래스.
    결합 충돌 해소에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Grace Reunited chapter (ch33).
    Generates data to be used for resolving join conflicts.
    """

    def generate_grace_data(self, num_records: int = 10) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        은혜와 관련된 두 개의 샘플 데이터프레임을 생성합니다.
        하나는 이스라엘 백성의 상태, 다른 하나는 하나님의 응답을 나타냅니다.
        결합 충돌을 시뮬레이션하기 위해 일부 중복되거나 누락된 ID를 포함합니다.

        Generates two sample DataFrames related to grace.
        One represents the state of the Israelites, the other God's response.
        Includes some duplicate or missing IDs to simulate join conflicts.

        Args:
            num_records (int): 생성할 레코드 수.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame]: 두 개의 샘플 데이터프레임.
        """
        np.random.seed(33)

        # 데이터셋 1: 이스라엘 백성의 상태 (Exodus 33)
        df1_data = {
            'id': np.arange(1, num_records + 1),
            'israelite_status': np.random.choice(['Rebellious', 'Repentant', 'Obedient'], size=num_records, p=[0.3, 0.4, 0.3]),
            'faith_level': np.random.randint(1, 10, size=num_records),
            'prayer_intensity': np.random.rand(num_records) * 10
        }
        df1 = pd.DataFrame(df1_data)

        # 데이터셋 2: 하나님의 응답 (Exodus 33, John 21)
        # 일부러 ID를 섞거나 중복, 누락시켜 결합 충돌 유발
        df2_ids = np.concatenate([np.arange(1, num_records // 2 + 1), np.arange(num_records // 2 + 2, num_records + 3)])
        np.random.shuffle(df2_ids)
        df2_data = {
            'id': df2_ids[:num_records],
            'divine_response': np.random.choice(['Grace', 'Judgment', 'Guidance'], size=num_records, p=[0.5, 0.2, 0.3]),
            'love_confession': np.random.randint(1, 10, size=num_records) # 베드로의 사랑 고백 관련
        }
        df2 = pd.DataFrame(df2_data)

        print("GraceDataGenerator: 샘플 데이터 생성 완료 (결합 충돌 포함).")
        return df1, df2

if __name__ == "__main__":
    generator = GraceDataGenerator()
    df1, df2 = generator.generate_grace_data()
    print("데이터프레임 1:")
    print(df1.head())
    print("\n데이터프레임 2:")
    print(df2.head())
