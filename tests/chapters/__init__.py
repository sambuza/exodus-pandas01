"""
챕터별 테스트 패키지
"말씀을 옳게 분별하는" (딤후 2:15) 각 챕터의 정확성 검증

각 챕터의 기능적/영적/성경적 정확성을 검증하는 테스트들을 포함합니다.
"""

import pytest
from pathlib import Path
import sys

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

__version__ = "1.0.0"
__test_category__ = "Chapter Tests"

# 테스트 가능한 챕터들
TESTABLE_CHAPTERS = [1]  # 현재 Chapter 01만 테스트 가능

# 챕터별 테스트 정보
CHAPTER_TEST_INFO = {
    1: {
        "test_file": "test_ch01.py",
        "test_classes": [
            "TestTwelveTribesAnalyzer",
            "TestJohnChapter1Analyzer",
            "TestPersonalSpiritualDNA",
            "TestChapterVisualizations",
            "TestChapterIntegration"
        ],
        "test_count": 25,  # 대략적인 테스트 수
        "categories": ["출애굽기 분석", "요한복음 분석", "개인 분석", "시각화", "통합"],
        "status": "완료"
    },
    2: {
        "test_file": "test_ch02.py",
        "test_classes": ["TestMosesAnalyzer", "TestCSVRescue"],
        "test_count": 20,
        "categories": ["CSV 처리", "모세 분석"],
        "status": "계획됨"
    }
    # ... 나머지 챕터들
}

def list_chapter_tests():
    """챕터별 테스트 목록 출력"""
    print("🧪 === 챕터별 테스트 목록 ===\n")

    for ch_num in sorted(CHAPTER_TEST_INFO.keys()):
        info = CHAPTER_TEST_INFO[ch_num]
        status_emoji = "✅" if ch_num in TESTABLE_CHAPTERS else "📋"

        print(f"{status_emoji} Chapter {ch_num:02d} 테스트")
        print(f"   📄 파일: {info['test_file']}")
        print(f"   🔍 테스트 클래스: {len(info['test_classes'])}개")
        print(f"   📊 예상 테스트 수: {info['test_count']}개")
        print(f"   📂 카테고리: {', '.join(info['categories'])}")
        print(f"   📈 상태: {info['status']}\n")

def run_chapter_test(chapter_num: int, verbose: bool = True):
    """특정 챕터 테스트 실행"""
    if chapter_num not in TESTABLE_CHAPTERS:
        available = ', '.join(map(str, TESTABLE_CHAPTERS))
        raise ValueError(f"Chapter {chapter_num:02d} 테스트가 구현되지 않았습니다. 가능한 챕터: {available}")

    test_file = Path(__file__).parent / f"test_ch{chapter_num:02d}.py"

    if not test_file.exists():
        raise FileNotFoundError(f"테스트 파일 {test_file.name}이 존재하지 않습니다.")

    # pytest 실행
    args = [str(test_file)]
    if verbose:
        args.append("-v")

    return pytest.main(args)

def run_all_chapter_tests(verbose: bool = True):
    """모든 구현된 챕터 테스트 실행"""
    print("🚀 === 모든 챕터 테스트 실행 ===\n")

    results = {}
    for chapter_num in TESTABLE_CHAPTERS:
        print(f"🔍 Chapter {chapter_num:02d} 테스트 시작...")

        try:
            result = run_chapter_test(chapter_num, verbose)
            results[chapter_num] = "성공" if result == 0 else "실패"
            print(f"{'✅' if result == 0 else '❌'} Chapter {chapter_num:02d}: {results[chapter_num]}\n")
        except Exception as e:
            results[chapter_num] = f"오류: {e}"
            print(f"💥 Chapter {chapter_num:02d}: {results[chapter_num]}\n")

    # 결과 요약
    print("📋 === 테스트 결과 요약 ===")
    for ch_num, result in results.items():
        status_emoji = "✅" if result == "성공" else "❌"
        print(f"  {status_emoji} Chapter {ch_num:02d}: {result}")

    success_count = sum(1 for result in results.values() if result == "성공")
    total_count = len(results)
    print(f"\n🎯 총 결과: {success_count}/{total_count} 챕터 테스트 통과")

    return results

# 빠른 테스트 함수들
def test_ch01(verbose: bool = True):
    """Chapter 01 테스트 빠른 실행"""
    return run_chapter_test(1, verbose)

def test_integration():
    """통합 테스트만 실행"""
    test_file = Path(__file__).parent / "integration"
    if test_file.exists():
        return pytest.main([str(test_file), "-v", "-m", "integration"])
    else:
        print("⚠️ 통합 테스트 폴더가 아직 구현되지 않았습니다.")
        return 1

# 테스트 통계 정보
def test_statistics():
    """테스트 통계 출력"""
    total_tests = sum(info['test_count'] for info in CHAPTER_TEST_INFO.values())
    implemented_tests = sum(info['test_count'] for ch_num, info in CHAPTER_TEST_INFO.items()
                          if ch_num in TESTABLE_CHAPTERS)

    print("📊 === 테스트 통계 ===")
    print(f"   전체 계획된 테스트: {total_tests}개")
    print(f"   구현된 테스트: {implemented_tests}개")
    print(f"   구현률: {implemented_tests/total_tests*100:.1f}%")
    print(f"   테스트 가능한 챕터: {len(TESTABLE_CHAPTERS)}개")
    print(f"   계획된 챕터: {len(CHAPTER_TEST_INFO)}개")

if __name__ == "__main__":
    test_statistics()
    print("\n")
    list_chapter_tests()