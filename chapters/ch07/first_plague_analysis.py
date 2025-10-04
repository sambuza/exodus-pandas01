import pandas as pd
import numpy as np

def analyze_plague_severity():
    """출애굽기 7장 첫 재앙의 강도 분석: 정렬된 심판"""
    print("\n🌊 첫 재앙, 나일강의 피: 정렬된 심판의 시작")
    print("=" * 50)

    plague_data = pd.DataFrame({
        '재앙_번호': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        '재앙_이름': ['피', '개구리', '이', '파리', '돌림병', '독종', '우박', '메뚜기', '흑암', '장자 죽음'],
        '영향_범위': ['나일강', '애굽 전역', '애굽 전역', '애굽 전역', '가축', '애굽인', '애굽 전역', '애굽 전역', '애굽 전역', '애굽 전역'],
        '피해_강도': [8, 6, 4, 7, 9, 8, 9.5, 9.2, 7.5, 10], # 1-10 스케일
        '파라오_반응_강도': [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] # 1-10 스케일, 거부 강도
    })
    print(plague_data)

    # '피해_강도'를 기준으로 재앙을 내림차순 정렬
    sorted_by_severity = plague_data.sort_values(by='피해_강도', ascending=False)
    print("\n📈 피해 강도 기준으로 재앙 정렬 (내림차순):")
    print(sorted_by_severity[['재앙_이름', '피해_강도']])

    # '파라오_반응_강도'를 기준으로 오름차순 정렬
    sorted_by_pharaoh_response = plague_data.sort_values(by='파라오_반응_강도', ascending=True)
    print("\n⚖️ 파라오 반응 강도 기준으로 재앙 정렬 (오름차순):")
    print(sorted_by_pharaoh_response[['재앙_이름', '파라오_반응_강도']])

    # '피해_강도'에 따른 순위 매기기
    plague_data['피해_강도_순위'] = plague_data['피해_강도'].rank(ascending=False, method='min')
    print("\n🏆 피해 강도 순위:")
    print(plague_data[['재앙_이름', '피해_강도', '피해_강도_순위']].sort_values(by='피해_강도_순위'))

    return plague_data

def analyze_pharaoh_response_ranking():
    """출애굽기 7장 파라오의 반응 순위 분석: 고정된 마음의 순위"""
    print("\n🗿 파라오의 강퍅한 마음: 재앙 속 반응 순위")
    print("=" * 50)

    pharaoh_response = pd.DataFrame({
        '재앙_이름': ['피', '개구리', '이', '파리', '돌림병', '독종', '우박', '메뚜기', '흑암', '장자 죽음'],
        '마음_굳기_점수': [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], # 1-10 스케일 (점수가 높을수록 더 굳은 마음)
        '고백_가능성': [0.1, 0.2, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.6, 0.7]
    })
    print(pharaoh_response)

    # '마음_굳기_점수'에 따른 순위 매기기 (오름차순, 동일 순위는 평균)
    pharaoh_response['굳기_순위'] = pharaoh_response['마음_굳기_점수'].rank(ascending=True, method='average')
    print("\n🏆 파라오 마음 굳기 순위 (오름차순):")
    print(pharaoh_response[['재앙_이름', '마음_굳기_점수', '굳기_순위']].sort_values(by='굳기_순위'))

    # 가장 마음이 굳은 3가지 재앙 시기 찾기 (`nlargest`)
    hardest_hearts = pharaoh_response.nlargest(3, '마음_굳기_점수')
    print("\n🚨 가장 마음이 굳은 3가지 재앙 시기:")
    print(hardest_hearts[['재앙_이름', '마음_굳기_점수']])

    return pharaoh_response

def main():
    analyze_plague_severity()
    analyze_pharaoh_response_ranking()

if __name__ == "__main__":
    main()
