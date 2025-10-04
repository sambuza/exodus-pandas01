import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch22.tabernacle_multiindex_analysis import TabernacleMultiIndexAnalyzer
from chapters.ch22.temple_body_multiindex_access import TempleBodyMultiIndexAccessAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 22: 성막과 성전 — MultiIndex 고급                  ║
║                                                                      ║
║    "그들은 하늘에 있는 것의 모형과 그림자라 모세가 장막을 지으려 할 때에 ║
║     지시하심을 얻음과 같으니 이르시되 삼가 모든 것을 산에서 네게 보이던 ║
║     본을 따라 지으라 하셨느니라" (히브리서 8:5)                         ║
║    "예수께서 대답하여 이르시되 너희가 이 성전을 헐라 내가 사흘 동안에  ║
║     일으키리라 하시니라" (요한복음 2:19)                                ║
║                                                                      ║
║    🗺️  출애굽기 25-31장: 성막의 설계와 건축                            ║
║    📊 요한복음 2:13-22: 성전 정화와 예수님의 몸된 성전                 ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_tabernacle_analysis():
    """출애굽기 성막 구조 MultiIndex 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 성막의 복잡한 구조 MultiIndex 분석 ===")
    print("성막의 각 부분과 재료, 치수 등 다층적인 정보를 MultiIndex로 구조화하여 하나님의 세밀한 설계를 탐구해보자!")
    try:
        analyzer = TabernacleMultiIndexAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 성막 구조 분석 중 오류 발생: {e}")
        return None

def run_temple_body_analysis():
    """요한복음 예수님의 몸된 성전 MultiIndex 접근 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 예수님의 몸된 성전 MultiIndex 접근 분석 ===")
    print("예수님의 신성과 인성, 그리고 성도들의 영적 성장 단계를 MultiIndex로 접근하여 예수님의 말씀을 탐구해보자!")
    try:
        analyzer = TempleBodyMultiIndexAccessAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 예수님의 몸된 성전 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 MultiIndex = 성막과 성전의 복잡하고 계층적인 구조를 데이터로 표현",
        "🏺 성막 = 하나님의 임재와 구원의 계획을 보여주는 정교한 모형",
        "📜 예수님의 몸된 성전 = 하나님과 인간을 잇는 유일한 통로이자 새 언약의 실체",
        "💡 MultiIndex 접근 = 데이터의 깊은 층위까지 탐구하여 하나님의 지혜 발견"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 성막 구성 요소 수와 성전 속성 수를 기반으로 통찰 제공
        num_tabernacle_components = len(exodus_results.get('components_multiindex', pd.DataFrame())) if exodus_results else 0
        num_temple_attributes = len(john_results.get('attributes_multiindex', pd.DataFrame())) if john_results else 0

        if num_tabernacle_components > 5 and num_temple_attributes > 3:
            print(f"✨ 성막({num_tabernacle_components}개 구성)의 정교함처럼, 예수님의 몸된 성전({num_temple_attributes}개 속성)을 통해 당신의 삶은 하나님의 임재로 충만합니다!")
            print(f"✨ Like the intricacy of the Tabernacle ({num_tabernacle_components} components), through Jesus, the Temple ({num_temple_attributes} attributes), your life is filled with God's presence!")
        else:
            print(f"🙏 MultiIndex처럼 복잡한 하나님의 설계 속에서, 예수님을 통해 그 깊은 의미를 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to discover the deep meaning of God's complex design, like MultiIndex, through Jesus!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 23 미리보기 (Preview) ===

"제사장 위임식 — 데이터 검증과 클렌징 (Data Validation and Cleansing)"

아론과 그의 아들들이 제사장으로 위임될 때, 정결 예식과 복장 규례 등 엄격한 절차를 따랐듯이,
데이터 분석에서도 데이터의 정확성과 일관성을 보장하기 위한 '검증(Validation)'과 '클렌징(Cleansing)'은 필수적입니다.

다음 장에서는:
📁 데이터 유효성 검사 (예: 값 범위, 형식)
🔍 이상치(Outliers) 처리 및 데이터 정제
🎯 데이터 일관성 유지 (예: 중복 제거, 표준화)
📊 제사장 위임식처럼 깨끗하고 거룩한 데이터 준비

"너는 이스라엘 자손 중 네 형 아론과 그 아들들 곧 나답과 아비후와 엘르아살과 이다말을 그와 함께 네게로 나아오게 하여 나를 섬기는 제사장 직분을 행하게 하되" (출애굽기 28:1)
"내가 온 것은 양으로 생명을 얻게 하고 더 풍성히 얻게 하려는 것이라" (요한복음 10:10)
    """
    print(preview)

def run_chapter22(interactive: bool = True):
    """Chapter 22 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 22을 시작합니다!")
        print("이 챕터에서는 MultiIndex를 사용하여 성막과 성전의 복잡한 구조를 데이터로 탐구합니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '22',
        'title': '성막과 성전 — MultiIndex 고급',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 성막 분석
    exodus_results = run_tabernacle_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 예수님의 몸된 성전 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's temple body analysis...)")

    # 2. 요한복음 예수님의 몸된 성전 분석
    john_results = run_temple_body_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 성막과 성전의 정교한 설계 속에 담긴 주님의 임재와 구원의 계획을 찬양합니다.
MultiIndex처럼 복잡한 삶의 구조 속에서 주님의 세밀한 섭리를 발견하게 하시고,
예수님이라는 몸된 성전을 통해 주님과 깊이 교제하게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, I praise Your presence and plan of salvation embedded in the intricate design of the Tabernacle and Temple.
May I discover Your meticulous providence in the complex structure of life, like MultiIndex,
and may I deeply commune with You through Jesus, the Temple. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 22 완료! 스물두 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 22 Complete! You have finished the twenty-second wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter22(interactive=False)

        # 결과 저장 (선택사항)
        if results:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch22_results_{timestamp}.json"

            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_exodus_analysis': results['exodus_analysis'] is not None,
                'has_john_analysis': results['john_analysis'] is not None
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary_results, f, ensure_ascii=False, indent=2)

            print(f"✅ 결과가 {filename}에 저장되었습니다! (Results saved to {filename}!) ")

        return results

    except KeyboardInterrupt:
        print("\n\n⏸️ 사용자가 중단했습니다. (User interrupted.)")
        return None
    except Exception as e:
        print(f"\n❌ 실행 중 오류가 발생했습니다: {e}")
        print("🔧 코드와 데이터를 확인해주세요. (Please check the code and data.)")
        return None


if __name__ == "__main__":
    print("🚀 JesusBornd Pandas Chapter 22 시작! (Starting JesusBornd Pandas Chapter 22!)\n")
    main()
