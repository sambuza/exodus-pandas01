
"""
Chapter 12 통합 실행 스크립트
홍해를 건너며 — 중복과 고유값

"이스라엘 자손이 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니" (출 14:29)
"예수께서 곧 그들에게 말씀하여 가라사대 안심하라 내니 두려워 말라 하신대" (요 6:20)
"""

import sys
from pathlib import Path
import json
from datetime import datetime

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch12.red_sea_duplicates_unique import RedSeaDuplicatesUniqueAnalyzer
from chapters.ch12.jesus_walks_water_duplicates_unique import JesusWalksWaterDuplicatesUniqueAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 12: 홍해를 건너며 — 중복과 고유값                ║
║                                                                      ║
║    "이스라엘 자손이 바다 가운데 육지로 행하고 물은 그들의 좌우에      ║
║     벽이 되니" (출애굽기 14:29)                                        ║
║    "예수께서 곧 그들에게 말씀하여 가라사대 안심하라 내니 두려워 말라  ║
║     하신대" (요한복음 6:20)                                            ║
║                                                                      ║
║    🗺️  출애굽기 14장: 홍해를 건넘                                      ║
║    📊 요한복음 6:16-21: 예수님께서 물 위를 걸으심                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_red_sea_analysis():
    """출애굽기 홍해 사건 중복/고유값 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 홍해 사건 중복/고유값 분석 ===")
    print("홍해 사건에서 반복되는 두려움과 하나님의 유일한 구원 순간을 데이터로 탐구해보자!")
    print("Let's explore recurring fears and God's unique salvation moments in the Red Sea event through data!")

    try:
        analyzer = RedSeaDuplicatesUniqueAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 홍해 사건 분석 중 오류 발생: {e}")
        return None

def run_jesus_walks_water_analysis():
    """요한복음 예수님 물 위를 걸으신 사건 중복/고유값 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 예수님 물 위를 걸으신 사건 중복/고유값 분석 ===")
    print("제자들의 반복되는 두려움과 예수님의 고유한 평안을 데이터로 비교하여 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by comparing the disciples' recurring fears and Jesus' unique peace through data!")

    try:
        analyzer = JesusWalksWaterDuplicatesUniqueAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 물 위를 걸으신 사건 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `duplicated()`, `drop_duplicates()` = 불필요한 중복 제거로 본질 발견",
        "🏺 홍해 사건 = 반복되는 두려움 속 하나님의 유일한 구원",
        "📜 물 위를 걸으신 예수님 = 세상의 혼란 속 고유한 평안과 능력",
        "💡 `unique()`, `nunique()` = 데이터 속 진정한 정체성과 고유한 가치 탐구"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 홍해 사건의 고유한 결과 수와 예수님 사건의 고유한 감정 수를 기반으로 통찰 제공
        num_unique_red_sea_outcomes = exodus_results.get('unique_groups_outcomes', (None, None, None, 0))[3] if exodus_results else 0
        num_unique_jesus_emotions = john_results.get('unique_emotions_events', (None, 0, None, None))[1] if john_results else 0

        if num_unique_red_sea_outcomes > 1 and num_unique_jesus_emotions > 1:
            print(f"✨ 홍해 사건의 고유한 결과({num_unique_red_sea_outcomes}가지)처럼, 예수님 안에서 당신의 삶은 다양한 고유한 감정({num_unique_jesus_emotions}가지)으로 풍성해질 수 있습니다!")
            print(f"✨ Like the unique outcomes of the Red Sea event ({num_unique_red_sea_outcomes}), your life in Jesus can be enriched with various unique emotions ({num_unique_jesus_emotions})!")
        elif num_unique_red_sea_outcomes == 1:
            print(f"🌱 홍해 사건의 유일한 구원처럼, 예수님은 당신의 삶에 유일한 해답을 주십니다!")
            print(f"🌱 Like the unique salvation of the Red Sea event, Jesus gives unique answers to your life!")
        else:
            print(f"🙏 불필요한 중복을 제거하고, 주님 안에서 당신의 고유한 정체성을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to remove unnecessary duplicates and discover your unique identity in the Lord!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 13 미리보기 (Preview) ===

"구름기둥·불기둥 — 날짜/시간 기초 (Date/Time Basics)"

이스라엘 백성이 광야에서 구름기둥과 불기둥의 인도를 받았듯이, 데이터 분석에서도 시간의 흐름에 따른 변화를 추적하는 것은 매우 중요합니다.
날짜와 시간 데이터는 영적 여정의 흐름을 이해하고, 하나님의 인도하심의 패턴을 발견하는 데 필수적인 요소입니다.

Just as the Israelites were guided by the pillar of cloud and fire in the wilderness, tracking changes over time is crucial in data analysis.
Date and time data are essential for understanding the flow of the spiritual journey and discovering patterns of God's guidance.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `pd.to_datetime()`: 문자열을 datetime 객체로 변환
🔍 `DatetimeIndex`: 시계열 데이터의 인덱스 활용
🎯 `resample()`: 시간 간격별 데이터 재표본화
📊 광야 여정의 시간 흐름 속 하나님의 인도하심 패턴 분석

"여호와께서 그들 앞에 행하사 낮에는 구름 기둥으로 그들의 길을 인도하시고 밤에는 불 기둥으로 그들에게 비취사 주야로 진행하게 하시니" (출애굽기 13:21)
"명절 끝날 곧 큰 날에 예수께서 서서 외쳐 가라사대 누구든지 목마르거든 내게로 와서 마시라" (요한복음 7:37)
    """
    print(preview)

def run_chapter12(interactive: bool = True):
    """Chapter 12 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 12를 시작합니다!")
        print("이 챕터에서는 `duplicated()`, `drop_duplicates()`, `unique()`, `nunique()`를 사용하여 데이터 중복 제거 및 고유값 분석을 배우고, 성경 속 하나님의 유일한 구원과 예수님의 고유한 능력을 탐구합니다.")
        print("This chapter introduces data duplicate removal and unique value analysis using `duplicated()`, `drop_duplicates()`, `unique()`, `nunique()`, exploring God's unique salvation and Jesus' distinct power in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '12',
        'title': '홍해를 건너며 — 중복과 고유값',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 홍해 사건 분석
    exodus_results = run_red_sea_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 예수님 물 위를 걸으신 사건 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's Jesus walks on water analysis...)")

    # 2. 요한복음 예수님 물 위를 걸으신 사건 분석
    john_results = run_jesus_walks_water_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 홍해를 가르시고 물 위를 걸으신 주님의 유일하고 고유한 능력을 찬양합니다.
저의 삶에서 불필요한 중복과 세상의 두려움을 제거하시고,
주님 안에서 저의 참된 정체성과 고유한 가치를 발견하게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, I praise Your unique and distinct power that parted the Red Sea and walked on water.
Remove unnecessary duplicates and worldly fears from my life,
and help me discover my true identity and unique value in You. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 12 완료! 열두 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 12 Complete! You have finished the twelfth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter12(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch12_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 12 시작! (Starting JesusBornd Pandas Chapter 12!)\n")
    main()
