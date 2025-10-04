

"""
Chapter 10 통합 실행 스크립트
흑암 중의 빛 — 그룹 연산

"여호와께서 모세에게 이르시되 하늘을 향하여 네 손을 내밀어 애굽 땅 위에 흑암이 있게 하라 곧 더듬을 만한 흑암이니라" (출 10:21)
"예수께서 또 일러 가라사대 나는 세상의 빛이니 나를 따르는 자는 어두움에 다니지 아니하고 생명의 빛을 얻으리라" (요 8:12)
"""

import sys
from pathlib import Path
import json
from datetime import datetime

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch10.locusts_darkness_groupby import LocustsDarknessGroupbyAnalyzer
from chapters.ch10.light_of_the_world_groupby import LightOfTheWorldGroupbyAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 10: 흑암 중의 빛 — 그룹 연산                     ║
║                                                                      ║
║    "여호와께서 모세에게 이르시되 하늘을 향하여 네 손을 내밀어          ║
║     애굽 땅 위에 흑암이 있게 하라 곧 더듬을 만한 흑암이니라" (출 10:21) ║
║    "예수께서 또 일러 가라사대 나는 세상의 빛이니 나를 따르는 자는      ║
║     어두움에 다니지 아니하고 생명의 빛을 얻으리라" (요 8:12)            ║
║                                                                      ║
║    🗺️  출애굽기 10장: 메뚜기 재앙과 흑암 재앙                           ║
║    📊 요한복음 8:12: "나는 세상의 빛이니"                               ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_locusts_darkness_analysis():
    """출애굽기 메뚜기/흑암 재앙 그룹 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 재앙의 그룹별 영향 분석 ===")
    print("애굽과 고센, 두 그룹에 미친 재앙의 영향을 비교하여 하나님의 구별된 보호를 확인해보자!")
    print("Let's compare the impact of plagues on Egypt and Goshen to confirm God's distinct protection!")

    try:
        analyzer = LocustsDarknessGroupbyAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 재앙 그룹 분석 중 오류 발생: {e}")
        return None

def run_light_of_the_world_analysis():
    """요한복음 빛과 어둠 그룹 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 빛과 어둠의 그룹별 특성 분석 ===")
    print("빛을 따르는 삶과 어둠에 거하는 삶의 영적 특성을 비교하여 예수님의 말씀을 데이터로 탐구해보자!")
    print("Let's explore Jesus' words by comparing the spiritual characteristics of lives following light versus darkness!")

    try:
        analyzer = LightOfTheWorldGroupbyAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 빛과 어둠 그룹 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `groupby()` = 복잡한 데이터 속 하나님의 질서와 구별 발견",
        "🏺 애굽과 고센의 구별 = 하나님의 구별된 보호와 심판",
        "📜 빛과 어둠의 극명한 차이 = 예수님 말씀의 영적 진리",
        "💡 `agg()` = 그룹별 다양한 통계로 하나님의 일하심의 패턴 탐구"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        egypt_avg_impact = exodus_results['impact_by_location'].get('Egypt', 0) if 'impact_by_location' in exodus_results else 0
        light_avg_impact = john_results['impact_by_category'].get('Light', 0) if 'impact_by_category' in john_results else 0

        if egypt_avg_impact > 50 and light_avg_impact > 5:
            print(f"✨ 애굽의 큰 고통({egypt_avg_impact:.1f}) 속에서도 빛({light_avg_impact:.1f})을 따르는 삶은 구별된 평안을 누립니다!")
            print(f"✨ Even amidst great suffering in Egypt ({egypt_avg_impact:.1f}), a life following the light ({light_avg_impact:.1f}) enjoys distinct peace!")
        elif egypt_avg_impact > 30:
            print(f"🌱 세상의 어둠({egypt_avg_impact:.1f})이 깊을수록, 빛 되신 예수님({light_avg_impact:.1f})을 더욱 의지해야 합니다!")
            print(f"🌱 The deeper the darkness of the world ({egypt_avg_impact:.1f}), the more we must rely on Jesus, the Light ({light_avg_impact:.1f})!")
        else:
            print(f"🙏 데이터 속에서 하나님의 구별된 사랑과 빛의 능력을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to discover God's distinct love and the power of light within the data!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 11 미리보기 (Preview) ===

"유월절 — 병합과 연결의 방식 (Merging and Joining Data)"

유월절은 이스라엘 백성의 구원과 애굽의 심판이라는 두 가지 사건이 하나의 큰 그림 속에서 연결되는 중요한 절기입니다.
데이터 분석에서도 서로 다른 데이터셋을 하나의 의미 있는 정보로 '병합(merge)'하고 '연결(join)'하는 것은 전체적인 그림을 이해하는 데 필수적입니다.

The Passover is a crucial festival where two events—the salvation of Israel and the judgment of Egypt—are connected within one grand narrative.
Similarly, in data analysis, 'merging' and 'joining' different datasets into a single meaningful piece of information are essential for understanding the complete picture.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `merge()`: 두 DataFrame을 특정 키를 기준으로 병합
🔍 `join()`: 인덱스를 기준으로 DataFrame 결합
🎯 `concat()`: DataFrame을 단순히 이어 붙이기
📊 유월절 어린 양의 피처럼 흩어진 정보들을 하나로 모으기

"내가 그 밤에 애굽 땅에 두루 다니며 사람이나 짐승을 무론하고 애굽 가운데 처음 난 것을 다 치고 애굽의 모든 신에게 벌을 내리리라 나는 여호와로라" (출애굽기 12:12)
"예수께서 이르시되 내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요한복음 6:35)
    """
    print(preview)

def run_chapter10(interactive: bool = True):
    """Chapter 10 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 10을 시작합니다!")
        print("이 챕터에서는 `groupby()`를 사용하여 데이터 그룹별 분석을 배우고, 성경 속 하나님의 구별된 역사와 빛의 능력을 탐구합니다.")
        print("This chapter introduces data analysis by group using `groupby()`, exploring God's distinct work and the power of light in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '10',
        'title': '흑암 중의 빛 — 그룹 연산',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 재앙 그룹 분석
    exodus_results = run_locusts_darkness_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 빛과 어둠 그룹 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's light and darkness group analysis...)")

    # 2. 요한복음 빛과 어둠 그룹 분석
    john_results = run_light_of_the_world_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 흑암 같은 세상 속에서도 빛 되신 주님을 따르며 살게 하소서.
복잡한 데이터 속에서 `groupby()`를 통해 주님의 질서와 구별된 사랑을 발견하게 하시고,
어둠 속에서도 빛을 찾아내는 지혜를 주소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, help me to live following You, the Light, even in a world like darkness.
Through `groupby()` in complex data, help me discover Your order and distinct love,
and grant me wisdom to find light even in darkness. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 10 완료! 열 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 10 Complete! You have finished the tenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter10(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch10_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 10 시작! (Starting JesusBornd Pandas Chapter 10!)\n")
    main()
