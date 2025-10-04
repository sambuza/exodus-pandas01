

"""
Chapter 14 통합 실행 스크립트
바다 한가운데 길 — 멀티인덱스 입문

"이스라엘 자손이 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니" (출 14:29)
"내가 곧 문이니 누구든지 나로 말미암아 들어가면 구원을 얻고 또는 들어가며 나오며 꼴을 얻으리라" (요 10:9)
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
from chapters.ch14.red_sea_multiindex_analysis import RedSeaMultiIndexAnalyzer
from chapters.ch14.door_multiindex_access import DoorMultiIndexAccessAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 14: 바다 한가운데 길 — 멀티인덱스 입문             ║
║                                                                      ║
║    "이스라엘 자손이 바다 가운데 육지로 행하고 물은 그들의 좌우에      ║
║     벽이 되니" (출애굽기 14:29)                                        ║
║    "내가 곧 문이니 누구든지 나로 말미암아 들어가면 구원을 얻고        ║
║     또는 들어가며 나오며 꼴을 얻으리라" (요한복음 10:9)                 ║
║                                                                      ║
║    🗺️  출애굽기 14장: 홍해를 건넘                                      ║
║    📊 요한복음 10:9: "나는 문이니"                                     ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_red_sea_analysis():
    """출애굽기 홍해 길 멀티인덱스 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 홍해 길의 다층적 구조 분석 ===")
    print("홍해를 건너는 길의 시간, 그룹, 상태 등 다층적인 정보를 `MultiIndex`로 구조화하여 하나님의 세밀한 섭리를 탐구해보자!")
    print("Let's explore God's meticulous providence by structuring multi-layered information like time, group, and path condition of the Red Sea crossing using `MultiIndex`!")

    try:
        analyzer = RedSeaMultiIndexAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 홍해 길 분석 중 오류 발생: {e}")
        return None

