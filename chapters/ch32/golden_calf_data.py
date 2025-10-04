import pandas as pd
import numpy as np

class GoldenCalfDataGenerator:
    """
    금송아지 챕터(ch32)를 위한 샘플 데이터를 생성하는 클래스.
    롤백 및 감사 로그에 사용될 데이터 변경 이력을 포함하는 데이터를 생성합니다.

    Class to generate sample data for the Golden Calf chapter (ch32).
    Generates data including change history for rollback and audit logs.
    """

    def generate_golden_calf_data(self, num_events: int = 10) -> pd.DataFrame:
        """
        금송아지 사건과 관련된 샘플 데이터를 생성합니다.
        예: 이벤트 유형, 순종 점수, 하나님의 진노 지수 등.

        Generates sample data related to the Golden Calf incident.
        E.g., event type, obedience score, divine wrath index.

        Args:
            num_events (int): 생성할 이벤트 레코드 수.

        Returns:
            pd.DataFrame: 샘플 데이터.
        """
        np.random.seed(32)
        event_types = np.random.choice(['Worship', 'Repentance', 'Judgment', 'Instruction'], size=num_events, p=[0.3, 0.3, 0.2, 0.2])
        
        data = {
            'event_id': range(1, num_events + 1),
            'event_date': pd.to_datetime('1446-01-01') + pd.to_timedelta(np.arange(num_events), unit='D'),
            'event_type': event_types,
            'obedience_score': np.random.randint(1, 10, size=num_events), # 1-10 scale
            'divine_favor': np.random.rand(num_events)
        }
        df = pd.DataFrame(data)

        # 금송아지 사건 시뮬레이션 (불순종 시 점수 하락, 진노 증가)
        df.loc[df['event_type'] == 'Worship', 'obedience_score'] = np.random.randint(1, 3, size=(df['event_type'] == 'Worship').sum())
        df.loc[df['event_type'] == 'Worship', 'divine_favor'] = np.random.rand((df['event_type'] == 'Worship').sum()) * 0.3

        print("GoldenCalfDataGenerator: 샘플 데이터 생성 완료.")
        return df

if __name__ == "__main__":
    generator = GoldenCalfDataGenerator()
    df = generator.generate_golden_calf_data()
    print(df.head())
    print(df.info())