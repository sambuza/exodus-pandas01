import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd
import numpy as np
import os

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch24.covenant_data import CovenantDataGenerator
from chapters.ch24.data_snapshotter import DataSnapshotter
from chapters.ch24.version_tracker import VersionTracker
from chapters.ch24.checkpoint_saver import CheckpointSaver

def print_chapter_header():
    """챕터 헤더 출력"""
    header = """
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║             Chapter 24: 피의 언약 - 스냅샷과 버전                    ║
║                                                                      ║
║    "모세가 피를 가지고 백성에게 뿌리며 이르되 이는 여호와께서 이 모든 말씀에 대하여 너희와 세우신 언약의 피니라" (출애굽기 24:8) 
║    "예수께서 신 포도주를 받으시고 이르시되 다 이루었다 하시고 머리를 숙이니 영혼이 떠나가시니라" (요한복음 19:30) 
║                                                                      ║
║      출애굽기 24장: 피의 언약                                        ║
║      요한복음 19:30: 예수님의 "다 이루었다"                           ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    print(header)

def run_covenant_data_generation():
    """피의 언약 데이터 생성 섹션 실행"""
    print("\n📜 === 피의 언약 데이터 생성 ===")
    print("데이터 스냅샷 및 버전 관리에 사용될 언약 관련 데이터를 생성합니다.")
    print("Generates covenant-related data for data snapshotting and version control.")

    try:
        generator = CovenantDataGenerator()
        data = generator.generate_covenant_data()
        print("\n✅ 피의 언약 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 피의 언약 데이터 생성 중 오류 발생: {e}")
        return None

def run_data_snapshotting(df):
    """데이터 스냅샷 섹션 실행"""
    print("\n📸 === 데이터 스냅샷 ===")
    print("데이터의 특정 시점 상태를 스냅샷으로 기록하여 무결성과 재현성을 보장합니다.")
    print("Records the state of data at specific points in time as snapshots to ensure integrity and reproducibility.")

    if df is None:
        print("⚠️ 데이터가 없어 데이터 스냅샷을 건너뜁니다.")
        return None

    try:
        snapshotter = DataSnapshotter(df)
        snapshot_initial = snapshotter.create_snapshot("initial_covenant_state")
        print("\n✅ 초기 언약 상태 스냅샷 생성 완료 (일부):")
        print(snapshot_initial.head())
        return snapshot_initial
    except Exception as e:
        print(f"❌ 데이터 스냅샷 중 오류 발생: {e}")
        return None

def run_version_tracking(df):
    """버전 추적 섹션 실행"""
    print("\n🔄 === 버전 추적 ===")
    print("데이터에 'version' 컬럼을 추가하고 변경 이력을 추적하여 데이터의 진화를 이해합니다.")
    print("Adds a 'version' column to data and tracks change history to understand data evolution.")

    if df is None:
        print("⚠️ 데이터가 없어 버전 추적을 건너뜁니다.")
        return None

    try:
        tracker = VersionTracker(df)
        # 데이터 변경 시뮬레이션
        modified_df = df.copy()
        modified_df.loc[modified_df['event_type'] == 'Disobedience', 'obedience_score'] = 1 # 불순종 시 점수 하락
        updated_df = tracker.update_version(modified_df, "Disobedience event recorded")
        print("\n✅ 데이터 버전 추적 및 업데이트 완료 (일부):")
        print(updated_df.head())
        return updated_df
    except Exception as e:
        print(f"❌ 버전 추적 중 오류 발생: {e}")
        return None

def run_checkpoint_saving(df):
    """체크포인트 저장 섹션 실행"""
    print("\n💾 === 체크포인트 저장 ===")
    print("데이터를 CSV 또는 Parquet 파일로 저장하여 분석의 재현성을 확보합니다.")
    print("Saves data to CSV or Parquet files as checkpoints to ensure reproducibility of analysis.")

    if df is None:
        print("⚠️ 데이터가 없어 체크포인트 저장을 건너뜁니다.")
        return None

    try:
        saver = CheckpointSaver(df)
        csv_path = saver.save_checkpoint("ch24_covenant_checkpoint.csv", file_format='csv')
        parquet_path = saver.save_checkpoint("ch24_covenant_checkpoint.parquet", file_format='parquet')
        
        # 저장된 파일 불러오기 시연
        loaded_csv = saver.load_checkpoint("ch24_covenant_checkpoint.csv", file_format='csv')
        print("\n✅ CSV 체크포인트 불러오기 완료 (일부):")
        print(loaded_csv.head())
        
        # 생성된 파일 삭제 (정리)
        if os.path.exists(csv_path):
            os.remove(csv_path)
        if os.path.exists(parquet_path):
            os.remove(parquet_path)

        return {'csv_path': csv_path, 'parquet_path': parquet_path}
    except Exception as e:
        print(f"❌ 체크포인트 저장 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, snapshot_df, versioned_df, checkpoint_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 데이터 스냅샷과 버전 = 하나님의 변치 않는 약속과 구원의 확실성",
        "📜 피의 언약 = 중요한 순간의 기록과 언약의 무결성",
        "✝️ 예수님의 '다 이루었다' = 구원의 완성된 버전과 영원한 진리",
        "💡 데이터 재현성 = 영적 진리의 불변성과 신뢰성"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and snapshot_df is not None and versioned_df is not None and checkpoint_results is not None:
        initial_records = len(original_df)
        versioned_records = len(versioned_df)
        
        print(f"✨ 피의 언약처럼 견고한 데이터 관리 전략을 통해 {initial_records}개의 초기 데이터를 스냅샷하고 {versioned_records}개의 버전으로 추적했습니다.")
        print("✨ 예수님의 '다 이루었다'는 선언처럼, 데이터의 무결성과 재현성을 확보하여 영원한 진리를 탐구합니다.")
    else:
        print("🙏 피의 언약처럼 견고하고 재현 가능한 데이터 관리 전략을 통해, 영원한 진리 속에서 우리의 삶을 세우는 지혜를 구하세요.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = """
