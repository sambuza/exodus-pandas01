
"""
Chapter 29 통합 실행 스크립트
위임식 - 테스트 데이터 세팅

"내가 비옵는 것은 이 사람들을 위함이요 세상은 위함이 아니요 내게 주신 자들을 위함이니이다" (요한복음 17:9)
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
from chapters.ch29.ordination_data import OrdinationDataGenerator
from chapters.ch29.data_sampling import DataSampler
from chapters.ch29.train_test_splitter import TrainTestSplitter
from chapters.ch29.reproducible_split import ReproducibleSplitter

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 29: 위임식 - 테스트 데이터 세팅                ║
║                                                                      ║
║    "내가 비옵는 것은 이 사람들을 위함이요 세상은 위함이 아니요 내게 주신 자들을 위함이니이다" (요한복음 17:9) ║
║                                                                      ║
║    🙏 출애굽기 29장: 제사장 위임식                                     ║
║    🛡️ 요한복음 17:17-19: 예수님의 제자들을 위한 기도                   ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)

def run_ordination_data_generation():
    """위임식 데이터 생성 섹션 실행"""
    print("\n🙏 === 위임식 데이터 생성 ===")
    print("제사장 위임식처럼 모델의 성능을 검증하기 위한 기초 데이터를 생성합니다.")
    print("Generates foundational data for validating model performance, like the ordination of priests.")

    try:
        generator = OrdinationDataGenerator()
        data = generator.generate_ordination_data()
        print("\n✅ 위임식 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 위임식 데이터 생성 중 오류 발생: {e}")
        return None

def run_data_sampling(df):
    """데이터 샘플링 섹션 실행"""
    print("\n📊 === 데이터 샘플링 ===")
    print("전체 데이터셋에서 대표성 있는 샘플을 추출하여 효율적인 분석을 수행합니다.")
    print("Extracts representative samples from the entire dataset for efficient analysis.")

    if df is None:
        print("⚠️ 데이터가 없어 데이터 샘플링을 건너뜁니다.")
        return None

    try:
        sampler = DataSampler(df)
        sampled_df = sampler.perform_sampling()
        print("\n✅ 데이터 샘플링 적용 완료 (일부):")
        print(sampled_df.head())
        return sampled_df
    except Exception as e:
        print(f"❌ 데이터 샘플링 중 오류 발생: {e}")
        return None

def run_train_test_split(df):
    """훈련/테스트 데이터 분할 섹션 실행"""
    print("\n✂️ === 훈련/테스트 데이터 분할 ===")
    print("모델 학습과 평가를 위해 데이터를 훈련 세트와 테스트 세트로 분할합니다.")
    print("Splits data into training and testing sets for model learning and evaluation.")

    if df is None:
        print("⚠️ 데이터가 없어 훈련/테스트 데이터 분할을 건너뜁니다.")
        return None

    try:
        splitter = TrainTestSplitter(df)
        train_df, test_df = splitter.split_data()
        print("\n✅ 훈련/테스트 데이터 분할 완료:")
        print(f"훈련 세트 크기: {len(train_df)}, 테스트 세트 크기: {len(test_df)}")
        print("훈련 세트 (일부):")
        print(train_df.head())
        return train_df, test_df
    except Exception as e:
        print(f"❌ 훈련/테스트 데이터 분할 중 오류 발생: {e}")
        return None, None

def run_reproducible_split(df):
    """재현 가능한 데이터 분할 섹션 실행"""
    print("\n🌱 === 재현 가능한 데이터 분할 ===")
    print("동일한 결과를 얻기 위해 시드(seed)를 설정하여 데이터 분할의 재현성을 확보합니다.")
    print("Ensures reproducibility of data splitting by setting a seed to obtain consistent results.")

    if df is None:
        print("⚠️ 데이터가 없어 재현 가능한 데이터 분할을 건너뜁니다.")
        return None, None

    try:
        splitter = ReproducibleSplitter(df)
        train_df, test_df = splitter.split_data_reproducibly()
        print("\n✅ 재현 가능한 데이터 분할 완료:")
        print(f"훈련 세트 크기: {len(train_df)}, 테스트 세트 크기: {len(test_df)}")
        print("훈련 세트 (일부):")
        print(train_df.head())
        return train_df, test_df
    except Exception as e:
        print(f"❌ 재현 가능한 데이터 분할 중 오류 발생: {e}")
        return None, None

def show_blending_insights(original_df, sampled_df, train_df, test_df):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 데이터 샘플링 및 분할 = 모델 검증의 기초와 신뢰성",
        "🙏 제사장 위임식 = 직분 수행을 위한 준비와 거룩한 분리",
        "🛡️ 요한복음 17:17-19 = 세상으로부터 구별된 제자들을 위한 예수님의 기도",
        "💡 재현 가능한 데이터 세팅 = 모델의 신뢰성과 영적 진리의 불변성"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and sampled_df is not None and train_df is not None and test_df is not None:
        print("✨ 제사장 위임식이 거룩한 직분을 위한 준비이듯, 테스트 데이터 세팅은 모델의 신뢰성을 위한 필수 과정입니다.")
        print("✨ 예수님께서 제자들을 세상으로부터 구별하여 기도하셨듯, 데이터 분할은 모델의 객관적인 평가를 가능하게 합니다.")
    else:
        print("🙏 위임식처럼 견고하고 재현 가능한 데이터 세팅을 통해, 모델의 신뢰성을 확보하고 영적 진리를 탐구하는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
 === Chapter 30 미리보기 (Preview) ===

"분향단과 계수 - 시간·주기 데이터"

분향단에서 향이 끊이지 않고 피어 오르듯, 시간과 주기를 가지는 데이터는 연속적인 흐름 속에서 중요한 패턴과 통찰을 제공합니다.
`date_range`, `period`, 시계열 주기 변환과 같은 도구는 시간 기반 데이터의 분석과 모델링에 필수적입니다.

Just as incense continuously rises from the altar of incense, time-series and periodic data provide important patterns and insights within a continuous flow.
Tools like `date_range`, `period`, and time-series frequency conversion are essential for analyzing and modeling time-based data.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 시계열 데이터 생성 및 관리
🔍 주기성 분석 및 변환
🎯 시간 기반 데이터의 패턴 탐색
📊 분향단처럼 끊임없이 피어나는 시간 데이터의 통찰

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 30:1-10)
"예수께서 성전에 들어가사 성전 안에서 매매하는 자들을 내어쫓으시며 돈 바꾸는 자들의 상과 비둘기 파는 자들의 의자를 둘러 엎으시고" (요한복음 2:13-17)
    """
    print(preview)

