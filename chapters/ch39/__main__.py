
'''
Chapter 39 통합 실행 스크립트
제사장의 옷 - 시계열 데이터 처리
'''

import sys
from pathlib import Path
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch39.priestly_garments_data import PriestlyGarmentsDataGenerator
from chapters.ch39.the_way_data import TheWayDataGenerator
from chapters.ch39.time_series_analysis import TimeSeriesAnalysis

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        """
        ╔══════════════════════════════════════════════════════════════════════╗
        ║                    JesusBornd Pandas Edition                         ║
        ║                                                                      ║
        ║             Chapter 39: 제사장의 옷 - 시계열 데이터 처리             ║
        ║                                                                      ║
        ║    "그들이 여호와께서 모세에게 명령하신 대로 청색 자색 홍색 실로 성소에서 섬기기 위한 정교한 옷을 만들고 또 아론을 위한 거룩한 옷을 만들었더라" (출애굽기 39:1) 
        ║    "예수께서 이르시되 내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라" (요한복음 14:6)
        ╚══════════════════════════════════════════════════════════════════════╝
        """
    )
    print(header)

def run_chapter39(interactive: bool = True):
    """Chapter 39 전체 실행"""
    print_chapter_header()

    if interactive:
        input("\n▶️ Chapter 39를 시작하려면 Enter를 눌러주세요...")

    # 데이터 생성
    garments_df = PriestlyGarmentsDataGenerator().generate_garments_data()
    the_way_df = TheWayDataGenerator().generate_the_way_data()

    print("\n--- 제사장의 옷 제작 데이터 ---")
    print(garments_df.head())
    print("\n--- 길, 진리, 생명 데이터 ---")
    print(the_way_df.head())

    if interactive:
        input("\n▶️ 시계열 분석을 시작하려면 Enter를 눌러주세요...")

    # 시계열 분석
    ts_analysis = TimeSeriesAnalysis(garments_df, date_column='date')
    resampled_df = ts_analysis.resample_data(rule='W', agg_func={'progress_percentage': 'mean'})
    print("\n--- 주별 제작 진행률 평균 ---")
    print(resampled_df)

    rolling_avg = ts_analysis.rolling_average(window=7, column='progress_percentage')
    print("\n--- 7일 이동 평균 진행률 ---")
    print(rolling_avg.tail())

    print("\n🎉 Chapter 39 완료!")

def main():
    """메인 실행 함수"""
    run_chapter39(interactive=False)

if __name__ == "__main__":
    main()
