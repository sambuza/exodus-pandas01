
"""
Chapter 27 통합 실행 스크립트
번제단 - 파생변수와 전처리 파이프

"그가 흥하여야 하겠고 나는 쇠하여야 하리라" (요한복음 3:30)
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
from chapters.ch27.altar_data import AltarDataGenerator
from chapters.ch27.derived_variables import DerivedVariableCreator
from chapters.ch27.conditional_processing import ConditionalProcessor
from chapters.ch27.preprocessing_pipeline import PreprocessingPipeline

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 27: 번제단 - 파생변수와 전처리 파이프            ║
║                                                                      ║
║    "그가 흥하여야 하겠고 나는 쇠하여야 하리라" (요한복음 3:30)           ║
║                                                                      ║
║    🔥 출애굽기 27장: 번제단                                            ║
║    💧 요한복음 3:30: 세례 요한의 고백                                  ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_altar_data_generation():
    """번제단 데이터 생성 섹션 실행"""
    print("\n🔥 === 번제단 데이터 생성 ===")
    print("번제단처럼 정결하고 분석에 적합한 데이터 생성을 위한 기초 데이터를 만듭니다.")
    print("Creates foundational data for generating clean and analysis-ready data, like the altar of burnt offering.")

    try:
        generator = AltarDataGenerator()
        data = generator.generate_altar_data()
        print("\n✅ 번제단 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 번제단 데이터 생성 중 오류 발생: {e}")
        return None

def run_derived_variables_creation(df):
    """파생변수 생성 섹션 실행"""
    print("\n📊 === 파생변수 생성 ===")
    print("기존 데이터로부터 새로운 의미 있는 파생변수를 생성하여 데이터의 풍성함을 더합니다.")
    print("Enriches data by creating new meaningful derived variables from existing data.")

    if df is None:
        print("⚠️ 데이터가 없어 파생변수 생성을 건너뜁니다.")
        return None

    try:
        creator = DerivedVariableCreator(df)
        df_with_derived = creator.create_variables()
        print("\n✅ 파생변수 생성 완료 (일부):")
        print(df_with_derived.head())
        return df_with_derived
    except Exception as e:
        print(f"❌ 파생변수 생성 중 오류 발생: {e}")
        return None

def run_conditional_processing(df):
    """조건부 처리 섹션 실행"""
    print("\n💡 === 조건부 처리 ===")
    print("특정 조건에 따라 데이터를 분류하거나 변환하여 분석의 깊이를 더합니다.")
    print("Adds depth to analysis by classifying or transforming data based on specific conditions.")

    if df is None:
        print("⚠️ 데이터가 없어 조건부 처리를 건너뜁니다.")
        return None

    try:
        processor = ConditionalProcessor(df)
        processed_df = processor.apply_conditions()
        print("\n✅ 조건부 처리 적용 완료 (일부):")
        print(processed_df.head())
        return processed_df
    except Exception as e:
        print(f"❌ 조건부 처리 중 오류 발생: {e}")
        return None

def run_preprocessing_pipeline(df):
    """전처리 파이프라인 실행 섹션"""
    print("\n⚙️ === 전처리 파이프라인 실행 ===")
    print("여러 전처리 단계를 하나의 파이프라인으로 묶어 데이터 처리의 효율성과 일관성을 확보합니다.")
    print("Ensures efficiency and consistency in data processing by combining multiple preprocessing steps into a single pipeline.")

    if df is None:
        print("⚠️ 데이터가 없어 전처리 파이프라인 실행을 건너뜁니다.")
        return None

    try:
        pipeline = PreprocessingPipeline(df)
        final_df = pipeline.run_pipeline()
        print("\n✅ 전처리 파이프라인 실행 완료 (일부):")
        print(final_df.head())
        return final_df
    except Exception as e:
        print(f"❌ 전처리 파이프라인 실행 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, derived_df, processed_df, final_df):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 파생변수와 전처리 = 데이터의 정결함과 분석 적합성",
        "🔥 번제단 = 죄를 정결케 하고 하나님께 나아가는 길",
        "💧 요한복음 3:30 = 자신을 낮추고 그리스도를 높이는 겸손한 전처리 과정",
        "💡 데이터 파이프라인 = 영적 성장의 단계별 과정과 일관성"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and derived_df is not None and processed_df is not None and final_df is not None:
        print("✨ 번제단이 정결함을 상징하듯, 데이터 전처리는 분석의 순수성을 보장합니다.")
        print("✨ 세례 요한이 자신을 낮춰 예수님을 높였듯, 데이터 전처리는 원본 데이터의 가치를 극대화합니다.")
    else:
        print("🙏 번제단처럼 정결한 마음으로, 그리고 세례 요한처럼 겸손한 자세로 데이터 분석에 임하는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
 === Chapter 28 미리보기 (Preview) ===

"제사장 옷 - 라벨링과 스타일링"

제사장 옷이 하나님의 영광과 거룩함을 드러내듯, 데이터 분석에서도 라벨링과 스타일링은 데이터의 의미를 명확히 하고 시각적 효과를 높여 통찰을 더욱 풍성하게 합니다.
`Categorical` 데이터 타입과 `DataFrame.style` 객체는 데이터의 표현력을 극대화하는 데 사용됩니다.

Just as the priestly garments reveal God's glory and holiness, in data analysis, labeling and styling clarify data meaning and enhance visual impact, enriching insights.
`Categorical` data types and `DataFrame.style` objects are used to maximize data expressiveness.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 범주형 데이터의 효과적인 관리
🔍 데이터프레임 스타일링을 통한 시각화 강화
🎯 데이터의 의미를 명확히 하는 라벨링 기법
📊 제사장 옷처럼 아름답고 의미 있는 데이터 표현

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 28:1-5)
"나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이" (요한복음 10:14)
    """
    print(preview)

