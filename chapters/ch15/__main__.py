
"""
Chapter 15 통합 실행 스크립트
바다의 노래 — 피벗과 형태변환

"여호와는 나의 힘이요 노래시며 나의 구원이시로다 그는 나의 하나님이시니 내가 그를 찬송할 것이요 내 아비의 하나님이시니 내가 그를 높이리로다" (출 15:2)
"하나님은 영이시니 예배하는 자가 신령과 진정으로 예배할지니라" (요 4:24)
"""

import sys
from pathlib import Path
import json
from datetime import datetime

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch15.song_pivot_reshape import SongPivotReshapeAnalyzer
from chapters.ch15.worship_stack_unstack import WorshipStackUnstackAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 15: 바다의 노래 — 피벗과 형태변환                  ║
║                                                                      ║
║    "여호와는 나의 힘이요 노래시며 나의 구원이시로다 그는 나의 하나님이시니 
║     내가 그를 찬송할 것이요 내 아비의 하나님이시니 내가 그를 높이리로다" (출 15:2) 
║    "하나님은 영이시니 예배하는 자가 신령과 진정으로 예배할지니라" (요 4:24) 
║                                                                      ║
║    🗺️  출애굽기 15장: 모세와 미리암의 노래                             ║
║    📊 요한복음 4:23-24: 신령과 진정으로 예배할 때                       ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_song_of_sea_analysis():
    """출애굽기 바다의 노래 피벗/형태변환 분석 섹션 실행"""
    print("\n🏺 === 출애굽기 여정: 바다의 노래 피벗/형태변환 분석 ===")
    print("하나님의 구원 역사를 다양한 관점으로 재구성하여 그 위대함을 데이터로 찬양해보자!")
    print("Let's praise God's greatness by reconfiguring His salvation history from various perspectives through data!")

    try:
        analyzer = SongPivotReshapeAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"❌ 출애굽기 바다의 노래 분석 중 오류 발생: {e}")
        return None

def run_worship_analysis():
    """요한복음 예배 스택/언스택 분석 섹션 실행"""
    print("\n📜 === 요한복음 여정: 예배 스택/언스택 분석 ===")
    print("예배의 본질과 다양한 형태를 인덱스와 컬럼 간에 전환하며 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by pivoting the essence and various forms of worship between index and columns!")

    try:
        analyzer = WorshipStackUnstackAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"❌ 요한복음 예배 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 `pivot_table()`, `melt()`, `stack()`, `unstack()` = 데이터 형태변환으로 숨겨진 패턴 발견",
        "🏺 바다의 노래 = 구원 역사를 다양한 관점에서 재구성하여 찬양",
        "📜 예배 = 신령과 진정으로 드리는 다층적인 본질과 표현",
        "💡 데이터 형태변환 = 하나님의 위대함과 예배의 깊이를 다각도로 탐구"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 바다의 노래 강도와 예배의 본질 수준을 기반으로 통찰 제공
        song_intensity_sum = exodus_results.get('pivoted_song', pd.DataFrame()).sum().sum() if exodus_results and 'pivoted_song' in exodus_results else 0
        worship_essence_avg = john_results.get('stack_unstack_results', (pd.Series(), pd.Series()))[0].loc[(slice(None), slice(None), 'essence_level')].mean() if john_results and 'stack_unstack_results' in john_results else 0

        if song_intensity_sum > 50 and worship_essence_avg > 8:
            print(f"✨ 바다의 노래({song_intensity_sum:.1f})처럼, 신령과 진정({worship_essence_avg:.1f})으로 드리는 당신의 예배는 하나님께 큰 영광이 됩니다!")
            print(f"✨ Like the Song of the Sea ({song_intensity_sum:.1f}), your worship in spirit and truth ({worship_essence_avg:.1f}) brings great glory to God!")
        elif song_intensity_sum > 30:
            print(f"🌱 바다의 노래({song_intensity_sum:.1f})는 위대하지만, 예배의 본질({worship_essence_avg:.1f})을 더 깊이 탐구해야 합니다!")
            print(f"🌱 The Song of the Sea ({song_intensity_sum:.1f}) is great, but you need to delve deeper into the essence of worship ({worship_essence_avg:.1f})!")
        else:
            print(f"🙏 데이터 형태변환처럼, 삶의 다양한 관점에서 하나님을 예배하고 찬양하는 지혜를 구하세요!")
            print(f"🙏 Seek wisdom to worship and praise God from various perspectives, just like data reshaping!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 16 미리보기 (Preview) ===

"만나의 규례 — 윈도우와 롤링 (Window and Rolling Functions)"

이스라엘 백성이 광야에서 매일 만나를 거두었듯이, 데이터 분석에서도 시간의 흐름에 따라 일정 기간 동안의 데이터를 묶어 분석하는 '윈도우(Window)' 함수와 '롤링(Rolling)' 연산은 추세와 변화를 파악하는 데 필수적입니다.

Just as the Israelites gathered manna daily in the wilderness, in data analysis, 'window' functions and 'rolling' operations—which group data over a specified period along a timeline—are essential for identifying trends and changes.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `df.rolling()`: 이동 평균, 이동 합계 등 계산
🔍 `df.expanding()`: 누적 계산
🎯 윈도우 함수(mean, sum, std) 적용
📊 만나의 규례처럼 시간의 흐름 속 하나님의 신실한 공급 패턴 분석

"여호와께서 모세에게 이르시되 하늘에서 너희를 위하여 양식을 비같이 내리리니 백성이 나가서 일용할 것을 날마다 거둘 것이라" (출애굽기 16:4)
"예수께서 이르시되 내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요한복음 6:35)
    """
    print(preview)

def run_chapter15(interactive: bool = True):
    """Chapter 15 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 15를 시작합니다!")
        print("이 챕터에서는 `pivot_table()`, `melt()`, `stack()`, `unstack()`을 사용하여 데이터 형태변환을 배우고, 성경 속 구원 역사와 예배의 본질을 다각도로 탐구합니다.")
        print("This chapter introduces data reshaping using `pivot_table()`, `melt()`, `stack()`, `unstack()`, exploring salvation history and the essence of worship in the Bible from various angles.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '15',
        'title': '바다의 노래 — 피벗과 형태변환',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 바다의 노래 분석
    exodus_results = run_song_of_sea_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n▶️ 요한복음 예배 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's worship analysis...)")

    # 2. 요한복음 예배 분석
    john_results = run_worship_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 바다의 노래처럼 주님의 위대한 구원 역사를 다양한 관점에서 찬양합니다.
신령과 진정으로 드리는 예배를 통해 주님을 기쁘시게 하고,
데이터의 형태변환처럼 저의 삶을 주님의 뜻대로 재구성하여 주님께 영광 돌리게 하소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, like the Song of the Sea, I praise Your great salvation history from various perspectives.
Through worship in spirit and truth, may I please You,
and like data reshaping, may my life be reconfigured according to Your will to bring You glory. I pray in Jesus' name. Amen."
    """
    print(prayer)

    print(f"\n🎉 Chapter 15 완료! 열다섯 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 15 Complete! You have finished the fifteenth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter15(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch15_results_{timestamp}.json"

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
    print("🚀 JesusBornd Pandas Chapter 15 시작! (Starting JesusBornd Pandas Chapter 15!)\n")
    main()
