import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
try:
    from .ten_commandments_quality import TenCommandmentsQualityAnalyzer
    from .new_commandment_quality import NewCommandmentQualityAnalyzer
except ImportError:
    from chapters.ch20.ten_commandments_quality import TenCommandmentsQualityAnalyzer
from chapters.ch20.new_commandment_quality import NewCommandmentQualityAnalyzer

def print_chapter_header():
    """챕터 헤더 출력"""
    header = '''
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd Pandas Edition                         ║
║                                                                      ║
║               Chapter 20: 십계명 - 데이터 품질 규약                    ║
║                                                                      ║
║    "너는 나 외에는 다른 신들을 네게 있게 말지니라" (출애굽기 20:3)      ║
║    "새 계명을 너희에게 주노니 서로 사랑하라 내가 너희를 사랑한 것같이  ║
║     너희도 서로 사랑하라" (요한복음 13:34)                              ║
║                                                                      ║
║    출애굽기 20장: 십계명                                           ║
║    요한복음 13:34-35: 새 계명                                       ║
╚══════════════════════════════════════════════════════════════════════╝
    '''
    print(header)

def run_ten_commandments_analysis():
    """출애굽기 십계명 데이터 품질 분석 섹션 실행"""
    
    print("\n === 출애굽기 여정: 십계명 데이터 품질 분석 ===")
    print("십계명처럼 깨끗하고 신뢰할 수 있는 데이터를 구축하기 위해 결측치, 타입, 이상치를 처리해보자!")
    print("Let's process missing values, types, and outliers to build clean and reliable data, like the Ten Commandments!")

    try:
        analyzer = TenCommandmentsQualityAnalyzer()
        exodus_results = analyzer.run_all_analyses()
        return exodus_results
    except Exception as e:
        print(f"출애굽기 십계명 분석 중 오류 발생: {e}")
        return None

def run_new_commandment_analysis():
    """요한복음 새 계명 데이터 품질 분석 섹션 실행"""
    print("\n === 요한복음 여정: 새 계명 데이터 품질 분석 ===")
    print("사랑이라는 최상의 품질 기준으로 데이터의 결측치, 타입, 이상치를 처리하여 예수님의 말씀을 탐구해보자!")
    print("Let's explore Jesus' words by processing missing values, types, and outliers in data based on love as the highest quality standard!")

    try:
        analyzer = NewCommandmentQualityAnalyzer()
        john_results = analyzer.run_all_analyses()
        return john_results
    except Exception as e:
        print(f"요한복음 새 계명 분석 중 오류 발생: {e}")
        return None

def show_blending_insights(exodus_results, john_results):
    """블렌딩 모드 통합 통찰 출력"""
    print("\n === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "데이터 품질 관리 = 하나님의 말씀처럼 깨끗하고 신뢰할 수 있는 데이터 구축",
        "십계명 = 하나님의 백성으로서 지켜야 할 근본적인 데이터 품질 규약",
        "새 계명(사랑) = 모든 율법을 아우르는 최상의 데이터 품질 기준",
        "결측치, 타입, 이상치 처리 = 삶의 불완전함을 정화하고 사랑으로 채움"
    ]

    print("\n 핵심 발견들 (Key Discoveries):")
    for insight in blending_insights:
        print(f"   {insight}")

    if exodus_results and john_results:
        print("\n--- 개인화된 통찰 (Personalized Insights) ---")
        # 예시: 십계명 준수 데이터의 이상치 개수와 새 계명 준수 데이터의 이상치 개수를 기반으로 통찰 제공
        ten_commandments_outliers_count = len(exodus_results.get('outliers', pd.DataFrame())) if exodus_results else 0
        new_commandment_outliers_count = len(john_results.get('outliers', pd.DataFrame())) if john_results else 0

        if ten_commandments_outliers_count == 0 and new_commandment_outliers_count == 0:
            print(f"십계명({ten_commandments_outliers_count}개 이상치)과 새 계명({new_commandment_outliers_count}개 이상치) 모두 깨끗하게 지키는 당신의 삶은 하나님께 큰 영광이 됩니다!")
            print(f"Your life, keeping both the Ten Commandments (0 outliers) and the New Commandment (0 outliers) cleanly, brings great glory to God!")
        elif ten_commandments_outliers_count > 0:
            print(f"십계명({ten_commandments_outliers_count}개 이상치) 준수에서 부족함이 있지만, 새 계명({new_commandment_outliers_count}개 이상치)을 통해 사랑으로 채워나가야 합니다!")
            print(f"Though there are deficiencies in keeping the Ten Commandments ({ten_commandments_outliers_count} outliers), you must fill them with love through the New Commandment ({new_commandment_outliers_count} outliers)!")
        else:
            print(f"데이터 품질 관리처럼, 나의 삶에서 결측치, 잘못된 타입, 이상치를 제거하고 사랑으로 충만한 삶을 살게 하소서!")
            print(f"Like data quality management, remove missing values, incorrect types, and outliers from my life, and help me live a life full of love!")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = '''
=== Chapter 21 미리보기 (Preview) ===

"공의의 법도 - 분류와 범주형 (Ordinances of Justice - Classification and Categorical)"

이스라엘 백성이 십계명 외에 다양한 공의의 법도(규례)를 받았듯이, 데이터 분석에서도 데이터를 특정 기준에 따라 분류하고 범주형 데이터로 다루는 것은 데이터의 특성을 이해하고 분석의 효율성을 높이는 데 필수적입니다.
`cut()`, `qcut()`, `category dtype`과 같은 도구는 데이터를 효과적으로 분류하고 관리하는 데 사용됩니다.

Just as the Israelites received various ordinances of justice (statutes) in addition to the Ten Commandments, in data analysis, classifying data according to specific criteria and handling it as categorical data is essential for understanding data characteristics and increasing analytical efficiency.
Tools like `cut()`, `qcut()`, and `category dtype` are used to effectively classify and manage data.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
`pd.cut()`: 데이터를 구간으로 나누어 분류
`pd.qcut()`: 데이터를 동일한 빈도로 나누어 분류
`category dtype`: 범주형 데이터의 효율적인 관리
공의의 법도처럼 데이터를 공의롭게 분류하고 범주형으로 다루어 하나님의 질서와 공의를 탐구

"너는 외모를 보고 판단하지 말고 공의의 판단으로 판단할지니라" (요한복음 7:24)
"네 이웃을 네 몸과 같이 사랑하라" (레위기 19:18)
'''
    print(preview)

