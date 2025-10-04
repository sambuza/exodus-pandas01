
"""
Chapter 26 통합 실행 스크립트
휘장과 덮개 - 컬럼 가림/익명화

"진리를 알지니 진리가 너희를 자유롭게 하리라" (요한복음 8:32)
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
from chapters.ch26.veil_data import VeilDataGenerator
from chapters.ch26.column_masking import ColumnMaskingProcessor
from chapters.ch26.anonymization_techniques import AnonymizationTechniques
from chapters.ch26.toggle_visibility import VisibilityToggler

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 26: 휘장과 덮개 - 컬럼 가림/익명화             ║
║                                                                      ║
║    "진리를 알지니 진리가 너희를 자유롭게 하리라" (요한복음 8:32)         ║
║                                                                      ║
║    🛡️  출애굽기 26장: 성막의 휘장과 덮개                               ║
║    🔓 요한복음 8:32: 진리가 주는 자유                                  ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_veil_data_generation():
    """휘장과 덮개 데이터 생성 섹션 실행"""
    print("\n🛡️ === 휘장과 덮개 데이터 생성 ===")
    print("성막의 휘장과 덮개처럼 데이터의 중요한 부분을 가리거나 드러내는 데이터를 생성합니다.")
    print("Generates data that hides or reveals important parts, like the veil and covers of the tabernacle.")

    try:
        generator = VeilDataGenerator()
        data = generator.generate_veil_data()
        print("\n✅ 휘장 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 휘장 데이터 생성 중 오류 발생: {e}")
        return None

def run_column_masking_analysis(df):
    """컬럼 마스킹 분석 섹션 실행"""
    print("\n🔒 === 컬럼 마스킹 분석 ===")
    print("데이터의 특정 컬럼을 마스킹하여 민감한 정보를 보호하는 기법을 탐구합니다.")
    print("Explores techniques to protect sensitive information by masking specific columns.")

    if df is None:
        print("⚠️ 데이터가 없어 컬럼 마스킹 분석을 건너뜁니다.")
        return None

    try:
        processor = ColumnMaskingProcessor(df)
        masked_df = processor.apply_masking()
        print("\n✅ 컬럼 마스킹 적용 완료 (일부):")
        print(masked_df.head())
        return masked_df
    except Exception as e:
        print(f"❌ 컬럼 마스킹 분석 중 오류 발생: {e}")
        return None

def run_anonymization_techniques(df):
    """익명화 기법 적용 섹션 실행"""
    print("\n👻 === 익명화 기법 적용 ===")
    print("데이터 익명화 기법을 적용하여 개인 식별 정보를 제거하는 방법을 알아봅니다.")
    print("Applies data anonymization techniques to remove personally identifiable information.")

    if df is None:
        print("⚠️ 데이터가 없어 익명화 기법 적용을 건너뜁니다.")
        return None

    try:
        anonymizer = AnonymizationTechniques(df)
        anonymized_df = anonymizer.apply_anonymization()
        print("\n✅ 익명화 기법 적용 완료 (일부):")
        print(anonymized_df.head())
        return anonymized_df
    except Exception as e:
        print(f"❌ 익명화 기법 적용 중 오류 발생: {e}")
        return None

def run_toggle_visibility(df):
    """표시/비표시 토글 섹션 실행"""
    print("\n👁️ === 표시/비표시 토글 ===")
    print("데이터의 특정 컬럼을 필요에 따라 표시하거나 비표시하는 기능을 시뮬레이션합니다.")
    print("Simulates the ability to show or hide specific data columns as needed.")

    if df is None:
        print("⚠️ 데이터가 없어 표시/비표시 토글을 건너뜁니다.")
        return None

    try:
        toggler = VisibilityToggler(df)
        hidden_df = toggler.hide_columns(['sensitive_info'])
        print("\n✅ 'sensitive_info' 컬럼 숨김:")
        print(hidden_df.head())
        shown_df = toggler.show_columns(['sensitive_info'])
        print("\n✅ 'sensitive_info' 컬럼 다시 표시:")
        print(shown_df.head())
        return shown_df
    except Exception as e:
        print(f"❌ 표시/비표시 토글 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, masked_df, anonymized_df, toggled_df):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 데이터 가림/익명화 = 민감한 정보 보호와 진정한 자유",
        "🛡️ 성막의 휘장 = 거룩함과 접근의 제한, 동시에 그리스도를 통한 열림",
        "🔓 요한복음 8:32 = 진리를 알 때 얻는 영적 자유",
        "💡 데이터의 적절한 공개와 보호 = 지혜로운 데이터 관리와 영적 분별력"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and masked_df is not None and anonymized_df is not None and toggled_df is not None:
        print("✨ 성막의 휘장이 지성소를 가리듯, 데이터 익명화는 민감한 정보를 보호합니다.")
        print("✨ 진리가 우리를 자유롭게 하듯, 적절한 데이터 관리는 데이터의 가치를 높입니다.")
    else:
        print("🙏 데이터의 휘장과 덮개처럼, 무엇을 가리고 무엇을 드러낼지 지혜롭게 분별하는 영적 통찰을 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
 === Chapter 27 미리보기 (Preview) ===

"번제단 - 파생변수와 전처리 파이프"

성막의 번제단이 죄를 정결하게 하는 것처럼, 데이터 분석에서도 파생변수를 생성하고 데이터를 전처리하는 과정은 데이터의 품질을 높이고 분석에 적합한 형태로 만드는 데 필수적입니다.
`assign`, `np.where`와 같은 도구는 새로운 의미 있는 변수를 만들고 데이터를 정제하는 데 사용됩니다.

Just as the altar of burnt offering in the tabernacle purifies sin, in data analysis, creating derived variables and preprocessing data are essential for improving data quality and making it suitable for analysis.
Tools like `assign` and `np.where` are used to create new meaningful variables and refine data.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 파생변수 생성 및 활용
🔍 조건부 로직을 이용한 데이터 변환
🎯 전처리 파이프라인 구축
📊 번제단처럼 정결하고 분석에 적합한 데이터 준비

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 27:1-8)
"그가 흥하여야 하겠고 나는 쇠하여야 하리라" (요한복음 3:30)
    """
    print(preview)

