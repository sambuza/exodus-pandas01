# ch03_three_signs.py
"""
세 가지 표적 - 권위와 능력의 증거
"""

import pandas as pd
import numpy as np


def create_signs_matrix():
    """세 가지 표적의 상세 분석"""

    signs_detail = pd.DataFrame({
        '표적': ['지팡이→뱀', '손→나병', '물→피'],
        '원상태': ['목자의 도구', '건강한 손', '나일강 물'],
        '변환상태': ['위협적인 뱀', '나병 든 손', '피'],
        '복원여부': ['복원됨', '복원됨', '복원 안됨'],
        '대상': ['바로/술객', '이스라엘', '애굽 전체'],
        '목적': ['권위 증명', '능력 증명', '심판 예고'],
        '위험도': [7, 5, 10],
        '영향범위': ['개인', '집단', '국가'],
        '재앙연결': ['해당없음', '6재앙(독종)', '1재앙(피)']
    })

    print("🔮 세 가지 표적 상세 분석")
    print("=" * 60)
    print(signs_detail)

    return signs_detail


def analyze_sign_progression():
    """표적의 점진적 강화 패턴"""

    # 강도 분석
    intensity = pd.Series([3, 5, 10],
                          index=['표적1', '표적2', '표적3'],
                          name='강도')

    # 범위 분석
    scope = pd.Series([1, 2, 5],
                      index=['표적1', '표적2', '표적3'],
                      name='범위')

    # 종합 영향력
    impact = intensity * scope
    impact.name = '영향력'

    progression_df = pd.DataFrame({
        '강도': intensity,
        '범위': scope,
        '영향력': impact
    })

    print("\n📊 표적의 점진적 강화:")
    print(progression_df)
    print(f"\n평균 영향력: {impact.mean():.1f}")
    print(f"증가율: {(impact.iloc[-1] / impact.iloc[0] - 1) * 100:.0f}%")

    return progression_df


def compare_exodus_john_signs():
    """출애굽기와 요한복음 표적 비교"""

    comparison = pd.DataFrame({
        '구분': ['첫표적', '대상', '물질', '목적', '반응'],
        '모세': ['지팡이→뱀', '자기자신', '목자도구', '소명확인', '두려움→순종'],
        '예수': ['물→포도주', '혼인잔치', '정결예식물', '영광나타냄', '제자들믿음']
    })

    print("\n✝️ 모세와 예수의 첫 표적 비교:")
    print(comparison)

    # 요한복음 7표적
    john_signs = pd.Series({
        '물→포도주': '가나',
        '왕의신하아들': '가버나움',
        '38년된병자': '베데스다',
        '오병이어': '갈릴리',
        '물위를걷심': '갈릴리바다',
        '맹인치유': '예루살렘',
        '나사로': '베다니'
    }, name='장소')

    print("\n📖 요한복음 7가지 표적:")
    for sign, place in john_signs.items():
        print(f"  {sign}: {place}")

    return comparison, john_signs


def simulate_transformation():
    """표적의 변환 과정 시뮬레이션"""

    print("\n🔄 변환 시뮬레이션:")
    print("-" * 40)

    # 지팡이 변환
    staff_states = pd.Series({
        't0_초기': '지팡이',
        't1_던짐': '떨어짐',
        't2_변환': '뱀',
        't3_도망': '모세도망',
        't4_명령': '꼬리를잡으라',
        't5_복원': '지팡이'
    })

    print("지팡이 변환 과정:")
    for time, state in staff_states.items():
        print(f"  {time}: {state}")

    # 손 변환
    hand_transform = pd.DataFrame({
        '시간': ['t0', 't1', 't2', 't3'],
        '동작': ['품에 넣음', '꺼냄', '다시 넣음', '꺼냄'],
        '상태': ['정상', '나병', '나병', '정상'],
        '의미': ['원래상태', '부정', '은폐', '회복']
    })

    print("\n✋ 손 변환 과정:")
    print(hand_transform)

    return staff_states, hand_transform


def analyze_theological_meaning():
    """표적의 신학적 의미 분석"""

    theology = pd.DataFrame({
        '표적': ['지팡이', '손', '물'],
        '구약배경': ['목자의 권위', '제사장 검증', '생명의 근원'],
        '신약성취': ['선한 목자', '정결케 하시는 이', '생명수'],
        '종말론적의미': ['철장 권세', '거룩한 백성', '생명강']
    })

    print("\n📜 표적의 삼중적 의미:")
    print(theology)

    return theology


def main():
    print("=" * 60)
    print("  세 가지 표적 - 하나님의 능력 증거")
    print("=" * 60)

    # 분석 실행
    signs = create_signs_matrix()
    progression = analyze_sign_progression()
    comparison, john_signs = compare_exodus_john_signs()
    staff, hand = simulate_transformation()
    theology = analyze_theological_meaning()

    # 요약
    print("\n💡 핵심 통찰:")
    print("1. 표적은 점진적으로 강화된다 (개인→집단→국가)")
    print("2. 각 표적은 하나님의 다른 속성을 계시한다")
    print("3. 복원 가능성이 줄어든다 (완전→부분→불가)")
    print("4. 모세의 표적은 심판, 예수의 표적은 은혜")


if __name__ == "__main__":
    main()