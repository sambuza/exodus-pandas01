import pandas as pd
import numpy as np

def create_biblical_characters_df():
    """성경 인물 DataFrame 생성"""
    characters = pd.DataFrame({
        '이름': ['모세', '아론', '바로', '안드레', '베드로', '빌립', '나다나엘', '마리아', '요셉'],
        '등장_챕터': ['출4', '출4', '출4', '요1', '요1', '요1', '요1', '마1', '마1'],
        '역할': ['선지자', '대변자', '왕', '제자', '제자', '제자', '제자', '예수님 어머니', '예수님 아버지'],
        '특징': ['말못함', '웅변', '강퍅함', '전도자', '반석', '이성적', '의심함', '순종적', '의로운'],
        '중요도': [10, 8, 9, 7, 9, 7, 8, 10, 9],
        '소명_여부': [True, True, False, True, True, True, True, True, True]
    })
    return characters

def demo_column_selection():
    """열 선택 데모: 특정 열만 선택하여 DataFrame 생성"""
    print("\n✂️ 열 선택 데모: 특정 정보만 집중하기")
    print("=" * 50)
    characters = create_biblical_characters_df()

    # '이름'과 '역할' 열만 선택
    names_roles = characters[['이름', '역할']]
    print("\n--- 이름과 역할만 선택 ---")
    print(names_roles)

    # 중요도가 높은 인물들의 '이름'과 '특징' 선택
    important_characters = characters[characters['중요도'] >= 9]
    important_names_features = important_characters[['이름', '특징', '중요도']]
    print("\n--- 중요도 9 이상 인물의 이름과 특징 ---")
    print(important_names_features)
    return names_roles, important_names_features

def demo_row_slicing():
    """행 슬라이싱 데모: 특정 범위의 행 선택"""
    print("\n📊 행 슬라이싱 데모: 특정 구간의 사건/인물 탐색")
    print("=" * 50)
    characters = create_biblical_characters_df()

    # 처음 3명의 인물만 선택 (모세, 아론, 바로)
    first_three = characters.iloc[0:3]
    print("\n--- 처음 3명의 인물 ---")
    print(first_three)

    # 중간 인물들 (인덱스 3부터 6까지, 안드레, 베드로, 빌립, 나다나엘)
    middle_characters = characters.iloc[3:7]
    print("\n--- 중간 인물들 (요한복음 1장 제자들) ---")
    print(middle_characters)
    return first_three, middle_characters

def demo_boolean_filtering():
    """불리언 필터링 데모: 특정 조건에 맞는 행 선택"""
    print("\n🎯 불리언 필터링 데모: 하나님의 기준에 맞는 데이터 찾기")
    print("=" * 50)
    characters = create_biblical_characters_df()

    # 소명 받은 인물만 필터링
    called_ones = characters[characters['소명_여부'] == True]
    print("\n--- 소명 받은 인물 ---")
    print(called_ones[['이름', '역할', '소명_여부']])

    # 등장 챕터가 '출4'이면서 소명 받은 인물 필터링 (모세, 아론)
    exodus_called = characters[(characters['등장_챕터'] == '출4') & (characters['소명_여부'] == True)]
    print("\n--- 출애굽기 4장에서 소명 받은 인물 ---")
    print(exodus_called[['이름', '역할', '등장_챕터', '소명_여부']])

    # 중요도가 8 이상이면서 제자인 인물 필터링
    important_disciples = characters[(characters['중요도'] >= 8) & (characters['역할'] == '제자')]
    print("\n--- 중요도 8 이상인 제자 ---")
    print(important_disciples[['이름', '역할', '중요도']])

    return called_ones, exodus_called, important_disciples

def main():
    demo_column_selection()
    demo_row_slicing()
    demo_boolean_filtering()

if __name__ == "__main__":
    main()
