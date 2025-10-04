import pandas as pd
import numpy as np

def analyze_moses_call():
    """모세의 소명 분석: 호렙산에서 하나님과의 만남"""
    print("\n🔥 모세의 소명: 불타는 떨기나무 앞에서")
    print("=" * 50)

    call_data = pd.DataFrame({
        '요소': ['장소', '현상', '하나님의_말씀', '모세의_반응', '소명_내용'],
        '내용': [
            '호렙산 (하나님의 산)',
            '불타는 떨기나무 (타지 않음)',
            '내가 너를 바로에게 보내리라',
            '신을 벗음, 두려워 얼굴을 가림',
            '이스라엘 백성을 애굽에서 인도'
        ]
    })
    print(call_data)
    print(f"\n💡 소명 요약: {call_data.loc[4, '내용']}")
    return call_data

def analyze_moses_objections():
    """모세의 다섯 가지 항변과 하나님의 응답 분석"""
    print("\n🗣️ 모세의 다섯 가지 항변과 하나님의 응답")
    print("=" * 50)

    objections = pd.DataFrame({
        '항변_순서': [1, 2, 3, 4, 5],
        '모세의_항변': [
            '내가 누구관대 바로에게 가며',
            '그들이 나를 믿지 아니하며 내 말을 듣지 아니하고',
            '나는 본래 말에 능치 못한 자라',
            '보낼만한 자를 보내소서',
            '그의 이름이 무엇이냐 하리니 내가 무엇이라고 그들에게 말하리이까' # Moved from ch03, better fit here for context
        ],
        '하나님의_응답': [
            '내가 정녕 너와 함께 있으리라',
            '세 가지 표적(지팡이-뱀, 손-나병, 물-피)을 주리라',
            '누가 사람의 입을 지었느냐? 내가 네 입과 함께하며 할 말을 가르치리라',
            '네 형 아론이 너와 함께 갈 것이며 네 대변인이 되리라',
            '나는 스스로 있는 자 (I AM WHO I AM)' # Moved from ch03, better fit here for context
        ],
        '항변_유형': ['정체성 부족', '증거 부족', '능력 부족', '회피', '지식 부족'],
        '하나님의_속성_계시': ['임재', '권능', '창조주', '섭리', '자존성']
    })
    print(objections)

    # 특정 항변 유형만 선택
    lack_objections = objections[objections['항변_유형'].str.contains('부족')]
    print("\n🔍 '부족' 유형 항변들:")
    print(lack_objections[['모세의_항변', '하나님의_응답']])

    # 하나님의 응답 중 '함께'라는 키워드가 포함된 응답 필터링
    gods_presence_responses = objections[objections['하나님의_응답'].str.contains('함께')]
    print("\n💖 하나님의 '함께' 응답:")
    print(gods_presence_responses[['모세의_항변', '하나님의_응답']])

    return objections

def main():
    analyze_moses_call()
    analyze_moses_objections()

if __name__ == "__main__":
    main()
