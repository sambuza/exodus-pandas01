import pandas as pd
import numpy as np

def analyze_pharaoh_response():
    """출애굽기 5장 파라오의 반응 분석: 데이터 타입의 강퍅함"""
    print("\n🏛️ 파라오의 강퍅한 반응: 데이터 타입으로 이해하기")
    print("=" * 50)

    pharaoh_actions = pd.DataFrame({
        '단계': [1, 2, 3, 4],
        '사건': ['모세의 요청', '파라오의 거절', '고통 증가', '더욱 강퍅'],
        '반응_유형': ['명령', '경멸', '압제', '완고'],
        '긍정적_요소': [0, 0, 0, 0],
        '부정적_요소': [10, 15, 20, 25],
        '결과': ['좌절', '분노', '고통', '불신'],
        '데이터_타입_비유': ['string', 'string', 'integer', 'string']
    })
    print(pharaoh_actions)
    print("\n📊 파라오 반응 DataFrame의 데이터 타입:\n", pharaoh_actions.dtypes)

    # '긍정적_요소'를 float으로 변환 시도 (원래 0이라 의미 없지만 타입 변환 시연)
    pharaoh_actions['긍정적_요소_float'] = pharaoh_actions['긍정적_요소'].astype(float)
    print("\n🔄 '긍정적_요소'를 float으로 변환 후 데이터 타입:\n", pharaoh_actions[['긍정적_요소', '긍정적_요소_float']].dtypes)

    return pharaoh_actions

def analyze_israelites_burden():
    """출애굽기 5장 이스라엘 백성의 고통 분석: 데이터 타입의 변화"""
    print("\n⛓️ 이스라엘 백성의 증가된 고통: 숫자의 변화와 좌절")
    print("=" * 50)

    burden_data = pd.DataFrame({
        '시기': ['모세 방문 전', '모세 방문 후'],
        '벽돌_수량': [100, '기존대로'],  # '기존대로'는 숫자가 아님
        '짚_제공': [True, False],
        '감독관_폭행': ['없음', '있음'],
        '원망_수준': [5, 9.5] # float 타입
    })
    print(burden_data)
    print("\n📊 이스라엘 고통 DataFrame의 데이터 타입:\n", burden_data.dtypes)

    # '벽돌_수량' 열의 데이터 타입을 숫자로 변환 시도
    # 에러 발생 예정: '기존대로'는 숫자가 아니므로, errors='coerce' 사용
    burden_data['벽돌_수량_numeric'] = pd.to_numeric(burden_data['벽돌_수량'], errors='coerce')
    print("\n🔄 '벽돌_수량'을 숫자로 변환 시도 후 (오류 처리):\n", burden_data[['벽돌_수량', '벽돌_수량_numeric']].dtypes)
    print(burden_data[['벽돌_수량', '벽돌_수량_numeric']])
    print("   -> '기존대로'가 NaN으로 변환되어 float 타입이 됨. 데이터 타입의 중요성!")

    # 원망 수준이 높은 시기 필터링
    high_resentment = burden_data[burden_data['원망_수준'] > 8]
    print("\n🚨 원망 수준이 높은 시기:")
    print(high_resentment)

    return burden_data

def main():
    analyze_pharaoh_response()
    analyze_israelites_burden()

if __name__ == "__main__":
    main()
