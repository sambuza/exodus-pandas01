
'''
Chapter 36 통합 실행 스크립트
장인의 손 - 결합·재구성 심화
'''

import sys
from pathlib import Path
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch36.craftsmen_data import CraftsmenDataGenerator
from chapters.ch36.tabernacle_construction_data import TabernacleConstructionDataGenerator
from chapters.ch36.advanced_joining import AdvancedJoining
from chapters.ch36.advanced_reshaping import AdvancedReshaping

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        """
        ╔══════════════════════════════════════════════════════════════════════╗
        ║                    JesusBornd Pandas Edition                         ║
        ║                                                                      ║
        ║             Chapter 36: 장인의 손 - 결합·재구성 심화                 ║
        ║                                                                      ║
        ║    "모세가 브살렐과 오홀리압과 및 마음이 지혜로운 사람 곧 그 마음에 여호와께로부터 지혜를 얻고 와서 그 일을 하려고 마음에 원하는 모든 자를 부르매" (출애굽기 36:2)
        ║    "예수께서 대답하여 이르시되 너희가 이 성전을 헐라 내가 사흘 동안에 일으키리라" (요한복음 2:19)
        ╚══════════════════════════════════════════════════════════════════════╝
        """
    )
    print(header)

def run_chapter36(interactive: bool = True):
    """Chapter 36 전체 실행"""
    print_chapter_header()

    if interactive:
        input("\n▶️ Chapter 36을 시작하려면 Enter를 눌러주세요...")

    # 데이터 생성
    craftsmen_df = CraftsmenDataGenerator().generate_craftsmen_data()
    construction_df = TabernacleConstructionDataGenerator().generate_construction_data()

    print("\n--- 장인 데이터 ---")
    print(craftsmen_df.head())
    print("\n--- 성막 건축 데이터 ---")
    print(construction_df.head())

    if interactive:
        input("\n▶️ 데이터 조인을 시작하려면 Enter를 눌러주세요...")

    # 데이터 조인
    joining = AdvancedJoining(construction_df, craftsmen_df)
    merged_df = joining.merge_dataframes(left_on='assigned_craftsman_id', right_on='craftsman_id')
    print("\n--- 조인된 데이터 ---")
    print(merged_df.head())

    if interactive:
        input("\n▶️ 데이터 재구성을 시작하려면 Enter를 눌러주세요...")

    # 데이터 재구성 (피벗 테이블)
    reshaping = AdvancedReshaping(merged_df)
    pivot_df = reshaping.create_pivot_table(values='quantity_needed', index='name', columns='component', aggfunc='sum')
    print("\n--- 재구성된 데이터 (피벗 테이블) ---")
    print(pivot_df)

    print("\n🎉 Chapter 36 완료!")

def main():
    """메인 실행 함수"""
    run_chapter36(interactive=False)

if __name__ == "__main__":
    main()
