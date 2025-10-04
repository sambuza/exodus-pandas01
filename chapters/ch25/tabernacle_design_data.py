import pandas as pd
import numpy as np

class TabernacleDesignDataGenerator:
    """
    성막 설계 챕터(ch25)를 위한 샘플 데이터를 생성하는 클래스.
    스키마 설계 및 메타데이터 관리에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Tabernacle Design chapter (ch25).
    Generates data to be used for schema design and metadata management.
    """

    def generate_design_data(self, num_components: int = 10) -> pd.DataFrame:
        """
        성막 설계와 관련된 샘플 데이터를 생성합니다.
        예: 구성 요소, 재료, 치수, 용도 등.

        Generates sample data related to the Tabernacle design.
        E.g., components, materials, dimensions, purpose.

        Args:
            num_components (int): 생성할 성막 구성 요소 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(25)
        components = np.random.choice(['Ark', 'Mercy Seat', 'Table', 'Lampstand', 'Altar of Incense', 'Altar of Burnt Offering', 'Laver', 'Curtain', 'Pillar'], size=num_components)
        materials = np.random.choice(['Gold', 'Silver', 'Bronze', 'Fine Linen', 'Acacia Wood'], size=num_components)
        
        data = {
            'component': components,
            'material': materials,
            'length_cubits': np.random.randint(1, 10, size=num_components),
            'width_cubits': np.random.randint(1, 10, size=num_components),
            'height_cubits': np.random.randint(1, 10, size=num_components),
            'purpose': np.random.choice(['Worship', 'Offering', 'Storage', 'Boundary', 'Light'], size=num_components)
        }
        df = pd.DataFrame(data)
        print("TabernacleDesignDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = TabernacleDesignDataGenerator()
    df = generator.generate_design_data()
    print(df.head())
    print(df.info())