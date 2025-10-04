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
from chapters.ch31.craftsmen_data import CraftsmenDataGenerator
from chapters.ch31.vectorization_optimizer import VectorizationOptimizer
from chapters.ch31.eval_query_accelerator import EvalQueryAccelerator
from chapters.ch31.dtype_tuner import DtypeTuner

def print_chapter_header():
    """챕터 헤더 출력"""
    header = (
        "╔══════════════════════════════════════════════════════════════════════╗\n"
        "║                    JesusBornd Pandas Edition                         ║\n"
        "║                                                                      ║\n"
        "║             Chapter 31: 브살렐과 오홀리압 - 성능 최적화                ║\n"
        "║                                                                      ║\n"
        "║    \"모세가 그 장인의 말을 듣고 그 말대로 하여\" (출애굽기 31:1-11)\n"
        "║    \"내 아버지께서 이제까지 일하시니 나도 일한다\" (요한복음 5:17)\n"
        "║                                                                      ║\n"
        "║      출애굽기 31장: 브살렐과 오홀리압의 지혜와 기술                    ║\n"
        "║      요한복음 5:17: 예수님의 일하심과 하나님의 효율성                  ║\n"
        "╚══════════════════════════════════════════════════════════════════════╝"
    )
    print(header)

def run_craftsmen_data_generation():
    """장인 데이터 생성 섹션 실행"""
    print("\n🛠️ === 장인 데이터 생성 ===")
    print("성능 최적화에 사용될 성막 건축 장인 관련 데이터를 생성합니다.")
    print("Generates Tabernacle craftsmen data for performance optimization.")

    try:
        generator = CraftsmenDataGenerator()
        data = generator.generate_craftsmen_data()
        print("\n✅ 장인 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 장인 데이터 생성 중 오류 발생: {e}")
        return None

def run_vectorization_optimization(df):
    """벡터화 연산 최적화 섹션 실행"""
    print("\n⚡ === 벡터화 연산 최적화 ===")
    print("벡터화 연산을 통해 대규모 데이터를 효율적으로 처리하고 성능을 향상시킵니다.")
    print("Optimizes performance by efficiently processing large datasets through vectorized operations.")

    if df is None:
        print("⚠️ 데이터가 없어 벡터화 연산 최적화를 건너뜁니다.")
        return None

    try:
        optimizer = VectorizationOptimizer(df)
        optimized_df = optimizer.calculate_total_time_vectorized()
        print("\n✅ 벡터화 연산 최적화 적용 완료 (일부):")
        print(optimized_df.head())
        return optimized_df
    except Exception as e:
        print(f"❌ 벡터화 연산 최적화 중 오류 발생: {e}")
        return None

def run_eval_query_acceleration(df):
    """eval()/query() 가속 섹션 실행"""
    print("\n🚀 === eval()/query() 가속 ===")
    print("`eval()` 및 `query()`를 이용하여 복잡한 조건부 계산이나 필터링을 빠르게 수행합니다.")
    print("Accelerates complex conditional calculations or filtering using `eval()` and `query()`.")

    if df is None:
        print("⚠️ 데이터가 없어 eval()/query() 가속을 건너뜁니다.")
        return None

    try:
        accelerator = EvalQueryAccelerator(df)
        eval_result = accelerator.apply_eval("total_time_minutes > 100 and material_cost > 500")
        query_result = accelerator.apply_query("craftsman == 'Bezalel' and total_time_minutes > 150")
        print("\n✅ eval()/query() 가속 적용 완료 (일부):")
        print(eval_result.head())
        print(query_result.head())
        return {'eval_result': eval_result, 'query_result': query_result}
    except Exception as e:
        print(f"❌ eval()/query() 가속 중 오류 발생: {e}")
        return None

