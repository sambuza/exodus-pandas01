

"""
Chapter 13 통합 실행 스크립트
구름기둥·불기둥 — 날짜/시간 기초

"여호와께서 그들 앞에 행하사 낮에는 구름 기둥으로 그들의 길을 인도하시고 밤에는 불 기둥으로 그들에게 비취사 주야로 진행하게 하시니" (출 13:21)
"명절 끝날 곧 큰 날에 예수께서 서서 외쳐 가라사대 누구든지 목마르거든 내게로 와서 마시라" (요 7:37)
"""

import sys
from pathlib import Path
import json
from datetime import datetime

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch13.pillar_datetime_analysis import PillarDatetimeAnalyzer
from chapters.ch13.living_water_resample_analysis import LivingWaterResampleAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 13: 구름기둥·불기둥 — 날짜/시간 기초                ║
║                                                                      ║
║    \"여호와께서 그들 앞에 행하사 낮에는 구름 기둥으로 그들의 길을      ║
║     인도하시고 밤에는 불 기둥으로 그들에게 비취사 주야로 진행하게 하시니\" (출 13:21) ║
║    \"명절 끝날 곧 큰 날에 예수께서 서서 외쳐 가라사대 누구든지 목마르거든 ║
║     내게로 와서 마시라\" (요한복음 7:37)                                  ║
║                                                                      ║
║      출애굽기 13장: 구름기둥과 불기둥의 인도                         ║
║      요한복음 7:37-39: 생수의 강                                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_pillar_guidance_analysis():
    """출애굽기 구름기둥/불기둥 날짜/시간 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 구름기둥/불기둥 날짜/시간 분석 ===")
    print("광야 여정의 시간 흐름에 따른 하나님의 인도하심 패턴을 데이터로 탐구해보자!")
    print("Let's explore the patterns of God's guidance over the wilderness journey's timeline through data!")

    try:
        analyzer = PillarDatetimeAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 구름기둥/불기둥 분석 중 오류 발생: {e}")
        return None

def run_living_water_analysis():
    """요한복음 생수의 강 재표본화 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 생수의 강 재표본화 분석 ===")
    print("영적 갈증과 말씀으로 인한 채움의 변화를 시간 간격별로 분석하여 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by analyzing changes in spiritual thirst and fulfillment through the Word over time intervals!")

    try:
        analyzer = LivingWaterResampleAnalyzer()
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
        "📊 `to_datetime()`, `DatetimeIndex` = 시간의 흐름 속 하나님의 신실한 인도",
        "🏺 구름기둥/불기둥 = 낮과 밤, 모든 시간에 걸친 세밀한 인도",
        "📜 생수의 강 = 영적 갈증을 채우는 말씀의 지속적인 역사",
        "💡 `resample()` = 시간 간격별 영적 상태 변화를 통한 패턴 발견"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 구름기둥/불기둥 인도 빈도와 생수의 강 채움 수준을 기반으로 통찰 제공
        guidance_frequency = exodus_results.get('guidance_frequency', pd.DataFrame()).sum().sum() if exodus_results else 0
        avg_fulfillment = john_results.get('daily_resample_avg', pd.DataFrame())['fulfillment_level'].mean() if john_results and 'daily_resample_avg' in john_results else 0

        if guidance_frequency > 5 and avg_fulfillment > 7:
            print(f"✨ 구름기둥/불기둥({guidance_frequency}회)의 세밀한 인도처럼, 당신의 삶도 말씀({avg_fulfillment:.1f})으로 충만하여 영적 갈증이 해소됩니다!")
            print(f"✨ Like the meticulous guidance of the pillar ({guidance_frequency} times), your life is filled with the Word ({avg_fulfillment:.1f}), and your spiritual thirst is quenched!")
        elif guidance_frequency > 3:
            print(f"🌱 하나님의 인도({guidance_frequency}회)는 꾸준하지만, 생수의 강({avg_fulfillment:.1f})으로 더 깊이 채워져야 합니다!")
            print(f"🌱 God's guidance ({guidance_frequency} times) is constant, but you need to be more deeply filled by the river of living water ({avg_fulfillment:.1f})!")
        else:
            print(f"🙏 시간의 흐름 속에서 하나님의 인도하심과 말씀의 채움을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to discover God's guidance and the fulfillment of His Word in the flow of time!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 14 미리보기 (Preview) ===

"바다 한가운데 길 — 멀티인덱스 입문 (MultiIndex Introduction)"

이스라엘 백성이 홍해를 건너 바다 한가운데 마른 땅으로 걸어갔듯이, 데이터 분석에서도 여러 계층의 인덱스를 사용하여 복잡한 데이터를 구조화하고 접근하는 '멀티인덱스'는 깊이 있는 통찰을 얻는 데 필수적입니다.

Just as the Israelites walked on dry ground through the midst of the Red Sea, in data analysis, using multiple levels of indexes to structure and access complex data—'MultiIndex'—is essential for gaining deep insights.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `pd.MultiIndex.from_arrays()`: 멀티인덱스 생성
🔍 `df.set_index()`: 기존 열로 멀티인덱스 설정
🎯 `df.loc[]`를 이용한 멀티인덱스 데이터 접근
📊 광야 여정의 복잡한 데이터 속 하나님의 세밀한 인도 패턴 분석

"이스라엘 자손이 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니" (출애굽기 14:29)
"내가 곧 문이니 누구든지 나로 말미암아 들어가면 구원을 얻고 또는 들어가며 나오며 꼴을 얻으리라" (요한복음 10:9)
    """
    print(preview)

def run_chapter13(interactive: bool = True):
    """Chapter 13 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 13을 시작합니다!")
        print("이 챕터에서는 날짜/시간 데이터의 기초를 배우고, 성경 속 하나님의 시간적인 인도하심과 말씀의 지속적인 채움을 탐구합니다.")
        print("This chapter introduces date/time data basics, exploring God's temporal guidance and the continuous fulfillment of His Word in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '13',
        'title': '구름기둥·불기둥 — 날짜/시간 기초',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 구름기둥/불기둥 분석
    exodus_results = run_pillar_guidance_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 생수의 강 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's living water analysis...)")

    # 2. 요한복음 생수의 강 분석
    john_results = run_living_water_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 광야 같은 세상 속에서 구름기둥과 불기둥으로 저희를 인도하시니 감사합니다.
시간의 흐름 속에서 주님의 신실한 인도하심과 말씀의 채움을 발견하게 하시고,
영적 갈증이 해소되는 생수의 강을 경험하게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, Thank You for guiding us with the pillar of cloud and fire in a world like a wilderness.
Help us discover Your faithful guidance and the fulfillment of Your Word in the flow of time,
and let us experience the river of living water that quenches spiritual thirst. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 13 완료! 열세 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 13 Complete! You have finished the thirteenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter13(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch13_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 13 시작! (Starting JesusBornd Pandas Chapter 13!)\n")
    main()