def run_chapter26(interactive: bool = True):
    """Chapter 26 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 26을 시작합니다!")
        print("이 챕터에서는 데이터의 컬럼을 가리거나 익명화하는 기법을 배우고, 성막의 휘장과 진리가 주는 자유를 탐구합니다.")
        print("This chapter introduces techniques for hiding or anonymizing data columns, exploring the tabernacle's veil and the freedom that truth brings.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '26',
        'title': '휘장과 덮개 - 컬럼 가림/익명화',
        'original_data': None,
        'masked_data': None,
        'anonymized_data': None,
        'toggled_data': None
    }

    # 1. 휘장과 덮개 데이터 생성
    original_df = run_veil_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 컬럼 마스킹 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start column masking analysis...)")

    # 2. 컬럼 마스킹 분석
    masked_df = run_column_masking_analysis(original_df)
    results['masked_data'] = masked_df

    if interactive:
        input("\n▶️ 익명화 기법 적용을 시작하려면 Enter를 눌러주세요... (Press Enter to start anonymization techniques...)")

    # 3. 익명화 기법 적용
    anonymized_df = run_anonymization_techniques(original_df) # 원본 데이터에 적용
    results['anonymized_data'] = anonymized_df

    if interactive:
        input("\n▶️ 표시/비표시 토글을 시작하려면 Enter를 눌러주세요... (Press Enter to start toggle visibility...)")

    # 4. 표시/비표시 토글
    toggled_df = run_toggle_visibility(original_df) # 원본 데이터에 적용
    results['toggled_data'] = toggled_df

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, masked_df, anonymized_df, toggled_df)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 성막의 휘장처럼 데이터의 민감한 부분을 지혜롭게 가리고 드러내며, 진리가 주는 자유를 누리게 하소서.
데이터 익명화와 마스킹을 통해 정보의 가치를 보존하고, 동시에 개인의 프라이버시를 존중하는 분석가가 되게 하소서.
예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 26 완료! 스물여섯 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 26 Complete! You have finished the twenty-sixth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter26(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch26_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_masked_data': results['masked_data'] is not None,
                'has_anonymized_data': results['anonymized_data'] is not None,
                'has_toggled_data': results['toggled_data'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 26 시작! (Starting JesusBornd Pandas Chapter 26!)\n")
    main()
