# ch03_signs_series.py
"""
Chapter 03. 신(神)의 능력과 표적 — Series와 DataFrame의 변환

출애굽 여정: 출 3-4장 - 불타는 떨기나무와 세 표적
요한복음 데이터: 요 2:1-11 - 가나의 첫 표적
"""

import pandas as pd
import numpy as np


def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("  Chapter 03: 신의 능력과 표적")
    print("  Series와 DataFrame의 변환")
    print("=" * 60)

    # 1. 모세와 하나님의 대화 Series
    create_dialogue_series()

    # 2. 세 가지 표적 분석
    analyze_three_signs()

    # 3. 가나 혼인잔치 표적
    analyze_cana_miracle()

    # 4. Series와 DataFrame 변환 실습
    practice_transformations()

    print("\n✨ Chapter 3 완료!")
    print("다음 장: Chapter 4 - 재앙의 알고리즘")


def create_dialogue_series():
    """모세와 하나님의 대화를 Series로 구성"""
    print("\n📜 1. 모세와 하나님의 대화")
    print("-" * 40)

    moses_objections = pd.Series({
        '변명1_정체성': '내가 누구이기에',
        '변명2_이름': '하나님의 이름이 무엇',
        '변명3_신뢰': '그들이 믿지 아니하면',
        '변명4_능력': '말을 잘 못하는 자',
        '변명5_거부': '보낼 만한 자를 보내소서'
    })

    gods_responses = pd.Series({
        '변명1_정체성': '내가 너와 함께',
        '변명2_이름': '나는 스스로 있는 자',
        '변명3_신뢰': '세 표적을 주노라',
        '변명4_능력': '누가 입을 지었느냐',
        '변명5_거부': '아론이 대언자가 되리라'
    })

    dialogue_df = pd.DataFrame({
        '모세': moses_objections,
        '하나님': gods_responses
    })

    print(dialogue_df)
    return dialogue_df


def analyze_three_signs():
    """세 가지 표적 분석"""
    print("\n🔮 2. 세 가지 표적 분석")
    print("-" * 40)

    signs_data = {
        ('표적1', '원형'): '지팡이',
        ('표적1', '변환'): '뱀',
        ('표적1', '의미'): '권위',
        ('표적2', '원형'): '정상_손',
        ('표적2', '변환'): '나병_손',
        ('표적2', '의미'): '정결',
        ('표적3', '원형'): '물',
        ('표적3', '변환'): '피',
        ('표적3', '의미'): '심판'
    }

    signs_series = pd.Series(signs_data)
    signs_df = signs_series.unstack()

    print("변환 매트릭스:")
    print(signs_df)

    return signs_df


def analyze_cana_miracle():
    """가나 혼인잔치 표적 분석"""
    print("\n🍷 3. 가나 혼인잔치 표적")
    print("-" * 40)

    water_jars = pd.Series([40] * 6,
                           index=[f'항아리{i + 1}' for i in range(6)])

    print(f"총 물의 양: {water_jars.sum()} 리터")

    transformation = pd.DataFrame({
        '단계': [1, 2, 3],
        '상태': ['물', '변환중', '포도주'],
        '품질': [0, 50, 100]
    })

    print("\n변환 과정:")
    print(transformation)

    return transformation


def practice_transformations():
    """Series와 DataFrame 변환 실습"""
    print("\n🔄 4. Series ↔ DataFrame 변환")
    print("-" * 40)

    # Series to DataFrame
    names = pd.Series(['אֶהְיֶה', 'יהוה', 'אֱלֹהִים'],
                      index=['에흐예', '야훼', '엘로힘'])

    # 방법1: to_frame()
    df1 = names.to_frame('히브리어')
    print("to_frame() 결과:")
    print(df1)

    # 방법2: reset_index()
    df2 = names.reset_index()
    df2.columns = ['한글', '히브리어']
    print("\nreset_index() 결과:")
    print(df2)

    return df2


if __name__ == "__main__":
    main()