
import pandas as pd
import numpy as np

class TrueVineDataGenerator:
    """
    요한복음 15장의 참 포도나무 데이터를 생성하는 클래스.
    가지의 연결 상태, 가지치기 여부, 열매 수확량 등을 시뮬레이션합니다.

    Class to generate True Vine data from John Chapter 15.
    Simulates branch connection status, pruning status, fruit yield, etc.
    """

    def __init__(self):
        self.vine_elements = self._load_vine_elements()

    def _load_vine_elements(self):
        """
        참 포도나무 비유의 주요 요소에 대한 기본 정보를 로드합니다.
        Loads basic information about key elements of the True Vine parable.
        """
        # KJV: John 15:5 - "I am the vine, ye are the branches: He that abideth in me, and I in him, the same bringeth forth much fruit..."
        # ESV: John 15:5 - "I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit..."
        # 개역한글: 요한복음 15:5 - "나는 포도나무요 너희는 가지니 저가 내 안에, 내가 저 안에 있으면 이 사람은 과실을 많이 맺나니..."
        return pd.DataFrame({
            'branch_id': range(1, 11), # 10개의 가지 시뮬레이션
            'connection_to_vine': np.random.choice(['Strong', 'Weak', 'Disconnected'], size=10, p=[0.6, 0.3, 0.1]),
            'pruning_status': np.random.choice(['Pruned', 'Not Pruned'], size=10, p=[0.4, 0.6]),
            'spiritual_health': np.random.randint(5, 10, size=10), # 1-10 스케일 (10: 매우 건강)
            'fruit_yield': np.random.randint(0, 10, size=10) # 0-10 스케일 (10: 많은 열매)
        })

    def generate_true_vine_data(self) -> pd.DataFrame:
        """
        상세한 참 포도나무 데이터를 생성합니다.
        가지의 연결 상태, 가지치기 여부, 열매 수확량 등을 포함합니다.

        Generates detailed True Vine data.
        Includes branch connection status, pruning status, fruit yield, etc.

        Returns:
            pd.DataFrame: 상세 참 포도나무 데이터
        """
        df = self.vine_elements.copy()

        # 연결 상태와 가지치기 여부에 따른 열매 수확량 조정
        df.loc[df['connection_to_vine'] == 'Disconnected', 'fruit_yield'] = 0
        df.loc[(df['connection_to_vine'] == 'Strong') & (df['pruning_status'] == 'Pruned'), 'fruit_yield'] = np.clip(df['fruit_yield'] + np.random.randint(3, 5), 0, 10)
        df.loc[(df['connection_to_vine'] == 'Strong') & (df['pruning_status'] == 'Not Pruned'), 'fruit_yield'] = np.clip(df['fruit_yield'] + np.random.randint(0, 2), 0, 10)

        # KJV: John 15:2 - "Every branch in me that beareth not fruit he taketh away: and every branch that beareth fruit, he purgeth it, that it may bring forth more fruit."
        # ESV: John 15:2 - "Every branch in me that does not bear fruit he takes away, and every branch that does bear fruit he prunes, that it may bear more fruit."
        # 개역한글: 요한복음 15:2 - "무릇 내게 있어 과실을 맺지 아니하는 가지는 아버지께서 이를 제해 버리시고 무릇 과실을 맺는 가지는 더 많은 과실을 맺게 하려 하여 이를 깨끗케 하시느니라"
        print("✨ 요한복음 15장 참 포도나무 데이터가 생성되었습니다.")
        print("가지의 연결 상태, 가지치기 여부, 열매 수확량 등을 시뮬레이션합니다.")
        print(df.to_string(index=False))
        print("\n---")
        print("영적 통찰: 예수님과의 긴밀한 연결과 아버지의 가지치기(정리) 과정을 통해 열매 맺는 삶이 이루어집니다.")
        print("Spiritual Insight: A fruitful life is achieved through a close connection with Jesus and the Father's pruning process.")

        return df

def demo_true_vine_data_generation():
    """
    TrueVineDataGenerator 클래스의 데모 실행 함수.
    Demonstration function for TrueVineDataGenerator class.
    """
    print("--- True Vine Data Generation Demo ---")
    print("--- 참 포도나무 데이터 생성 데모 ---")
    generator = TrueVineDataGenerator()
    data = generator.generate_true_vine_data()
    return data

if __name__ == "__main__":
    demo_true_vine_data_generation()
