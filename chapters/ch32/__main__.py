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
from chapters.ch32.golden_calf_data import GoldenCalfDataGenerator
from chapters.ch32.change_history_tracker import ChangeHistoryTracker
from chapters.ch32.data_version_reverter import DataVersionReverter
from chapters.ch32.audit_logger import AuditLogger

def print_chapter_header():
    """챕터 헤더 출력"""
    header = (
        "╔══════════════════════════════════════════════════════════════════════╗\n"
        "║                    JesusBornd Pandas Edition                         ║\n"
        "║                                                                      ║\n"
        "║             Chapter 32: 금송아지 - 롤백과 감사 로그                    ║\n"
        "║                                                                      ║\n"
        "║    \"모세가 여호와께로 다시 나아가 여짜오되 슬프도소이다 이 백성이 자기들을 위하여 금신을 만들었사오니 큰 죄를 범하였나이다\" (출애굽기 32:31)\n"
        "║    \"예수께서 다시 그들에게 말씀하여 이르시되 나는 세상의 빛이니 나를 따르는 자는 어둠에 다니지 아니하고 생명의 빛을 얻으리라\" (요한복음 8:12)\n"
        "║                                                                      ║\n"
        "║      출애굽기 32장: 금송아지 사건                                    ║\n"
        "║      요한복음 8:12: 예수님은 세상의 빛                                 ║\n"
        "╚══════════════════════════════════════════════════════════════════════╝"
    )
    print(header)

def run_golden_calf_data_generation():
    """금송아지 데이터 생성 섹션 실행"""
    print("\n🐂 === 금송아지 데이터 생성 ===")
    print("잘못된 변경과 회복을 시뮬레이션하기 위한 금송아지 관련 데이터를 생성합니다.")
    print("Generates Golden Calf related data to simulate incorrect changes and recovery.")

    try:
        generator = GoldenCalfDataGenerator()
        data = generator.generate_golden_calf_data()
        print("\n✅ 금송아지 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 금송아지 데이터 생성 중 오류 발생: {e}")
        return None

def run_change_history_tracking(df):
    """변경 이력 추적 섹션 실행"""
    print("\n📜 === 변경 이력 추적 ===")
    print("데이터 변경 이력 컬럼을 추가하고 모든 변경 사항을 기록하여 데이터의 무결성을 유지합니다.")
    print("Maintains data integrity by adding a change history column and recording all modifications.")

    if df is None:
        print("⚠️ 데이터가 없어 변경 이력 추적을 건너뜁니다.")
        return None

    try:
        tracker = ChangeHistoryTracker(df)
        # 데이터 변경 시뮬레이션
        modified_df_v1 = df.copy()
        modified_df_v1.loc[modified_df_v1['event_type'] == 'Worship', 'obedience_score'] = 1 # 불순종
        modified_df_v1.loc[modified_df_v1['event_type'] == 'Worship', 'divine_favor'] = 0.1 # 진노
        tracker.add_change(modified_df_v1, "금송아지 숭배로 인한 데이터 변경")
        
        modified_df_v2 = modified_df_v1.copy()
        modified_df_v2.loc[modified_df_v2['event_type'] == 'Repentance', 'obedience_score'] = 9 # 회개
        modified_df_v2.loc[modified_df_v2['event_type'] == 'Repentance', 'divine_favor'] = 0.9 # 회복
        tracker.add_change(modified_df_v2, "모세의 중보와 백성의 회개")

        print("\n✅ 변경 이력 추적 완료 (최신 데이터 일부):")
        print(tracker.get_current_data().head())
        return tracker
    except Exception as e:
        print(f"❌ 변경 이력 추적 중 오류 발생: {e}")
        return None

def run_rollback_functionality(tracker):
    """롤백 기능 섹션 실행"""
    print("\n↩️ === 롤백 기능 ===")
    print("잘못된 변경 사항을 이전의 올바른 상태로 되돌려 데이터의 무결성을 회복합니다.")
    print("Restores data integrity by reverting incorrect changes to a previous correct state.")

    if tracker is None:
        print("⚠️ 변경 이력 추적기가 없어 롤백 기능을 건너뜁니다.")
        return None

    try:
        reverter = DataVersionReverter(tracker.get_history())
        rolled_back_df = reverter.revert_to_version(0) # 초기 버전으로 롤백
        print("\n✅ 초기 버전으로 롤백 완료 (일부):")
        print(rolled_back_df.head())
        return rolled_back_df
    except Exception as e:
        print(f"❌ 롤백 기능 중 오류 발생: {e}")
        return None

