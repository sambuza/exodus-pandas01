
"""
Chapter 28 통합 실행 스크립트
제사장 옷 - 라벨링과 스타일링

"나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이" (요한복음 10:14)
"""

import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd
import numpy as np

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch28.priestly_garments_data import PriestlyGarmentsDataGenerator
from chapters.ch28.categorical_labeling import CategoricalLabeler
from chapters.ch28.dataframe_styling import DataFrameStyler
from chapters.ch28.styled_report_generator import StyledReportGenerator

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 28: 제사장 옷 - 라벨링과 스타일링              ║
║                                                                      ║
║    \"나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이\" (요한복음 10:14) ║
║                                                                      ║
║     출애굽기 28장: 제사장 옷                                         ║
║     요한복음 10:14-16: 선한 목자                                     ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_priestly_garments_data_generation():
    """제사장 옷 데이터 생성 섹션 실행"""
    print("\n👑 === 제사장 옷 데이터 생성 ===")
    print("제사장 옷처럼 데이터의 특징을 명확히 보여줄 수 있는 데이터를 생성합니다.")
    print("Generates data that clearly shows data characteristics, like priestly garments.")

    try:
        generator = PriestlyGarmentsDataGenerator()
        data = generator.generate_garments_data()
        print("\n✅ 제사장 옷 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 제사장 옷 데이터 생성 중 오류 발생: {e}")
        return None

def run_categorical_labeling(df):
    """범주형 라벨링 섹션 실행"""
    print("\n🏷️ === 범주형 라벨링 ===")
    print("데이터의 범주형 특성을 명확하게 라벨링하여 분석의 효율성을 높입니다.")
    print("Enhances analysis efficiency by clearly labeling categorical features of data.")

    if df is None:
        print("⚠️ 데이터가 없어 범주형 라벨링을 건너뜁니다.")
        return None

    try:
        labeler = CategoricalLabeler(df)
        labeled_df = labeler.apply_categorical_labels()
        print("\n✅ 범주형 라벨링 적용 완료 (일부):")
        print(labeled_df.head())
        return labeled_df
    except Exception as e:
        print(f"❌ 범주형 라벨링 중 오류 발생: {e}")
        return None

def run_dataframe_styling(df):
    """데이터프레임 스타일링 섹션 실행"""
    print("\n✨ === 데이터프레임 스타일링 ===")
    print("데이터프레임에 시각적 스타일을 적용하여 데이터의 가독성과 통찰력을 향상시킵니다.")
    print("Enhances data readability and insights by applying visual styles to the DataFrame.")

    if df is None:
        print("⚠️ 데이터가 없어 데이터프레임 스타일링을 건너뜁니다.")
        return None

    try:
        styler = DataFrameStyler(df)
        styled_df = styler.apply_styles()
        print("\n✅ 데이터프레임 스타일링 적용 완료 (HTML 출력):")
        # styled_df는 Styler 객체이므로 to_html()로 출력
        print(styled_df.to_html(max_rows=5))
        return styled_df
    except Exception as e:
        print(f"❌ 데이터프레임 스타일링 중 오류 발생: {e}")
        return None

