import pandas as pd
import numpy as np

class DisciplesMissionDataGenerator:
    """
    제자들의 사명(ch40)을 위한 샘플 데이터를 생성하는 클래스.
    제자들의 상태와 사명을 데이터로 표현합니다.
    """

    def generate_mission_data(self, num_disciples: int = 12) -> pd.DataFrame:
        """
        제자들의 사명 관련 샘플 데이터를 생성합니다.
        """
        np.random.seed(4040)
        
        disciples = ['Peter', 'Andrew', 'James', 'John', 'Philip', 'Bartholomew', 'Thomas', 'Matthew', 'James son of Alphaeus', 'Thaddaeus', 'Simon the Zealot', 'Judas Iscariot']
        
        data = {
            'disciple': disciples,
            'status_before_resurrection': np.random.choice(['Fearful', 'Doubtful', 'Confident'], size=num_disciples, p=[0.6, 0.3, 0.1]),
            'mission_assigned': [False] * num_disciples
        }
        df = pd.DataFrame(data)
        print("DisciplesMissionDataGenerator: 샘플 데이터 생성 완료.")
        return df
