"""
Chapter 05 통합 실행 스크립트
파라오 앞에 서다 — dtypes와 astype

"모세와 아론이 바로에게 가서 이르되 이스라엘의 하나님 여호와께서 말씀하시기를 내 백성을 보내라."
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# ch05의 분석 모듈들 (예상)
# TODO: Replace these with actual imports when the files are created.
from chapters.ch05.pharaohs_stand import analyze_pharaoh_response, analyze_israelites_burden
from chapters.ch05.cana_dtypes_analysis import analyze_cana_miracle_datatypes
from chapters.ch05.data_type_conversion import demo_dtype_inspection, demo_astype_conversion, demo_to_numeric_conversion

def analyze_pharaoh_response():
    print("출애굽기 5장 파라오의 반응 분석 (placeholder)")
    return {"pharaoh_response": "data"}

def analyze_israelites_burden():
    print("출애굽기 5장 이스라엘 백성의 고통 분석 (placeholder)")
    return {"israelites_burden": "data"}

def analyze_cana_miracle_datatypes():
    print("요한복음 2:1-11 가나 혼인잔치 데이터타입 분석 (placeholder)")
    return {"cana_datatypes": "data"}

def demo_dtype_inspection():
    print("데이터 타입 점검 데모 (placeholder)")
    return {"dtype_inspection": "data"}

def demo_astype_conversion():
    print("astype 변환 데모 (placeholder)")
    return {"astype_conversion": "data"}

def demo_to_numeric_conversion():
    print("to_numeric 변환 데모 (placeholder)")
    return {"to_numeric_conversion": "data"}

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║         Chapter 05: 파라오 앞에 서다 — dtypes와 astype                 ║
║                                                                      ║
║    "모세와 아론이 바로에게 가서 이르되 이스라엘의 하나님 여호와께서   ║
║     말씀하시기를 내 백성을 보내라 그들이 나를 섬길 것이니라" (출 5:1)      ║
║    "예수께서 그들에게 이르시되 항아리에 물을 채우라 하시매            ║
║     아귀까지 채우니" (요한복음 2:7)                                    ║
║                                                                      ║
║    🗺️  출애굽기 5장: 파라오의 거절과 이스라엘의 고난                 ║
║    📊 요한복음 2:1–11: 가나 혼인잔치 (데이터 타입의 변화)             ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_pharaoh_encounter_analysis():
    """파라오와 모세의 만남 섹션 실행"""
    print("\n🏛️ === 출애굽기 여정: 파라오 앞에 서다 ===\n")
    print("모세가 파라오에게 나아가 하나님의 명령을 전하는 과정을 데이터로 분석합니다.")
    try:
        pharaoh_results = analyze_pharaoh_response()
        burden_results = analyze_israelites_burden()
        return {"pharaoh_response": pharaoh_results, "israelites_burden": burden_results}
    except Exception as e:
        print(f"❌ 파라오와의 만남 분석 중 오류 발생: {e}")
        return None

def run_cana_dtypes_analysis():
    """요한복음 가나 혼인잔치 데이터타입 분석 섹션 실행"""
    print("\n🍷 === 요한복음 여정: 가나의 물과 데이터 타입 ===\n")
    print("가나 혼인잔치에서 물이 포도주로 변하듯, 데이터 타입의 변화를 탐구합니다.")
    try:
        cana_dtypes_results = analyze_cana_miracle_datatypes()
        return {"cana_datatypes_analysis": cana_dtypes_results}
    except Exception as e:
        print(f"❌ 가나 혼인잔치 데이터타입 분석 중 오류 발생: {e}")
        return None

def run_personal_dtype_conversion_practice(name: str = None):
    """개인 데이터 타입 점검 및 변환 실습 섹션 실행"""
    if name is None:
        name = input("\n🔄 개인 데이터 타입 실습을 위해 이름을 입력해주세요 (기본값: 신앙인): ").strip()
        if not name:
            name = "신앙인"

    print(f"\n💡 === 개인 데이터 여정: {name}의 데이터 타입 탐험 ===\n")
    print("DataFrame의 `dtypes`, `astype()`, `pd.to_numeric()`를 활용하여 데이터 타입을 점검하고 변환합니다.")
    try:
        dtype_inspection_results = demo_dtype_inspection()
        astype_results = demo_astype_conversion()
        to_numeric_results = demo_to_numeric_conversion()
        return {"dtype_inspection": dtype_inspection_results, "astype_conversion": astype_results, "to_numeric_conversion": to_numeric_results}
    except Exception as e:
        print(f"❌ 개인 데이터 타입 실습 중 오류 발생: {e}")
        return None

def show_blending_insights(pharaoh_results, cana_results, personal_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 개인 여정 ===\n")

    blending_insights = [
        "🏛️ 파라오의 강퍅함: 데이터의 잘못된 타입처럼, 분석을 방해하는 요소들",
        "🍷 물이 포도주로: `astype`처럼 데이터의 본질을 변화시키는 기적",
        "🔄 `dtypes`와 `astype`: 데이터의 정체성을 파악하고 변화시키는 영적 지혜",
        "💡 참된 이해: 데이터 타입을 정확히 알면 올바른 분석이 가능하듯, 영적 본질을 알면 바른 신앙생활이 가능",
        "✨ 변환의 능력: 물이 포도주로 변하듯, 우리의 삶도 그리스도 안에서 새로운 본질로 변화"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

    # 개인화된 통찰 추가 (예시)
    if personal_results and personal_results.get("dtype_inspection"):
        print("\n✨ 개인 데이터 타입 실습 통찰:")
        print("   데이터의 숨겨진 본질을 파악하고 올바르게 변환하는 것은 중요한 영적 분별력과 같습니다.")
        name = "신앙인"
        if "name" in personal_results and personal_results["name"] is not None:
            name = personal_results["name"]
        print(f"   오늘 당신은 {name}의 이름으로 데이터 타입 변환의 중요성을 깨달았습니다!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 06 미리보기 ===

"하나님의 약속과 NaN — 결측치 다루기"

출애굽기 6장에서 이스라엘 백성이 모세의 말을 듣지 못하고(결측), 하나님은 다시 약속(채워주심)을 상기시키셨듯이,
데이터에서도 '결측치(NaN)'는 분석의 흐름을 방해합니다. 그러나 결측치는 단순히 없는 것이 아니라, 우리가 찾아내고 채워야 할 하나님의 약속과 같은 부분입니다.

다음 장에서는:

-   **출애굽기 6장**: 하나님의 다시 하신 약속 → 결측치 속에 담긴 의미
-   **요한복음 3:1–8**: 니고데모와 예수님의 대화 → 영적 결측치(거듭남의 필요) 채우기
-   **pandas 기술**: `df.isna()`, `df.notna()`로 결측치 확인, `df.fillna()`로 채우기, `df.dropna()`로 제거, `df.interpolate()`로 보간법 활용

하나님은 결코 우리를 버리지 않으시고, 우리의 부족함(결측치)을 채워주십니다.
데이터 결측치를 지혜롭게 다루는 법을 배워, 하나님의 온전한 그림을 볼 것입니다.
    """
    print(preview)

