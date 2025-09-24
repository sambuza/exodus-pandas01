"""
JesusBornd 통합 테스트 실행기
"모든 것을 시험하여 좋은 것을 취하고" (살전 5:21)

사용법:
    python tests/run_tests.py                    # 모든 테스트
    python tests/run_tests.py --chapter 1       # Chapter 01만
    python tests/run_tests.py --utils           # 유틸리티만
    python tests/run_tests.py --fast            # 빠른 테스트만
    python tests/run_tests.py --visual          # 시각화 테스트만
"""

import argparse
import sys
import time
from pathlib import Path
import subprocess

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

def print_header(title: str):
    """테스트 섹션 헤더 출력"""
    print("\n" + "="*60)
    print(f"🧪 {title}")
    print("="*60)

def run_pytest_command(args: list, description: str) -> bool:
    """pytest 명령 실행"""
    print(f"\n🔍 {description} 시작...")
    
    start_time = time.time()
    result = subprocess.run([sys.executable, "-m", "pytest"] + args, 
                          capture_output=False, text=True)
    execution_time = time.time() - start_time
    
    if result.returncode == 0:
        print(f"✅ {description} 완료 ({execution_time:.1f}초)")
        return True
    else:
        print(f"❌ {description} 실패 ({execution_time:.1f}초)")
        return False

def run_all_tests() -> bool:
    """모든 테스트 실행"""
    print_header("전체 테스트 스위트 실행")
    
    tests = [
        (["tests/test_utils.py", "-v"], "유틸리티 모듈 테스트"),
        (["tests/test_data_integrity.py", "-v"], "데이터 무결성 테스트"), 
        (["tests/chapters/test_ch01.py", "-v"], "Chapter 01 테스트"),
        (["tests/", "-v", "--tb=short"], "전체 통합 테스트")
    ]
    
    results = []
    for args, description in tests:
        success = run_pytest_command(args, description)
        results.append((description, success))
    
    print_summary(results)
    return all(result[1] for result in results)

def run_chapter_tests(chapter_num: int) -> bool:
    """특정 챕터 테스트"""
    print_header(f"Chapter {chapter_num:02d} 테스트")
    
    test_file = PROJECT_ROOT / "tests" / "chapters" / f"test_ch{chapter_num:02d}.py"
    
    if not test_file.exists():
        print(f"❌ Chapter {chapter_num:02d} 테스트 파일이 존재하지 않습니다.")
        return False
    
    return run_pytest_command([str(test_file), "-v"], f"Chapter {chapter_num:02d}")

def run_utils_tests() -> bool:
    """유틸리티 테스트만"""
    print_header("유틸리티 모듈 테스트")
    return run_pytest_command(["tests/test_utils.py", "-v"], "유틸리티 모듈")

def run_fast_tests() -> bool:
    """빠른 테스트만 (slow 마커 제외)"""
    print_header("빠른 테스트 (성능 테스트 제외)")
    return run_pytest_command(["tests/", "-v", "-m", "not slow"], "빠른 테스트")

def run_visual_tests() -> bool:
    """시각화 테스트만"""
    print_header("시각화 테스트")
    return run_pytest_command(["tests/", "-v", "-m", "visualization"], "시각화")

def run_integration_tests() -> bool:
    """통합 테스트만"""
    print_header("통합 테스트")
    return run_pytest_command(["tests/", "-v", "-m", "integration"], "통합 테스트")

def run_data_integrity_tests() -> bool:
    """데이터 무결성 테스트"""
    print_header("데이터 무결성 검증")
    return run_pytest_command(["tests/test_data_integrity.py", "-v"], "데이터 무결성")

def print_summary(results: list):
    """테스트 결과 요약 출력"""
    print("\n" + "="*60)
    print("📋 테스트 결과 요약")
    print("="*60)
    
    passed = 0
    for description, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {status} {description}")
        if success:
            passed += 1
    
    print(f"\n🎯 총 결과: {passed}/{len(results)} 테스트 그룹 통과")
    
    if passed == len(results):
        print("🎉 모든 테스트가 성공했습니다!")
        print("✨ JesusBornd Chapter 01이 정상 동작합니다!")
    else:
        print("⚠️ 일부 테스트가 실패했습니다.")
        print("🔧 실패한 부분을 확인하고 수정해주세요.")

