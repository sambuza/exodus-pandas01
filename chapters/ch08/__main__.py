"""
Chapter 08 통합 실행 스크립트
재앙 속의 구분 — 고센과 마스킹

"여호와께서 이스라엘 자손과 애굽 사람 사이에 구별을 두시리니 내일 이 표적이 있으리라 하시고" (출애굽기 8:23)
"예수께서 대답하여 이르시되 네가 만일 하나님의 선물과 또 네게 물 좀 달라 하는 이가 누구인 줄 알았더라면 네가 그에게 구하였을 것이요 그가 생수를 네게 주었으리라" (요한복음 4:10)
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
from chapters.ch08.goshen_data import GoshenDataGenerator
from chapters.ch08.masking_operations import MaskingOperations
from chapters.ch08.query_filtering import QueryFiltering
from chapters.ch08.distinction_analysis import DistinctionAnalysis

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 08: 재앙 속의 구분 — 고센과 마스킹                 ║
║                                                                      ║
║    "여호와께서 이스라엘 자손과 애굽 사람 사이에 구별을 두시리니 내일 이 표적이 있으리라 하시고" (출애굽기 8:23) 
║    "예수께서 대답하여 이르시되 네가 만일 하나님의 선물과 또 네게 물 좀 달라 하는 이가 누구인 줄 알았더라면 네가 그에게 구하였을 것이요 그가 생수를 네게 주었으리라" (요한복음 4:10) 
║                                                                      ║
║      출애굽기 8장: 파리 재앙과 고센 땅의 구별                        ║
║      요한복음 4:1-15: 사마리아 여인과 생수                           ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    print(header)

def run_goshen_data_generation():
    """고센 데이터 생성 섹션 실행"""
    print("\n🌍 === 고센 데이터 생성 ===")
    print("재앙 속에서 구별된 고센 땅처럼, 특정 조건에 따라 구분될 데이터를 생성합니다.")
    print("Generates data that will be distinguished by specific conditions, like the land of Goshen in the midst of plagues.")

    try:
        generator = GoshenDataGenerator()
        data = generator.generate_goshen_data()
        print("\n✅ 고센 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 고센 데이터 생성 중 오류 발생: {e}")
        return None

def run_masking_operations(df):
    """마스킹 연산 섹션 실행"""
    print("\n🎭 === 마스킹 연산 ===")
    print("`mask()`와 `where()`를 사용하여 특정 조건에 따라 데이터를 가리거나 선택합니다.")
    print("Hides or selects data based on specific conditions using `mask()` and `where()`.")

    if df is None:
        print("⚠️ 데이터가 없어 마스킹 연산을 건너뜁니다.")
        return None

    try:
        masker = MaskingOperations(df)
        masked_df = masker.apply_masking('plague_affected', condition_value=True, mask_value='Unaffected')
        where_df = masker.apply_where('is_israelite', condition_value=False, where_value='Egyptian')
        print("\n✅ 마스킹 연산 적용 완료 (일부):")
        print(masked_df.head())
        print(where_df.head())
        return {'masked_df': masked_df, 'where_df': where_df}
    except Exception as e:
        print(f"❌ 마스킹 연산 중 오류 발생: {e}")
        return None

def run_query_filtering(df):
    """쿼리 필터링 섹션 실행"""
    print("\n🔍 === 쿼리 필터링 ===")
    print("`query()` 메서드를 사용하여 복잡한 조건으로 데이터를 필터링합니다.")
    print("Filters data with complex conditions using the `query()` method.")

    if df is None:
        print("⚠️ 데이터가 없어 쿼리 필터링을 건너뜁니다.")
        return None

    try:
        query_filter = QueryFiltering(df)
        filtered_df = query_filter.apply_query("population_density > 500 and is_israelite == True")
        print("\n✅ 쿼리 필터링 적용 완료 (일부):")
        print(filtered_df.head())
        return filtered_df
    except Exception as e:
        print(f"❌ 쿼리 필터링 중 오류 발생: {e}")
        return None

def run_distinction_analysis(df):
    """구분 분석 섹션 실행"""
    print("\n✨ === 구분 분석 ===")
    print("고센 땅의 구별처럼, 데이터 속에서 특정 그룹의 특징을 분석하여 통찰을 얻습니다.")
    print("Analyzes characteristics of specific groups in data, like the distinction of Goshen, to gain insights.")

    if df is None:
        print("⚠️ 데이터가 없어 구분 분석을 건너뜁니다.")
        return None

    try:
        analyzer = DistinctionAnalysis(df)
        analysis_results = analyzer.analyze_distinctions('is_israelite', 'plague_affected')
        print("\n✅ 구분 분석 완료:")
        print(analysis_results)
        return analysis_results
    except Exception as e:
        print(f"❌ 구분 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, masking_results, query_results, analysis_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `mask()`, `where()`, `query()` = 혼돈 속에서 질서를 발견하는 지혜",
        "🌍 고센 땅의 구별 = 하나님의 백성을 보호하고 구별하는 은혜",
        "💧 사마리아 여인과 생수 = 영적 목마름을 채우는 조건부 선택",
        "💡 데이터 마스킹 = 중요한 정보를 보호하고 필요한 것에 집중"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and masking_results is not None and query_results is not None and analysis_results is not None:
        num_israelites = original_df[original_df['is_israelite'] == True].shape[0]
        num_egyptians = original_df[original_df['is_israelite'] == False].shape[0]
        
        print(f"✨ 고센 땅의 구별처럼, {num_israelites}명의 이스라엘 백성과 {num_egyptians}명의 애굽 사람을 데이터적으로 구분하여 하나님의 섭리를 이해합니다.")
        print("✨ 사마리아 여인처럼, 데이터 속에서 영적 목마름을 발견하고 생수로 채우는 지혜를 구합니다.")
    else:
        print("🙏 재앙 속에서도 구별된 은혜를 발견하고, 혼돈 속에서 질서를 찾아내는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 09 미리보기 (Preview) ===

"견고한 마음 - 집계의 기초 (Hardened Heart - Basics of Aggregation)"

출애굽기 9장에서 파라오의 마음이 견고해져 재앙이 계속되듯이,
데이터 분석에서도 복잡한 데이터를 요약하고 핵심적인 통계를 '집계'하는 것은
데이터의 본질을 파악하고 숨겨진 패턴을 발견하는 데 필수적입니다.

Just as Pharaoh's heart hardened in Exodus 9, leading to continued plagues,
in data analysis, 'aggregating' complex data to summarize and extract key statistics
is essential for grasping the essence of the data and discovering hidden patterns.

다음 장에서는:
📁 기술 통계 (`describe`)
🔍 `sum()`, `mean()`, `count()`를 이용한 기본 집계
🎯 파라오의 견고한 마음처럼 데이터 속 숨겨진 패턴 발견
📊 성경 속 사건의 통계적 요약

"여호와의 손이 들에 있는 네 생축에게 더하리니... 심한 악질이 있을 것이며" (출애굽기 9:3)
"예수께서 가라사대 가라 네 아들이 살았다 하신대 그 사람이 예수의 하신 말씀을 믿고 가더니" (요한복음 4:50)
"""
    print(preview)

