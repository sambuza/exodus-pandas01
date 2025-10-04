import pandas as pd
import numpy as np

class CraftsmenDataGenerator:
    """
    브살렐과 오홀리압 챕터(ch31)를 위한 샘플 데이터를 생성하는 클래스.
    성능 최적화 기법에 사용될 데이터를 생성합니다.

    Class to generate sample data for the Bezalel and Oholiab chapter (ch31).
    Generates data to be used for performance optimization techniques.
    """

    def generate_craftsmen_data(self, num_tasks: int = 10000) -> pd.DataFrame:
        """
        성막 건축 장인들의 작업과 관련된 샘플 데이터를 생성합니다.
        예: 장인 이름, 작업 유형, 소요 시간, 재료 비용 등.

        Generates sample data related to the work of Tabernacle craftsmen.
        E.g., craftsman name, task type, time spent, material cost.

        Args:
            num_tasks (int): 생성할 작업 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(31)
        craftsmen = np.random.choice(['Bezalel', 'Oholiab', 'Other'], size=num_tasks, p=[0.3, 0.3, 0.4])
        task_types = np.random.choice(['Gold Work', 'Silver Work', 'Bronze Work', 'Wood Carving', 'Embroidery'], size=num_tasks)
        
        data = {
            'task_id': range(1, num_tasks + 1),
            'craftsman': craftsmen,
            'task_type': task_types,
            'time_spent_minutes': np.random.randint(10, 300, size=num_tasks),
            'material_cost': np.random.rand(num_tasks) * 1000 + 50,
            'quality_score': np.random.randint(70, 100, size=num_tasks)
        }
        df = pd.DataFrame(data)
        print("CraftsmenDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = CraftsmenDataGenerator()
    df = generator.generate_craftsmen_data()
    print(df.head())
    print(df.info())