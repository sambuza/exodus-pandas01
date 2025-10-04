import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

class ThirdPlagueDataGenerator:
    """세 번째 재앙 (이/티끌) 데이터 생성 클래스"""

    def __init__(self, simulation_days: int = 7):
        """초기화
        
        Args:
            simulation_days: 시뮬레이션 일수
        """
        self.simulation_days = simulation_days
        self.plague_data = None

    def generate_gnat_data(self) -> pd.DataFrame:
        """이/티끌 재앙 데이터 생성"""

        print(f"\n🦟 === 이/티끌 재앙 데이터 생성 (총 {self.simulation_days}일) ===\n")

        dates = pd.date_range(start='Exodus-Day-3', periods=self.simulation_days, freq='D')
        
        # 각 지역별 이/티끌 출현 강도 (0-100)
        regions = ['사람_몸', '가축', '땅_티끌', '애굽_술객_영향', '애굽_전역']
        data = {
            '날짜': dates
        }
        for region in regions:
            data[f'{region}_이_수준'] = [random.randint(0, 100) for _ in range(self.simulation_days)]
        
        # 고센 땅은 항상 0 또는 매우 낮은 수준으로 유지 (구별)
        data['고센_이_수준'] = [random.randint(0, 3) if random.random() < 0.2 else 0 for _ in range(self.simulation_days)]

        # 파라오의 반응 (0: 강퍅, 1: 타협 시도, 2: 신하들의 조언)
        pharaoh_responses = [0, 1, 2]
        data['파라오_반응'] = random.choices(pharaoh_responses, weights=[0.6, 0.3, 0.1], k=self.simulation_days)
        
        # 술객들의 반응 (0: 실패, 1: 성공 시도)
        data['술객_성공_여부'] = [0] * (self.simulation_days - 2) + [1, 0] # 이 재앙은 술객들이 흉내내지 못함
        random.shuffle(data['술객_성공_여부'])
        
        self.plague_data = pd.DataFrame(data)
        
        print("📝 생성된 이/티끌 재앙 데이터 미리보기:")
        print(self.plague_data.head())
        print(f"\n✅ 총 {len(self.plague_data)}개의 이/티끌 재앙 데이터가 생성되었습니다.")

        return self.plague_data

    def add_random_missing_values(self, column: str, ratio: float = 0.1):
        """특정 컬럼에 랜덤하게 결측치 추가 (시뮬레이션용)"""
        if self.plague_data is not None:
            num_missing = int(len(self.plague_data) * ratio)
            missing_indices = random.sample(range(len(self.plague_data)), num_missing)
            self.plague_data.loc[missing_indices, column] = np.nan
            print(f"⚠️ '{column}' 컬럼에 {num_missing}개의 결측치(NaN)가 추가되었습니다.")

def generate_third_plague_data(days: int = 10) -> pd.DataFrame:
    """외부에서 호출할 수 있는 세 번째 재앙 데이터 생성 함수"""
    generator = ThirdPlagueDataGenerator(simulation_days=days)
    data = generator.generate_gnat_data()
    # 필요시 결측치 추가 시뮬레이션
    generator.add_random_missing_values('땅_티끌_이_수준', ratio=0.15)
    generator.add_random_missing_values('파라오_반응', ratio=0.1)
    return generator.plague_data

if __name__ == "__main__":
    print("📚 Third Plague Data Generator 모듈 테스트")
    gnat_data = generate_third_plague_data(days=15)
    print("\n📊 최종 생성된 데이터:")
    print(gnat_data)
    print(f"\n결측치 확인:\n{gnat_data.isnull().sum()}")
    print("\n✅ 테스트 완료!")
