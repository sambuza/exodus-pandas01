"""
Chapter 03 통합 실행 스크립트
신(神)의 능력과 표적 — Series와 DataFrame의 변환

"모세가 장성한 후에 자기 형제들에게 나아가서 그들의 고역을 보고..." (출 2:11)
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from chapters.ch03.burning_bush import analyze_burning_bush, analyze_divine_revelation, compare_theophanies
from chapters.ch03.three_signs import create_signs_matrix, analyze_sign_progression, compare_exodus_john_signs, simulate_transformation, analyze_theological_meaning
from chapters.ch03.cana_miracle import analyze_water_jars, analyze_transformation_process, compare_water_blood_transformation, analyze_wedding_context, analyze_disciples_faith
from chapters.ch03.signs_series import create_dialogue_series, practice_transformations # Using specific functions from signs_series

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║         Chapter 03: 신(神)의 능력과 표적 — DataFrame Index             ║
║                                                                      ║
║    "하나님이 불타는 떨기나무 가운데서 그에게 나타나시니라" (출 3:2)         ║
║    "이 표적은 예수께서 갈릴리 가나에서 행하여 그의 영광을 나타내시매     ║
║     제자들이 그를 믿으니라" (요한복음 2:11)                             ║
║                                                                      ║
║    🗺️  출애굽기 3-4장: 모세의 소명과 세 표적                         ║
║    📊 요한복음 2:1-11: 가나 혼인잔치 첫 표적                           ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_burning_bush_analysis():
    """불타는 떨기나무 섹션 실행"""
    print("\n🔥 === 출애굽기 여정: 불타는 떨기나무 ===\n")
    print("모세가 호렙산에서 하나님을 만난 경외의 순간을 데이터로 분석합니다.")
    try:
        bb_names, bb_response, bb_ground = analyze_burning_bush()
        bb_revelation = analyze_divine_revelation()
        bb_theophanies = compare_theophanies()
        return {"names": bb_names, "response": bb_response, "ground": bb_ground, "revelation": bb_revelation, "theophanies": bb_theophanies}
    except Exception as e:
        print(f"❌ 불타는 떨기나무 분석 중 오류 발생: {e}")
        return None

def run_three_signs_analysis():
    """세 가지 표적 섹션 실행"""
    print("\n🔮 === 출애굽기 여정: 세 가지 표적 ===\n")
    print("하나님의 권능을 증명하는 세 가지 표적의 의미와 강도를 탐구합니다.")
    try:
        signs_matrix = create_signs_matrix()
        sign_progression = analyze_sign_progression()
        comparison_signs, john_signs = compare_exodus_john_signs()
        return {"matrix": signs_matrix, "progression": sign_progression, "comparison": comparison_signs, "john_signs": john_signs}
    except Exception as e:
        print(f"❌ 세 가지 표적 분석 중 오류 발생: {e}")
        return None

def run_cana_miracle_analysis():
    """가나 혼인잔치 섹션 실행"""
    print("\n🍷 === 요한복음 여정: 가나의 첫 표적 ===\n")
    print("물이 포도주로 변한 기적을 통해 새 언약의 시작을 데이터로 살펴봅니다.")
    try:
        jars, symbolism = analyze_water_jars()
        process, quality = analyze_transformation_process()
        comparison_water_blood = compare_water_blood_transformation()
        context, consumption = analyze_wedding_context()
        faith = analyze_disciples_faith()
        return {"jars": jars, "symbolism": symbolism, "process": process, "quality": quality, "comparison_water_blood": comparison_water_blood, "context": context, "consumption": consumption, "faith": faith}
    except Exception as e:
        print(f"❌ 가나 혼인잔치 분석 중 오류 발생: {e}")
        return None

def run_personal_transformation_practice(name: str = None):
    """개인 Series/DataFrame 변환 실습 섹션 실행 (signs_series.py 활용)"""
    if name is None:
        name = input("\n🔄 개인 데이터 변환 실습을 위해 이름을 입력해주세요 (기본값: 신앙인): ").strip()
        if not name:
            name = "신앙인"
            
    print(f"\n💡 === 개인 데이터 여정: {name}의 변환 실습 ===\n")
    print("Series와 DataFrame을 자유롭게 변환하며 데이터 핸들링 능력을 키워봅시다!")
    try:
        # Using a function from signs_series.py that involves transformations
        dialogue_df = create_dialogue_series()
        df_transformed = practice_transformations()
        return {"dialogue_df": dialogue_df, "transformed_df": df_transformed}
    except Exception as e:
        print(f"❌ 개인 변환 실습 중 오류 발생: {e}")
        return None

def show_blending_insights(bb_results, signs_results, cana_results, personal_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 개인 여정 ===\n")

    blending_insights = [
        "🔥 불타는 떨기나무: 하나님의 변치 않는 임재와 거룩",
        "🔮 세 가지 표적: 하나님의 권능과 심판, 그리고 구원",
        "🍷 가나의 혼인잔치: 율법에서 은혜로, 구시대에서 새 시대로의 변환",
        "🔄 Series/DataFrame 변환: 데이터 속에서 하나님의 패턴을 발견하는 지혜",
        "💡 거룩한 땅: 경외함으로 데이터를 다루는 태도",
        "✨ 첫 표적의 영광: 데이터 분석을 통해 드러나는 하나님의 영광"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

    # 개인화된 통찰 추가 (예시)
    if personal_results and "transformed_df" in personal_results:
        print("\n✨ 개인 변환 실습 통찰:")
        print("   데이터 변환을 통해 숨겨진 의미를 찾아내는 여정은 끝없이 이어집니다.")
        print(f"   오늘 당신은 {len(personal_results['transformed_df'])}개의 중요한 개념을 DataFrame으로 만들었습니다.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 04 미리보기 ===

"재앙의 알고리즘 — 조건부 선택과 필터링"

출애굽기 7-12장의 10가지 재앙이 단순히 무작위적인 사건이 아니듯이,
DataFrame의 조건부 선택과 필터링은 단순한 데이터 추출이 아닌
"재앙의 알고리즘" 속에 숨겨진 하나님의 섭리를 찾아내는 여정입니다.

다음 장에서 배울 내용:
🚨 10가지 재앙 데이터로 조건부 선택 마스터
✂️ df.loc, df.iloc, df[]를 이용한 데이터 필터링
📊 특정 조건을 만족하는 데이터만 골라내기
📈 논리 연산자를 활용한 복합 조건 필터링

"여호와께서 모세에게 이르시되 바로에게 가서 그에게 이르기를 히브리 사람의 하나님 여호와께서 말씀하시기를 내 백성을 보내라 그들이 나를 섬길 것이니라" (출 9:1)
    """
    print(preview)

