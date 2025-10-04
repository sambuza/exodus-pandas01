import pandas as pd
import numpy as np

def analyze_spiritual_ranking():
    """요한복음 3:16-21 빛과 어둠의 영적 순위 분석"""
    print("\n💡 빛과 어둠의 영적 순위: 행위에 따른 심판")
    print("=" * 50)

    spiritual_status = pd.DataFrame({
        '행위_유형': ['하나님 사랑', '어둠을 사랑', '진리를 행함', '악을 행함', '예수님 믿음', '빛을 미워함'],
        '영적_가치': [10, 1, 9, 2, 9.5, 0.5], # 0-10 스케일
        '결과': ['빛으로 나옴', '어둠에 머뭄', '하나님 안에 있음', '정죄 받음', '영생 얻음', '정죄 받음'],
        '구원_가능성_지수': [0.9, 0.1, 0.8, 0.2, 1.0, 0.0] # 0-1 스케일
    })
    print(spiritual_status)

    # '영적_가치'를 기준으로 내림차순 정렬
    sorted_by_spiritual_value = spiritual_status.sort_values(by='영적_가치', ascending=False)
    print("\n📈 영적 가치 기준으로 정렬 (내림차순):")
    print(sorted_by_spiritual_value[['행위_유형', '영적_가치', '결과']])

    # '구원_가능성_지수'에 따른 순위 매기기 (내림차순, 동일 순위는 가장 높은 순위 부여)
    spiritual_status['구원_가능성_순위'] = spiritual_status['구원_가능성_지수'].rank(ascending=False, method='first')
    print("\n🏆 구원 가능성 순위:")
    print(spiritual_status[['행위_유형', '구원_가능성_지수', '구원_가능성_순위']].sort_values(by='구원_가능성_순위'))

    # 가장 구원 가능성이 높은 2가지 행위 찾기 (`nlargest`)
    top_spiritual_acts = spiritual_status.nlargest(2, '구원_가능성_지수')
    print("\n✨ 가장 높은 구원 가능성을 가진 행위 2가지:")
    print(top_spiritual_acts[['행위_유형', '구원_가능성_지수']])

    return spiritual_status

def main():
    analyze_spiritual_ranking()

if __name__ == "__main__":
    main()
