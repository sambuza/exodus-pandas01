import pandas as pd
import numpy as np

def analyze_john_disciples_calling():
    """요한복음 1:40-51: 제자들의 부름과 나다나엘의 고백"""
    print("\n👥 제자들의 부름과 고백")
    print("=" * 50)

    disciples_data = pd.DataFrame({
        '이름': ['안드레', '시몬 베드로', '빌립', '나다나엘'],
        '부름_계기': [
            '요한의 증거(어린양)',
            '안드레의 소개',
            '예수님의 직접 부르심',
            '빌립의 소개(나사렛에서 뭔 선한 것)'
        ],
        '예수님_반응': [
            '와서 보라',
            '게바(반석)라 부르심',
            '나를 따르라',
            '참 이스라엘 사람이라 (무화과나무 아래)'
        ],
        '고백': [
            '메시아 발견',
            '메시아 확인',
            '메시아 믿음',
            '하나님의 아들, 이스라엘의 임금'
        ],
        '믿음_수준': [7, 7, 8, 9] # 1-10 스케일
    })
    print(disciples_data)

    # 초기 고백이 '메시아'인 제자들 선택
    messiah_confessors = disciples_data[disciples_data['고백'].str.contains('메시아')]
    print("\n🎯 '메시아' 고백 제자들:")
    print(messiah_confessors[['이름', '고백']])

    # 믿음 수준이 8 이상인 제자들 선택
    strong_faith = disciples_data[disciples_data['믿음_수준'] >= 8]
    print("\n📈 믿음 수준 8 이상인 제자들:")
    print(strong_faith[['이름', '믿음_수준', '고백']])

    return disciples_data

def main():
    analyze_john_disciples_calling()

if __name__ == "__main__":
    main()
