"""
Chapter 07 통합 실행 스크립트
첫 재앙의 시작 — 정렬과 순위

"여호와께서 모세에게 이르시되 바로에게 가서 그에게 이르기를 히브리 사람의 하나님 여호와께서 말씀하시기를 내 백성을 보내라 그들이 나를 섬길 것이니라"
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# ch07의 분석 모듈들 (예상)
from chapters.ch07.first_plague_analysis import analyze_plague_severity, analyze_pharaoh_response_ranking
from chapters.ch07.light_and_darkness_ranking import analyze_spiritual_ranking
from chapters.ch07.sorting_and_ranking_demos import demo_sort_values, demo_sort_index, demo_rank

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║         Chapter 07: 첫 재앙의 시작 — 정렬과 순위                       ║
║                                                                      ║
║    "여호와께서 모세에게 이르시되 바로에게 가서 그에게 이르기를        ║
║     히브리 사람의 하나님 여호와께서 말씀하시기를 내 백성을 보내라      ║
║     그들이 나를 섬길 것이니라" (출 7:16)                               ║
║    "하나님이 그 아들을 세상에 보내신 것은 세상을 심판하려 하심이       ║
║     아니요 그로 말미암아 세상이 구원을 받게 하려 하심이라" (요 3:17)     ║
║                                                                      ║
║    🗺️  출애굽기 7장: 나일강의 피 재앙과 파라오의 강퍅함              ║
║    📊 요한복음 3:16–21: 빛과 어둠, 행위에 따른 심판                   ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_first_plague_analysis():
    """첫 재앙 분석 섹션 실행"""
    print("\n🌊 === 출애굽기 여정: 첫 재앙, 나일강의 피 ===\n")
    print("나일강이 피로 변하는 첫 재앙을 통해 재앙의 강도와 파라오의 반응을 정렬하고 순위 매깁니다.")
    try:
        severity_results = analyze_plague_severity()
        response_ranking_results = analyze_pharaoh_response_ranking()
        return {"plague_severity": severity_results, "pharaoh_response_ranking": response_ranking_results}
    except Exception as e:
        print(f"❌ 첫 재앙 분석 중 오류 발생: {e}")
        return None

def run_spiritual_ranking_analysis():
    """영적 순위 분석 섹션 실행"""
    print("\n💡 === 요한복음 여정: 빛과 어둠의 영적 질서 ===\n")
    print("요한복음 3:16-21 말씀을 통해 빛과 어둠, 행위에 따른 영적 순위를 탐구합니다.")
    try:
        spiritual_ranking_results = analyze_spiritual_ranking()
        return {"spiritual_ranking": spiritual_ranking_results}
    except Exception as e:
        print(f"❌ 영적 순위 분석 중 오류 발생: {e}")
        return None

def run_personal_sorting_ranking_practice(name: str = None):
    """개인 정렬 및 순위 매기기 실습 섹션 실행"""
    if name is None:
        name = input("\n🔄 개인 정렬/순위 실습을 위해 이름을 입력해주세요 (기본값: 신앙인): ").strip()
        if not name:
            name = "신앙인"

    print(f"\n💡 === 개인 데이터 여정: {name}의 우선순위 정하기 탐험 ===\n")
    print("DataFrame의 `sort_values()`, `sort_index()`, `rank()`를 활용하여 데이터를 정렬하고 순위를 매깁니다.")
    try:
        sort_values_results = demo_sort_values()
        sort_index_results = demo_sort_index()
        rank_results = demo_rank()
        return {"sort_values": sort_values_results, "sort_index": sort_index_results, "rank": rank_results}
    except Exception as e:
        print(f"❌ 개인 정렬/순위 실습 중 오류 발생: {e}")
        return None

def show_blending_insights(plague_results, spiritual_ranking_results, personal_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 개인 여정 ===\n")

    blending_insights = [
        "🌊 재앙의 정렬: 하나님의 주권적 심판의 질서와 순위",
        "💡 빛과 어둠의 순위: 영적 행위에 따른 명확한 구분",
        "📊 `sort_values`와 `rank`: 세상의 혼돈 속에서 하나님의 우선순위를 찾는 지혜",
        "✨ 재정렬된 삶: 하나님의 뜻에 따라 나의 삶을 정돈하고 우선순위를 정하는 영적 훈련"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

    # 개인화된 통찰 추가 (예시)
    if personal_results and personal_results.get("sort_values_demo"):
        print("\n✨ 개인 정렬/순위 실습 통찰:")
        print("   삶의 우선순위를 재정렬하고, 하나님의 뜻에 합당한 순위를 매기는 것은 중요한 영적 분별력과 같습니다.")
        name = "신앙인"
        if "name" in personal_results and personal_results["name"] is not None:
            name = personal_results["name"]
        print(f"   오늘 당신은 {name}의 이름으로 삶의 우선순위를 정하는 지혜를 깨달았습니다!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 08 미리보기 ===

"재앙 속의 구분 — 고센과 마스킹"

출애굽기 8장에서 이스라엘 백성이 거하는 고센 땅만 재앙에서 면제되듯이,
데이터 분석에서도 특정 조건에 따라 데이터를 '구분'하고 '마스킹(mask)'하는 것은
중요한 정보를 보호하고, 필요한 데이터에만 집중하는 데 필수적인 기술입니다.

다음 장에서는:

-   **출애굽기 8장**: 고센 땅에 임하지 않는 재앙 → 데이터의 조건부 선택과 제외
-   **요한복음 4:1–15**: 사마리아 여인과 생수 → 영적 목마름의 발견과 채워짐 (조건부 선택)
-   **pandas 기술**: `df.mask()`, `df.where()`, `df.query()` 등

하나님은 재앙 속에서도 당신의 백성을 분명히 구분하시고 보호하십니다.
데이터를 효과적으로 구분하고 마스킹하는 법을 배워, 혼돈 속에서도 하나님의 구별된 은혜를 발견할 것입니다.
    """
    print(preview)

