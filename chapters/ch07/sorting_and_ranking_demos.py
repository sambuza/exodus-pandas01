import pandas as pd
import numpy as np

def demo_sort_values():
    """sort_values 데모: 재앙의 심각성 순서"""
    print("\n📈 `sort_values()` 데모: 재앙의 심각성 순서")
    print("=" * 50)

    plague_impact = pd.DataFrame({
        '재앙_이름': ['피', '개구리', '이', '파리', '돌림병'],
        '피해_점수': [8, 6, 4, 7, 9], # 1-10
        '발생_순서': [1, 2, 3, 4, 5]
    })
    print(plague_impact)

    # '피해_점수'를 기준으로 내림차순 정렬
    sorted_by_damage = plague_impact.sort_values(by='피해_점수', ascending=False)
    print("\n🔄 '피해_점수' 내림차순 정렬:")
    print(sorted_by_damage)

    # '발생_순서'를 기준으로 오름차순 정렬
    sorted_by_order = plague_impact.sort_values(by='발생_순서', ascending=True)
    print("\n🔄 '발생_순서' 오름차순 정렬:")
    print(sorted_by_order)

    return plague_impact

def demo_sort_index():
    """sort_index 데모: 말씀 순서대로 정렬"""
    print("\n📜 `sort_index()` 데모: 말씀 순서대로 정렬")
    print("=" * 50)

    bible_verses = pd.DataFrame({
        '내용': ['하나님 사랑', '독생자를 주셨으니', '영생을 얻으리라', '심판'],
        '중요도': [10, 9, 8, 7]
    }, index=['요3:16a', '요3:16b', '요3:16c', '요3:17'])

    # 인덱스 순서를 섞음
    shuffled_verses = bible_verses.sample(frac=1, random_state=42)
    print(shuffled_verses)

    # 인덱스를 기준으로 정렬
    sorted_by_index = shuffled_verses.sort_index()
    print("\n🔄 인덱스 기준으로 정렬:")
    print(sorted_by_index)

    return bible_verses

def demo_rank():
    """rank 데모: 영적 성숙도 순위 매기기"""
    print("\n🏆 `rank()` 데모: 영적 성숙도 순위 매기기")
    print("=" * 50)

    spiritual_growth = pd.DataFrame({
        '인물': ['베드로', '요한', '야고보', '도마', '바울'],
        '성숙도_점수': [85, 92, 88, 70, 95], # 0-100
        '봉사_헌신도': [90, 85, 88, 75, 98]
    })
    print(spiritual_growth)

    # '성숙도_점수'에 따른 순위 (내림차순, 동일 점수는 평균 순위 부여)
    spiritual_growth['성숙도_순위'] = spiritual_growth['성숙도_점수'].rank(ascending=False, method='average')
    print("\n🔄 '성숙도_점수' 순위:")
    print(spiritual_growth[['인물', '성숙도_점수', '성숙도_순위']].sort_values(by='성숙도_순위'))

    # '봉사_헌신도'에 따른 순위 (오름차순, 동일 점수는 가장 낮은 순위 부여)
    spiritual_growth['헌신도_순위'] = spiritual_growth['봉사_헌신도'].rank(ascending=True, method='min')
    print("\n🔄 '봉사_헌신도' 순위:")
    print(spiritual_growth[['인물', '봉사_헌신도', '헌신도_순위']].sort_values(by='헌신도_순위'))

    # 가장 높은 순위 (숫자가 작을수록 높음) 2명 찾기 (성숙도 기준)
    top_2_mature = spiritual_growth.nsmallest(2, '성숙도_순위')
    print("\n✨ 가장 성숙도가 높은 2명:")
    print(top_2_mature[['인물', '성숙도_점수', '성숙도_순위']])

    return spiritual_growth

def main():
    demo_sort_values()
    demo_sort_index()
    demo_rank()

if __name__ == "__main__":
    main()
