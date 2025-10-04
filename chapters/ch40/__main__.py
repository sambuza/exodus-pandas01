
'''
Chapter 40 통합 실행 스크립트
성막 봉헌 - 데이터 파이프라인 및 함수 적용
'''

import sys
from pathlib import Path
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch40.tabernacle_dedication_data import TabernacleDedicationDataGenerator
from chapters.ch40.disciples_mission_data import DisciplesMissionDataGenerator
from chapters.ch40.data_pipeline import DataPipeline

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        """
        ╔══════════════════════════════════════════════════════════════════════╗
        ║                    JesusBornd Pandas Edition                         ║
        ║                                                                      ║
        ║             Chapter 40: 성막 봉헌 - 데이터 파이프라인 및 함수 적용   ║
        ║                                                                      ║
        ║    "모세가 이같이 행하되 곧 여호와께서 자기에게 명령하신 대로 다 행하였더라" (출애굽기 40:16)
        ║    "예수께서 또 이르시되 너희에게 평강이 있을지어다 아버지께서 나를 보내신 것 같이 나도 너희를 보내노라" (요한복음 20:21)
        ╚══════════════════════════════════════════════════════════════════════╝
        """
    )
    print(header)

def run_chapter40(interactive: bool = True):
    """Chapter 40 전체 실행"""
    print_chapter_header()

    if interactive:
        input("\n▶️ Chapter 40을 시작하려면 Enter를 눌러주세요...")

    # 데이터 생성
    dedication_df = TabernacleDedicationDataGenerator().generate_dedication_data()
    mission_df = DisciplesMissionDataGenerator().generate_mission_data()

    print("\n--- 성막 봉헌 데이터 ---")
    print(dedication_df.head())
    print("\n--- 제자들의 사명 데이터 ---")
    print(mission_df.head())

    if interactive:
        input("\n▶️ 데이터 파이프라인을 시작하려면 Enter를 눌러주세요...")

    # 데이터 파이프라인
    def assign_mission(status):
        if status in ['Fearful', 'Doubtful']:
            return True
        return False

    mission_df['mission_assigned'] = mission_df['status_before_resurrection'].apply(assign_mission)

    pipeline = DataPipeline(mission_df)

    mission_mapping = {True: 'Sent', False: 'Not Sent'}

    pipeline_steps = [
        (DataPipeline.map_values, {'column': 'mission_assigned', 'mapping': mission_mapping})
    ]
    final_df = pipeline.run_pipeline(*pipeline_steps)

    print("\n--- 파이프라인 실행 후 데이터 ---")
    print(final_df)

    print("\n🎉 Chapter 40 완료!")

def main():
    """메인 실행 함수"""
    run_chapter40(interactive=False)

if __name__ == "__main__":
    main()
