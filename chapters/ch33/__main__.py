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
from chapters.ch33.grace_data import GraceDataGenerator
from chapters.ch33.merge_indicator_resolver import MergeIndicatorResolver
from chapters.ch33.merge_validator import MergeValidator
from chapters.ch33.column_conflict_resolver import ColumnConflictResolver

def print_chapter_header():
    """챕터 헤더 출력"""
    header = (
        "╔══════════════════════════════════════════════════════════════════════╗\n"
        "║                    JesusBornd Pandas Edition                         ║\n"
        "║                                                                      ║\n"
        "║             Chapter 33: 다시 만난 은혜 - 결합 충돌 해소                ║\n"
        "║                                                                      ║\n"
        "║    \"여호와께서 모세에게 이르시되 내가 너와 함께 가리라 내가 너를 안위하리라\" (출애굽기 33:14)\n"
        "║    \"예수께서 이르시되 시몬 베드로야 네가 나를 사랑하느냐 하시니 베드로가 이르되 주님 그러하나이다 내가 주님을 사랑하는 줄 주님께서 아시나이다\" (요한복음 21:15)\n"
        "║                                                                      ║\n"
        "║      출애굽기 33장: 다시 만난 은혜                                     ║\n"
        "║      요한복음 21:15: 베드로의 회복                                     ║\n"
        "╚══════════════════════════════════════════════════════════════════════╝"
    )
    print(header)

def run_grace_data_generation():
    """은혜 데이터 생성 섹션 실행"""
    print("\n🙏 === 은혜 데이터 생성 ===")
    print("결합 충돌을 시뮬레이션하고 해소하기 위한 은혜 관련 데이터를 생성합니다.")
    print("Generates grace-related data to simulate and resolve join conflicts.")

    try:
        generator = GraceDataGenerator()
        df1, df2 = generator.generate_grace_data()
        print("\n✅ 은혜 데이터 생성 완료 (데이터셋 1 일부):")
        print(df1.head())
        return df1, df2
    except Exception as e:
        print(f"❌ 은혜 데이터 생성 중 오류 발생: {e}")
        return None, None

def run_merge_indicator_resolution(df1, df2):
    """merge() indicator 파라미터 해소 섹션 실행"""
    print("\n📊 === merge() indicator 파라미터 해소 ===")
    print("`merge()`의 `indicator` 파라미터를 사용하여 결합 출처를 확인하고 데이터 불일치를 파악합니다.")
    print("Identifies join sources and data discrepancies using `merge()`'s `indicator` parameter.")

    if df1 is None or df2 is None:
        print("⚠️ 데이터가 없어 `indicator` 파라미터 해소를 건너뜁니다.")
        return None

    try:
        resolver = MergeIndicatorResolver(df1, df2)
        merged_df = resolver.resolve_with_indicator(on='id', how='outer')
        print("\n✅ `indicator` 파라미터 해소 완료 (일부):")
        print(merged_df.head())
        return merged_df
    except Exception as e:
        print(f"❌ `indicator` 파라미터 해소 중 오류 발생: {e}")
        return None

def run_merge_validation(df1, df2):
    """merge() validate 파라미터 유효성 검사 섹션 실행"""
    print("\n✅ === merge() validate 파라미터 유효성 검사 ===")
    print("`validate` 파라미터를 사용하여 결합의 유효성을 검사하고 잘못된 결합을 방지합니다.")
    print("Validates joins and prevents incorrect merges using the `validate` parameter.")

    if df1 is None or df2 is None:
        print("⚠️ 데이터가 없어 `validate` 파라미터 유효성 검사를 건너뜁니다.")
        return None

    try:
        validator = MergeValidator(df1, df2)
        # 1대1 결합 유효성 검사 시도
        merged_df = validator.validate_merge(on='id', how='inner', validate='one_to_one')
        print("\n✅ `validate` 파라미터 유효성 검사 완료 (일부):")
        print(merged_df.head())
        return merged_df
    except Exception as e:
        print(f"❌ `validate` 파라미터 유효성 검사 중 오류 발생: {e}")
        return None

