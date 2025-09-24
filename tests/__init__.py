"""
JesusBornd 테스트 패키지
"모든 것을 시험하여 좋은 것을 취하고" (살전 5:21)

이 패키지는 다음 테스트들을 포함합니다:
- utils 모듈 테스트
- 데이터 무결성 테스트
- 챕터별 기능 테스트
- 통합 파이프라인 테스트
"""

import sys
from pathlib import Path
import subprocess
import time

# 프로젝트 루트 경로 설정
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

__version__ = "1.0.0"
__test_suite__ = "JesusBornd Pandas Edition"

# 공통 테스트 설정
TEST_DATA_PATH = PROJECT_ROOT / "data" / "examples"
TEST_CONFIG_PATH = PROJECT_ROOT / "config.yml"

# 테스트 카테고리 정보
TEST_CATEGORIES = {
    "utils": {
        "description": "유틸리티 모듈 테스트",
        "file": "test_utils.py",
        "estimated_time": 10,  # 초
        "test_count": 15
    },
    "data": {
        "description": "데이터 무결성 테스트",
        "file": "test_data_integrity.py",
        "estimated_time": 5,
        "test_count": 20
    },
    "chapters": {
        "description": "챕터별 기능 테스트",
        "file": "chapters/",
        "estimated_time": 30,
        "test_count": 25
    },
    "integration": {
        "description": "통합 테스트",
        "file": "chapters/integration/",
        "estimated_time": 60,
        "test_count": 10
    }
}


def print_test_header():
    """테스트 시작 헤더 출력"""
    header = f"""
╔══════════════════════════════════════════════════════════════════════╗
║                    JesusBornd 테스트 스위트                           ║
║                                                                      ║
║          "모든 것을 시험하여 좋은 것을 취하고" (살전 5:21)              ║
║                                                                      ║
║    🧪 프로젝트 품질과 정확성을 검증합니다                              ║
║    📊 성경적 데이터와 분석의 무결성을 확인합니다                        ║
╚══════════════════════════════════════════════════════════════════════╝
    """
    print(header)


def run_pytest_safely(args: list, description: str) -> tuple:
    """pytest를 안전하게 실행하고 결과 반환"""
    print(f"\n🔍 {description} 시작...")

    start_time = time.time()

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest"] + args,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )

        execution_time = time.time() - start_time
        success = result.returncode == 0

        if success:
            print(f"✅ {description} 성공 ({execution_time:.1f}초)")
        else:
            print(f"❌ {description} 실패 ({execution_time:.1f}초)")
            if result.stderr:
                print(f"   오류: {result.stderr[:200]}...")

        return success, execution_time, result.stdout, result.stderr

    except Exception as e:
        execution_time = time.time() - start_time
        print(f"💥 {description} 예외 발생 ({execution_time:.1f}초): {e}")
        return False, execution_time, "", str(e)


def run_all_tests() -> bool:
    """모든 테스트 실행"""
    print_test_header()

    test_plan = [
        (["tests/test_utils.py", "-v"], "유틸리티 모듈 테스트"),
        (["tests/test_data_integrity.py", "-v"], "데이터 무결성 테스트"),
        (["tests/chapters/test_ch01.py", "-v"], "Chapter 01 테스트"),
        (["tests/", "-v", "--tb=short", "-x"], "전체 통합 테스트")
    ]

    results = []
    total_time = 0

    for args, description in test_plan:
        success, exec_time, stdout, stderr = run_pytest_safely(args, description)
        results.append((description, success, exec_time))
        total_time += exec_time

    # 결과 요약
    print("\n" + "=" * 60)
    print("📋 테스트 결과 요약")
    print("=" * 60)

    passed = 0
    for description, success, exec_time in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {status} {description} ({exec_time:.1f}초)")
        if success:
            passed += 1

    print(f"\n🎯 총 결과: {passed}/{len(results)} 테스트 그룹 통과")
    print(f"⏱️ 총 실행 시간: {total_time:.1f}초")

    if passed == len(results):
        print("🎉 모든 테스트가 성공했습니다!")
        print("✨ JesusBornd 프로젝트가 정상 동작합니다!")
        return True
    else:
        print("⚠️ 일부 테스트가 실패했습니다.")
        print("🔧 실패한 부분을 확인하고 수정해주세요.")
        return False


def run_chapter_tests(chapter_num: int) -> bool:
    """특정 챕터 테스트만 실행"""
    print_test_header()
    print(f"🎯 Chapter {chapter_num:02d} 집중 테스트")

    test_file = PROJECT_ROOT / "tests" / "chapters" / f"test_ch{chapter_num:02d}.py"

    if not test_file.exists():
        print(f"❌ Chapter {chapter_num:02d} 테스트 파일이 존재하지 않습니다.")
        return False

    success, exec_time, stdout, stderr = run_pytest_safely(
        [str(test_file), "-v"],
        f"Chapter {chapter_num:02d}"
    )

    if success:
        print(f"🎉 Chapter {chapter_num:02d} 테스트 완료!")
    else:
        print(f"💥 Chapter {chapter_num:02d} 테스트 실패")
        if stderr:
            print(f"상세 오류:\n{stderr}")

    return success


