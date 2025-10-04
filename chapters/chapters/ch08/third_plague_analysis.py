import pandas as pd
import numpy as np

def analyze_third_plague(data: pd.DataFrame):
    """세 번째 재앙 (이/티끌) 분석: 애굽 술객들의 한계와 하나님의 구별"""
    print("\n🦟 세 번째 재앙, 이/티끌: 애굽 술객들의 한계와 하나님의 구별")
    print("=" * 60)

    if data is None:
        print("⚠️ 분석할 데이터가 없습니다.")
        return None

    print("📊 원본 이/티끌 재앙 데이터 미리보기:")
    print(data.head())
    print("\n")

    # 1. 고센 땅과 다른 지역의 이/티끌 수준 비교 (하나님의 구별)
    print("🔍 고센 땅과 애굽 전역의 이/티끌 수준 비교 (데이터 구별):")
    goshen_gnat_data = data[data['고센_이_수준'] > 0][['날짜', '고센_이_수준']]
    egypt_gnat_data = data[data['애굽_전역_이_수준'] > 50][['날짜', '애굽_전역_이_수준']]

    if not goshen_gnat_data.empty:
        print("   고센 땅 (이/티끌 출현 기록):\n", goshen_gnat_data)
    else:
        print("   고센 땅에는 이/티끌 출현 기록이 거의 없습니다. (하나님의 분명한 구별)")

    if not egypt_gnat_data.empty:
        print("\n   애굽 전역 (심각한 이/티끌 출현 기록):\n", egypt_gnat_data)

    # 2. 애굽 술객들의 성공 여부 분석 (마스킹으로 실패 강조)
    print("\n🔮 애굽 술객들의 시도와 실패 (데이터 마스킹으로 실패 강조):")
    # 술객_성공_여부가 1인 경우 (성공 시도)를 마스크하여, 실제로 실패했음을 강조
    magicians_attempt = data[['날짜', '술객_성공_여부', '애굽_술객_영향_이_수준']].copy()
    magicians_attempt['실패_강조'] = magicians_attempt['술객_성공_여부'].mask(magicians_attempt['술객_성공_여부'] == 1, 0) # 1을 0으로 바꿔서 실패를 나타냄
    print(magicians_attempt.head())
    print("\n   통찰: `mask()`를 통해 술객들이 이 재앙을 흉내 내지 못하여 하나님이 진정한 신이심이 드러난 사건을 시뮬레이션합니다.")

    # 3. 파라오의 반응 변화 분석 (df.where를 이용한 조건부 필터링)
    print("\n👑 파라오의 반응 변화 (신하들의 조언에 대한 데이터 필터링):")
    # 파라오 반응이 2 (신하들의 조언)인 날짜의 데이터를 필터링
    pharaoh_advised_days = data.where(data['파라오_반응'] == 2).dropna(subset=['파라오_반응'])
    if not pharaoh_advised_days.empty:
        print("   신하들이 조언한 날짜:\n", pharaoh_advised_days[['날짜', '파라오_반응', '애굽_전역_이_수준']])
        print("\n   통찰: `where()`는 파라오의 강퍅함이 흔들리기 시작한 시점을 포착하는 데 사용됩니다.")
    else:
        print("   신하들이 파라오에게 조언한 기록이 없습니다.")

    # 4. 각 재앙 수준에 따른 파라오 반응 분포 (groupby and value_counts)
    print("\n📊 이/티끌 수준별 파라오 반응 분포:")
    gnat_level_response = data.groupby(pd.cut(data['애굽_전역_이_수준'], bins=[0, 30, 70, 100], labels=['낮음', '보통', '높음']))['파라오_반응'].value_counts(normalize=True).unstack().fillna(0)
    print(gnat_level_response)
    print("\n   통찰: 재앙의 강도가 높을수록 파라오의 반응(특히 타협 시도나 신하들의 조언)이 어떻게 달라지는지 파악할 수 있습니다.")

    return {
        "goshen_distinction": goshen_gnat_data,
        "magicians_attempt_analysis": magicians_attempt,
        "pharaoh_advised_days": pharaoh_advised_days,
        "gnat_level_response": gnat_level_response
    }

if __name__ == "__main__":
    print("📚 Third Plague Analysis 모듈 테스트")
    from chapters.ch08.third_plague_data import generate_third_plague_data
    test_data = generate_third_plague_data(days=15)
    if test_data is not None:
        results = analyze_third_plague(test_data)
        print("\n✅ 분석 완료!")
    else:
        print("❌ 데이터 생성 실패. 분석을 진행할 수 없습니다.")