def run_column_conflict_resolution(df1, df2):
    """컬럼 이름 충돌 해결 섹션 실행"""
    print("\n💥 === 컬럼 이름 충돌 해결 ===")
    print("`suffixes` 파라미터를 사용하여 `merge()` 시 발생하는 컬럼 이름 충돌을 해결합니다.")
    print("Resolves column name conflicts during `merge()` using the `suffixes` parameter.")

    if df1 is None or df2 is None:
        print("⚠️ 데이터가 없어 컬럼 이름 충돌 해결을 건너뜁니다.")
        return None

    try:
        # 충돌을 유발하기 위해 컬럼 이름 변경
        df1_conflict = df1.rename(columns={'value': 'score'})
        df2_conflict = df2.rename(columns={'value': 'score'})
        resolver = ColumnConflictResolver(df1_conflict, df2_conflict)
        merged_df = resolver.resolve_column_conflicts(on='id', how='inner', suffixes=['_left', '_right'])
        print("\n✅ 컬럼 이름 충돌 해결 완료 (일부):")
        print(merged_df.head())
        return merged_df
    except Exception as e:
        print(f"❌ 컬럼 이름 충돌 해결 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df1, original_df2, merged_indicator_df, merged_validated_df, merged_suffixes_df):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 결합 충돌 해소 = 깨어진 관계의 회복과 데이터 무결성 유지",
        "🙏 다시 만난 은혜 = 하나님의 변치 않는 사랑과 회복의 역사",
        "✝️ 베드로의 회복 = 잘못된 길에서 돌이켜 다시 사명을 받는 은혜",
        "💡 데이터 신뢰성 = 정확한 분석 결과를 얻기 위한 필수 과정"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df1 is not None and original_df2 is not None and merged_indicator_df is not None and merged_validated_df is not None and merged_suffixes_df is not None:
        left_only_count = merged_indicator_df['_merge'].value_counts().get('left_only', 0)
        right_only_count = merged_indicator_df['_merge'].value_counts().get('right_only', 0)
        
        print(f"✨ 다시 만난 은혜처럼, {left_only_count}개의 데이터 불일치와 {right_only_count}개의 데이터 불일치를 해소하여 데이터의 무결성을 회복했습니다.")
        print("✨ 베드로의 회복처럼, 결합 충돌을 지혜롭게 해결하여 데이터의 신뢰성을 확보합니다.")
    else:
        print("🙏 깨어진 관계를 회복하고 데이터의 무결성을 유지하는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = (
        "🌟 === Chapter 34 미리보기 (Preview) ===\n\n"
        "\"새 돌판 - 정규화와 표준화 (New Tablets - Normalization and Standardization)\"\n\n"
        "이스라엘 백성이 금송아지 사건 이후 깨어진 돌판 대신 새 돌판에 십계명을 다시 받았듯이, 데이터 분석에서도 데이터의 스케일을 조정하는 '정규화(Normalization)'와 '표준화(Standardization)'는 데이터의 특성을 통일하고 모델의 성능을 향상시키는 데 필수적입니다.\n\n"
        "Just as the Israelites received the Ten Commandments again on new tablets after the Golden Calf incident, replacing the broken ones, in data analysis, adjusting the scale of data through 'Normalization' and 'Standardization' is essential for unifying data characteristics and improving model performance.\n\n"
        "다음 장에서 배울 내용 (What you'll learn in the next chapter):\n"
        "📁 정규화(Normalization) 기법 (Min-Max Scaling)\n"
        "🔍 표준화(Standardization) 기법 (Z-score Standardization)\n"
        "🎯 문자열 정규화 (str.normalize)\n"
        "📊 새 돌판처럼 데이터의 스케일을 조정하여 하나님의 공의를 명확히 드러내는 전략\n\n"
        "\"여호와께서 모세에게 이르시되 너는 돌판 둘을 처음 것과 같이 깎아 만들라 네가 깨뜨린 처음 판에 쓴 말을 내가 그 판에 쓰리라\" (출애굽기 34:1)\n"
        "\"우리가 다 그의 충만한 데서 받으니 은혜 위에 은혜러라\" (요한복음 1:16)"
    )
    print(preview)

def run_chapter33(interactive: bool = True):
    """Chapter 33 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 33을 시작합니다!")
        print("이 챕터에서는 데이터 결합 충돌 해소 기법을 배우고, 다시 만난 은혜와 베드로의 회복을 탐구합니다.")
        print("This chapter introduces data join conflict resolution techniques, exploring grace reunited and Peter's restoration.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '33',
        'title': '다시 만난 은혜 - 결합 충돌 해소',
        'original_data1': None,
        'original_data2': None,
        'merged_indicator_data': None,
        'merged_validated_data': None,
        'merged_suffixes_data': None
    }

    # 1. 은혜 데이터 생성
    original_df1, original_df2 = run_grace_data_generation()
    results['original_data1'] = original_df1
    results['original_data2'] = original_df2

    if interactive:
        input("\n▶️ `merge()` indicator 파라미터 해소를 시작하려면 Enter를 눌러주세요... (Press Enter to start merge indicator resolution...)")

    # 2. `merge()` indicator 파라미터 해소
    merged_indicator_df = run_merge_indicator_resolution(original_df1, original_df2)
    results['merged_indicator_data'] = merged_indicator_df

    if interactive:
        input("\n▶️ `merge()` validate 파라미터 유효성 검사를 시작하려면 Enter를 눌러주세요... (Press Enter to start merge validation...)")

    # 3. `merge()` validate 파라미터 유효성 검사
    merged_validated_df = run_merge_validation(original_df1, original_df2) # 원본 데이터에 유효성 검사 적용
    results['merged_validated_data'] = merged_validated_df

    if interactive:
        input("\n▶️ 컬럼 이름 충돌 해결을 시작하려면 Enter를 눌러주세요... (Press Enter to start column conflict resolution...)")

    # 4. 컬럼 이름 충돌 해결
    merged_suffixes_df = run_column_conflict_resolution(original_df1, original_df2) # 원본 데이터에 충돌 해결 적용
    results['merged_suffixes_data'] = merged_suffixes_df

    # 5. 블렌딩 통찰
    show_blending_insights(original_df1, original_df2, merged_indicator_df, merged_validated_df, merged_suffixes_df)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = (
        "\"주님, 다시 만난 은혜처럼 저의 삶의 깨어진 관계와 데이터 결합 충돌을 해소하게 하소서.\n"
        "`merge()`의 `indicator`, `validate`, `suffixes` 파라미터처럼 지혜롭게 충돌을 해결하고,\n"
        "데이터의 무결성을 유지하여 주님의 뜻을 온전히 이해하게 하소서. 예수님의 이름으로 기도합니다. 아멘.\""
    )
    print(prayer)

    print(f"\n🎉 Chapter 33 완료! 서른세 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 33 Complete! You have finished the thirty-third wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter33(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch33_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data1': results['original_data1'] is not None,
                'has_original_data2': results['original_data2'] is not None,
                'has_merged_indicator_data': results['merged_indicator_data'] is not None,
                'has_merged_validated_data': results['merged_validated_data'] is not None,
                'has_merged_suffixes_data': results['merged_suffixes_data'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 33 시작! (Starting JesusBornd Pandas Chapter 33!)\n")
    main()