def run_utils_tests() -> bool:
    """유틸리티 테스트만 실행"""
    print_test_header()
    print("🔧 유틸리티 모듈 집중 테스트")

    success, exec_time, stdout, stderr = run_pytest_safely(
        ["tests/test_utils.py", "-v"],
        "유틸리티 모듈"
    )

    return success


def run_data_tests() -> bool:
    """데이터 무결성 테스트만 실행"""
    print_test_header()
    print("📊 데이터 무결성 집중 테스트")

    success, exec_time, stdout, stderr = run_pytest_safely(
        ["tests/test_data_integrity.py", "-v"],
        "데이터 무결성"
    )

    return success


def run_fast_tests() -> bool:
    """빠른 테스트만 실행 (slow 마커 제외)"""
    print_test_header()
    print("⚡ 빠른 테스트만 실행")

    success, exec_time, stdout, stderr = run_pytest_safely(
        ["tests/", "-v", "-m", "not slow", "--tb=short"],
        "빠른 테스트"
    )

    return success


def run_integration_tests() -> bool:
    """통합 테스트만 실행"""
    print_test_header()
    print("🔗 통합 테스트 실행")

    success, exec_time, stdout, stderr = run_pytest_safely(
        ["tests/", "-v", "-m", "integration"],
        "통합 테스트"
    )

    return success


def run_visual_tests() -> bool:
    """시각화 테스트만 실행"""
    print_test_header()
    print("🎨 시각화 테스트 실행")

    success, exec_time, stdout, stderr = run_pytest_safely(
        ["tests/", "-v", "-m", "visualization"],
        "시각화 테스트"
    )

    return success


def get_test_statistics() -> dict:
    """테스트 통계 정보 반환"""
    total_estimated_time = sum(info["estimated_time"] for info in TEST_CATEGORIES.values())
    total_estimated_tests = sum(info["test_count"] for info in TEST_CATEGORIES.values())

    return {
        "categories": len(TEST_CATEGORIES),
        "estimated_tests": total_estimated_tests,
        "estimated_time_seconds": total_estimated_time,
        "estimated_time_minutes": round(total_estimated_time / 60, 1),
        "test_categories": TEST_CATEGORIES
    }


def print_test_info():
    """테스트 정보 출력"""
    stats = get_test_statistics()

    print("📊 === JesusBornd 테스트 정보 ===")
    print(f"   테스트 카테고리: {stats['categories']}개")
    print(f"   예상 테스트 수: {stats['estimated_tests']}개")
    print(f"   예상 실행 시간: {stats['estimated_time_minutes']}분")

    print(f"\n📂 테스트 카테고리:")
    for category, info in TEST_CATEGORIES.items():
        print(f"   🔹 {category}: {info['description']} ({info['test_count']}개 테스트)")

    print(f"\n🚀 실행 방법:")
    print(f"   from tests import run_all_tests")
    print(f"   run_all_tests()  # 모든 테스트")


# 환경 검증 함수
def check_test_environment() -> bool:
    """테스트 환경 검증"""
    print("🔍 테스트 환경 검증 중...")

    # Python 버전 확인
    if sys.version_info < (3, 8):
        print(f"❌ Python {sys.version_info.major}.{sys.version_info.minor}는 너무 낮습니다. Python 3.8+ 필요")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")

    # 필수 패키지 확인
    required_packages = ['pytest', 'pandas', 'numpy', 'matplotlib']
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} 누락")
            return False

    # 데이터 파일 확인
    if not TEST_DATA_PATH.exists():
        print(f"❌ 테스트 데이터 경로 없음: {TEST_DATA_PATH}")
        return False
    print(f"✅ 테스트 데이터 경로")

    # 설정 파일 확인
    if not TEST_CONFIG_PATH.exists():
        print(f"⚠️ 설정 파일 없음: {TEST_CONFIG_PATH} (선택사항)")
    else:
        print(f"✅ 설정 파일")

    print("🎉 테스트 환경 검증 완료!")
    return True


if __name__ == "__main__":
    print("🧪 JesusBornd 테스트 패키지")
    print_test_info()
    print("\n" + "=" * 50)
    print("테스트 실행 예시:")
    print("  python tests/run_tests.py           # 통합 실행기 사용")
    print("  python -c 'from tests import run_all_tests; run_all_tests()'")