"""
Chapter 04 통합 실행 스크립트
소명과 항변 — 선택과 필터링

"하나님은 모세를 부르시고, 모세는 항변하며, 주님은 다시 약속하신다."
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# ch04의 분석 모듈들 (예상)
# 실제 함수는 ch04/moses_calling.py, ch04/disciples_calling.py, ch04/data_filtering.py 등에 정의될 것임
# 현재는 더미 함수로 대체하거나, 필요시 생성하여 임포트

# TODO: Replace these with actual imports when the files are created.
from chapters.ch04.moses_calling import analyze_moses_call, analyze_moses_objections
from chapters.ch04.disciples_calling import analyze_john_disciples_calling
from chapters.ch04.data_filtering import demo_column_selection, demo_row_slicing, demo_boolean_filtering, create_biblical_characters_df

def analyze_moses_call():
    print("출애굽기 4장 모세의 소명 분석 (placeholder)")
    return {"moses_call": "data"}

def analyze_moses_objections():
    print("출애굽기 4장 모세의 항변 분석 (placeholder)")
    return {"moses_objections": "data"}

def analyze_john_disciples_calling():
    print("요한복음 1:40-51 제자들의 부름 분석 (placeholder)")
    return {"disciples_calling": "data"}

def demo_column_selection():
    print("열 선택 데모 (placeholder)")
    return {"column_selection": "data"}

def demo_row_slicing():
    print("행 슬라이싱 데모 (placeholder)")
    return {"row_slicing": "data"}

def demo_boolean_filtering():
    print("불리언 필터링 데모 (placeholder)")
    return {"boolean_filtering": "data"}

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║         Chapter 04: 소명과 항변 — 선택과 필터링                          ║
║                                                                      ║
║    "내가 너를 바로에게 보내어 너에게서 내 백성 이스라엘 자손을         ║
║     애굽에서 인도하여 내게 하리라" (출애굽기 3:10)                       ║
║    "또 이르시되 와 보라 그러므로 그들이 가서 계신 데를 보고           ║
║     그 날 함께 거하니 때가 제십 시쯤 되었더라" (요한복음 1:39)            ║
║                                                                      ║
║    🗺️  출애굽기 4장: 모세의 소명과 다섯 가지 항변                      ║
║    📊 요한복음 1:40–51: 제자들의 부름과 나다나엘의 고백                  ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_moses_calling_analysis():
    """모세의 소명과 항변 섹션 실행"""
    print("\n🔥 === 출애굽기 여정: 모세의 소명과 항변 ===\n")
    print("하나님의 부르심과 인간의 항변 사이의 갈등을 데이터로 분석합니다.")
    try:
        call_results = analyze_moses_call()
        objection_results = analyze_moses_objections()
        return {"call": call_results, "objections": objection_results}
    except Exception as e:
        print(f"❌ 모세의 소명 분석 중 오류 발생: {e}")
        return None

def run_john_disciples_analysis():
    """요한복음 제자들의 부름 섹션 실행"""
    print("\n👥 === 요한복음 여정: 제자들의 부름과 고백 ===\n")
    print("예수님의 부르심에 제자들이 어떻게 반응했는지 데이터를 통해 탐구합니다.")
    try:
        disciples_results = analyze_john_disciples_calling()
        return {"disciples_calling": disciples_results}
    except Exception as e:
        print(f"❌ 요한복음 제자들의 부름 분석 중 오류 발생: {e}")
        return None

def run_personal_filtering_practice(name: str = None):
    """개인 데이터 선택 및 필터링 실습 섹션 실행"""
    if name is None:
        name = input("\n✂️ 개인 데이터 필터링 실습을 위해 이름을 입력해주세요 (기본값: 신앙인): ").strip()
        if not name:
            name = "신앙인"

    print(f"\n💡 === 개인 데이터 여정: {name}의 선택과 필터링 ===\n")
    print("DataFrame의 핵심 기술인 열 선택, 행 슬라이싱, 불리언 필터링을 실습합니다.")
    try:
        col_selection_results, _ = demo_column_selection()
        row_slicing_results, _ = demo_row_slicing()
        bool_filtering_results, _, _ = demo_boolean_filtering()
        return {"column_selection": col_selection_results, "row_slicing": row_slicing_results, "boolean_filtering": bool_filtering_results}
    except Exception as e:
        print(f"❌ 개인 필터링 실습 중 오류 발생: {e}")
        return None

def show_blending_insights(moses_results, john_results, personal_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 개인 여정 ===\n")

    blending_insights = [
        "🔥 소명과 항변: 데이터 분석에서도 문제 해결을 위한 선택과 거절의 순간이 있다.",
        "👥 제자들의 부름: 특정 조건(믿음, 순종)을 가진 데이터만 선택하는 것과 같다.",
        "✂️ 열 선택: 하나님이 각 사람에게 주신 고유한 은사를 선택적으로 사용하는 것",
        "📊 행 슬라이싱: 역사 속 특정 시점의 데이터(사건)를 집중적으로 탐구하는 것",
        "🎯 불리언 필터: 오직 하나님의 기준(True)에 맞는 데이터(사람, 사건)만 걸러내는 것",
        "💡 나다나엘의 고백: 데이터 속에서 예수님이 메시아임을 발견하는 영적 통찰"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

    # 개인화된 통찰 추가 (예시)
    if personal_results and personal_results.get("boolean_filtering"):
        print("\n✨ 개인 필터링 실습 통찰:")
        print("   데이터를 선택하고 필터링하는 능력은 하나님의 뜻을 분별하는 영적 능력과 같습니다.")
        name = "신앙인" # Default name if not provided
        if "name" in personal_results and personal_results["name"] is not None: # Check if name was actually passed
            name = personal_results["name"]
        print(f"   오늘 당신은 {name}의 이름으로 중요한 데이터 필터링 기술을 익혔습니다!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 05 미리보기 ===

"만나와 메추라기 — 데이터 병합과 정렬"

광야에서 이스라엘 백성에게 만나와 메추라기가 내렸듯이,
흩어져 있는 데이터를 하나로 병합하고 질서정연하게 정렬하는 방법을 배울 것입니다.

다음 장에서 배울 내용:
🔗 pd.concat(), pd.merge()를 이용한 데이터 병합
⬆️ .sort_values()로 데이터 정렬하기
🔄 인덱스 재설정과 중복 데이터 처리
🍞 만나와 메추라기 데이터로 영적 양식 분석

"내가 너희를 위하여 하늘에서 양식을 비같이 내리리니 백성이 나가서 일용할 것을 날마다 거둘 것이라" (출애굽기 16:4)
    """
    print(preview)