def run_styled_report_generation(df):
    """스타일링된 보고서 생성 섹션 실행"""
    print("\n📄 === 스타일링된 보고서 생성 ===")
    print("라벨링과 스타일링이 적용된 데이터를 기반으로 보고서를 생성하여 데이터의 의미를 효과적으로 전달합니다.")
    print("Generates reports based on labeled and styled data to effectively communicate data insights.")

    if df is None:
        print("⚠️ 데이터가 없어 스타일링된 보고서 생성을 건너뜁니다.")
        return None

    try:
        report_generator = StyledReportGenerator(df)
        report_output = report_generator.generate_report()
        print("\n✅ 스타일링된 보고서 생성 완료 (일부):")
        print(report_output[:500]) # 보고서 내용의 일부만 출력
        return report_output
    except Exception as e:
        print(f"❌ 스타일링된 보고서 생성 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, labeled_df, styled_df, report_output):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 라벨링과 스타일링 = 데이터의 명확성과 시각적 아름다움",
        "👑 제사장 옷 = 하나님의 영광과 거룩함을 드러내는 상징",
        "🐑 요한복음 10:14-16 = 선한 목자가 양을 알고 양이 목자를 아는 친밀함",
        "💡 데이터의 효과적인 표현 = 데이터와 사용자 간의 깊은 이해와 소통"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and labeled_df is not None and styled_df is not None and report_output is not None:
        print("✨ 제사장 옷이 하나님의 영광을 드러내듯, 데이터 스타일링은 데이터의 본질을 아름답게 표현합니다.")
        print("✨ 선한 목자가 양을 알듯, 명확한 라벨링은 데이터의 의미를 깊이 이해하게 돕습니다.")
    else:
        print("🙏 제사장 옷처럼 아름답고 선한 목자처럼 친밀하게 데이터를 이해하고 표현하는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
 === Chapter 29 미리보기 (Preview) ===

"위임식 - 테스트 데이터 세팅"

제사장 위임식이 제사장의 직분을 공식적으로 시작하는 것처럼, 데이터 분석에서도 테스트 데이터 세팅은 모델의 성능을 검증하고 신뢰성을 확보하는 데 필수적입니다.
`sample`, `train_test_split`과 같은 도구는 데이터를 적절히 분할하여 모델 학습과 평가의 기반을 마련하는 데 사용됩니다.

Just as the ordination of priests officially begins their ministry, in data analysis, setting up test data is essential for validating model performance and ensuring reliability.
Tools like `sample` and `train_test_split` are used to properly partition data, laying the foundation for model training and evaluation.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 데이터 샘플링 기법
🔍 훈련/테스트 데이터 분할의 중요성
🎯 재현 가능한 데이터 분할을 위한 시드(seed) 설정
📊 위임식처럼 견고하고 신뢰할 수 있는 모델 검증 환경 구축

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 29:1-9)
"내가 비옵는 것은 이 사람들을 위함이요 세상은 위함이 아니요 내게 주신 자들을 위함이니이다" (요한복음 17:9)
    """
    print(preview)

def run_chapter28(interactive: bool = True):
    """Chapter 28 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 28을 시작합니다!")
        print("이 챕터에서는 데이터 라벨링과 스타일링 기법을 배우고, 제사장 옷과 선한 목자의 비유를 탐구합니다.")
        print("This chapter introduces data labeling and styling techniques, exploring priestly garments and the parable of the Good Shepherd.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '28',
        'title': '제사장 옷 - 라벨링과 스타일링',
        'original_data': None,
        'labeled_data': None,
        'styled_data': None,
        'report_output': None
    }

    # 1. 제사장 옷 데이터 생성
    original_df = run_priestly_garments_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 범주형 라벨링을 시작하려면 Enter를 눌러주세요... (Press Enter to start categorical labeling...)")

    # 2. 범주형 라벨링
    labeled_df = run_categorical_labeling(original_df)
    results['labeled_data'] = labeled_df

    if interactive:
        input("\n▶️ 데이터프레임 스타일링을 시작하려면 Enter를 눌러주세요... (Press Enter to start DataFrame styling...)")

    # 3. 데이터프레임 스타일링
    styled_df = run_dataframe_styling(labeled_df) # 라벨링된 데이터에 스타일링 적용
    results['styled_data'] = styled_df

    if interactive:
        input("\n▶️ 스타일링된 보고서 생성을 시작하려면 Enter를 눌러주세요... (Press Enter to start styled report generation...)")

    # 4. 스타일링된 보고서 생성
    report_output = run_styled_report_generation(labeled_df) # 라벨링된 데이터로 보고서 생성
    results['report_output'] = report_output

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, labeled_df, styled_df, report_output)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 제사장 옷처럼 데이터의 본질을 아름답게 표현하고, 선한 목자가 양을 알듯 데이터를 깊이 이해하는 분석가가 되게 하소서.
라벨링과 스타일링을 통해 데이터의 가치를 높이고, 통찰을 명확하게 전달하게 하소서.
예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 28 완료! 스물여덟 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 28 Complete! You have finished the twenty-eighth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter28(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch28_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_labeled_data': results['labeled_data'] is not None,
                'has_styled_data': results['styled_data'] is not None,
                'has_report_output': results['report_output'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 28 시작! (Starting JesusBornd Pandas Chapter 28!)\n")
    main()