def run_chapter29(interactive: bool = True):
    """Chapter 29 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 29을 시작합니다!")
        print("이 챕터에서는 데이터 샘플링과 훈련/테스트 데이터 분할 기법을 배우고, 제사장 위임식과 예수님의 제자들을 위한 기도를 탐구합니다.")
        print("This chapter introduces data sampling and train/test data splitting techniques, exploring the ordination of priests and Jesus' prayer for His disciples.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '29',
        'title': '위임식 - 테스트 데이터 세팅',
        'original_data': None,
        'sampled_data': None,
        'train_data': None,
        'test_data': None
    }

    # 1. 위임식 데이터 생성
    original_df = run_ordination_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 데이터 샘플링을 시작하려면 Enter를 눌러주세요... (Press Enter to start data sampling...)")

    # 2. 데이터 샘플링
    sampled_df = run_data_sampling(original_df)
    results['sampled_data'] = sampled_df

    if interactive:
        input("\n▶️ 훈련/테스트 데이터 분할을 시작하려면 Enter를 눌러주세요... (Press Enter to start train/test data splitting...)")

    # 3. 훈련/테스트 데이터 분할
    train_df, test_df = run_train_test_split(original_df) # 원본 데이터에 분할 적용
    results['train_data'] = train_df
    results['test_data'] = test_df

    if interactive:
        input("\n▶️ 재현 가능한 데이터 분할을 시작하려면 Enter를 눌러주세요... (Press Enter to start reproducible data splitting...)")

    # 4. 재현 가능한 데이터 분할
    reproducible_train_df, reproducible_test_df = run_reproducible_split(original_df) # 원본 데이터에 재현 가능한 분할 적용
    # 이 결과는 별도로 저장하거나, 위의 train_data/test_data를 덮어쓸 수 있음
    # 여기서는 단순히 실행만 하고 결과는 위에서 저장된 것을 사용

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, sampled_df, train_df, test_df)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 제사장 위임식처럼 견고하고 재현 가능한 데이터 세팅을 통해 모델의 신뢰성을 확보하게 하소서.
예수님께서 제자들을 위해 기도하셨듯, 데이터 분석 과정에서 공정하고 객관적인 평가를 위한 지혜를 주소서.
예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 29 완료! 스물아홉 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 29 Complete! You have finished the twenty-ninth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter29(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch29_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_sampled_data': results['sampled_data'] is not None,
                'has_train_data': results['train_data'] is not None,
                'has_test_data': results['test_data'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 29 시작! (Starting JesusBornd Pandas Chapter 29!)\n")
    main()