🌟 === Chapter 25 미리보기 (Preview) ===

"성막 설계 - 스키마 설계와 메타데이터 (Tabernacle Design - Schema Design and Metadata)"

성막이 하나님의 세밀한 지시와 설계도에 따라 지어졌듯이, 데이터 분석에서도 데이터의 구조(스키마)를 명확히 정의하고, 데이터에 대한 정보(메타데이터)를 관리하는 것은 데이터의 이해와 활용도를 높이는 데 필수적입니다.

Just as the Tabernacle was built according to God's detailed instructions and blueprint, in data analysis, clearly defining the data structure (schema) and managing information about the data (metadata) is essential for enhancing data understanding and usability.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 데이터 스키마 정의 및 검증
🔍 메타데이터 컬럼 추가 및 관리
🎯 `df.info()`를 이용한 데이터프레임 정보 확인
📊 성막 설계처럼 정교하고 체계적인 데이터 스키마와 메타데이터 관리 전략

"무릇 내가 네게 보이는 대로 장막의 식양과 그 기구의 식양을 따라 지을지니라" (출애굽기 25:9)
"말씀이 육신이 되어 우리 가운데 거하시매 우리가 그의 영광을 보니 아버지의 독생자의 영광이요 은혜와 진리가 충만하더라" (요한복음 1:14)
    """
    print(preview)

def run_chapter24(interactive: bool = True):
    """Chapter 24 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 24을 시작합니다!")
        print("이 챕터에서는 데이터 스냅샷과 버전 관리 기법을 배우고, 피의 언약과 예수님의 '다 이루었다'는 선언을 탐구합니다.")
        print("This chapter introduces data snapshotting and version control techniques, exploring the covenant of blood and Jesus' 'It is finished' declaration.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '24',
        'title': '피의 언약 - 스냅샷과 버전',
        'original_data': None,
        'snapshot_data': None,
        'versioned_data': None,
        'checkpoint_results': None
    }

    # 1. 피의 언약 데이터 생성
    original_df = run_covenant_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 데이터 스냅샷을 시작하려면 Enter를 눌러주세요... (Press Enter to start data snapshotting...)")

    # 2. 데이터 스냅샷
    snapshot_df = run_data_snapshotting(original_df)
    results['snapshot_data'] = snapshot_df

    if interactive:
        input("\n▶️ 버전 추적을 시작하려면 Enter를 눌러주세요... (Press Enter to start version tracking...)")

    # 3. 버전 추적
    versioned_df = run_version_tracking(original_df) # 원본 데이터에 버전 추적 적용
    results['versioned_data'] = versioned_df

    if interactive:
        input("\n▶️ 체크포인트 저장을 시작하려면 Enter를 눌러주세요... (Press Enter to start checkpoint saving...)")

    # 4. 체크포인트 저장
    checkpoint_results = run_checkpoint_saving(versioned_df) # 버전 추적된 데이터 저장
    results['checkpoint_results'] = checkpoint_results

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, snapshot_df, versioned_df, checkpoint_results)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = """
"주님, 피의 언약처럼 견고하고 재현 가능한 데이터 관리 전략을 통해 주님의 변치 않는 약속과 구원의 확실성을 이해하게 하소서.
데이터 스냅샷과 버전 관리를 통해 저의 삶의 변화 이력을 주님께 아뢰고,
영원한 진리 안에서 견고한 믿음의 삶을 살게 하소서. 예수님의 이름으로 기도합니다. 아멘."
"""
    print(prayer)

    print(f"\n🎉 Chapter 24 완료! 스물네 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 24 Complete! You have finished the twenty-fourth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter24(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch24_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_snapshot_data': results['snapshot_data'] is not None,
                'has_versioned_data': results['versioned_data'] is not None,
                'has_checkpoint_results': results['checkpoint_results'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 24 시작! (Starting JesusBornd Pandas Chapter 24!)\n")
    main()