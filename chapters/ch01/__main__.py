"""
Chapter 01 통합 실행 스크립트
태초에 DataFrame — 데이터의 탄생

"태초에 말씀이 계시니라" (요 1:1) - 모든 분석의 시작점
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from chapters.ch01.exodus_analysis import TwelveTribesAnalyzer, demo_twelve_tribes
from chapters.ch01.john_analysis import JohnChapter1Analyzer, demo_john_chapter1
from chapters.ch01.spiritual_dna import PersonalSpiritualDNA, demo_personal_spiritual_dna


def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║        Chapter 01: 태초에 DataFrame — 데이터의 탄생                      ║
║                                                                      ║
║    "태초에 말씀이 계시니라 이 말씀이 하나님과 함께 계셨으니                   ║
║     이 말씀은 곧 하나님이시니라" (요한복음 1:1)                            ║
║                                                                      ║
║    🗺️  출애굽기 1장: 이스라엘이 애굽에서 번성하다                           ║
║    📊 요한복음 1:1-14: 태초에 말씀이 계시니라                             ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_exodus_analysis():
    """출애굽기 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 12지파의 신비 ===")
    print("야곱의 70명이 어떻게 큰 민족이 되었을까?")
    print("12지파 이름 속에 숨겨진 하나님의 설계를 발견해보자!\n")

    try:
        exodus_results = demo_twelve_tribes()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 분석 중 오류 발생: {e}")
        return None

def run_john_analysis():
    """요한복음 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: λόγος(로고스)의 비밀 ===")
    print("'태초에 말씀이 계시니라' - 이 한 문장에 담긴 우주적 진리!")
    print("빛과 어둠, 은혜와 진리의 완벽한 설계를 숫자로 확인해보자!\n")

    try:
        john_results = demo_john_chapter1()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 분석 중 오류 발생: {e}")
        return None

def run_personal_analysis(name: str = None):
    """개인 신앙 분석 섹션 실행"""
    if name is None:
        name = input("\n🧬 개인 신앙 DNA 분석을 위해 이름을 입력해주세요 (기본값: 신앙인): ").strip()
        if not name:
            name = "신앙인"

    print(f"\n🧬 === 개인 영적 여정: {name}의 신앙 DNA ===")
    print("레아의 4단계 신앙 패턴과 비교해보고,")
    print("나의 빛/어둠 비율, 은혜/진리 균형을 점검해보자!\n")

    try:
        personal_results = demo_personal_spiritual_dna(name)
        return personal_results
    except Exception as e:
        print(f"❌ 개인 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results, personal_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 개인 여정 ===")

    blending_insights = [
        "📊 DataFrame = 하나님의 질서를 담는 디지털 성막",
        "🏺 12지파 = 완전수 12의 신비, 하나님의 완벽한 설계",
        "📜 λόγος(말씀) = 모든 창조와 분석의 시작점",
        "💡 빛 2.5:1 어둠 = 복음의 절대 우세, 승리의 확신",
        "⚖️ 은혜와 진리의 완벽한 균형 = 예수님의 성품",
        "🌱 레아의 여정 = 모든 신자의 성장 패턴 (관계→소통→연합→예배)",
        "🧬 개인 신앙 DNA = 성경적 패턴으로 검증 가능한 영적 현실"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

    # 개인화된 통찰 추가
    if personal_results:
        overall_score = personal_results.get('overall_score', 0)
        if overall_score >= 8:
            print(f"\n✨ 특별한 축복: 당신의 신앙 성숙도({overall_score:.1f}/10)는 레아의 패턴을 잘 따르고 있습니다!")
        elif overall_score >= 6:
            print(f"\n🌱 성장의 기회: 현재 성숙도({overall_score:.1f}/10)에서 더 체계적인 성장이 가능합니다!")
        else:
            print(f"\n🙏 새로운 시작: 하나님과의 관계부터 차근차근 시작해보세요!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 02 미리보기 ===

"나일강에서 건진 데이터 — read_csv 입문"

출애굽기 2장에서 모세가 나일강의 갈대 상자에서 건져졌듯이,
우리도 CSV 파일이라는 "갈대 상자"에서 귀중한 데이터를 건져올 것입니다.

다음 장에서 배울 내용:
📁 CSV 파일 읽기와 인코딩 처리
🔍 결측치와 이상값 첫 만남  
🎯 모세의 정체성처럼 데이터의 진짜 의미 찾기
📊 성경 족보 데이터로 하나님의 구원 계획 추적

"모세가 장성한 후에 자기 형제들에게 나아가서 그들의 고역을 보고..." (출 2:11)
    """
    print(preview)

def run_chapter01(interactive: bool = True, user_name: str = None):
    """Chapter 01 전체 실행

    Args:
        interactive: 대화형 모드 여부
        user_name: 사용자 이름 (개인 분석용)

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 01을 시작합니다!")
        print("이 챕터에서는 DataFrame의 기초와 성경 속 하나님의 질서를 함께 탐구합니다.")

        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '01',
        'title': '태초에 DataFrame — 데이터의 탄생',
        'exodus_analysis': None,
        'john_analysis': None,
        'personal_analysis': None
    }

    # 1. 출애굽기 분석
    exodus_results = run_exodus_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 요한복음 분석
    john_results = run_john_analysis()
    results['john_analysis'] = john_results

    if interactive:
        continue_personal = input("\n🤔 개인 신앙 DNA 분석도 해보시겠어요? (y/n, 기본값 y): ").strip().lower()
        if continue_personal != 'n':
            # 3. 개인 신앙 분석
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
"태초에 말씀으로 세상을 창조하신 주님,
오늘 DataFrame을 통해 하나님의 질서와 아름다움을 발견하게 하시니 감사합니다.

레아의 신앙 여정처럼 저희도 관계에서 시작하여 소통하고, 연합하며, 
마침내 순전한 예배에 이르는 성숙한 신앙으로 자라가게 하소서.

요한복음의 빛이 어둠을 이기듯, 저희 삶에서도 빛 되신 예수님이 
모든 어둠을 몰아내시고 승리하게 하소서.

데이터 속에서도 주님의 지혜를 더 깊이 깨닫고,
앞으로의 pandas 여정이 더 깊은 영적 성숙으로 이어지게 하소서.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 01 완료! 첫 번째 광야 여정을 마치셨습니다!")
    print(f"📊 분석 결과가 저장되었습니다.")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter01(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch01_results_{timestamp}.json"

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
        print("🔧 utils/bible_utils.py의 테스트를 먼저 실행해보세요.")
        return None


if __name__ == "__main__":
    print("🚀 JesusBornd Pandas Chapter 01 시작!\n")
    results = main()