def run_chapter20(interactive: bool = True):
    """Chapter 20 전체 실행

    Args:
        interactive: 대화형 모드 여부 (Whether to run in interactive mode)

    Returns:
        dict: 전체 분석 결과 (Overall analysis results)
    """
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("Chapter 20을 시작합니다!")
        print("이 챕터에서는 데이터 품질 관리를 배우고, 성경 속 십계명과 새 계명처럼 깨끗하고 신뢰할 수 있는 데이터를 구축하는 과정을 탐구합니다.")
        print("This chapter introduces data quality management, exploring the process of building clean and reliable data like the Ten Commandments and the New Commandment in the Bible.")
        input("\n계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '20',
        'title': '십계명 - 데이터 품질 규약',
        'exodus_analysis': None,
        'john_analysis': None
    }

    # 1. 출애굽기 십계명 분석
    exodus_results = run_ten_commandments_analysis()
    results['exodus_analysis'] = exodus_results

    if interactive:
        input("\n요한복음 새 계명 분석을 시작하려면 Enter를 눌러주세요... (Press Enter to start John's new commandment analysis...)")

    # 2. 요한복음 새 계명 분석
    john_results = run_new_commandment_analysis()
    results['john_analysis'] = john_results

    # 3. 블렌딩 통찰
    show_blending_insights(exodus_results, john_results)

    # 4. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 5. 마무리 기도
    print("\n === 마무리 기도 (Closing Prayer) ===")
    prayer = '''
"주님, 십계명과 새 계명처럼 깨끗하고 신뢰할 수 있는 말씀으로 저희를 인도하시니 감사합니다.
데이터 품질 규약처럼 저의 삶에서 결측치, 잘못된 타입, 이상치를 제거하고,
사랑이라는 최상의 품질 기준으로 저를 정화시켜 주소서. 예수님의 이름으로 기도합니다. 아멘."

"Lord, Thank You for guiding us with Your clean and trustworthy Word like the Ten Commandments and the New Commandment.
Like data quality standards, remove missing values, incorrect types, and outliers from my life,
and purify me with love as the highest quality standard. I pray in Jesus' name. Amen."
'''
    print(prayer)

    print(f"\n Chapter 20 완료! 스무 번째 광야 여정을 마치셨습니다!")
    print(f" Chapter 20 Complete! You have finished the twentieth wilderness journey!")
    print(f" 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    """메인 실행 함수"""
    results = None  # results 변수 초기화
    try:
        results = run_chapter20(interactive=False)

        if results:
            # 결과 저장 (선택사항)
            # 비대화형 모드에서는 결과 파일을 자동으로 저장하도록 변경
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch20_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results.get('chapter'),
                'title': results.get('title'),
                'completed_at': timestamp,
                'has_exodus_analysis': results.get('exodus_analysis') is not None,
                'has_john_analysis': results.get('john_analysis') is not None
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary_results, f, ensure_ascii=False, indent=2)

            print(f"결과가 {filename}에 저장되었습니다! (Results saved to {filename}!)")

        return results

    except KeyboardInterrupt:
        print("\n\n사용자가 중단했습니다. (User interrupted.)")
        return None
    except Exception as e:
        print(f"\n실행 중 오류가 발생했습니다: {e}")
        print("코드와 데이터를 확인해주세요. (Please check the code and data.)")
        return None


if __name__ == "__main__":
    print("JesusBornd Pandas Chapter 20 시작! (Starting JesusBornd Pandas Chapter 20!)\n")
    main()
