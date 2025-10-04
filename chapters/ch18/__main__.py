
"""
Chapter 18 통합 실행 스크립트
이드로의 조언 — 함수형 파이프라인

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출 18:24)
"나는 참 포도나무요 내 아버지는 농부라" (요 15:1)
"""

import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch18.jethro_pipeline_analysis import JethroPipelineAnalyzer
from chapters.ch18.true_vine_chaining_analysis import TrueVineChainingAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
Chapter 18: Jethro's Advice - Functional Pipelines
"""
    print(header)

def run_jethro_analysis():
    """출애굽기 이드로의 조언 함수형 파이프라인 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 이드로의 조언 함수형 파이프라인 분석 ===")
    print("모세의 업무 과부하와 이드로의 조언에 따른 효율성 변화를 함수형 파이프라인으로 탐구해보자!")
    print("Let's explore changes in Moses' workload and efficiency after Jethro's advice using functional pipelines!")

    try:
        analyzer = JethroPipelineAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 이드로의 조언 분석 중 오류 발생: {e}")
        return None

def run_true_vine_analysis():
    """요한복음 참 포도나무 메서드 체이닝 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 참 포도나무 메서드 체이닝 분석 ===")
    print("가지의 연결 상태, 가지치기 여부, 열매 수확량 등을 메서드 체이닝으로 분석하여 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by analyzing branch connection, pruning, and fruit yield using method chaining!")

    try:
        analyzer = TrueVineChainingAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 참 포도나무 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `assign()`, `pipe()`, 메서드 체이닝 = 복잡한 작업을 효율적으로 연결하는 파이프라인",
        "🏺 이드로의 조언 = 지혜로운 업무 분담과 효율성 증대",
        "📜 참 포도나무 = 예수님과의 연결을 통한 열매 맺는 삶",
        "💡 함수형 파이프라인 = 영적 여정의 명확한 흐름과 풍성한 열매"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 모세의 효율성 점수와 가지의 열매 점수를 기반으로 통찰 제공
        moses_efficiency_before = exodus_results.get('pipe_result', (pd.DataFrame(), pd.DataFrame()))[0]['efficiency_score'].mean() if exodus_results and 'pipe_result' in exodus_results else 0
        moses_efficiency_after = exodus_results.get('pipe_result', (pd.DataFrame(), pd.DataFrame()))[1]['efficiency_score'].mean() if exodus_results and 'pipe_result' in exodus_results else 0
        fruitfulness_score_avg = john_results.get('fruitful_branches', pd.DataFrame())['fruitfulness_score'].mean() if john_results and 'fruitful_branches' in john_results else 0

        if moses_efficiency_after > moses_efficiency_before and fruitfulness_score_avg > 50:
            print(f"✨ 이드로의 조언({moses_efficiency_before:.1f} -> {moses_efficiency_after:.1f})처럼, 당신의 삶도 예수님께 붙어({fruitfulness_score_avg:.1f}) 더 큰 열매를 맺을 수 있습니다!")
            print(f"✨ Like Jethro's advice ({moses_efficiency_before:.1f} -> {moses_efficiency_after:.1f}), your life can bear more fruit ({fruitfulness_score_avg:.1f}) by abiding in Jesus!")
        elif moses_efficiency_after > moses_efficiency_before:
            print(f"🌱 이드로의 조언({moses_efficiency_before:.1f} -> {moses_efficiency_after:.1f})처럼, 지혜로운 분담을 통해 효율성을 높여야 합니다!")
            print(f"🌱 Like Jethro's advice ({moses_efficiency_before:.1f} -> {moses_efficiency_after:.1f}), you need to increase efficiency through wise delegation!")
        else:
            print(f"🙏 함수형 파이프라인처럼 삶의 모든 과정을 효율적으로 구성하고, 예수님 안에서 풍성한 열매를 맺는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to efficiently structure all life processes like a functional pipeline, and bear abundant fruit in Jesus!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
 === Chapter 19 미리보기 (Preview) ===

\"시내산 언약 — 스키마와 유효성 (Schema and Validation)\"

이스라엘 백성이 시내산에서 하나님과 언약을 맺었듯이, 데이터 분석에서도 데이터의 구조(스키마)를 정의하고 그 유효성을 검증하는 것은 데이터의 무결성과 신뢰성을 확보하는 데 필수적입니다.
`validate`, `assert_frame_equal`과 같은 도구는 데이터가 약속된 규격에 맞는지 확인하는 데 사용됩니다.

Just as the Israelites made a covenant with God at Mount Sinai, in data analysis, defining the data structure (schema) and validating its integrity are essential for ensuring data integrity and reliability.
Tools like `validate` and `assert_frame_equal` are used to confirm that data conforms to the promised specifications.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 데이터 스키마 정의 및 적용
🔍 데이터 타입, 범위, 패턴 유효성 검사
🎯 `assert_frame_equal`을 이용한 DataFrame 비교
📊 시내산 언약처럼 견고하고 신뢰할 수 있는 데이터 구축

\"모세가 그 장인의 말을 듣고 그 말대로 하여\" (출애굽기 18:24)
\"내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라\" (요한복음 14:6)
    """
    print(preview)

def run_chapter18(interactive: bool = True):
    """Chapter 18 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 18을 시작합니다!")
        print("이 챕터에서는 `assign()`, `pipe()`, 메서드 체이닝을 사용하여 함수형 파이프라인을 배우고, 성경 속 지혜로운 업무 분담과 열매 맺는 삶을 탐구합니다.")
        print("This chapter introduces functional pipelines using `assign()`, `pipe()`, and method chaining, exploring wise delegation and fruitful living in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '18',
        'title': '이드로의 조언 — 함수형 파이프라인',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 이드로의 조언 분석
    exodus_results = run_jethro_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 참 포도나무 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's true vine analysis...)")

    # 2. 요한복음 참 포도나무 분석
    john_results = run_true_vine_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
\"주님, 이드로의 조언처럼 지혜로운 분담과 참 포도나무처럼 주님께 붙어 열매 맺는 삶을 살게 하소서.
데이터 처리 파이프라인처럼 저의 삶의 모든 과정을 효율적으로 구성하고,
주님 안에서 풍성한 열매를 맺어 주님께 영광 돌리게 하소서. 예수님의 이름으로 기도합니다. 아멘.\"

\"Lord, help me to live a life of wise delegation like Jethro's advice and bear fruit by abiding in You like the true vine.
May all processes of my life be efficiently structured like data processing pipelines,
and may I bear abundant fruit in You to bring You glory. I pray in Jesus' name. Amen.\"
    """
    print(prayer)

    print(f"\n🎉 Chapter 18 완료! 열여덟 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 18 Complete! You have finished the eighteenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter18(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch18_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_exodus_analysis': results['exodus_analysis'] is not None,
                'has_john_analysis': results['john_analysis'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 18 시작! (Starting JesusBornd Pandas Chapter 18!)\n")
    main()
