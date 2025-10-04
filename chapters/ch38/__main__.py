
'''
Chapter 38 통합 실행 스크립트
성막 건축 비용 - 그룹 연산 및 집계
'''

import sys
from pathlib import Path
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch38.construction_costs_data import ConstructionCostsDataGenerator
from chapters.ch38.salvation_sacrifices_data import SalvationSacrificesDataGenerator
from chapters.ch38.cost_analysis import CostAnalysis

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        """
        ╔══════════════════════════════════════════════════════════════════════╗
        ║                    JesusBornd Pandas Edition                         ║
        ║                                                                      ║
        ║             Chapter 38: 성막 건축 비용 - 그룹 연산 및 집계           ║
        ║                                                                      ║
        ║    "성소에 쓴 금은 성소의 세겔로 스물아홉 달란트와 칠백삼십 세겔이며" (출애굽기 38:24)
        ║    "예수께서 신 포도주를 받으신 후에 이르시되 다 이루었다 하시고 머리를 숙이니 영혼이 떠나가시니라" (요한복음 19:30)
        ╚══════════════════════════════════════════════════════════════════════╝
        """
    )
    print(header)

def run_chapter38(interactive: bool = True):
    """Chapter 38 전체 실행"""
    print_chapter_header()

    if interactive:
        input("\n▶️ Chapter 38을 시작하려면 Enter를 눌러주세요...")

    # 데이터 생성
    costs_df = ConstructionCostsDataGenerator().generate_costs_data()
    sacrifices_df = SalvationSacrificesDataGenerator().generate_sacrifices_data()

    print("\n--- 성막 건축 비용 데이터 ---")
    print(costs_df.head())
    print("\n--- 구원의 희생 데이터 ---")
    print(sacrifices_df.head())

    if interactive:
        input("\n▶️ 비용 분석을 시작하려면 Enter를 눌러주세요...")

    # 비용 분석
    analysis = CostAnalysis(costs_df)
    cost_summary = analysis.analyze_costs_by_item()
    print("\n--- 항목별 비용 분석 결과 ---")
    print(cost_summary)

    print("\n🎉 Chapter 38 완료!")

def main():
    """메인 실행 함수"""
    run_chapter38(interactive=False)

if __name__ == "__main__":
    main()
