import pandas as pd
import numpy as np

def demo_isna_notna():
    """결측치 확인 데모: 믿음 여정의 시험과 결핍"""
    print("\n🔎 결측치 확인 (`isna`, `notna`): 믿음 여정의 시험과 결핍")
    print("=" * 50)

    faith_journey = pd.DataFrame({
        '시기': ['광야 초기', '반석에서 물', '가나안 정탐', '바벨론 포로', '예수님 부활'],
        '백성_반응': ['불평', '원망', '불신', '회개', '믿음'],
        '하나님의_인도': [True, True, True, True, True],
        '믿음_수준': [3, 5, np.nan, 8, 10], # np.nan은 결핍된 믿음 또는 측정 불가
        '기도_응답_횟수': [5, 3, np.nan, 7, 10]
    })
    print(faith_journey)

    print("\n📊 DataFrame의 전체 결측치 위치:")
    print(faith_journey.isna())
    print("\n✅ '믿음_수준' 열의 결측치 확인:")
    print(faith_journey['믿음_수준'].isna())
    print("\n✅ '기도_응답_횟수' 열의 결측치가 아닌 값 확인:")
    print(faith_journey['기도_응답_횟수'].notna())

    # 결측치가 하나라도 있는 행만 필터링
    rows_with_nan = faith_journey[faith_journey.isna().any(axis=1)]
    print("\n🤔 결측치가 있는 행:")
    print(rows_with_nan)

    return faith_journey

def demo_fillna_dropna():
    """결측치 채우기 및 제거 데모: 부족함을 채우시는 하나님"""
    print("\n💧 결측치 채우기 (`fillna`) 및 제거 (`dropna`): 부족함을 채우시는 하나님")
    print("=" * 50)

    manna_supply = pd.DataFrame({
        '날짜': pd.to_datetime(['2025-09-01', '2025-09-02', '2025-09-03', '2025-09-04', '2025-09-05', '2025-09-06', '2025-09-07']),
        '만나_수량(오멜)': [10, 12, np.nan, 15, np.nan, 20, np.nan], # 안식일, 또는 누락된 날
        '특별_공급_여부': [False, False, False, False, True, False, False], # 금요일은 두 배 공급
        '백성_만족도': [7, 8, np.nan, 9, 6, 8, np.nan]
    })
    print(manna_supply)
    print("\n📊 초기 DataFrame (결측치 포함):")
    print(manna_supply.isna().sum())

    # 1. '만나_수량(오멜)' 결측치를 이전 값으로 채우기 (forward fill)
    manna_ffill = manna_supply.copy()
    manna_ffill['만나_수량(오멜)'] = manna_ffill['만나_수량(오멜)'].fillna(method='ffill')
    print("\n🔄 '만나_수량(오멜)' 결측치를 이전 값으로 채운 후 (`ffill`):")
    print(manna_ffill)

    # 2. '백성_만족도' 결측치를 평균값으로 채우기
    manna_mean_fill = manna_supply.copy()
    mean_satisfaction = manna_mean_fill['백성_만족도'].mean()
    manna_mean_fill['백성_만족도'] = manna_mean_fill['백성_만족도'].fillna(mean_satisfaction)
    print(f"\n🔄 '백성_만족도' 결측치를 평균({mean_satisfaction:.2f})으로 채운 후 (`fillna(mean)`):")
    print(manna_mean_fill)

    # 3. 결측치가 있는 행 제거 (`dropna`)
    manna_dropna = manna_supply.copy()
    manna_dropna = manna_dropna.dropna()
    print("\n🗑️ 결측치가 있는 모든 행 제거 후 (`dropna()`):")
    print(manna_dropna)
    print("   -> 결측치 제거는 때로 많은 정보 손실을 의미합니다. 지혜로운 선택이 필요!")

    return manna_supply

def demo_interpolate():
    """결측치 보간법 데모: 하나님의 연속적인 인도하심"""
    print("\n📈 결측치 보간법 (`interpolate`): 하나님의 연속적인 인도하심")
    print("=" * 50)

    prophetic_timeline = pd.DataFrame({
        '연도': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        '영적_부흥_지수': [10, 12, np.nan, 15, np.nan, np.nan, 18, 17, np.nan, 22], # np.nan은 중간 단계의 영적 상태
        '메시아_기대치': [5, np.nan, 6, np.nan, 8, np.nan, np.nan, 9, 10, 12]
    })
    print(prophetic_timeline)
    print("\n📊 초기 DataFrame (결측치 포함):")
    print(prophetic_timeline.isna().sum())

    # 1. '영적_부흥_지수'를 선형 보간법으로 채우기
    prophetic_linear = prophetic_timeline.copy()
    prophetic_linear['영적_부흥_지수_linear'] = prophetic_linear['영적_부흥_지수'].interpolate(method='linear')
    print("\n🔄 '영적_부흥_지수'를 선형 보간법으로 채운 후 (`interpolate(linear)`):")
    print(prophetic_linear[['연도', '영적_부흥_지수', '영적_부흥_지수_linear']])

    # 2. '메시아_기대치'를 다항 보간법으로 채우기 (order=2)
    prophetic_polynomial = prophetic_timeline.copy()
    prophetic_polynomial['메시아_기대치_polynomial'] = prophetic_polynomial['메시아_기대치'].interpolate(method='polynomial', order=2)
    print("\n🔄 '메시아_기대치'를 다항 보간법(2차)으로 채운 후 (`interpolate(polynomial, order=2)`):")
    print(prophetic_polynomial[['연도', '메시아_기대치', '메시아_기대치_polynomial']])

    print("   -> 보간법은 하나님의 연속적인 인도하심처럼, 중간의 공백을 자연스럽게 채워줍니다.")

    return prophetic_timeline

def main():
    demo_isna_notna()
    demo_fillna_dropna()
    demo_interpolate()

if __name__ == "__main__":
    main()
