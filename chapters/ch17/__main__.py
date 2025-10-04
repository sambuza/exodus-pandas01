
"""
Chapter 17 통합 실행 스크립트
반석에서 난 물 — 결합과 보간

"여호와께서 모세에게 이르시되 백성 앞을 지나 지팡이를 잡고 호렙 산 반석을 치라 그리하면 그곳에서 물이 나리니 백성이 마시리라" (출 17:5-6)
"누구든지 목마르거든 내게로 와서 마시라 나를 믿는 자는 성경에 이름과 같이 그 배에서 생수의 강이 흘러나리라" (요 7:37-38)
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
from chapters.ch17.water_reindex_interpolate import WaterReindexInterpolateAnalyzer
from chapters.ch17.living_water_combine_align import LivingWaterCombineAlignAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 17: 반석에서 난 물 — 결합과 보간                 ║
║                                                                      ║
║    "여호와께서 모세에게 이르시되 백성 앞을 지나 지팡이를 잡고 호렙 산  ║
║     반석을 치라 그리하면 그곳에서 물이 나리니 백성이 마시리라" (출 17:5-6) ║
║    "누구든지 목마르거든 내게로 와서 마시라 나를 믿는 자는 성경에 이름과 ║
║     같이 그 배에서 생수의 강이 흘러나리라" (요한복음 7:37-38)           ║
║                                                                      ║
║    🗺️  출애굽기 17장: 르비딤 반석에서 난 물                           ║
║    📊 요한복음 7:37-38: 생수의 강                                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_water_from_rock_analysis():
    """출애굽기 반석에서 난 물 재색인/보간 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 반석에서 난 물 재색인/보간 분석 ===")
    print("이스라엘의 갈증과 하나님의 기적적인 공급을 `reindex()`와 `interpolate()`로 연속적으로 파악해보자!")
    print("Let's continuously understand Israel's thirst and God's miraculous provision using `reindex()` and `interpolate()`!")

    try:
        analyzer = WaterReindexInterpolateAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 반석에서 난 물 분석 중 오류 발생: {e}")
        return None

def run_living_water_flow_analysis():
    """요한복음 생수의 강 결합/정렬 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 생수의 강 결합/정렬 분석 ===")
    print("말씀 섭취와 기도 강도 데이터를 `align()`과 `merge_asof()`로 결합하여 영적 흐름을 통합적으로 탐구해보자!")
    print("Let's integratively explore spiritual flow by combining Word intake and prayer intensity data using `align()` and `merge_asof()`!")

    try:
        analyzer = LivingWaterCombineAlignAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 생수의 강 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `reindex()`, `interpolate()` = 파편화된 정보 속 하나님의 신실한 공급 추적",
        "🏺 반석에서 난 물 = 불완전한 상황 속 하나님의 완전한 공급",
        "📜 생수의 강 = 말씀 섭취와 기도를 통한 지속적인 영적 채움",
        "💡 `align()`, `merge_asof()` = 서로 다른 영적 요소들의 통합적 이해"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 갈증 수준 보간 평균과 영적 흐름 속도 평균을 기반으로 통찰 제공
        thirst_avg = exodus_results.get('reindex_interpolate_result', pd.DataFrame())['thirst_level_interpolated'].mean() if exodus_results and 'reindex_interpolate_result' in exodus_results else 0
        flow_rate_avg = john_results.get('merged_asof_data', pd.DataFrame())['spiritual_flow_rate'].mean() if john_results and 'merged_asof_data' in john_results else 0

        if thirst_avg < 5 and flow_rate_avg > 7:
            print(f"✨ 반석에서 난 물({thirst_avg:.1f})처럼, 생수의 강({flow_rate_avg:.1f})으로 당신의 영적 갈증은 해소되고 풍성한 흐름을 경험합니다!")
            print(f"✨ Like water from the rock ({thirst_avg:.1f}), your spiritual thirst is quenched and you experience an abundant flow ({flow_rate_avg:.1f}) through the river of living water!")
        elif thirst_avg > 7:
            print(f"🌱 갈증({thirst_avg:.1f})이 심할수록, 생수의 강({flow_rate_avg:.1f})으로 더 깊이 나아가야 합니다!")
            print(f"🌱 The deeper your thirst ({thirst_avg:.1f}), the more you must go deeper into the river of living water ({flow_rate_avg:.1f})!")
        else:
            print(f"🙏 파편화된 삶의 정보들을 주님 안에서 결합하고 보간하여, 주님의 완전한 인도하심을 이해하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to combine and interpolate the fragmented information of your life in the Lord, and understand His complete guidance!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 18 미리보기 (Preview) ===

"이트로의 조언 — 함수형 파이프라인 (Functional Pipelines)"

모세가 이드로의 조언을 받아들여 재판 업무를 분담했듯이, 데이터 분석에서도 여러 단계를 거치는 복잡한 작업을 함수형 파이프라인으로 구성하면 효율성과 가독성을 높일 수 있습니다.
`assign()`, `pipe()`와 같은 함수는 데이터 처리 과정을 명확하고 간결하게 연결하는 데 필수적입니다.

Just as Moses accepted Jethro's advice to delegate judicial tasks, in data analysis, structuring complex multi-step operations into functional pipelines can increase efficiency and readability.
Functions like `assign()` and `pipe()` are essential for clearly and concisely connecting data processing steps.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `df.assign()`: 새로운 컬럼을 추가하며 DataFrame 반환
🔍 `df.pipe()`: DataFrame 메서드 체이닝을 넘어선 함수형 파이프라인 구축
🎯 메서드 체이닝 패턴: 여러 연산을 간결하게 연결
📊 이드로의 조언처럼 데이터 처리 과정을 효율적으로 구성하여 하나님의 지혜를 탐구

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 18:24)
"나는 참 포도나무요 내 아버지는 농부라" (요한복음 15:1)
    """
    print(preview)

def run_chapter17(interactive: bool = True):
    """Chapter 17 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 17을 시작합니다!")
        print("이 챕터에서는 `reindex()`, `align()`, `merge_asof()`, `interpolate()`를 사용하여 데이터 결합 및 보간을 배우고, 성경 속 하나님의 완전한 인도하심과 지속적인 채움을 탐구합니다.")
        print("This chapter introduces data combining and interpolation using `reindex()`, `align()`, `merge_asof()`, `interpolate()`, exploring God's complete guidance and continuous provision in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '17',
        'title': '반석에서 난 물 — 결합과 보간',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 반석에서 난 물 분석
    exodus_results = run_water_from_rock_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 생수의 강 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's living water flow analysis...)")

    # 2. 요한복음 생수의 강 분석
    john_results = run_living_water_flow_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 반석에서 물을 내시고 생수의 강으로 저희를 채우시니 감사합니다.
파편화된 저의 삶의 정보들을 주님 안에서 결합하고 보간하여,
주님의 완전한 인도하심과 지속적인 채움을 온전히 이해하게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, thank You for bringing water from the rock and filling us with the river of living water.
May the fragmented information of my life be combined and interpolated in You,
so that I may fully understand Your complete guidance and continuous provision. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 17 완료! 열일곱 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 17 Complete! You have finished the seventeenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter17(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch17_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 17 시작! (Starting JesusBornd Pandas Chapter 17!)\n")
    main()