def run_chapter03(interactive: bool = True, user_name: str = None):
    """Chapter 03 전체 실행

    Args:
        interactive: 대화형 모드 여부
        user_name: 사용자 이름 (개인 분석용)

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 03을 시작합니다!\n")
        print("이 챕터에서는 하나님의 현현과 표적을 DataFrame의 인덱스와 변환으로 탐구합니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '03',
        'title': '신의 능력과 표적 — DataFrame Index',
        'burning_bush_analysis': None,
        'three_signs_analysis': None,
        'cana_miracle_analysis': None,
        'personal_transformation_practice': None
    }

    # 1. 불타는 떨기나무 분석
    bb_results = run_burning_bush_analysis()
    results['burning_bush_analysis'] = bb_results

    if interactive:
        input("\n▶️ 세 가지 표적 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 세 가지 표적 분석
    signs_results = run_three_signs_analysis()
    results['three_signs_analysis'] = signs_results

    if interactive:
        input("\n▶️ 가나 혼인잔치 분석을 시작하려면 Enter를 눌러주세요...")

    # 3. 가나 혼인잔치 분석
    cana_results = run_cana_miracle_analysis()
    results['cana_miracle_analysis'] = cana_results

    if interactive:
        continue_personal = input("\n🤔 개인 데이터 변환 실습도 해보시겠어요? (y/n, 기본값 y): ").strip().lower()
        if continue_personal != 'n':
            # 4. 개인 데이터 변환 실습
            personal_results = run_personal_transformation_practice(user_name)
            results['personal_transformation_practice'] = personal_results
        else:
            personal_results = None
    else:
        personal_results = run_personal_transformation_practice(user_name)
        results['personal_transformation_practice'] = personal_results

    # 5. 블렌딩 통찰
    show_blending_insights(bb_results, signs_results, cana_results, personal_results)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 ===\n")
    prayer = """
"나는 스스로 있는 자"라고 계시하신 주님,
오늘 DataFrame의 인덱스를 통해 주님의 신실한 이름과 능력을 묵상하게 하시니 감사합니다.

불타는 떨기나무 앞에서 신을 벗었던 모세처럼,
가나 혼인잔치에서 물을 포도주로 바꾸신 예수님처럼,
데이터 속에서도 주님의 임재와 변혁의 능력을 발견하게 하소서.

저희가 데이터를 다루는 모든 과정에서 경외함을 잃지 않게 하시고,
하나님의 질서와 섭리를 깊이 이해하며 주님의 영광을 드러내게 하소서.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print("\n🎉 Chapter 03 완료! 세 번째 광야 여정을 마치셨습니다!\n")
    print("📊 분석 결과가 저장되었습니다.")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter03(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch03_results_{timestamp}.json"

            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_burning_bush_analysis': results['burning_bush_analysis'] is not None,
                'has_three_signs_analysis': results['three_signs_analysis'] is not None,
                'has_cana_miracle_analysis': results['cana_miracle_analysis'] is not None,
                'has_personal_transformation_practice': results['personal_transformation_practice'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 03 시작!\n")
    results = main()