def run_audit_logging(tracker):
    """감사 로그 섹션 실행"""
    print("\n📝 === 감사 로그 ===")
    print("모든 데이터 변경 이력을 기록하여 투명성을 확보하고 문제 발생 시 원인을 추적합니다.")
    print("Ensures transparency and tracks the root cause of issues by recording all data change history.")

    if tracker is None:
        print("⚠️ 변경 이력 추적기가 없어 감사 로그를 건너뜁니다.")
        return None

    try:
        audit_logger = AuditLogger()
        for entry in tracker.get_history():
            audit_logger.log_action('System', 'Data_Change', entry['description'], entry['data_snapshot'].shape)
        
        print("\n✅ 감사 로그 기록 완료 (일부):")
        print(audit_logger.get_logs().head())
        return audit_logger.get_logs()
    except Exception as e:
        print(f"❌ 감사 로그 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, history_tracker, rolled_back_df, audit_logs):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 롤백과 감사 로그 = 데이터의 무결성 회복과 신뢰성 유지",
        "🐂 금송아지 사건 = 잘못된 변경과 그로 인한 하나님의 진노",
        "💡 예수님은 세상의 빛 = 어둠을 밝히고 진실을 드러내는 역할",
        "↩️ 데이터 회복 = 영적 회개와 언약의 갱신"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and history_tracker is not None and rolled_back_df is not None and audit_logs is not None:
        num_changes = len(history_tracker.get_history()) - 1 # 초기 상태 제외
        print(f"✨ 금송아지 사건처럼 {num_changes}번의 데이터 변경 이력을 추적하고, 잘못된 변경을 롤백하여 데이터의 무결성을 회복했습니다.")
        print("✨ 예수님은 세상의 빛처럼, 감사 로그를 통해 데이터의 어두운 부분을 밝히고 진실을 드러냅니다.")
    else:
        print("🙏 금송아지 사건처럼 잘못된 길에서 돌이켜 생명의 빛으로 나아가게 하시고, 롤백과 감사 로그를 통해 저의 삶을 정결하게 하소서.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = (
        "🌟 === Chapter 33 미리보기 (Preview) ===\n\n"
        "\"다시 만난 은혜 - 결합 충돌 해소 (Grace Reunited - Resolving Join Conflicts)\"\n\n"
        "이스라엘 백성이 금송아지 사건 이후 하나님의 진노를 샀지만, 모세의 중보로 다시 하나님의 은혜를 입고 언약을 갱신했듯이, 데이터 분석에서도 여러 데이터셋을 결합할 때 발생하는 '결합 충돌(Join Conflicts)'을 지혜롭게 해소하는 것은 데이터의 무결성을 유지하고 정확한 분석 결과를 얻는 데 필수적입니다.\n\n"
        "Just as the Israelites, after the Golden Calf incident, incurred God's wrath but were reunited with His grace and renewed the covenant through Moses' intercession, in data analysis, wisely resolving 'join conflicts' that arise when combining multiple datasets is essential for maintaining data integrity and obtaining accurate analytical results.\n\n"
        "다음 장에서 배울 내용 (What you'll learn in the next chapter):\n"
        "📁 `merge()`의 `indicator` 파라미터를 이용한 결합 출처 확인\n"
        "🔍 `validate` 파라미터를 이용한 결합 유효성 검사\n"
        "🎯 `suffixes` 파라미터를 이용한 컬럼 이름 충돌 해결\n"
        "📊 다시 만난 은혜처럼 데이터 결합 충돌을 해소하고 데이터의 무결성을 회복하는 전략\n\n"
        "\"여호와께서 모세에게 이르시되 내가 너와 함께 가리라 내가 너를 안위하리라\" (출애굽기 33:14)\n"
        "\"예수께서 이르시되 시몬 베드로야 네가 나를 사랑하느냐 하시니 베드로가 이르되 주님 그러하나이다 내가 주님을 사랑하는 줄 주님께서 아시나이다\" (요한복음 21:15)"
    )
    print(preview)

def run_chapter32(interactive: bool = True):
    """Chapter 32 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 32을 시작합니다!")
        print("이 챕터에서는 데이터 롤백과 감사 로그 기법을 배우고, 금송아지 사건과 예수님은 세상의 빛이라는 말씀을 탐구합니다.")
        print("This chapter introduces data rollback and audit log techniques, exploring the Golden Calf incident and Jesus' declaration as the Light of the World.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '32',
        'title': '금송아지 - 롤백과 감사 로그',
        'original_data': None,
        'history_tracker': None,
        'rolled_back_data': None,
        'audit_logs': None
    }

    # 1. 금송아지 데이터 생성
    original_df = run_golden_calf_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ 변경 이력 추적을 시작하려면 Enter를 눌러주세요... (Press Enter to start change history tracking...)")

    # 2. 변경 이력 추적
    history_tracker = run_change_history_tracking(original_df)
    results['history_tracker'] = history_tracker

    if interactive:
        input("\n▶️ 롤백 기능을 시작하려면 Enter를 눌러주세요... (Press Enter to start rollback functionality...)")

    # 3. 롤백 기능
    rolled_back_df = run_rollback_functionality(history_tracker) # 변경 이력 추적된 데이터에 롤백 적용
    results['rolled_back_data'] = rolled_back_df

    if interactive:
        input("\n▶️ 감사 로그를 시작하려면 Enter를 눌러주세요... (Press Enter to start audit logging...)")

    # 4. 감사 로그
    audit_logs = run_audit_logging(history_tracker) # 변경 이력 추적된 데이터로 감사 로그 생성
    results['audit_logs'] = audit_logs

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, history_tracker, rolled_back_df, audit_logs)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = (
        "\"주님, 금송아지 사건처럼 잘못된 길에서 돌이켜 생명의 빛으로 나아가게 하시고, 롤백과 감사 로그를 통해 저의 삶을 정결하게 하소서.\n"
        "데이터의 무결성과 신뢰성을 유지하며, 주님의 빛 가운데서 진실을 드러내는 분석가가 되게 하소서. 예수님의 이름으로 기도합니다. 아멘.\""
    )
    print(prayer)

    print(f"\n🎉 Chapter 32 완료! 서른두 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 32 Complete! You have finished the thirty-second wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter32(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch32_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_history_tracker': results['history_tracker'] is not None,
                'has_rolled_back_data': results['rolled_back_data'] is not None,
                'has_audit_logs': results['audit_logs'] is not None
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
    print("🚀 JesusBornd Pandas Chapter 32 시작! (Starting JesusBornd Pandas Chapter 32!)\n")
    main()