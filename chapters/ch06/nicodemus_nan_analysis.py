import pandas as pd
import numpy as np

def analyze_nicodemus_missing_understanding():
    """요한복음 3:1-8 니고데모의 결핍된 이해 분석: 영적 NaN"""
    print("\n🕯️ 니고데모의 영적 결핍: '거듭남'이라는 NaN")
    print("=" * 50)

    nicodemus_dialogue = pd.DataFrame({
        '말씀_주체': ['니고데모', '예수님', '니고데모', '예수님'],
        '내용': ['랍비여 우리가 당신은 하나님께로서 오신 선생인줄 아나이다', '진실로 진실로 네게 이르노니 사람이 거듭나지 아니하면 하나님 나라를 볼수 없느니라', '사람이 늙으면 어떻게 날 수 있삽나이까', '바람이 임의로 불매 성령으로 난 사람은 다 이러하니라'],
        '이해_수준': [7, np.nan, 3, np.nan], # 1-10 스케일, np.nan은 이해 부족
        '영적_상태': ['지도자', '가르치심', '육적인 생각', '성령의 역사']
    })
    print(nicodemus_dialogue)
    print("\n📊 DataFrame의 결측치(NaN) 확인:")
    print(nicodemus_dialogue.isna())

    # 이해 수준이 결측치인 행만 필터링
    missing_understanding = nicodemus_dialogue[nicodemus_dialogue['이해_수준'].isna()]
    print("\n🤔 이해 수준에 결측치가 있는 대화:")
    print(missing_understanding)

    # 결측치를 특정 값으로 채우기 (예: 5점)
    nicodemus_dialogue['이해_수준_fillna'] = nicodemus_dialogue['이해_수준'].fillna(5)
    print("\n🔄 '이해_수준' 결측치를 5점으로 채운 후:")
    print(nicodemus_dialogue[['말씀_주체', '이해_수준', '이해_수준_fillna']])
    print("   -> 니고데모의 'NaN' 이해가 예수님의 가르침으로 '채워지는' 것을 비유")

    # '성령의 역사'에 대한 이해가 '결측치 아님'으로 간주되는 행만 선택
    spiritual_insight = nicodemus_dialogue[nicodemus_dialogue['영적_상태'].notna() & (nicodemus_dialogue['영적_상태'] == '성령의 역사')]
    print("\n✨ '성령의 역사'를 언급하며 영적 통찰을 보여주는 대화:")
    print(spiritual_insight)

    return nicodemus_dialogue

def main():
    analyze_nicodemus_missing_understanding()

if __name__ == "__main__":
    main()
