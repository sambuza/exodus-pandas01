import pandas as pd
import numpy as np

def analyze_gods_promise():
    """출애굽기 6장 하나님의 약속 분석: NaN과 채워지는 진리"""
    print("\n📜 하나님의 약속: 결핍된 믿음을 채우시는 하나님")
    print("=" * 50)

    promise_data = pd.DataFrame({
        '약속_대상': ['아브라함', '이삭', '야곱', '모세', '이스라엘 백성'],
        '하나님의_이름_계시': ['전능의 하나님', '전능의 하나님', '전능의 하나님', '여호와', '여호와'],
        '모세에게_주신_약속': [np.nan, np.nan, np.nan, '내가 애굽 사람의 손에서 너희를 건져낼 것이요', '너희를 내 백성으로 삼고'],
        '약속_반응(백성)': [np.nan, np.nan, np.nan, np.nan, '마음의 상함과 가혹한 노동으로 모세의 말을 듣지 아니함'],
        '백성의_믿음_수준': [np.nan, np.nan, np.nan, 7, 3] # 1-10 스케일, NaN은 결측치
    })
    print(promise_data)
    print("\n📊 DataFrame의 결측치(NaN) 확인:")
    print(promise_data.isna())

    # '모세에게_주신_약속' 열의 결측치 확인
    print("\n✅ '모세에게_주신_약속' 열의 결측치:\n", promise_data['모세에게_주신_약속'].isna())

    # '백성의_믿음_수준' 열의 결측치가 아닌 값 (notna) 확인
    print("\n✅ '백성의_믿음_수준' 열의 결측치가 아닌 값:\n", promise_data['백성의_믿음_수준'].notna())

    # 결측치가 있는 행만 필터링
    missing_faith = promise_data[promise_data['백성의_믿음_수준'].isna()]
    print("\n🤔 '백성의_믿음_수준'에 결측치가 있는 행:")
    print(missing_faith)

    return promise_data

def analyze_israelites_disbelief():
    """이스라엘 백성의 불신 분석: NaN으로 표현되는 영적 결핍"""
    print("\n⛓️ 이스라엘 백성의 불신: '영적 NaN' 상태")
    print("=" * 50)

    disbelief_data = pd.DataFrame({
        '시기': ['모세 방문 후', '고통 증가', '광야 여정 중'],
        '모세의_말씀_수용': [False, False, np.nan], # np.nan은 불확실한 또는 결핍된 수용 상태
        '하나님께_대한_태도': ['원망', '불평', np.nan],
        '희망_수준': [2, 1, np.nan],
        '영적_상태_설명': ['마음 상함', '고통으로 듣지 못함', np.nan]
    })
    print(disbelief_data)
    print("\n📊 DataFrame의 결측치(NaN) 확인:")
    print(disbelief_data.isna())

    # '모세의_말씀_수용' 열의 결측치가 아닌 값만 필터링
    accepting_moments = disbelief_data[disbelief_data['모세의_말씀_수용'].notna()]
    print("\n✅ '모세의_말씀_수용'에 결측치가 아닌 행:")
    print(accepting_moments)

    # '희망_수준' 열의 결측치 개수 확인
    print(f"\n🔢 '희망_수준' 열의 결측치 개수: {disbelief_data['희망_수준'].isna().sum()}")

    return disbelief_data

def main():
    analyze_gods_promise()
    analyze_israelites_disbelief()

if __name__ == "__main__":
    main()