def run_chapter07(interactive: bool = True, user_name: str = None):
    """Chapter 07 전체 실행

    Args:
        interactive: 대화형 모드 여부
        user_name: 사용자 이름 (개인 분석용)

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 07을 시작합니다!\n")
        print("이 챕터에서는 첫 재앙의 시작처럼, 데이터의 정렬과 순위를 다룹니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '07',
        'title': '첫 재앙의 시작 — 정렬과 순위',
        'first_plague_analysis': None,
        'spiritual_ranking_analysis': None,
        'personal_sorting_ranking_practice': None
    }

    # 1. 첫 재앙 분석
    plague_results = run_first_plague_analysis()
    results['first_plague_analysis'] = plague_results

    if interactive:
        input("\n▶️ 요한복음 빛과 어둠의 영적 순위 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 요한복음 영적 순위 분석
    spiritual_ranking_results = run_spiritual_ranking_analysis()
    results['spiritual_ranking_analysis'] = spiritual_ranking_results

    if interactive:
        continue_personal = input("\n🤔 개인 정렬 및 순위 매기기 실습도 해보시겠어요? (y/n, 기본값 y): ").strip().lower()
        if continue_personal != 'n':
            # 3. 개인 정렬 및 순위 매기기 실습
            personal_results = run_personal_sorting_ranking_practice(user_name)
            results['personal_sorting_ranking_practice'] = personal_results
        else:
            personal_results = None
    else:
        personal_results = run_personal_sorting_ranking_practice(user_name)
        results['personal_sorting_ranking_practice'] = personal_results

    # 4. 블렌딩 통찰
    show_blending_insights(plague_results, spiritual_ranking_results, personal_results)

    # 5. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 6. 마무리 기도
    print("\n🙏 === 마무리 기도 ===\n")
    prayer = """
혼돈 속에서 질서를 세우시고, 모든 것을 정렬하시는 하나님, 감사합니다.
오늘 데이터의 정렬과 순위 매기기를 배우며, 세상의 재앙과 영적 심판 속에서도
하나님의 주권적인 질서와 우선순위를 발견하게 하시니 감사합니다.

세상의 가치관이 아닌, 주님의 말씀에 따라 나의 삶을 정돈하고,
영적인 우선순위를 바로 세워 빛 가운데 행하게 하소서.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print("\n🎉 Chapter 07 완료! 일곱 번째 광야 여정을 마치셨습니다!\n")
    print("📊 이제 데이터를 정렬하고 순위를 매길 수 있습니다!")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter07(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch07_results_{timestamp}.json"

            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'first_plague_analysis': results['first_plague_analysis'] is not None,
                'spiritual_ranking_analysis': results['spiritual_ranking_analysis'] is not None,
                'personal_sorting_ranking_practice': results['personal_sorting_ranking_practice'] is not None
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary_results, f, ensure_ascii=False, indent=2)

            print(f"✅ 결과가 {filename}에 저장되었습니다!")

        return results

    except KeyboardInterrupt:
        print("\n\n⏸️ 사용자가 중단했습니다.")
        return None
    except Exception as e:
        print(f"\n❌ 실행 중 오류가 발생했습니다: {e}")
        print("🔧 필요한 모듈이 있는지 확인해보세요.")
        return None


if __name__ == "__main__":
    print("🚀 JesusBornd Pandas Chapter 07 시작!\n")
    results = main()
