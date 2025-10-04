import pandas as pd
import numpy as np

class NewTabletsDataGenerator:
    """
    새 돌판 챕터(ch34)를 위한 샘플 데이터를 생성하는 클래스.
    정규화와 표준화에 사용될 데이터를 생성합니다.

    Class to generate sample data for the New Tablets chapter (ch34).
    Generates data to be used for normalization and standardization.
    """

    def generate_tablets_data(self, num_records: int = 100) -> pd.DataFrame:
        """
        새 돌판과 관련된 샘플 데이터를 생성합니다.
        예: 순종 점수, 하나님의 은혜 지수, 계명 텍스트 등.

        Generates sample data related to the new tablets.
        E.g., obedience score, divine grace index, commandment text.

        Args:
            num_records (int): 생성할 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(34)
        
        data = {
            'commandment_id': range(1, num_records + 1),
            'obedience_score': np.random.randint(1, 100, size=num_records), # 1-100 scale
            'divine_favor': np.random.rand(num_records) * 1000, # 0-1000 scale
            'commandment_text': np.random.choice([
                "Thou shalt have no other gods before me.",
                "Thou shalt not make unto thee any graven image.",
                "Thou shalt not take the name of the Lord thy God in vain.",
                "Remember the sabbath day, to keep it holy.",
                "Honour thy father and thy mother.",
                "Thou shalt not kill.",
                "Thou shalt not commit adultery.",
                "Thou shalt not steal.",
                "Thou shalt not bear false witness against thy neighbour.",
                "Thou shalt not covet."
            ], size=num_records)
        }
        df = pd.DataFrame(data)

        # 일부러 스케일이 다른 컬럼 추가
        df['small_value'] = np.random.rand(num_records) * 10
        df['large_value'] = np.random.rand(num_records) * 100000

        print("NewTabletsDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = NewTabletsDataGenerator()
    df = generator.generate_tablets_data()
    print(df.head())
    print(df.info())