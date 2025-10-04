

"""
Chapter 30 통합 실행 스크립트
분향단과 계수 - 시간·주기 데이터

"예수께서 성전에 들어가사 성전 안에서 매매하는 자들을 내어쫓으시며 돈 바꾸는 자들의 상과 비둘기 파는 자들의 의자를 둘러 엎으시고" (요한복음 2:13-17)
"""

import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd
import numpy as np

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch30.incense_altar_data import IncenseAltarDataGenerator
from chapters.ch30.date_range_generator import DateRangeGenerator
from chapters.ch30.period_converter import PeriodConverter
from chapters.ch30.time_series_analyzer import TimeSeriesAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 30: 분향단과 계수 - 시간·주기 데이터            ║
║                                                                      ║
║    "예수께서 성전에 들어가사 성전 안에서 매매하는 자들을 내어쫓으시며 돈 바꾸는 자들의 상과 비둘기 파는 자들의 의자를 둘러 엎으시고" (요한복음 2:13-17) ║
║                                                                      ║
║    🕯️ 출애굽기 30장: 분향단과 계수                                     ║
║    ⚖️ 요한복음 2:13-17: 성전 정화 사건                                 ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_incense_altar_data_generation():
    """분향단 데이터 생성 섹션 실행"""
    print("\n🕯️ === 분향단 데이터 생성 ===")
    print("분향단에서 피어나는 향처럼 연속적인 시간 데이터를 생성합니다.")
    print("Generates continuous time-series data, like incense rising from the altar.")

    try:
        generator = IncenseAltarDataGenerator()
        data = generator.generate_incense_data()
        print("\n✅ 분향단 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 분향단 데이터 생성 중 오류 발생: {e}")
        return None

def run_date_range_demonstration():
    """date_range 시연 섹션 실행"""
    print("\n📅 === date_range 시연 ===")
    print("Pandas의 `date_range` 기능을 사용하여 다양한 시간 간격의 시계열 인덱스를 생성합니다.")
    print("Demonstrates Pandas' `date_range` functionality to create time-series indices with various frequencies.")

    try:
        generator = DateRangeGenerator()
        date_ranges = generator.generate_ranges()
        print("\n✅ date_range 생성 완료:")
        for name, dr in date_ranges.items():
            print(f"  - {name}: {dr[0]} ~ {dr[-1]} ({len(dr)}개)")
        return date_ranges
    except Exception as e:
        print(f"❌ date_range 시연 중 오류 발생: {e}")
        return None

def run_period_conversion(df):
    """period 변환 섹션 실행"""
    print("\n⏳ === period 변환 ===")
    print("시계열 데이터를 특정 주기로 변환하고 분석하는 방법을 탐구합니다.")
    print("Explores methods for converting and analyzing time-series data at specific periods.")

    if df is None:
        print("⚠️ 데이터가 없어 period 변환을 건너뜁니다.")
        return None

    try:
        converter = PeriodConverter(df)
        converted_df = converter.convert_to_period()
        print("\n✅ period 변환 적용 완료 (일부):")
        print(converted_df.head())
        return converted_df
    except Exception as e:
        print(f"❌ period 변환 중 오류 발생: {e}")
        return None

