import pandas as pd
import numpy as np

class PriestlyGarmentsDataGenerator:
    """
    제사장 옷 챕터(ch28)를 위한 샘플 데이터를 생성하는 클래스.
    범주형 라벨링 및 데이터프레임 스타일링에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Priestly Garments chapter (ch28).
    Generates data to be used for categorical labeling and DataFrame styling.
    """

    def generate_garments_data(self) -> pd.DataFrame:
        """
        범주형 라벨링 및 데이터프레임 스타일링에 사용될 샘플 데이터를 생성합니다.

        Generates sample data to be used for categorical labeling and DataFrame styling.

        Returns:
            pd.DataFrame: 샘플 데이터
        """
        np.random.seed(28)
        data = {
            'priest_id': range(1, 11),
            'garment_type': np.random.choice(['Ephod', 'Breastplate', 'Robe', 'Tunic'], size=10),
            'material_quality': np.random.randint(1, 10, size=10), # 1-10 scale
            'color_purity': np.random.rand(10), # 0-1 scale
            'gemstone_count': np.random.randint(0, 12, size=10),
            'status': np.random.choice(['Clean', 'Worn', 'New'], size=10)
        }
        df = pd.DataFrame(data)
        print("PriestlyGarmentsDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = PriestlyGarmentsDataGenerator()
    df = generator.generate_garments_data()
    print(df)