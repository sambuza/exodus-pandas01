"""
Chapter 08 통합 실행 스크립트
재앙 속의 구분 — 고센과 마스킹

"여호와께서 말씀하시기를 내 백성을 보내라 그들이 나를 섬길 것이니라 내가 이 파리를 너와 네 신하와 네 백성과 네 집들에 보내리니 애굽 사람의 집집에 파리가 가득할 것이며 그들의 거하는 땅에도 그러하리라 그러나 그 날에 내가 내 백성이 거주하는 고센 땅을 구별하여 파리가 거기 있지 못하게 하리니 이로 말미암아 너는 내가 세상 중에서 여호와인 줄을 알게 될 것이라 내가 내 백성과 네 백성 사이에 구별을 두리니 내일 이 표징이 있으리라 하시고"
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# ch08의 분석 모듈들 (예상)
from chapters.ch08.second_plague_analysis import analyze_second_plague
from chapters.ch08.second_plague_data import generate_second_plague_data
from chapters.ch08.third_plague_analysis import analyze_third_plague
from chapters.ch08.third_plague_data import generate_third_plague_data

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║           Chapter 08: 재앙 속의 구분 — 고센과 마스킹                 ║
║                                                                      ║
║    "그러나 그 날에 내가 내 백성이 거주하는 고센 땅을 구별하여         ║
║     파리가 거기 있지 못하게 하리니 이로 말미암아 너는 내가 세상       ║
║     중에서 여호와인 줄을 알게 될 것이라 내가 내 백성과 네 백성       ║
║     사이에 구별을 두리니 내일 이 표징이 있으리라 하시고" (출 8:22-23)   ║
║    "예수께서 또 말씀하여 이르시되 나는 세상의 빛이니 나를 따르는      ║
║     자는 어둠에 다니지 아니하고 생명의 빛을 얻으리라" (요 8:12)         ║
║                                                                      ║
║    🗺️  출애굽기 8장: 두 번째(개구리)와 세 번째(이) 재앙과 고센 땅의 구별 ║
║    📊 요한복음 8:12–20: 세상의 빛이신 예수님과 영적 분별력            ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_second_plague_section():
    """두 번째 재앙 분석 섹션 실행"""
    print("\n🐸 === 출애굽기 여정: 두 번째 재앙, 개구리 재앙 ===\n")
    print("개구리 재앙 데이터를 생성하고, 재앙의 확산과 영향을 분석합니다.")
    try:
        data = generate_second_plague_data()
        results = analyze_second_plague(data)
        return {"data": data, "analysis_results": results}
    except Exception as e:
        print(f"❌ 두 번째 재앙 분석 중 오류 발생: {e}")
        return None

def run_third_plague_section():
    """세 번째 재앙 분석 섹션 실행"""
    print("\n🦟 === 출애굽기 여정: 세 번째 재앙, 이 재앙 ===\n")
    print("이 재앙 데이터를 생성하고, 재앙의 특성과 고센 땅의 구별을 분석합니다.")
    try:
        data = generate_third_plague_data()
        results = analyze_third_plague(data)
        return {"data": data, "analysis_results": results}
    except Exception as e:
        print(f"❌ 세 번째 재앙 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(second_plague_results, third_plague_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음 × 고센 땅의 구별 ===\n")

    blending_insights = [
        "🐸 재앙의 확산과 하나님의 주권적인 개입",
        "🦟 이 재앙: 애굽의 술객들도 흉내 낼 수 없었던 하나님의 능력",
        "📍 고센 땅의 구별: 하나님께서 당신의 백성을 재앙 속에서 보호하심",
        "✨ `df.mask()`, `df.where()`: 데이터에서 하나님의 구별된 은혜를 찾아내는 지혜"
    ]

    print("💎 핵심 발견들:")
    for insight in blending_insights:
        print(f"   {insight}")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 09 미리보기 ===

"더 큰 재앙과 인내 — 데이터 통합과 병합"

출애굽기 9장에서 더 큰 재앙(악성 종기, 우박)이 임하고 파라오의 강퍅함이 지속되듯이,
데이터 분석에서도 여러 재앙 데이터를 '통합'하고 '병합'하는 것은
복잡한 상황을 종합적으로 이해하고, 숨겨진 패턴을 발견하는 데 필수적인 기술입니다.

다음 장에서는:

-   **출애굽기 9장**: 악성 종기, 우박 재앙 → 여러 데이터 소스의 통합
-   **요한복음 9:1–12**: 날 때부터 맹인 된 자를 고치심 → 영적 통찰의 통합
-   **pandas 기술**: `pd.concat()`, `pd.merge()`, `df.join()` 등

하나님은 재앙을 통해 당신의 계획을 이루시고, 인내하며 당신의 백성을 구원하십니다.
여러 데이터를 효과적으로 통합하고 병합하는 법을 배워, 복잡한 세상 속에서
하나님의 큰 그림과 인내를 발견할 것입니다.
    """
    print(preview)

def run_chapter08(interactive: bool = True):
    """Chapter 08 전체 실행

    Args:
        interactive: 대화형 모드 여부

    Returns:
        dict: 전체 분석 결과
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 08을 시작합니다!\n")
        print("이 챕터에서는 재앙 속에서 하나님이 어떻게 구별하시는지를 데이터 마스킹을 통해 다룹니다.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요...")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '08',
        'title': '재앙 속의 구분 — 고센과 마스킹',
        'second_plague_section': None,
        'third_plague_section': None,
    }

    # 1. 두 번째 재앙 분석
    second_plague_results = run_second_plague_section()
    results['second_plague_section'] = second_plague_results

    if interactive:
        input("\n▶️ 세 번째 재앙 분석을 시작하려면 Enter를 눌러주세요...")

    # 2. 세 번째 재앙 분석
    third_plague_results = run_third_plague_section()
    results['third_plague_section'] = third_plague_results

    # 3. 블렌딩 통찰
    show_blending_insights(second_plague_results, third_plague_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n🙏 === 마무리 기도 ===\n")
    prayer = """
재앙 속에서도 당신의 백성을 구별하시고 보호하시는 하나님, 감사합니다.
오늘 데이터의 구별과 마스킹을 배우며, 세상의 혼돈 속에서도
하나님의 명확한 주권과 구별된 은혜를 발견하게 하시니 감사합니다.

세상의 유혹과 고난 속에서도 주님을 따르는 자들을 구별하시어
생명의 빛 가운데 거하게 하시는 주님의 은혜를 찬양합니다.

예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print("\n🎉 Chapter 08 완료! 여덟 번째 광야 여정을 마치셨습니다!\n")
    print("📊 이제 데이터를 효과적으로 구별하고 마스킹할 수 있습니다!")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter08(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            import json
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch08_results_{timestamp}.json"

            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'second_plague_section_completed': results['second_plague_section'] is not None,
                'third_plague_section_completed': results['third_plague_section'] is not None,
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
    print("🚀 JesusBornd Pandas Chapter 08 시작!\n")
    results = main()
