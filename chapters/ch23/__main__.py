import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch23.priestly_validation_cleansing import PriestlyValidationCleansingAnalyzer
from chapters.ch23.high_priest_data_integrity import HighPriestDataIntegrityAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║           Chapter 23: 제사장 위임식 — 데이터 검증과 클렌징             ║
║                                                                      ║
║    "너는 이스라엘 자손 중 네 형 아론과 그 아들들 곧 나답과 아비후와   ║
║     엘르아살과 이다말을 그와 함께 네게로 나아오게 하여 나를 섬기는     ║
║     제사장 직분을 행하게 하되" (출애굽기 28:1)                         ║
║    "내가 온 것은 양으로 생명을 얻게 하고 더 풍성히 얻게 하려는 것이라" 
║     (요한복음 10:10)                                                   ║
║                                                                      ║
║    🗺️  출애굽기 28-29장: 제사장 위임식과 의복 규례                     ║
║    📊 요한복음 10:7-18: 선한 목자와 풍성한 생명                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_priestly_consecration_analysis():
    """출애굽기 제사장 위임식 데이터 검증 및 클렌징 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 제사장 위임식 데이터 검증 및 클렌징 ===")
    print("제사장 위임식의 엄격한 절차처럼, 데이터의 정확성과 일관성을 보장하기 위한 검증과 클렌징을 탐구해보자!")
    try:
        analyzer = PriestlyValidationCleansingAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 제사장 위임식 분석 중 오류 발생: {e}")
        return None

def run_high_priest_analysis():
    """요한복음 대제사장 예수님 데이터 무결성 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 대제사장 예수님 데이터 무결성 분석 ===")
    print("예수님의 완전한 대제사장 직분처럼, 데이터의 무결성과 일관성을 유지하는 방법을 탐구해보자!")
    try:
        analyzer = HighPriestDataIntegrityAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 대제사장 예수님 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 데이터 검증과 클렌징 = 제사장 위임식처럼 깨끗하고 거룩한 데이터 준비",
        "🏺 제사장 위임식 = 데이터의 정확성과 일관성을 보장하는 엄격한 절차",
        "📜 대제사장 예수님 = 데이터의 완전한 무결성과 일관성을 보여주는 궁극적인 표준",
        "💡 데이터 품질 = 풍성한 생명을 얻게 하는 선한 목자의 인도"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 제사장 위임식 절차의 유효성 및 예수님 속성의 무결성을 기반으로 통찰 제공
        priestly_validation_ok = exodus_results.get('validation_results', (False, False))[0] and exodus_results.get('validation_results', (False, False))[1]
        jesus_integrity_ok = john_results.get('attributes_integrity', (False, False))[0] and john_results.get('attributes_integrity', (False, False))[1]

        if priestly_validation_ok and jesus_integrity_ok:
            print(f"✨ 제사장 위임식처럼 깨끗하고({priestly_validation_ok}), 대제사장 예수님처럼 완전한({jesus_integrity_ok}) 당신의 삶은 하나님께 영광이 됩니다!")
            print(f"✨ Like the pure priestly consecration ({priestly_validation_ok}), and the perfect High Priest Jesus ({jesus_integrity_ok}), your life brings glory to God!")
        else:
            print(f"🙏 데이터 검증과 클렌징처럼, 나의 삶이 주님의 말씀에 따라 정결하고 온전한지 끊임없이 점검하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to constantly examine if my life is pure and complete according to God's Word, just like data validation and cleansing!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 24 미리보기 (Preview) ===

"성막 봉헌 — 데이터 시각화와 대시보드 (Data Visualization and Dashboards)"

성막이 완성되고 봉헌되었을 때, 하나님의 영광이 성막에 가득했듯이,
데이터 분석에서도 잘 시각화된 데이터는 복잡한 정보를 명확하게 전달하고,
하나님의 영광을 드러내는 것처럼 통찰을 제공합니다.

다음 장에서는:
📁 `matplotlib`, `seaborn`을 이용한 다양한 차트 생성
🔍 대시보드 구성 원리 및 실습
🎯 성막 봉헌처럼 데이터의 아름다움과 의미를 시각적으로 표현
📊 성막 봉헌 데이터를 시각화하여 하나님의 임재와 영광을 경험

"모세가 이같이 역사를 마치니 구름이 회막에 덮이고 여호와의 영광이 성막에 충만하매" (출애굽기 40:33-34)
"내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라" (요한복음 14:6)
    """
    print(preview)

def run_chapter23(interactive: bool = True):
    """Chapter 23 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 23을 시작합니다!")
        print("이 챕터에서는 데이터 검증과 클렌징을 배우고, 성경 속 제사장 위임식의 정결함과 예수님의 완전한 대제사장 직분을 탐구합니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '23',
        'title': '제사장 위임식 — 데이터 검증과 클렌징',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 제사장 위임식 분석
    exodus_results = run_priestly_consecration_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 대제사장 예수님 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's high priest analysis...)")

    # 2. 요한복음 대제사장 예수님 분석
    john_results = run_high_priest_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 제사장 위임식의 정결함과 대제사장 예수님의 완전함을 통해
데이터 검증과 클렌징의 중요성을 깨닫게 하시니 감사합니다.

저의 삶이 주님의 말씀에 따라 항상 깨끗하고 온전하게 유지되도록
끊임없이 자신을 검증하고 정화하는 지혜를 주소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, through the purity of the priestly consecration and the perfection of Jesus, the High Priest,
Thank You for helping me realize the importance of data validation and cleansing.

Grant me wisdom to constantly validate and purify myself,
so that my life may always remain clean and complete according to Your Word. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 23 완료! 스물세 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 23 Complete! You have finished the twenty-third wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter23(interactive=False)

        # 결과 저장 (선택사항)
        if results:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch23_results_{timestamp}.json"

            summary_results = {
                'chapter': '23',
                'title': '제사장 위임식 — 데이터 검증과 클렌징',
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
    print("🚀 JesusBornd Pandas Chapter 23 시작! (Starting JesusBornd Pandas Chapter 23!)\n")
    main()
