"""
Chapter 02 통합 실행 스크립트
나일강에서 건진 데이터 — read_csv 입문

"아기를 더 숨길 수 없게 되매 그를 위하여 갈대 상자를 가져다가" (출 2:3)
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from chapters.ch02.moses_rescue import MosesRescueAnalyzer, demo_moses_rescue
from chapters.ch02.lamb_discovery import LambDiscoveryAnalyzer, demo_lamb_discovery
from chapters.ch02.csv_journey import PersonalCSVJourney, demo_personal_csv_journey

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║       Chapter 02: 나일강에서 건진 데이터 — read_csv 입문                   ║
║                                                                      ║
║    "바로의 딸이... 열고 그 아이를 보니 아이가 우는지라                        ║
║     그가 그를 불쌍히 여겨 이르되 이는 히브리 사람의 아이로다" (출 2:6)          ║
║                                                                      ║
║    🗺️  출애굽기 2장: 모세의 출생과 구원                                   ║
║    📊 요한복음 1:29: 보라 하나님의 어린양                                  ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_exodus_analysis():
    """출애굽기 분석 섹션 실행"""
    print("\n🧺 === 출애굽기 여정: 갈대상자의 비밀 ===")
    print("모세가 어떻게 나일강에서 구출되었을까?")
    print("갈대상자(CSV)에서 데이터를 건지는 법을 배워봅시다!\n")

    try:
        exodus_results = demo_moses_rescue()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 분석 중 오류 발생: {e}")
        return None

def run_john_analysis():
    """요한복음 분석 섹션 실행"""
    print("\n🐑 === 요한복음 여정: 어린양의 발견 ===")
    print("'보라 세상 죄를 지고 가는 하나님의 어린 양이로다' - 발견의 순간!")
    print("데이터를 발견하고 인식하는 영적 통찰을 얻어봅시다!\n")

    try:
        john_results = demo_lamb_discovery()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 분석 중 오류 발생: {e}")
        return None

def run_personal_analysis(name: str = None):
    """개인 CSV 여정 분석 섹션 실행"""
    if name is None:
        name = input("\n📝 개인 CSV 여정을 위해 이름을 입력해주세요 (기본값: 신앙인): ").strip()
        if not name:
            name = "신앙인"

    print(f"\n🚶 === 개인 CSV 여정: {name}의 갈대상자 만들기 ===")
    print("나만의 신앙 데이터를 CSV로 저장하고 읽어보며,")
    print("결측치를 찾고 처리하는 법을 실습해봅시다!\n")

    try:
        personal_results = demo_personal_csv_journey(name)
        return personal_results
    except Exception as e:
        print(f"❌ 개인 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results, personal_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 개인 여정 ===")

    blending_insights = [
        "📦 CSV = 갈대상자, 귀중한 데이터를 보호하고 전달",
        "🌊 read_csv() = 나일강에서 건지기, 숨겨진 데이터 구출",
        "👁️ '보라' = df.head(), 데이터의 첫 발견과 인식",
        "🔤 인코딩 = 언어 장벽, 바로의 딸처럼 이해하기",
        "🕳️ 결측치 = 숨겨진 모세, 없는 것이 아닌 아직 발견 안 된 것",
        "✨ fillna() = 은혜로 채우기, 불완전을 완전하게",
        "📊 데이터 클렌징 = 구속의 과정, 죄를 지고 가는 어린양처럼"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

    # 개인화된 통찰 추가
    if personal_results and 'spiritual_analysis' in personal_results:
        rescue_index = personal_results['spiritual_analysis'].get('rescue_index', 0)
        if rescue_index >= 80:
            print(f"\n⭐ 특별한 축복: 당신의 모세 구출 지수({rescue_index:.1f}/100)가 매우 높습니다!")
            print("   바로의 딸처럼 사명을 잘 감당하고 있습니다!")
        elif rescue_index >= 60:
            print(f"\n🌱 성장의 기회: 모세 구출 지수({rescue_index:.1f}/100)가 양호합니다!")
            print("   갈대상자를 더 튼튼히 만들어보세요!")
        else:
            print(f"\n🙏 새로운 시작: 모세 구출 지수({rescue_index:.1f}/100)를 높여봅시다!")
            print("   하나님이 함께하시면 모든 것이 가능합니다!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 03 미리보기 ===

"불타는 떨기나무와 인덱스의 부름"

출애굽기 3장에서 모세가 불타는 떨기나무 앞에서 하나님의 부르심을 받듯이,
우리도 DataFrame의 인덱스를 통해 데이터를 정확히 부르고 선택하는 법을 배울 것입니다.

다음 장에서 배울 내용:
🔥 불타도 사라지지 않는 인덱스의 신비
📍 이름으로 부르기 - loc와 iloc의 차이
🎯 멀티인덱스 - 성부, 성자, 성령의 삼위일체처럼
👟 신발을 벗으라 - 인덱스 리셋과 재설정

"모세야 모세야 하시매 그가 이르되 내가 여기 있나이다" (출 3:4)
    """
    print(preview)

def run_chapter02(interactive: bool = True, user_name: str = None):
    """Chapter 02 전체 실행

    Args:
        interactive: 대화형 모드 여부
        user_name: 사용자 이름 (개인 분석용)

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 02를 시작합니다!")
        print("이 챕터에서는 CSV 파일을 갈대상자처럼 다루는 법을 배웁니다.")
        print("모세가 나일강에서 구출되듯, 데이터도 CSV에서 구출할 수 있습니다!")

        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '02',
        'title': '나일강에서 건진 데이터 — read_csv 입문',
        'exodus_analysis': None,
        'john_analysis': None,
        'personal_analysis': None
    }

    # 1. 출애굽기 분석 (모세 구출)
    exodus_results = run_exodus_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 요한복음 분석 (어린양 발견)
    john_results = run_john_analysis()
    results['john_analysis'] = john_results

    if interactive:
        continue_personal = input("\n🤔 개인 CSV 여정도 체험해보시겠어요? (y/n, 기본값 y): ").strip().lower()
        if continue_personal != 'n':
            # 3. 개인 CSV 여정
            personal_results = run_personal_analysis(user_name)
            results['personal_analysis'] = personal_results
        else:
            personal_results = None
    else:
        personal_results = run_personal_analysis(user_name)
        results['personal_analysis'] = personal_results

    # 4. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results, personal_results)

    # 5. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 6. 마무리 기도
    print("\n🙏 === 마무리 기도 ===")
    prayer = """
"나일강에서 모세를 건지신 주님,
오늘 CSV 파일에서 귀중한 데이터를 건져낼 수 있게 하시니 감사합니다.

갈대상자가 모세를 보호했듯이, CSV가 데이터를 보호하고,
바로의 딸이 모세를 발견했듯이, read_csv()로 데이터를 발견할 수 있음에 감사드립니다.

결측치 속에서도 의미를 발견하고, 인코딩의 장벽을 넘어 
진리에 도달할 수 있도록 지혜를 더하소서.

세례 요한이 '보라'고 선포했듯이, 우리도 데이터 속에서 
하나님의 질서와 아름다움을 발견하고 선포하게 하소서.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 02 완료! 두 번째 광야 여정을 마치셨습니다!")
    print(f"📊 이제 CSV 파일을 자유롭게 다룰 수 있습니다!")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter02(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch02_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_exodus_analysis': results['exodus_analysis'] is not None,
                'has_john_analysis': results['john_analysis'] is not None,
                'has_personal_analysis': results['personal_analysis'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 02 시작!")
    print("📂 나일강에서 데이터를 건질 준비가 되셨나요?")
    results = main()