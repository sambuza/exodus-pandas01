
"""
Chapter 16 통합 실행 스크립트
만나의 규례 — 윈도우와 롤링

"여호와께서 모세에게 이르시되 하늘에서 너희를 위하여 양식을 비같이 내리리니 백성이 나가서 일용할 것을 날마다 거둘 것이라" (출 16:4)
"예수께서 이르시되 내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요 6:35)
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
from chapters.ch16.manna_rolling_expanding import MannaRollingExpandingAnalyzer
from chapters.ch16.bread_window_functions import BreadWindowFunctionsAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 16: 만나의 규례 — 윈도우와 롤링                  ║
║                                                                      ║
║    "여호와께서 모세에게 이르시되 하늘에서 너희를 위하여 양식을 비같이  ║
║     내리리니 백성이 나가서 일용할 것을 날마다 거둘 것이라" (출 16:4)    ║
║    "예수께서 이르시되 내가 곧 생명의 떡이니 내게 오는 자는 결코        ║
║     주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요 6:35) ║
║                                                                      ║
║    🗺️  출애굽기 16장: 만나와 메추라기                                  ║
║    📊 요한복음 6:31-35: 생명의 떡                                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_manna_analysis():
    """출애굽기 만나 롤링/익스팬딩 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 만나 롤링/익스팬딩 분석 ===")
    print("만나 공급의 주기적 패턴과 이스라엘의 누적된 불평을 `rolling()`과 `expanding()`으로 탐구해보자!")
    print("Let's explore the periodic patterns of manna provision and Israel's accumulated complaints using `rolling()` and `expanding()`!")

    try:
        analyzer = MannaRollingExpandingAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 만나 분석 중 오류 발생: {e}")
        return None

def run_bread_of_life_analysis():
    """요한복음 생명의 떡 윈도우 함수 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 생명의 떡 윈도우 함수 분석 ===")
    print("영적 갈증과 채움의 변화 추세를 윈도우 함수로 분석하여 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by analyzing trends in spiritual hunger and fulfillment using window functions!")

    try:
        analyzer = BreadWindowFunctionsAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 생명의 떡 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `rolling()`, `expanding()` = 시간의 흐름 속 패턴과 누적 변화 발견",
        "🏺 만나의 규례 = 하나님의 매일의 신실한 공급과 순종의 시험",
        "📜 생명의 떡 = 예수님을 통한 영원한 채움과 영적 갈증 해소",
        "💡 윈도우 함수 = 세상적인 것과 영원한 것의 대조를 시계열로 분석"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 만나 수확량의 롤링 평균과 영적 채움의 롤링 평균을 기반으로 통찰 제공
        manna_avg = exodus_results.get('rolling_mean_manna', pd.Series()).mean() if exodus_results and 'rolling_mean_manna' in exodus_results else 0
        fulfillment_avg = john_results.get('rolling_mean_fulfillment', pd.Series()).mean() if john_results and 'rolling_mean_fulfillment' in john_results else 0

        if manna_avg > 100 and fulfillment_avg > 7:
            print(f"✨ 만나({manna_avg:.1f}kg)의 풍성한 공급처럼, 생명의 떡이신 예수님을 통해 당신의 영적 채움({fulfillment_avg:.1f})도 풍성합니다!")
            print(f"✨ Like the abundant provision of manna ({manna_avg:.1f}kg), your spiritual fulfillment ({fulfillment_avg:.1f}) is abundant through Jesus, the Bread of Life!")
        elif manna_avg > 50:
            print(f"🌱 만나({manna_avg:.1f}kg)의 공급은 꾸준하지만, 생명의 떡({fulfillment_avg:.1f})을 통해 더 깊은 영적 만족을 추구해야 합니다!")
            print(f"🌱 The provision of manna ({manna_avg:.1f}kg) is constant, but you should seek deeper spiritual satisfaction through the Bread of Life ({fulfillment_avg:.1f})!")
        else:
            print(f"🙏 시간의 흐름 속에서 하나님의 신실한 공급과 영원한 생명의 떡이신 예수님을 발견하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to discover God's faithful provision and Jesus, the eternal Bread of Life, in the flow of time!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 17 미리보기 (Preview) ===

"반석에서 난 물 — 결합과 보간 (Combining and Interpolation)"

이스라엘 백성이 르비딤에서 물이 없어 목마를 때, 모세가 반석을 쳐서 물을 내었습니다. 이처럼 데이터 분석에서도 서로 다른 데이터셋을 결합하고, 누락된 데이터를 보간(Interpolation)하여 완전한 정보를 얻는 것은 중요한 과정입니다.

When the Israelites thirsted for water at Rephidim, Moses struck the rock, and water flowed out. Similarly, in data analysis, combining different datasets and interpolating missing data to obtain complete information is a crucial process.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `df.combine_first()`: 두 DataFrame을 결합하여 결측치 채우기
🔍 `df.interpolate()`: 누락된 데이터 보간
🎯 `df.reindex()`: 인덱스 재설정 및 데이터 정렬
📊 광야 여정의 누락된 정보들을 채워 하나님의 완전한 인도하심을 이해

"여호와께서 모세에게 이르시되 백성 앞을 지나 지팡이를 잡고 호렙 산 반석을 치라 그리하면 그곳에서 물이 나리니 백성이 마시리라" (출애굽기 17:5-6)
"누구든지 목마르거든 내게로 와서 마시라 나를 믿는 자는 성경에 이름과 같이 그 배에서 생수의 강이 흘러나리라" (요한복음 7:37-38)
    """
    print(preview)

def run_chapter16(interactive: bool = True):
    """Chapter 16 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 16을 시작합니다!")
        print("이 챕터에서는 `rolling()`과 `expanding()`을 사용하여 시계열 데이터 분석을 배우고, 성경 속 하나님의 신실한 공급과 영원한 채움을 탐구합니다.")
        print("This chapter introduces time-series data analysis using `rolling()` and `expanding()`, exploring God's faithful provision and eternal sustenance in the Bible.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '16',
        'title': '만나의 규례 — 윈도우와 롤링',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 만나 분석
    exodus_results = run_manna_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 생명의 떡 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's bread of life analysis...)")

    # 2. 요한복음 생명의 떡 분석
    john_results = run_bread_of_life_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 광야에서 만나를 주시고 생명의 떡이신 예수님으로 저희를 먹이시니 감사합니다.
시간의 흐름 속에서 `rolling()`과 `expanding()`처럼 주님의 신실한 공급과 영원한 채움을 발견하게 하시고,
매일매일 주님 안에서 영적으로 성장하게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, Thank You for providing manna in the wilderness and for feeding us with Jesus, the Bread of Life.
In the flow of time, like `rolling()` and `expanding()`, help us discover Your faithful provision and eternal sustenance,
and may we grow spiritually in You every day. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 16 완료! 열여섯 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 16 Complete! You have finished the sixteenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter16(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch16_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 16 시작! (Starting JesusBornd Pandas Chapter 16!)\n")
    main()
