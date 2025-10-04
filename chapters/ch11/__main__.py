

"""
Chapter 11 통합 실행 스크립트
유월절 — 병합과 연결의 방식

"내가 그 밤에 애굽 땅에 두루 다니며 사람이나 짐승을 무론하고 애굽 가운데 처음 난 것을 다 치고 애굽의 모든 신에게 벌을 내리리라 나는 여호와로라" (출 12:12)
"예수께서 이르시되 내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요 6:35)
"""

import sys
from pathlib import Path
import json
from datetime import datetime

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch11.passover_merge_join import PassoverMergeJoinAnalyzer
from chapters.ch11.feeding_five_thousand_concat import FeedingFiveThousandConcatAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 11: 유월절 — 병합과 연결의 방식                  ║
║                                                                      ║
║    "내가 그 밤에 애굽 땅에 두루 다니며 사람이나 짐승을 무론하고        ║
║     애굽 가운데 처음 난 것을 다 치고 애굽의 모든 신에게 벌을 내리리라  ║
║     나는 여호와로라" (출애굽기 12:12)                                  ║
║    "예수께서 이르시되 내가 곧 생명의 떡이니 내게 오는 자는 결코        ║
║     주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요 6:35) ║
║                                                                      ║
║    🗺️  출애굽기 11장: 열 번째 재앙 예고와 유월절 준비                   ║
║    📊 요한복음 6:4-14: 오병이어 기적                                   ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_passover_analysis():
    """출애굽기 유월절 병합/연결 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 유월절 사건 병합 분석 ===")
    print("열 번째 재앙 예고와 유월절 규례를 병합하여 하나님의 구원 계획을 통합적으로 이해해보자!")
    print("Let's merge the tenth plague announcement and Passover ordinances to understand God's salvation plan integrally!")

    try:
        analyzer = PassoverMergeJoinAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 유월절 분석 중 오류 발생: {e}")
        return None

def run_feeding_five_thousand_analysis():
    """요한복음 오병이어 기적 연결 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 오병이어 기적 데이터 연결 분석 ===")
    print("초기 자원과 기적 후 남은 조각 데이터를 연결하여 예수님의 능력을 데이터로 탐구해보자!")
    print("Let's concatenate initial resources and leftover fragments to explore Jesus' power through data!")

    try:
        analyzer = FeedingFiveThousandConcatAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 오병이어 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `merge()`, `join()`, `concat()` = 파편화된 정보들을 하나로 모으는 도구",
        "🏺 유월절 = 심판과 구원이 병합되는 하나님의 완벽한 계획",
        "📜 오병이어 = 작은 자원을 통해 풍성함을 만드시는 예수님의 능력",
        "💡 데이터 연결 = 흩어진 조각들을 통해 큰 그림을 이해하는 영적 통찰"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 유월절 규례 순종 수준과 오병이어 자원 증폭률을 가정하여 통찰 제공
        passover_obedience_level = exodus_results.get('left_join_result', pd.DataFrame()).get('obedience_level', pd.Series()).mean() if exodus_results else 0
        initial_resources_sum = john_results.get('vertical_concat_result', pd.DataFrame())[john_results['vertical_concat_result']['source'] == 'boy']['quantity_initial'].sum() if john_results and 'vertical_concat_result' in john_results else 0
        final_resources_sum = john_results.get('vertical_concat_result', pd.DataFrame())[john_results['vertical_concat_result']['source'] == 'basket']['quantity_initial'].sum() if john_results and 'vertical_concat_result' in john_results else 0

        if passover_obedience_level > 90 and final_resources_sum > initial_resources_sum * 10:
            print(f"✨ 유월절 규례에 대한 높은 순종({passover_obedience_level:.1f}%)처럼, 당신의 작은 헌신도 예수님 안에서 오병이어({initial_resources_sum} -> {final_resources_sum}) 기적을 이룰 수 있습니다!")
            print(f"✨ Like the high obedience to Passover ordinances ({passover_obedience_level:.1f}%), your small dedication can also achieve a miracle of feeding five thousand ({initial_resources_sum} -> {final_resources_sum}) in Jesus!")
        elif passover_obedience_level > 80:
            print(f"🌱 유월절 준비({passover_obedience_level:.1f}%)처럼, 꾸준한 순종은 예수님의 풍성한 은혜를 경험하게 합니다!")
            print(f"🌱 Like Passover preparations ({passover_obedience_level:.1f}%), consistent obedience leads to experiencing Jesus' abundant grace!")
        else:
            print(f"🙏 흩어진 삶의 조각들을 예수님 안에서 연결하여, 큰 그림을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to connect the scattered pieces of your life in Jesus and discover the bigger picture!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 12 미리보기 (Preview) ===

"홍해를 건너며 — 중복과 고유값 (Duplicates and Unique Values)"

이스라엘 백성이 홍해를 건너 광야로 들어섰을 때, 그들은 애굽의 속박에서 벗어나 새로운 정체성을 얻었습니다.
데이터 분석에서도 중복된 값들을 제거하고 고유한 값들을 찾아내는 것은 데이터의 '진정한 정체성'을 발견하고 불필요한 노이즈를 제거하는 중요한 과정입니다.

When the Israelites crossed the Red Sea into the wilderness, they gained a new identity, freed from Egyptian bondage.
Similarly, in data analysis, removing duplicate values and finding unique ones is crucial for discovering the 'true identity' of data and eliminating unnecessary noise.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `duplicated()`: 중복된 행 식별
🔍 `drop_duplicates()`: 중복된 행 제거
🎯 `unique()`: 고유한 값 배열 반환
📊 `nunique()`: 고유한 값의 개수 계산

"이스라엘 자손이 바다 가운데 육지로 행하고 물은 그들의 좌우에 벽이 되니" (출애굽기 14:29)
"예수께서 곧 그들에게 말씀하여 가라사대 안심하라 내니 두려워 말라 하신대" (요한복음 6:20)
    """
    print(preview)

def run_chapter11(interactive: bool = True):
    """Chapter 11 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 11을 시작합니다!")
        print("이 챕터에서는 `merge()`, `join()`, `concat()`을 사용하여 데이터 병합 및 연결을 배우고, 성경 속 하나님의 구원 계획과 예수님의 능력을 탐구합니다.")
        print("This chapter introduces data merging and connecting using `merge()`, `join()`, `concat()`, exploring God's salvation plan and Jesus' power in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '11',
        'title': '유월절 — 병합과 연결의 방식',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 유월절 분석
    exodus_results = run_passover_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 오병이어 기적 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's feeding five thousand miracle analysis...)")

    # 2. 요한복음 오병이어 기적 분석
    john_results = run_feeding_five_thousand_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 유월절 어린 양의 피로 저희를 구원하시고, 오병이어의 기적으로 저희의 필요를 채우시니 감사합니다.
저의 삶의 흩어진 조각들을 주님 안에서 병합하고 연결하여, 주님의 크신 계획을 온전히 이해하게 하소서.
예수님의 이름으로 기도합니다. 아멘."

"Lord, thank You for saving us with the blood of the Passover lamb and for meeting our needs with the miracle of feeding the five thousand.
May the scattered pieces of my life be merged and connected in You, so that I may fully understand Your great plan.
I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 11 완료! 열한 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 11 Complete! You have finished the eleventh wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter11(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch11_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 11 시작! (Starting JesusBornd Pandas Chapter 11!)\n")
    main()