def run_time_series_analysis(df):
    """시계열 분석 섹션 실행"""
    print("\n📈 === 시계열 분석 ===")
    print("시간 기반 데이터에서 추세, 계절성, 주기성 등의 패턴을 분석합니다.")
    print("Analyzes patterns such as trends, seasonality, and periodicity in time-based data.")

    if df is None:
        print("⚠️ 데이터가 없어 시계열 분석을 건너뜁니다.")
        return None

    try:
        analyzer = TimeSeriesAnalyzer(df)
        analysis_results = analyzer.perform_analysis()
        print("\n✅ 시계열 분석 완료:")
        print(analysis_results)
        return analysis_results
    except Exception as e:
        print(f"❌ 시계열 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, date_ranges, converted_df, analysis_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 시간·주기 데이터 = 연속적인 흐름 속의 패턴과 통찰",
        "🕯️ 분향단 = 끊임없이 드려지는 기도와 시간의 흐름",
        "⚖️ 요한복음 2:13-17 = 성전 정화 사건과 때를 아는 지혜",
        "💡 시계열 분석 = 영적 흐름과 때를 분별하는 통찰력"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and date_ranges is not None and converted_df is not None and analysis_results is not None:
        print("✨ 분향단의 향처럼 끊임없이 흐르는 시간 데이터 속에서, 성전 정화 사건처럼 중요한 때를 분별하는 지혜가 필요합니다.")
        print("✨ 시계열 분석을 통해 데이터의 흐름을 이해하고, 영적 흐름 속에서 하나님의 뜻을 발견하는 통찰력을 기르세요.")
    else:
        print("🙏 분향단처럼 끊임없이 기도하며, 시간의 흐름 속에서 하나님의 때를 분별하는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
 === Chapter 31 미리보기 (Preview) ===

"브살렐과 오홀리압 - 성능 최적화"

브살렐과 오홀리압이 성막 건축에 필요한 모든 기술과 지혜를 부여받아 최고의 작품을 만들었듯이, 데이터 분석에서도 성능 최적화는 대규모 데이터를 효율적으로 처리하고 분석 결과를 빠르게 얻는 데 필수적입니다.
`vectorization`, `eval/query` 가속, `dtype` 튜닝과 같은 도구는 코드의 실행 속도를 향상시키고 자원 사용을 최적화하는 데 사용됩니다.

Just as Bezalel and Oholiab were endowed with all the skills and wisdom needed to build the tabernacle, creating the finest work, in data analysis, performance optimization is essential for efficiently processing large datasets and quickly obtaining analysis results.
Tools like `vectorization`, `eval/query` acceleration, and `dtype` tuning are used to improve code execution speed and optimize resource usage.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 벡터화 연산을 통한 성능 향상
🔍 `eval()` 및 `query()`를 이용한 빠른 데이터 처리
🎯 데이터 타입 최적화를 통한 메모리 및 속도 개선
📊 브살렐과 오홀리압처럼 효율적이고 최적화된 데이터 분석 환경 구축

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 31:1-11)
"내 아버지께서 이제까지 일하시니 나도 일한다" (요한복음 5:17)
    """
    print(preview)

def run_chapter30(interactive: bool = True):
    """Chapter 30 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 30을 시작합니다!")
        print("이 챕터에서는 시간·주기 데이터를 다루는 기법을 배우고, 분향단과 성전 정화 사건을 탐구합니다.")
        print("This chapter introduces techniques for handling time and periodic data, exploring the altar of incense and the temple cleansing event.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '30',
        'title': '분향단과 계수 - 시간·주기 데이터',
        'original_data': None,
        'date_ranges': None,
        'converted_data': None,
        'analysis_results': None
    }

    # 1. 분향단 데이터 생성
    original_df = run_incense_altar_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ date_range 시연을 시작하려면 Enter를 눌러주세요... (Press Enter to start date_range demonstration...)")

    # 2. date_range 시연
    date_ranges = run_date_range_demonstration()
    results['date_ranges'] = date_ranges

    if interactive:
        input("\n▶️ period 변환을 시작하려면 Enter를 눌러주세요... (Press Enter to start period conversion...)")

    # 3. period 변환
    converted_df = run_period_conversion(original_df) # 원본 데이터에 적용
    results['converted_data'] = converted_df

    if interactive:
        input("\n▶️ 시계열 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start time series analysis...)")

    # 4. 시계열 분석
    analysis_results = run_time_series_analysis(original_df) # 원본 데이터에 적용
    results['analysis_results'] = analysis_results

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, date_ranges, converted_df, analysis_results)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 분향단의 향처럼 끊임없이 흐르는 시간 데이터 속에서, 성전 정화 사건처럼 중요한 때를 분별하는 지혜를 주소서.
시계열 분석을 통해 데이터의 흐름을 이해하고, 영적 흐름 속에서 하나님의 뜻을 발견하는 통찰력을 기르소서.
예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 30 완료! 서른 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 30 Complete! You have finished the thirtieth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter30(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch30_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_date_ranges': results['date_ranges'] is not None,
                'has_converted_data': results['converted_data'] is not None,
                'has_analysis_results': results['analysis_results'] is not None
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary_results, f, ensure_ascii=False, indent=2)

            print(f"✅ 결과가 {filename}에 저장되었습니다! (Results saved to {filename}!)")

        return results

    except KeyboardInterrupt:
        print("\n\n⏸️ 사용자가 중단했습니다. (User interrupted.)")
        return None
    except Exception as e:
        print(f"\n❌ 실행 중 오류가 발생했습니다: {e}")
        print("🔧 코드와 데이터를 확인해주세요. (Please check the code and data.)")
        return None


if __name__ == "__main__":
    print("🚀 JesusBornd Pandas Chapter 30 시작! (Starting JesusBornd Pandas Chapter 30!)\n")
    main()
