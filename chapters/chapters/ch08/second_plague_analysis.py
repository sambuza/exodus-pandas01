import pandas as pd
import numpy as np

def analyze_second_plague(data: pd.DataFrame):
    """두 번째 재앙 (개구리) 분석: 고센 땅의 구별과 마스킹"""
    print("\n🐸 두 번째 재앙, 개구리: 고센 땅의 구별과 데이터 마스킹")
    print("=" * 60)

    if data is None:
        print("⚠️ 분석할 데이터가 없습니다.")
        return None

    print("📊 원본 개구리 재앙 데이터 미리보기:")
    print(data.head())
    print("\n")

    # 1. 고센 땅과 다른 지역의 개구리 수준 비교 (구별)
    print("🔍 고센 땅과 애굽 전역의 개구리 수준 비교 (데이터 구별):")
    goshen_data = data[data['고센_개구리_수준'] > 0][['날짜', '고센_개구리_수준']]
    egypt_data = data[data['애굽_전역_개구리_수준'] > 50][['날짜', '애굽_전역_개구리_수준']]

    if not goshen_data.empty:
        print("   고센 땅 (개구리 출현 기록):\n", goshen_data)
    else:
        print("   고센 땅에는 개구리 출현 기록이 거의 없습니다. (하나님의 구별)")

    if not egypt_data.empty:
        print("\n   애굽 전역 (심각한 개구리 출현 기록):\n", egypt_data)

    # 2. 데이터 마스킹 (df.mask)을 사용하여 고센 땅 데이터 '보호'
    # 애굽 전역의 개구리 수준을 보여주되, 고센 땅 수준이 0이 아닌 경우만 표시 (데이터 보호)
    print("\n🛡️ 데이터 마스킹 (고센 땅 보호): 애굽 전역 데이터에서 고센 땅 영향 제외")
    # 고센 땅 개구리 수준이 0보다 큰 경우 (즉, 고센 땅에 개구리가 있는 경우), 애굽 전역 값을 NaN으로 마스크
    masked_egypt_plague = data['애굽_전역_개구리_수준'].mask(data['고센_개구리_수준'] > 0, np.nan)
    # 원본 데이터프레임에 추가하여 비교
    data['마스킹된_애굽_개구리_수준'] = masked_egypt_plague
    print(data[['날짜', '애굽_전역_개구리_수준', '고센_개구리_수준', '마스킹된_애굽_개구리_수준']].head(7))
    print("\n   통찰: `mask()`는 특정 조건에 따라 값을 '숨기거나' 다른 값으로 대체할 때 유용합니다. 여기서는 고센 땅이 보호받는 것을 시뮬레이션합니다.")

    # 3. 데이터 필터링 (df.where)을 사용하여 파라오 반응 조건부 분석
    print("\n⚖️ 조건부 데이터 선택 (파라오의 강퍅함 분석): 파라오가 타협을 시도한 날만 분석")
    # 파라오가 반응(1)을 보인 날짜의 데이터만 선택
    pharaoh_response_days = data.where(data['파라오_반응'] == 1).dropna(subset=['파라오_반응'])
    if not pharaoh_response_days.empty:
        print(pharaoh_response_days[['날짜', '파라오_반응', '애굽_전역_개구리_수준']])
        print("\n   통찰: `where()`는 특정 조건을 만족하는 행만 선택하고, 나머지는 NaN으로 처리하여 데이터를 필터링하는 데 유용합니다.")
    else:
        print("   파라오가 타협을 시도한 날짜가 없습니다.")

    # 4. 재앙 강도에 따른 파라오 반응 경향 분석
    print("\n📈 재앙 강도에 따른 파라오 반응 경향:")
    plague_response_trend = data.groupby('파라오_반응')['애굽_전역_개구리_수준'].mean().reset_index()
    print(plague_response_trend)
    print("\n   통찰: 파라오가 타협적일 때 (반응=1) 개구리 수준이 더 높거나 낮은지 평균을 통해 경향을 파악할 수 있습니다.")

    # 추가: 특정 조건 만족하는 데이터 쿼리 (df.query)
    print("\n🔎 데이터 쿼리 (특정 재앙 조건 충족): 애굽 전역 개구리 수준이 70 이상인 날짜")
    high_plague_days = data.query('`애굽_전역_개구리_수준` >= 70')
    if not high_plague_days.empty:
        print(high_plague_days[['날짜', '애굽_전역_개구리_수준', '파라오_반응']])
        print("\n   통찰: `query()`는 SQL과 유사한 문자열 기반의 조건으로 DataFrame을 필터링할 때 매우 편리합니다.")
    else:
        print("   애굽 전역의 개구리 수준이 70 이상인 날짜가 없습니다.")


    return {
        "goshen_distinction_analysis": goshen_data,
        "masked_egypt_plague": masked_egypt_plague,
        "pharaoh_response_days": pharaoh_response_days,
        "plague_response_trend": plague_response_trend,
        "high_plague_days": high_plague_days
    }

if __name__ == "__main__":
    print("📚 Second Plague Analysis 모듈 테스트")
    from chapters.ch08.second_plague_data import generate_second_plague_data
    test_data = generate_second_plague_data(days=15)
    if test_data is not None:
        results = analyze_second_plague(test_data)
        print("\n✅ 분석 완료!")
    else:
        print("❌ 데이터 생성 실패. 분석을 진행할 수 없습니다.")
