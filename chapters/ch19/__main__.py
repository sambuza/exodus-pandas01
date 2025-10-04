
"""
Chapter 19 통합 실행 스크립트
시내산 언약 — 스키마와 유효성

"세계가 다 내게 속하였나니 너희가 내 말을 잘 듣고 내 언약을 지키면 너희는 열국 중에서 내 소유가 되겠고" (출 19:5)
"예수께서 가라사대 내가 곧 길이요 진리요 생명이니 나로 말미암지 않고는 아버지께로 올 자가 없느니라" (요 14:6)
"""

import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch19.sinai_schema_validation import SinaiSchemaValidationAnalyzer
from chapters.ch19.truth_assert_validation import TruthAssertValidationAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 19: 시내산 언약 — 스키마와 유효성                ║
║                                                                      ║
║    "세계가 다 내게 속하였나니 너희가 내 말을 잘 듣고 내 언약을 지키면  ║
║     너희는 열국 중에서 내 소유가 되겠고" (출애굽기 19:5)                ║
║    "예수께서 가라사대 내가 곧 길이요 진리요 생명이니 나로 말미암지 않고 
║     는 아버지께로 올 자가 없느니라" (요한복음 14:6)                     ║
║                                                                      ║
║    🗺️  출애굽기 19장: 시내산 언약                                      ║
║    📊 요한복음 14:6: "나는 길이요 진리요 생명이니"                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_sinai_covenant_analysis():
    """출애굽기 시내산 언약 스키마/유효성 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 시내산 언약 스키마/유효성 분석 ===")
    print("하나님의 언약처럼 데이터의 무결성과 신뢰성을 확보하고, 이스라엘의 순종 여부를 데이터로 검증해보자!")
    print("Let's ensure data integrity and reliability like God's covenant, and validate Israel's obedience through data!")

    try:
        analyzer = SinaiSchemaValidationAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 시내산 언약 분석 중 오류 발생: {e}")
        return None

def run_truth_life_analysis():
    """요한복음 진리 유효성 검증 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 예수님 말씀의 진리 유효성 검증 ===")
    print("예수님 말씀의 절대적인 유효성을 `assert_frame_equal()`로 데이터적으로 검증해보자!")
    print("Let's numerically validate the absolute truth of Jesus' words using `assert_frame_equal()`!")

    try:
        analyzer = TruthAssertValidationAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 진리 유효성 검증 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 스키마 정의와 유효성 검증 = 하나님의 말씀처럼 견고한 데이터 구축",
        "🏺 시내산 언약 = 하나님의 백성으로서 지켜야 할 명확한 규례와 유효성",
        "📜 예수님 = 하나님께 이르는 유일하고 절대적인 진리이자 규격",
        "💡 `assert_frame_equal` = 예수님 말씀의 절대적인 유효성을 데이터적으로 증명"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 언약 준수율과 진리 부합 여부를 기반으로 통찰 제공
        covenant_errors = exodus_results.get('validation_errors', []) if exodus_results else []
        truth_valid = john_results.get('validation_status', False) if john_results else False

        if not covenant_errors and truth_valid:
            print(f"✨ 시내산 언약({len(covenant_errors)}개 오류)처럼, 당신의 삶도 예수님이라는 진리({truth_valid}) 안에서 무결하고 신뢰할 수 있습니다!")
            print(f"✨ Like the Sinai Covenant (0 errors), your life can be integral and reliable in Jesus, the Truth ({truth_valid})!")
        elif not covenant_errors:
            print(f"🌱 시내산 언약({len(covenant_errors)}개 오류)은 잘 지켰지만, 예수님이라는 진리({truth_valid})에 더 깊이 부합해야 합니다!")
            print(f"🌱 The Sinai Covenant (0 errors) is well kept, but you need to conform more deeply to Jesus, the Truth ({truth_valid})!")
        else:
            print(f"🙏 데이터 스키마와 유효성 검증처럼, 나의 신앙과 삶이 주님의 진리에 부합하는지 끊임없이 점검하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to constantly examine if your faith and life conform to God's truth, just like data schema and validation!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 20 미리보기 (Preview) ===

"십계명 — 데이터 품질 규약 (Ten Commandments - Data Quality Standards)"

이스라엘 백성이 시내산에서 십계명을 받아 하나님의 백성으로서 지켜야 할 근본적인 규약(데이터 품질 규약)을 얻었듯이, 데이터 분석에서도 데이터의 품질을 보장하는 것은 분석 결과의 신뢰성을 확보하는 데 필수적입니다.
`dropna()`, `fillna()`, `astype()`과 같은 도구는 데이터 품질을 향상시키는 데 사용됩니다.

Just as the Israelites received the Ten Commandments at Mount Sinai, obtaining fundamental standards (data quality standards) to live by as God's people, ensuring data quality is essential in data analysis to secure the reliability of analytical results.
Tools like `dropna()`, `fillna()`, and `astype()` are used to improve data quality.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 결측치 처리 (`dropna()`, `fillna()`)
🔍 데이터 타입 변환 (`astype()`)
🎯 이상치 탐지 및 처리
📊 십계명처럼 깨끗하고 신뢰할 수 있는 데이터 구축

"너는 나 외에는 다른 신들을 네게 있게 말지니라" (출애굽기 20:3)
"새 계명을 너희에게 주노니 서로 사랑하라 내가 너희를 사랑한 것같이 너희도 서로 사랑하라" (요한복음 13:34)
    """
    print(preview)

def run_chapter19(interactive: bool = True):
    """Chapter 19 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 19를 시작합니다!")
        print("이 챕터에서는 데이터 스키마 정의와 유효성 검증을 배우고, 성경 속 하나님의 언약과 예수님 말씀의 절대적인 진리를 탐구합니다.")
        print("This chapter introduces data schema definition and validation, exploring God's covenant and the absolute truth of Jesus' words in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '19',
        'title': '시내산 언약 — 스키마와 유효성',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 시내산 언약 분석
    exodus_results = run_sinai_covenant_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 진리 유효성 검증 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's truth validation analysis...)")

    # 2. 요한복음 진리 유효성 검증 분석
    john_results = run_truth_life_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 시내산 언약처럼 견고한 말씀과 예수님이라는 절대적인 진리 안에서 저의 삶을 살게 하시니 감사합니다.
데이터 스키마와 유효성 검증처럼 저의 신앙과 삶이 주님의 진리에 부합하는지 끊임없이 점검하게 하시고,
주님 안에서 무결하고 신뢰할 수 있는 삶을 살게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, Thank You for enabling me to live my life within Your solid Word like the Sinai Covenant and in Jesus, the absolute Truth.
Like data schema and validation, help me constantly examine if my faith and life conform to Your truth,
and enable me to live an integral and reliable life in You. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 19 완료! 열아홉 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 19 Complete! You have finished the nineteenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter19(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch19_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 19 시작! (Starting JesusBornd Pandas Chapter 19!)\n")
    main()