def run_chapter04(interactive: bool = True, user_name: str = None):
    """Chapter 04 전체 실행

    Args:
        interactive: 대화형 모드 여부
        user_name: 사용자 이름 (개인 분석용)

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 04를 시작합니다!\n")
        print("이 챕터에서는 소명과 항변, 그리고 데이터의 선택과 필터링을 함께 탐구합니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '04',
        'title': '소명과 항변 — 선택과 필터링',
        'moses_calling_analysis': None,
        'john_disciples_analysis': None,
        'personal_filtering_practice': None
    }

    # 1. 모세의 소명과 항변 분석
    moses_results = run_moses_calling_analysis()
    results['moses_calling_analysis'] = moses_results

    if interactive:
        input("\n▶️ 요한복음 제자들의 부름 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 요한복음 제자들의 부름 분석
    john_results = run_john_disciples_analysis()
    results['john_disciples_analysis'] = john_results

    if interactive:
        continue_personal = input("\n🤔 개인 데이터 선택 및 필터링 실습도 해보시겠어요? (y/n, 기본값 y): ").strip().lower()
        if continue_personal != 'n':
            # 3. 개인 데이터 선택 및 필터링 실습
            personal_results = run_personal_filtering_practice(user_name)
            results['personal_filtering_practice'] = personal_results
        else:
            personal_results = None
    else:
        personal_results = run_personal_filtering_practice(user_name)
        results['personal_filtering_practice'] = personal_results

    # 4. 블렌딩 통찰
    show_blending_insights(moses_results, john_results, personal_results)

    # 5. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 6. 마무리 기도
    print("\n🙏 === 마무리 기도 ===\n")
    prayer = """
주님, 저희를 부르시고 인도하시는 것에 감사드립니다.
오늘 DataFrame의 선택과 필터링을 통해 주님의 세밀한 섭리와 계획을 묵상하게 하시니 감사합니다.

모세의 항변에도 불구하고 포기하지 않으시고,
나다나엘의 의심에도 불구하고 확신을 주셨듯이,
저희가 데이터 속에서 주님의 음성을 듣고 바르게 선택하며,
주님의 뜻을 이루는 도구가 되게 하소서.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print("\n🎉 Chapter 04 완료! 네 번째 광야 여정을 마치셨습니다!\n")
    print("📊 이제 데이터를 더욱 정교하게 다룰 수 있습니다!")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter04(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch04_results_{timestamp}.json"

            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'moses_calling_analysis': results['moses_calling_analysis'] is not None,
                'john_disciples_analysis': results['john_disciples_analysis'] is not None,
                'personal_filtering_practice': results['personal_filtering_practice'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 04 시작!\n")
    results = main()
