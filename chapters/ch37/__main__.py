
'''
Chapter 37 통합 실행 스크립트
성막 기구 제작 - 데이터 시각화
'''

import sys
from pathlib import Path
import pandas as pd
import utils.font_config # 한글 폰트 설정을 위해 추가

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch37.holy_utensils_data import HolyUtensilsDataGenerator
from chapters.ch37.light_of_world_data import LightOfWorldDataGenerator
from chapters.ch37.visualizations import Visualizations

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        """
        ╔══════════════════════════════════════════════════════════════════════╗
        ║                    JesusBornd Pandas Edition                         ║
        ║                                                                      ║
        ║             Chapter 37: 성막 기구 제작 - 데이터 시각화               ║
        ║                                                                      ║
        ║    "브살렐이 조각목으로 궤를 만들었으니..." (출애굽기 37:1)
        ║    "나는 세상의 빛이니 나를 따르는 자는 어둠에 다니지 아니하고 생명의 빛을 얻으리라" (요한복음 8:12)
        ╚══════════════════════════════════════════════════════════════════════╝
        """
    )
    print(header)

def run_chapter37(interactive: bool = True):
    """Chapter 37 전체 실행"""
    print_chapter_header()

    if interactive:
        input("\n▶️ Chapter 37을 시작하려면 Enter를 눌러주세요...")

    # 데이터 생성
    utensils_df = HolyUtensilsDataGenerator().generate_utensils_data()
    light_df = LightOfWorldDataGenerator().generate_light_data()

    print("\n--- 성막 기구 데이터 ---")
    print(utensils_df.head())
    print("\n--- 빛과 어둠 데이터 ---")
    print(light_df.head())

    if interactive:
        input("\n▶️ 데이터 시각화를 시작하려면 Enter를 눌러주세요...")

    # 데이터 시각화
    vis_utensils = Visualizations(utensils_df)
    vis_utensils.plot_bar(x='utensil', y='weight_kg', title='성막 기구별 무게', filename='ch37_utensil_weights.png')

    vis_light = Visualizations(light_df)
    vis_light.plot_scatter(x='intensity', y='duration_hours', hue='event_type', title='빛과 어둠의 강도 및 지속시간', filename='ch37_light_darkness.png')

    print("\n🎉 Chapter 37 완료!")

def main():
    """메인 실행 함수"""
    run_chapter37(interactive=False)

if __name__ == "__main__":
    main()