def check_requirements():
    """필수 요구사항 확인"""
    print_header("환경 요구사항 확인")
    
    # Python 버전 확인
    python_version = sys.version_info
    if python_version < (3, 8):
        print(f"❌ Python 버전이 {python_version.major}.{python_version.minor}입니다. Python 3.8 이상이 필요합니다.")
        return False
    else:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # 필수 패키지 확인
    required_packages = ['pandas', 'numpy', 'matplotlib', 'pytest']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} 패키지 설치됨")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} 패키지 누락")
    
    if missing_packages:
        print(f"\n🔧 다음 명령어로 누락된 패키지를 설치하세요:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    # 데이터 파일 확인
    data_files = [
        "data/examples/ch01_tribes.csv",
        "data/examples/ch01_john_concepts.csv",
        "config.yml"
    ]
    
    missing_files = []
    for file_path in data_files:
        full_path = PROJECT_ROOT / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            missing_files.append(file_path)
            print(f"❌ {file_path} 누락")
    
    if missing_files:
        print(f"\n📁 다음 파일들을 생성해주세요:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        return False
    
    return True

def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description="JesusBornd 테스트 실행기")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="모든 테스트 실행 (기본값)")
    group.add_argument("--chapter", type=int, help="특정 챕터 테스트만 실행")
    group.add_argument("--utils", action="store_true", help="유틸리티 테스트만 실행")
    group.add_argument("--fast", action="store_true", help="빠른 테스트만 실행")
    group.add_argument("--visual", action="store_true", help="시각화 테스트만 실행")
    group.add_argument("--integration", action="store_true", help="통합 테스트만 실행")
    group.add_argument("--data", action="store_true", help="데이터 무결성 테스트만 실행")
    
    parser.add_argument("--no-check", action="store_true", help="환경 요구사항 확인 건너뛰기")
    parser.add_argument("--verbose", action="store_true", help="상세 출력")
    
    args = parser.parse_args()
    
    print("🧪 === JesusBornd 테스트 실행기 ===")
    print('"모든 것을 시험하여 좋은 것을 취하고" (살전 5:21)')
    
    # 환경 요구사항 확인
    if not args.no_check:
        if not check_requirements():
            print("\n💥 환경 요구사항을 만족하지 않습니다.")
            print("🔧 위의 지시사항을 따라 문제를 해결한 후 다시 실행해주세요.")
            return 1
    
    success = True
    
    try:
        if args.chapter:
            success = run_chapter_tests(args.chapter)
        elif args.utils:
            success = run_utils_tests()
        elif args.fast:
            success = run_fast_tests()
        elif args.visual:
            success = run_visual_tests()
        elif args.integration:
            success = run_integration_tests()
        elif args.data:
            success = run_data_integrity_tests()
        else:
            # 기본값: 모든 테스트
            success = run_all_tests()
            
    except KeyboardInterrupt:
        print("\n\n⏸️ 사용자가 테스트를 중단했습니다.")
        return 1
    except Exception as e:
        print(f"\n💥 예상치 못한 오류가 발생했습니다: {e}")
        return 1
    
    # 최종 결과
    if success:
        print("\n🎉 === 테스트 성공! ===")
        print("✨ 모든 테스트가 통과했습니다!")
        print("🚀 이제 Chapter 01을 안전하게 실행할 수 있습니다!")
        print("\n📖 다음 명령어로 Chapter 01을 시작해보세요:")
        print("   python -m chapters.ch01.main")
        return 0
    else:
        print("\n💥 === 테스트 실패! ===")
        print("⚠️ 일부 테스트가 실패했습니다.")
        print("🔧 실패한 테스트를 확인하고 문제를 해결해주세요.")
        print("\n🆘 도움말:")
        print("   - python tests/run_tests.py --utils     # 유틸리티만 테스트")
        print("   - python tests/run_tests.py --fast      # 빠른 테스트만")
        print("   - python tests/run_tests.py --chapter 1 # Chapter 01만")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)