def run_dtype_tuning(df):
    """데이터 타입 최적화 섹션 실행"""
    print("\n💾 === 데이터 타입 최적화 ===")
    print("데이터 타입(`dtype`) 튜닝을 통해 메모리 사용량을 줄이고 데이터 처리 속도를 개선합니다.")
    print("Optimizes memory usage and data processing speed through `dtype` tuning.")

    if df is None:
        print("⚠️ 데이터가 없어 데이터 타입 최적화를 건너뜁니다.")
        return None

    try:
        tuner = DtypeTuner(df)
        optimized_df = tuner.optimize_dtypes()
        print("\n✅ 데이터 타입 최적화 적용 완료 (일부):")
        print(optimized_df.head())
        return optimized_df
    except Exception as e:
        print(f"❌ 데이터 타입 최적화 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, optimized_df, eval_query_results, dtype_optimized_df):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 성능 최적화 = 하나님의 일하심의 효율성과 목적성",
        "🛠️ 브살렐과 오홀리압 = 최고의 기술과 지혜로 하나님의 명령 수행",
        "✝️ 예수님의 일하심 = 쉬지 않고 효율적으로 일하시는 하나님의 본성",
        "💡 자원 효율성 = 영적 절제와 지혜로운 자원 관리"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and optimized_df is not None and eval_query_results is not None and dtype_optimized_df is not None:
        original_memory = original_df.memory_usage(deep=True).sum()
        optimized_memory = dtype_optimized_df.memory_usage(deep=True).sum()
        memory_saved_percent = (1 - optimized_memory / original_memory) * 100 if original_memory > 0 else 0
        
        print(f"✨ 브살렐과 오홀리압처럼 효율적인 데이터 처리로 {memory_saved_percent:.2f}%의 메모리를 절감했습니다.")
        print("✨ 예수님의 일하심처럼, 최적화된 분석을 통해 하나님의 지혜와 효율성을 더욱 깊이 깨닫습니다.")
    else:
        print("🙏 브살렐과 오홀리압처럼 지혜와 기술로, 그리고 예수님처럼 효율적으로 주님을 섬기는 삶을 살게 하소서.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = (
        "🌟 === Chapter 32 미리보기 (Preview) ===\n\n"
        "\"금송아지 - 롤백과 감사 로그 (Golden Calf - Rollback and Audit Log)\"\n\n"
        "이스라엘 백성이 금송아지를 만들어 하나님을 진노케 했을 때, 모세가 중보하여 하나님의 진노를 돌이키고 언약을 회복했듯이, 데이터 분석에서도 잘못된 변경 사항을 되돌리고(롤백), 모든 변경 이력을 기록하는(감사 로그) 것은 데이터의 무결성과 신뢰성을 유지하는 데 필수적입니다.\n\n"
        "Just as the Israelites angered God by making the golden calf, and Moses interceded to turn away God's wrath and restore the covenant, in data analysis, rolling back incorrect changes and recording all change history (audit log) are essential for maintaining data integrity and reliability.\n\n"
        "다음 장에서 배울 내용 (What you'll learn in the next chapter):\n"
        "📁 데이터 변경 이력 컬럼 추가\n"
        "🔍 롤백(Rollback) 기능 구현 (특정 버전으로 되돌리기)\n"
        "🎯 감사 로그(Audit Log) 생성 및 관리\n"
        "📊 금송아지 사건처럼 데이터의 잘못된 변경을 되돌리고 신뢰성을 회복하는 전략\n\n"
        "\"모세가 여호와께로 다시 나아가 여짜오되 슬프도소이다 이 백성이 자기들을 위하여 금신을 만들었사오니 큰 죄를 범하였나이다\" (출애굽기 32:31)\n"
        "\"예수께서 다시 그들에게 말씀하여 이르시되 나는 세상의 빛이니 나를 따르는 자는 어둠에 다니지 아니하고 생명의 빛을 얻으리라\" (요한복음 8:12)"
    )
    print(preview)

def run_chapter31(interactive: bool = True):
    """Chapter 31 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 31을 시작합니다!")
        print("이 챕터에서는 데이터 성능 최적화 기법을 배우고, 브살렐과 오홀리압의 지혜와 예수님의 일하심을 탐구합니다.")
        print("This chapter introduces data performance optimization techniques, exploring the wisdom of Bezalel and Oholiab and the work of Jesus.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '31',
        'title': '브살렐과 오홀리압 - 성능 최적화',
        'original_data': None,
        'optimized_data': None,
        'eval_query_results': None,
        'dtype_optimized_data': None
    }

    # 1. 장인 데이터 생성
    original_df = run_craftsmen_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 벡터화 연산 최적화를 시작하려면 Enter를 눌러주세요... (Press Enter to start vectorization optimization...)")

    # 2. 벡터화 연산 최적화
    optimized_df = run_vectorization_optimization(original_df)
    results['optimized_data'] = optimized_df

    if interactive:
        input("\n▶️ eval()/query() 가속을 시작하려면 Enter를 눌러주세요... (Press Enter to start eval()/query() acceleration...)")

    # 3. eval()/query() 가속
    eval_query_results = run_eval_query_acceleration(optimized_df) # 최적화된 데이터에 적용
    results['eval_query_results'] = eval_query_results

    if interactive:
        input("\n▶️ 데이터 타입 최적화를 시작하려면 Enter를 눌러주세요... (Press Enter to start dtype tuning...)")

    # 4. 데이터 타입 최적화
    dtype_optimized_df = run_dtype_tuning(optimized_df) # eval/query 가속된 데이터에 적용
    results['dtype_optimized_data'] = dtype_optimized_df

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, optimized_df, eval_query_results, dtype_optimized_df)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = (
        "\"주님, 브살렐과 오홀리압처럼 지혜와 기술로 주님을 섬기게 하시고, 예수님처럼 효율적이고 목적이 분명한 삶을 살게 하소서.\n"
        "성능 최적화 전략을 통해 저의 시간과 자원을 주님의 영광을 위해 사용하게 하시고,\n"
        "데이터 분석을 통해 하나님의 창조 질서와 일하심의 효율성을 더욱 깊이 깨닫게 하소서. 예수님의 이름으로 기도합니다. 아멘.\""
    )
    print(prayer)

    print(f"\n🎉 Chapter 31 완료! 서른한 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 31 Complete! You have finished the thirty-first wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter31(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch31_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_optimized_data': results['optimized_data'] is not None,
                'has_eval_query_results': results['eval_query_results'] is not None,
                'has_dtype_optimized_data': results['dtype_optimized_data'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 31 시작! (Starting JesusBornd Pandas Chapter 31!)\n")
    main()