def run_chapter08(interactive: bool = True):
    """Chapter 08 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 08을 시작합니다!")
        print("이 챕터에서는 데이터 마스킹과 쿼리 필터링 기법을 배우고, 재앙 속 고센 땅의 구별과 사마리아 여인에게 주신 생수를 탐구합니다.")
        print("This chapter introduces data masking and query filtering techniques, exploring the distinction of Goshen in plagues and the living water given to the Samaritan woman.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '08',
        'title': '재앙 속의 구분 — 고센과 마스킹',
        'original_data': None,
        'masking_results': None,
        'query_results': None,
        'analysis_results': None
    }

    # 1. 고센 데이터 생성
    original_df = run_goshen_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 마스킹 연산을 시작하려면 Enter를 눌러주세요... (Press Enter to start masking operations...)")

    # 2. 마스킹 연산
    masking_results = run_masking_operations(original_df)
    results['masking_results'] = masking_results

    if interactive:
        input("\n▶️ 쿼리 필터링을 시작하려면 Enter를 눌러주세요... (Press Enter to start query filtering...)")

    # 3. 쿼리 필터링
    query_results = run_query_filtering(original_df) # 원본 데이터에 쿼리 필터링 적용
    results['query_results'] = query_results

    if interactive:
        input("\n▶️ 구분 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start distinction analysis...)")

    # 4. 구분 분석
    analysis_results = run_distinction_analysis(original_df) # 원본 데이터에 구분 분석 적용
    results['analysis_results'] = analysis_results

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, masking_results, query_results, analysis_results)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 재앙 속에서도 고센 땅을 구별하시고 보호하시니 감사합니다.
데이터 마스킹과 쿼리 필터링을 통해 혼돈 속에서 질서를 발견하고,
주님의 구별된 은혜를 깨닫는 지혜를 주소서. 예수님의 이름으로 기도합니다. 아멘."
"""
    print(prayer)

    print(f"\n🎉 Chapter 08 완료! 여덟 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 08 Complete! You have finished the eighth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter08(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch08_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_masking_results': results['masking_results'] is not None,
                'has_query_results': results['query_results'] is not None,
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
    print("🚀 JesusBornd Pandas Chapter 08 시작! (Starting JesusBornd Pandas Chapter 08!)\n")
    main()