def run_chapter27(interactive: bool = True):
    """Chapter 27 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 27을 시작합니다!")
        print("이 챕터에서는 파생변수 생성과 전처리 파이프라인을 배우고, 번제단과 세례 요한의 고백을 탐구합니다.")
        print("This chapter introduces derived variable creation and preprocessing pipelines, exploring the altar of burnt offering and John the Baptist's confession.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '27',
        'title': '번제단 - 파생변수와 전처리 파이프',
        'original_data': None,
        'derived_data': None,
        'processed_data': None,
        'final_data': None
    }

    # 1. 번제단 데이터 생성
    original_df = run_altar_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 파생변수 생성을 시작하려면 Enter를 눌러주세요... (Press Enter to start derived variables creation...)")

    # 2. 파생변수 생성
    derived_df = run_derived_variables_creation(original_df)
    results['derived_data'] = derived_df

    if interactive:
        input("\n▶️ 조건부 처리를 시작하려면 Enter를 눌러주세요... (Press Enter to start conditional processing...)")

    # 3. 조건부 처리
    processed_df = run_conditional_processing(derived_df) # 파생변수 적용된 데이터에 처리
    results['processed_data'] = processed_df

    if interactive:
        input("\n▶️ 전처리 파이프라인 실행을 시작하려면 Enter를 눌러주세요... (Press Enter to start preprocessing pipeline...)")

    # 4. 전처리 파이프라인 실행
    final_df = run_preprocessing_pipeline(original_df) # 원본 데이터에 파이프라인 적용
    results['final_data'] = final_df

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, derived_df, processed_df, final_df)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 번제단처럼 정결한 마음으로 데이터 분석에 임하게 하시고, 세례 요한처럼 자신을 낮춰 주님의 영광을 드러내는 파생변수와 전처리 과정을 통해 데이터의 가치를 극대화하게 하소서.
예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 27 완료! 스물일곱 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 27 Complete! You have finished the twenty-seventh wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter27(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch27_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_derived_data': results['derived_data'] is not None,
                'has_processed_data': results['processed_data'] is not None,
                'has_final_data': results['final_data'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 27 시작! (Starting JesusBornd Pandas Chapter 27!)\n")
    main()