def run_chapter05(interactive: bool = True, user_name: str = None):
    """Chapter 05 전체 실행

    Args:
        interactive: 대화형 모드 여부
        user_name: 사용자 이름 (개인 분석용)

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 05를 시작합니다!\n")
        print("이 챕터에서는 파라오 앞에 선 모세처럼, 데이터의 타입과 본질을 탐구합니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '05',
        'title': '파라오 앞에 서다 — dtypes와 astype',
        'pharaoh_encounter_analysis': None,
        'cana_dtypes_analysis': None,
        'personal_dtype_conversion_practice': None
    }

    # 1. 파라오와 모세의 만남 분석
    pharaoh_results = run_pharaoh_encounter_analysis()
    results['pharaoh_encounter_analysis'] = pharaoh_results

    if interactive:
        input("\n▶️ 요한복음 가나 혼인잔치 데이터타입 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 요한복음 가나 혼인잔치 데이터타입 분석
    cana_results = run_cana_dtypes_analysis()
    results['cana_dtypes_analysis'] = cana_results

    if interactive:
        continue_personal = input("\n🤔 개인 데이터 타입 점검 및 변환 실습도 해보시겠어요? (y/n, 기본값 y): ").strip().lower()
        if continue_personal != 'n':
            # 3. 개인 데이터 타입 점검 및 변환 실습
            personal_results = run_personal_dtype_conversion_practice(user_name)
            results['personal_dtype_conversion_practice'] = personal_results
        else:
            personal_results = None
    else:
        personal_results = run_personal_dtype_conversion_practice(user_name)
        results['personal_dtype_conversion_practice'] = personal_results

    # 4. 블렌딩 통찰
    show_blending_insights(pharaoh_results, cana_results, personal_results)

    # 5. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 6. 마무리 기도
    print("\n🙏 === 마무리 기도 ===\n")
    prayer = """
데이터의 타입을 정확히 이해하고 변환하는 지혜를 주신 주님,
오늘 파라오 앞에서 담대히 선 모세처럼, 그리고 물을 포도주로 바꾸신 예수님처럼
저희가 데이터 속에서 본질을 파악하고 변화를 일으키는 능력을 배우게 하시니 감사합니다.

세상의 강퍅함(잘못된 데이터 타입) 속에서도 주님의 진리(올바른 데이터 타입)를 분별하고,
그것을 통해 하나님의 영광을 드러내는 삶을 살게 하소서.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print("\n🎉 Chapter 05 완료! 다섯 번째 광야 여정을 마치셨습니다!\n")
    print("📊 이제 데이터 타입을 자유자재로 다룰 수 있습니다!")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter05(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch05_results_{timestamp}.json"

            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'pharaoh_encounter_analysis': results['pharaoh_encounter_analysis'] is not None,
                'cana_dtypes_analysis': results['cana_dtypes_analysis'] is not None,
                'personal_dtype_conversion_practice': results['personal_dtype_conversion_practice'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 05 시작!\n")
    results = main()
