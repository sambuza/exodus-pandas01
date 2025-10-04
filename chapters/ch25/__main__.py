import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch25.ark_data_modeling import ArkDataModeler
from chapters.ch25.revelation_db_integration import RevelationDBIntegrator

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 25: 언약궤와 보좌 — 고급 데이터 모델링             ║
║                                                                      ║
║    "거기서 내가 너와 만나고 속죄소 위 곧 증거궤 위에 있는 두 그룹      ║
║     사이에서 내가 이스라엘 자손을 위하여 네게 명할 모든 일을 네게     ║
║     이르리라" (출애굽기 25:22)                                        ║
║    "이 일 후에 내가 보니 하늘에 열린 문이 있는데 내가 들은 바 처음에 ║
║     내게 말하던 나팔 소리 같은 그 음성이 이르되 이리로 올라오라 이 후에 ║
║     마땅히 될 일을 내가 네게 보이리라 하시더라" (요한계시록 4:1)       ║
║                                                                      ║
║    🗺️  출애굽기 25장: 언약궤와 속죄소                                  ║
║    📊 요한계시록 4-5장: 하늘 보좌와 어린양의 예배                     ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_ark_data_modeling():
    """출애굽기 언약궤 고급 데이터 모델링 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 언약궤 고급 데이터 모델링 ===")
    print("성막의 가장 거룩한 곳에 있는 언약궤와 그 구성 요소들을 데이터 모델링하여 하나님의 임재와 언약의 깊은 의미를 탐구해보자!")
    try:
        modeler = ArkDataModeler()
        exodus_results = modeler.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 언약궤 데이터 모델링 중 오류 발생: {e}")
        return None

def run_revelation_integration():
    """요한계시록 하늘 보좌 데이터베이스 통합 섹션 실행"""
    print("\n📜 === 요한계시록 여정: 하늘 보좌 데이터베이스 통합 ===")
    print("하늘 보좌와 어린양의 예배 데이터를 통합하고 모델링하여 최종적인 하나님의 계획과 영원한 목적을 탐구해보자!")
    try:
        integrator = RevelationDBIntegrator()
        john_results = integrator.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 하늘 보좌 데이터 통합 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한계시록의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x Revelation")

    blending_insights = [
        "📊 고급 데이터 모델링 = 언약궤와 보좌처럼 복잡한 관계와 숨겨진 의미를 구조화",
        "🏺 언약궤 = 하나님의 임재와 언약의 핵심을 담은 데이터 모델",
        "📜 하늘 보좌와 어린양 = 최종적인 권위와 구속의 완성, 모든 데이터의 궁극적인 목적",
        "💡 데이터베이스 통합 = 흩어진 정보들을 연결하여 하나님의 큰 그림을 완성"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 언약궤 모델링의 복잡도와 하늘 보좌 데이터 통합 수준을 기반으로 통찰 제공
        ark_model_complexity = len(exodus_results.get('modeled_ark_data', pd.DataFrame()).columns) if exodus_results else 0
        integrated_data_rows = len(john_results.get('integrated_worship_data', pd.DataFrame())) if john_results else 0

        if ark_model_complexity > 5 and integrated_data_rows > 10:
            print(f"✨ 언약궤({ark_model_complexity}개 컬럼)의 정교한 모델링처럼, 하늘 보좌({integrated_data_rows}개 데이터)의 통합된 데이터를 통해 당신의 삶은 하나님의 깊은 계획 속에 있습니다!")
            print(f"✨ Like the intricate modeling of the Ark ({ark_model_complexity} columns), through the integrated data of the heavenly throne ({integrated_data_rows} rows), your life is within God's deep plan!")
        else:
            print(f"🙏 고급 데이터 모델링처럼, 나의 삶 속에서 하나님의 깊은 뜻과 계획을 구조화하고 통합하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to structure and integrate God's deep will and plan in my life, just like advanced data modeling!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 26 미리보기 (Preview) ===

"새 하늘과 새 땅 — 미래 예측과 머신러닝 (Future Prediction and Machine Learning)"

요한계시록에서 새 하늘과 새 땅이 도래할 것을 예언하듯이,
데이터 분석에서도 과거 데이터를 기반으로 미래를 예측하고,
머신러닝 모델을 구축하여 숨겨진 패턴을 학습하는 것은 매우 중요합니다.

다음 장에서는:
📁 시계열 예측 모델 (예: ARIMA, Prophet)
🔍 분류 및 회귀 모델 (예: Logistic Regression, Random Forest)
🎯 머신러닝 파이프라인 구축
📊 새 하늘과 새 땅처럼 데이터 속 하나님의 미래 계획을 예측

"또 내가 새 하늘과 새 땅을 보니 처음 하늘과 처음 땅이 없어졌고 바다도 다시 있지 않더라" (요한계시록 21:1)
"보라 내가 만물을 새롭게 하노라 하시고 또 이르시되 이 말은 신실하고 참되니 기록하라" (요한계시록 21:5)
    """
    print(preview)

def run_chapter25(interactive: bool = True):
    """Chapter 25 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 25을 시작합니다!")
        print("이 챕터에서는 고급 데이터 모델링과 데이터베이스 통합을 배우고, 성경 속 언약궤와 하늘 보좌의 깊은 의미를 탐구합니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '25',
        'title': '언약궤와 보좌 — 고급 데이터 모델링',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 언약궤 고급 데이터 모델링
    exodus_results = run_ark_data_modeling()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한계시록 하늘 보좌 데이터베이스 통합을 시작하려면 Enter를 눌러주세요... (Press Enter to start Revelation DB integration...)")

    # 2. 요한계시록 하늘 보좌 데이터베이스 통합
    john_results = run_revelation_integration()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 언약궤와 하늘 보좌의 깊은 의미를 통해 주님의 임재와 최종적인 계획을 찬양합니다.
고급 데이터 모델링처럼 저의 삶 속에서 주님의 깊은 뜻과 계획을 구조화하고 통합하게 하시고,
영원한 예배와 구속의 완성에 참여하게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, I praise Your presence and ultimate plan through the deep meaning of the Ark of the Covenant and the heavenly throne.
Like advanced data modeling, may I structure and integrate Your deep will and plan in my life,
and may I participate in eternal worship and the completion of redemption. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 25 완료! 스물다섯 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 25 Complete! You have finished the twenty-fifth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter25(interactive=False)

        # 결과 저장 (선택사항)
        if results:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch25_results_{timestamp}.json"

            summary_results = {
                'chapter': '25',
                'title': '언약궤와 보좌 — 고급 데이터 모델링',
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
    print("🚀 JesusBornd Pandas Chapter 25 시작! (Starting JesusBornd Pandas Chapter 25!)\n")
    main()