def run_door_of_salvation_analysis():
    """요한복음 구원의 문 멀티인덱스 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 예수님이라는 문의 다층적 의미 분석 ===")
    print("예수님을 통한 길과 다른 길의 결과 및 접근 방식을 `MultiIndex`로 구조화하여 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by structuring the outcomes and approaches of the path through Jesus versus other paths using `MultiIndex`!")

    try:
        analyzer = DoorMultiIndexAccessAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 구원의 문 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `MultiIndex` = 복잡한 데이터 속 하나님의 다층적인 섭리 발견",
        "🏺 홍해의 길 = 시간, 그룹, 상태 등 다층적인 하나님의 인도",
        "📜 예수님 = 구원과 풍성한 삶으로 들어가는 유일하고 다층적인 문",
        "💡 `df.loc[]` = 특정 경로를 따라 하나님의 뜻과 구원을 효율적으로 접근"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 홍해 길의 평균 안전 수준과 예수님 길의 평균 만족도/평안 수준을 기반으로 통찰 제공
        red_sea_avg_safety = exodus_results.get('multiindex_levels_analysis', pd.DataFrame())['safety_level'].mean() if exodus_results and 'multiindex_levels_analysis' in exodus_results else 0
        jesus_path_avg_fulfillment = john_results.get('multiindex_levels_analysis', pd.DataFrame())['fulfillment_level'].mean() if john_results and 'multiindex_levels_analysis' in john_results else 0
        jesus_path_avg_peace = john_results.get('multiindex_levels_analysis', pd.DataFrame())['peace_level'].mean() if john_results and 'multiindex_levels_analysis' in john_results else 0

        if red_sea_avg_safety > 8 and jesus_path_avg_fulfillment > 8:
            print(f"✨ 홍해 길의 높은 안전({red_sea_avg_safety:.1f})처럼, 예수님이라는 문을 통해 당신은 높은 만족({jesus_path_avg_fulfillment:.1f})과 평안({jesus_path_avg_peace:.1f})을 누립니다!")
            print(f"✨ Like the high safety of the Red Sea path ({red_sea_avg_safety:.1f}), through Jesus, the Door, you experience high fulfillment ({jesus_path_avg_fulfillment:.1f}) and peace ({jesus_path_avg_peace:.1f})!")
        elif red_sea_avg_safety > 6:
            print(f"🌱 홍해 길의 안전({red_sea_avg_safety:.1f})은 중요하지만, 예수님이라는 문({jesus_path_avg_fulfillment:.1f})을 통해 더 풍성한 삶을 경험해야 합니다!")
            print(f"🌱 The safety of the Red Sea path ({red_sea_avg_safety:.1f}) is important, but through Jesus, the Door ({jesus_path_avg_fulfillment:.1f}), you must experience a more abundant life!")
        else:
            print(f"🙏 복잡한 삶 속에서 `MultiIndex`처럼 다층적인 하나님의 섭리를 이해하고, 예수님이라는 문을 통해 명확한 길을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to understand God's multi-layered providence like `MultiIndex` in complex life, and find a clear path through Jesus, the Door!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 15 미리보기 (Preview) ===

"바다의 노래 — 피벗과 형태변환 (Pivot and Reshaping)"

이스라엘 백성이 홍해를 건넌 후, 모세와 미리암은 하나님을 찬양하는 노래를 불렀습니다. 이 노래는 단순한 찬양이 아니라, 하나님의 위대한 구원 역사를 다양한 관점에서 재구성하고 선포하는 것이었습니다.
데이터 분석에서도 `pivot_table()`, `melt()`, `stack()`, `unstack()`과 같은 형태변환(Reshaping) 기술은 데이터를 다양한 관점으로 재구성하여 숨겨진 패턴과 의미를 발견하는 데 필수적입니다.

After the Israelites crossed the Red Sea, Moses and Miriam sang a song of praise to God. This song was not merely a hymn, but a reshaping and proclamation of God's great salvation history from various perspectives.
Similarly, in data analysis, reshaping techniques like `pivot_table()`, `melt()`, `stack()`, and `unstack()` are essential for discovering hidden patterns and meanings by reconfiguring data from different viewpoints.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `pivot_table()`: 데이터를 재구성하여 요약
🔍 `melt()`: 넓은 형식의 데이터를 긴 형식으로 변환
🎯 `stack()` / `unstack()`: 인덱스와 컬럼 간의 전환
📊 구원 역사를 다양한 관점에서 재구성하여 하나님의 위대함을 찬양

"여호와는 나의 힘이요 노래시며 나의 구원이시로다 그는 나의 하나님이시니 내가 그를 찬송할 것이요 내 아비의 하나님이시니 내가 그를 높이리로다" (출애굽기 15:2)
"아버지께 참으로 예배하는 자들은 신령과 진정으로 예배할 때가 오나니 곧 이때라 아버지께서는 자기에게 이렇게 예배하는 자들을 찾으시느니라" (요한복음 4:23)
    """
    print(preview)

def run_chapter14(interactive: bool = True):
    """Chapter 14 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 14를 시작합니다!")
        print("이 챕터에서는 `MultiIndex`를 사용하여 다층적인 데이터를 구조화하고 접근하는 방법을 배우고, 성경 속 하나님의 세밀한 섭리와 예수님이라는 유일한 구원의 길을 탐구합니다.")
        print("This chapter introduces how to structure and access multi-layered data using `MultiIndex`, exploring God's meticulous providence and Jesus as the unique path to salvation in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '14',
        'title': '바다 한가운데 길 — 멀티인덱스 입문',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 홍해 길 분석
    exodus_results = run_red_sea_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 구원의 문 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's door of salvation analysis...)")

    # 2. 요한복음 구원의 문 분석
    john_results = run_door_of_salvation_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 홍해를 가르시고 예수님이라는 유일한 문을 통해 저희에게 구원의 길을 열어주시니 감사합니다.
복잡한 삶 속에서 `MultiIndex`처럼 다층적인 주님의 섭리를 이해하게 하시고,
예수님 안에서 참된 구원과 풍성한 삶을 누리게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, Thank You for parting the Red Sea and opening the path of salvation through Jesus, the only Door.
Help us understand Your multi-layered providence like `MultiIndex` in complex life,
and enable us to enjoy true salvation and abundant life in Jesus. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 14 완료! 열네 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 14 Complete! You have finished the fourteenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter14(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch14_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 14 시작! (Starting JesusBornd Pandas Chapter 14!)\n")
    main()
