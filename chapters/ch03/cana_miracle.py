# ch03_cana_miracle.py
"""
가나의 혼인잔치 - 첫 번째 표적
"""

import pandas as pd
import numpy as np


def analyze_water_jars():
    """6개 항아리 분석"""

    # 항아리 정보
    jars_df = pd.DataFrame({
        '항아리': [f'항아리{i + 1}' for i in range(6)],
        '용량_리터': [40] * 6,
        '용도': ['정결예식'] * 6,
        '재질': ['돌'] * 6,
        '상태': ['비어있음'] * 6
    })

    print("💧 6개 돌 항아리 분석")
    print("=" * 50)
    print(jars_df)

    total_capacity = jars_df['용량_리터'].sum()
    print(f"\n총 용량: {total_capacity} 리터")
    print(f"포도주 병 환산: 약 {total_capacity / 0.75:.0f} 병")

    # 상징적 의미
    symbolism = pd.Series({
        '6의 의미': '불완전수 (7-1)',
        '돌의 의미': '율법 (돌판)',
        '물의 의미': '정결 의식',
        '포도주 의미': '새 언약의 기쁨'
    })

    print("\n📖 상징적 의미:")
    for key, value in symbolism.items():
        print(f"  {key}: {value}")

    return jars_df, symbolism


def analyze_transformation_process():
    """물이 포도주로 변하는 과정"""

    process = pd.DataFrame({
        '단계': [1, 2, 3, 4, 5],
        '시간': ['혼인잔치', '포도주떨어짐', '마리아요청', '물채움', '떠서가져감'],
        '행위자': ['손님들', '하인들', '마리아', '하인들', '하인들'],
        '예수의_말씀': ['-', '-', '나와 무슨 상관', '항아리에 물을 채우라', '떠서 연회장에게 갖다주라'],
        '결과': ['축제진행', '위기발생', '믿음표현', '순종', '기적확인']
    })

    print("\n🍷 변환 과정 분석:")
    print(process)

    # 품질 변화
    quality = pd.Series({
        '물': 0,
        '일반포도주': 50,
        '좋은포도주': 75,
        '최상급포도주': 100
    })

    print("\n📊 품질 지수:")
    print(quality)
    print(f"품질 향상: {quality.iloc[-1] - quality.iloc[0]} 포인트")

    return process, quality


def compare_water_blood_transformation():
    """물의 변환: 출애굽 vs 가나"""

    comparison = pd.DataFrame({
        '항목': ['장소', '시기', '물질변화', '목적', '대상', '메시지'],
        '출애굽_물→피': ['나일강', '재앙시작', '물→피', '심판', '애굽인', '죽음과 심판'],
        '가나_물→포도주': ['혼인잔치', '사역시작', '물→포도주', '축복', '제자들', '생명과 기쁨']
    })

    print("\n⚖️ 물 변환 비교:")
    print(comparison.set_index('항목'))

    return comparison


def analyze_wedding_context():
    """혼인잔치의 문화적 배경"""

    cultural_context = pd.DataFrame({
        '요소': ['기간', '중요성', '포도주역할', '부족의미', '해결책'],
        '설명': [
            '보통 7일간 지속',
            '공동체 최대 축제',
            '기쁨과 축복의 상징',
            '가문의 수치',
            '예수의 개입'
        ]
    })

    print("\n🎊 혼인잔치 문화적 배경:")
    print(cultural_context)

    # 시간대별 포도주 소비 패턴 (가상)
    consumption = pd.Series({
        '첫째날': 100,
        '둘째날': 80,
        '셋째날': 60,
        '넷째날': 40,
        '다섯째날': 30,
        '여섯째날': 20,
        '일곱째날': 10
    })

    print("\n📉 일반적 포도주 소비 패턴:")
    print(consumption)

    return cultural_context, consumption


def analyze_disciples_faith():
    """제자들의 믿음 성장"""

    faith_growth = pd.DataFrame({
        '사건': ['부름받음', '가나표적', '성전청결', '사마리아', '오병이어', '고백'],
        '믿음수준': [20, 40, 50, 60, 75, 90],
        '핵심깨달음': [
            '메시아 만남',
            '영광 목격',
            '권위 확인',
            '구원의 보편성',
            '능력 체험',
            '그리스도 고백'
        ]
    })

    print("\n📈 제자들의 믿음 성장:")
    print(faith_growth)

    # 믿음 성장률
    growth_rate = faith_growth['믿음수준'].pct_change() * 100
    faith_growth['성장률%'] = growth_rate.fillna(0).round(1)

    print("\n믿음 성장률:")
    print(faith_growth[['사건', '믿음수준', '성장률%']])

    return faith_growth


def main():
    print("=" * 60)
    print("  가나의 혼인잔치 - 영광의 시작")
    print("=" * 60)

    # 분석 실행
    jars, symbolism = analyze_water_jars()
    process, quality = analyze_transformation_process()
    comparison = compare_water_blood_transformation()
    context, consumption = analyze_wedding_context()
    faith = analyze_disciples_faith()

    # 핵심 메시지
    print("\n✨ 핵심 메시지:")
    print("1. 첫 표적이 혼인잔치 = 메시아 시대는 혼인잔치")
    print("2. 율법(돌항아리+정결수)에서 은혜(포도주)로")
    print("3. 최상품 포도주 = 복음은 율법보다 우월")
    print("4. '나의 때' = 십자가를 향한 여정의 시작")


if __name__ == "__main__":
    main()