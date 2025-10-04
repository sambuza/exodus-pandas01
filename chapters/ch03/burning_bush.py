# ch03_burning_bush.py
"""
불타는 떨기나무 - 하나님의 현현과 이름 계시
"""

import pandas as pd
import numpy as np


def analyze_burning_bush():
    """불타는 떨기나무 사건 분석"""

    # 하나님의 이름들
    divine_names = pd.DataFrame({
        '히브리어': ['אֶהְיֶה', 'יהוה', 'אֱלֹהִים', 'אֵל שַׁדַּי'],
        '음역': ['에흐예', '야훼', '엘로힘', '엘 샤다이'],
        '의미': ['나는 있다', '자존하시는 분', '전능하신 하나님', '전능자'],
        '출현횟수': [3, 6828, 2598, 48],
        '첫등장': ['출3:14', '창2:4', '창1:1', '창17:1']
    })

    print("🔥 하나님의 이름 계시")
    print("=" * 50)
    print(divine_names)

    # 모세의 반응 단계
    moses_response = pd.Series({
        '목격': '이상한 광경을 보러 가야겠다',
        '부름': '내가 여기 있나이다',
        '경외': '신을 벗었다',
        '두려움': '얼굴을 가렸다',
        '의문': '내가 누구이기에'
    })

    print("\n📍 모세의 반응 과정:")
    for stage, response in moses_response.items():
        print(f"  {stage}: {response}")

    # 거룩한 땅의 의미
    holy_ground = pd.DataFrame({
        '요소': ['장소', '현상', '명령', '이유'],
        '내용': ['호렙산', '불타는 떨기나무', '신을 벗으라', '거룩한 땅'],
        '영적의미': ['하나님의 산', '영원한 임재', '경외와 순종', '구별된 공간']
    })

    print("\n⛰️ 거룩한 땅:")
    print(holy_ground)

    return divine_names, moses_response, holy_ground


def analyze_divine_revelation():
    """하나님의 자기 계시 분석"""

    revelation_structure = pd.DataFrame({
        '구분': ['정체성', '관계성', '영원성', '구원성'],
        '계시내용': [
            '나는 스스로 있는 자니라',
            '나는 네 조상의 하나님',
            '이는 나의 영원한 이름',
            '내가 내려와서 그들을 건져내고'
        ],
        '성경구절': ['출3:14', '출3:6', '출3:15', '출3:8']
    })

    print("\n✨ 하나님의 자기 계시 구조:")
    print(revelation_structure)

    return revelation_structure


def compare_theophanies():
    """구약의 하나님 현현 비교"""

    theophanies = pd.DataFrame({
        '사건': ['불타는 떨기나무', '시내산', '엘리야의 세미한 음성', '에스겔의 환상'],
        '장소': ['호렙산', '시내산', '호렙산', '그발강'],
        '현상': ['불', '불과 연기', '세미한 음성', '폭풍과 불'],
        '대상': ['모세', '이스라엘', '엘리야', '에스겔'],
        '목적': ['소명', '언약', '위로', '심판예고']
    })

    print("\n🌟 구약의 주요 신현 사건:")
    print(theophanies)

    return theophanies


def main():
    print("=" * 60)
    print("  불타는 떨기나무 - 거룩한 만남")
    print("=" * 60)

    # 분석 실행
    names, response, ground = analyze_burning_bush()
    revelation = analyze_divine_revelation()
    theophanies = compare_theophanies()

    # 핵심 통찰
    print("\n💡 핵심 통찰:")
    print("1. 불은 소멸시키지 않고 정화시킨다")
    print("2. 거룩한 공간은 일상적 태도를 요구하지 않는다")
    print("3. 하나님의 이름은 그분의 본질을 계시한다")
    print("4. 에흐예(אֶהְיֶה) - 영원한 현재로 존재하시는 분")


if __name__ == "__main__":
    main()