"""
Chapter 09 통합 실행 스크립트
견고한 마음 — 집계의 기초

"여호와의 손이 들에 있는 네 생축에게 더하리니... 심한 악질이 있을 것이며" (출 9:3)
"예수께서 가라사대 가라 네 아들이 살았다 하신대 그 사람이 예수의 하신 말씀을 믿고 가더니" (요 4:50)
"""

import sys
from pathlib import Path
import json
from datetime import datetime

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from chapters.ch09.plagues_aggregation import PlaguesAggregationAnalyzer
from chapters.ch09.officials_son_aggregation import OfficialsSonAggregationAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 09: 견고한 마음 — 집계의 기초                      ║
║                                                                      ║
║    "여호와의 손이 들에 있는 네 생축에게 더하리니... 심한 악질이          ║
║     있을 것이며" (출애굽기 9:3)                                        ║
║    "예수께서 가라사대 가라 네 아들이 살았다 하신대 그 사람이            ║
║     예수의 하신 말씀을 믿고 가더니" (요한복음 4:50)                     ║
║                                                                      ║
║    🗺️  출애굽기 9장: 다섯, 여섯, 일곱 번째 재앙                         ║
║    📊 요한복음 4:46-54: 왕의 신하의 아들을 고치심                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_plagues_analysis():
    """출애굽기 재앙 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 재앙의 심각도 집계 ===")
    print("파라오의 견고한 마음이 애굽에 가져온 고통을 숫자로 확인해보자!")
    print("Let's quantify the suffering brought upon Egypt by Pharaoh's hardened heart!")

    try:
        analyzer = PlaguesAggregationAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 재앙 분석 중 오류 발생: {e}")
        return None

def run_officials_son_analysis():
    """요한복음 왕의 신하 아들 치유 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 믿음의 성장 집계 ===")
    print("왕의 신하의 믿음이 예수님의 말씀을 통해 어떻게 성장했는지 확인해보자!")
    print("Let's see how the royal official's faith grew through Jesus' word!")

    try:
        analyzer = OfficialsSonAggregationAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 치유 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 집계(Aggregation) = 복잡한 데이터 속 하나님의 메시지 요약",
        "🏺 재앙의 심각도 = 파라오의 완악함과 하나님의 권능의 증거",
        "📜 믿음의 성장 = 예수님 말씀의 시공간 초월적 능력",
        "💡 `describe()`, `sum()`, `mean()`, `count()` = 데이터 속 영적 패턴 발견 도구"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        total_plague_severity = exodus_results.get('total_impact', 0)
        avg_faith_level = john_results.get('average_faith_and_time', (0,0))[0]

        if total_plague_severity > 200 and avg_faith_level > 90:
            print(f"✨ 당신은 애굽의 큰 고통 속에서도 왕의 신하처럼 굳건한 믿음({avg_faith_level:.1f})을 지킬 수 있습니다!")
            print(f"✨ You can maintain a steadfast faith ({avg_faith_level:.1f}) like the royal official even amidst great suffering in Egypt!")
        elif total_plague_severity > 150:
            print(f"🌱 애굽의 재앙({total_plague_severity})은 크지만, 믿음({avg_faith_level:.1f})으로 극복할 수 있습니다!")
            print(f"🌱 Though the plagues of Egypt ({total_plague_severity}) are great, you can overcome them with faith ({avg_faith_level:.1f})!")
        else:
            print(f"🙏 작은 데이터 속에서도 하나님의 큰 계획을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to find God's great plan even in small data!")


def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 10 미리보기 (Preview) ===

"흑암 중의 빛 — 그룹 연산 (Group Operations)"

애굽 땅에 흑암 재앙이 임했을 때, 이스라엘 자손이 거하는 고센 땅에는 빛이 있었습니다.
데이터 분석에서도 전체 데이터 속에서 특정 기준(그룹)별로 데이터를 나누어 분석하는
'그룹 연산'은 혼돈 속에서 질서를 발견하고, 어둠 속에서 빛을 찾아내는 중요한 통찰을 제공합니다.

When darkness covered Egypt, there was light in Goshen where the Israelites lived.
Similarly, in data analysis, 'group operations'—dividing data by specific criteria (groups)
within the entire dataset—provide crucial insights, finding order in chaos and light in darkness.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `groupby()` 기본(집계/필터/변환)
🔍 `agg()`를 이용한 다중 집계
🎯 데이터 속에서 하나님의 구별된 백성 찾기
📊 성경 속 그룹별 패턴 분석

"여호와께서 모세에게 이르시되 하늘을 향하여 네 손을 내밀어 애굽 땅 위에 흑암이 있게 하라 곧 더듬을 만한 흑암이니라" (출애굽기 10:21)
"예수께서 또 일러 가라사대 나는 세상의 빛이니 나를 따르는 자는 어두움에 다니지 아니하고 생명의 빛을 얻으리라" (요한복음 8:12)
    """
    print(preview)

def run_chapter09(interactive: bool = True):
    """Chapter 09 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 09를 시작합니다!")
        print("이 챕터에서는 데이터 집계의 기초를 배우고, 성경 속 하나님의 권능과 믿음의 성장을 탐구합니다.")
        print("This chapter introduces the basics of data aggregation, exploring God's power and the growth of faith in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '09',
        'title': '견고한 마음 — 집계의 기초',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 재앙 분석
    exodus_results = run_plagues_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 치유 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's healing analysis...)")

    # 2. 요한복음 치유 분석
    john_results = run_officials_son_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 복잡한 세상 속에서 저의 마음이 견고해지지 않도록 지켜주시고,
모든 상황 속에서 주님의 메시지를 집계하고 요약하여 깨닫게 하소서.
예수님의 이름으로 기도합니다. 아멘."

"Lord, keep my heart from hardening in this complex world,
and help me to aggregate and summarize Your message in all situations.
I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 09 완료! 아홉 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 09 Complete! You have finished the ninth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter09(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch09_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 09 시작! (Starting JesusBornd Pandas Chapter 09!)\n")
    main()