"""
통합 테스트 패키지
"모든 것을 합력하여 선을 이루시는" (롬 8:28) 전체 시스템 통합 검증

여러 챕터가 함께 동작하는지, 전체 파이프라인이 올바르게 작동하는지,
그리고 시리즈 전체의 일관성을 검증하는 테스트들을 포함합니다.
"""

import pytest
from pathlib import Path
import sys
import time
from typing import Dict, List, Any

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

__version__ = "1.0.0"
__test_category__ = "Integration Tests"

# 통합 테스트 카테고리
INTEGRATION_CATEGORIES = {
    "pipeline": {
        "name": "전체 파이프라인 테스트",
        "description": "데이터 로드 → 분석 → 시각화 → 저장의 전체 흐름",
        "status": "계획됨"
    },
    "cross_chapter": {
        "name": "챕터 간 연동 테스트",
        "description": "여러 챕터의 결과가 일관성 있게 연결되는지 확인",
        "status": "계획됨"
    },
    "biblical_consistency": {
        "name": "성경적 일관성 테스트",
        "description": "모든 챕터의 성경 해석과 적용이 일관된 신학을 유지하는지",
        "status": "계획됨"
    },
    "performance": {
        "name": "전체 성능 테스트",
        "description": "시리즈 전체를 연속 실행했을 때의 성능과 메모리 사용량",
        "status": "계획됨"
    },
    "data_lineage": {
        "name": "데이터 계보 테스트",
        "description": "챕터 간 데이터 흐름과 변환 과정의 정확성",
        "status": "계획됨"
    }
}

# 통합 테스트 시나리오
INTEGRATION_SCENARIOS = {
    "complete_journey": {
        "name": "완전한 40일 여정 시뮬레이션",
        "chapters": list(range(1, 41)),  # Chapter 1-40
        "expected_duration": 1800,  # 30분
        "memory_limit_mb": 1000,
        "status": "계획됨"
    },
    "weekly_sections": {
        "name": "주차별 섹션 통합 테스트",
        "chapters": [
            list(range(1, 11)),  # 1주차: 1-10장
            list(range(11, 21)),  # 2주차: 11-20장
            list(range(21, 31)),  # 3주차: 21-30장
            list(range(31, 41))  # 4주차: 31-40장
        ],
        "expected_duration": 450,  # 7.5분/주
        "status": "계획됨"
    },
    "core_concepts": {
        "name": "핵심 개념 통합 검증",
        "focus": ["DataFrame 생성", "데이터 정제", "시각화", "분석", "저장"],
        "chapters": [1, 5, 10, 15, 20, 25, 30, 35, 40],  # 핵심 챕터들
        "status": "부분 구현"
    }
}


def list_integration_categories():
    """통합 테스트 카테고리 목록 출력"""
    print("🔗 === 통합 테스트 카테고리 ===\n")

    for category_id, info in INTEGRATION_CATEGORIES.items():
        status_emoji = "✅" if info['status'] == "완료" else "📋" if info['status'] == "계획됨" else "🚧"

        print(f"{status_emoji} {info['name']}")
        print(f"   📝 설명: {info['description']}")
        print(f"   📊 상태: {info['status']}\n")


def list_integration_scenarios():
    """통합 테스트 시나리오 목록 출력"""
    print("🎬 === 통합 테스트 시나리오 ===\n")

    for scenario_id, info in INTEGRATION_SCENARIOS.items():
        status_emoji = "✅" if info['status'] == "완료" else "📋" if info['status'] == "계획됨" else "🚧"

        print(f"{status_emoji} {info['name']}")
        if 'chapters' in info:
            if isinstance(info['chapters'][0], list):
                chapter_count = sum(len(week) for week in info['chapters'])
                print(f"   📚 챕터: {len(info['chapters'])}주차, 총 {chapter_count}개 챕터")
            else:
                print(f"   📚 챕터: {len(info['chapters'])}개 ({min(info['chapters'])}-{max(info['chapters'])})")
        if 'expected_duration' in info:
            duration_min = info['expected_duration'] // 60
            print(f"   ⏱️ 예상 시간: {duration_min}분")
        if 'memory_limit_mb' in info:
            print(f"   💾 메모리 한계: {info['memory_limit_mb']}MB")
        print(f"   📊 상태: {info['status']}\n")


class IntegrationTestRunner:
    """통합 테스트 실행기"""

    def __init__(self):
        self.results = {}
        self.start_time = None
        self.memory_usage = []

    def run_pipeline_test(self) -> Dict[str, Any]:
        """전체 파이프라인 통합 테스트"""
        print("🔄 전체 파이프라인 통합 테스트 시작...")

        # 미래 구현: 데이터 로드 → 분석 → 시각화 → 저장
        # 현재는 Chapter 01만으로 파이프라인 테스트

        try:
            from chapters.ch01.__main__ import run_chapter01

            self.start_time = time.time()
            results = run_chapter01(interactive=False, user_name="통합테스트")
            duration = time.time() - self.start_time

            success = all([
                results is not None,
                results.get('exodus_analysis') is not None,
                results.get('john_analysis') is not None,
                results.get('personal_analysis') is not None
            ])

            return {
                'success': success,
                'duration': duration,
                'results': results,
                'message': "파이프라인 테스트 완료" if success else "일부 분석 실패"
            }

        except Exception as e:
            return {
                'success': False,
                'duration': time.time() - self.start_time if self.start_time else 0,
                'error': str(e),
                'message': f"파이프라인 테스트 실패: {e}"
            }

    def run_cross_chapter_test(self, chapters: List[int]) -> Dict[str, Any]:
        """챕터 간 연동 테스트"""
        print(f"🔗 챕터 간 연동 테스트 시작 (챕터 {chapters})...")

        # 미래 구현: 여러 챕터 결과의 일관성 검증
        # 현재는 Chapter 01만 있으므로 단일 챕터 테스트

        if 1 in chapters:
            return self.run_pipeline_test()
        else:
            return {
                'success': False,
                'message': f"챕터 {chapters}는 아직 구현되지 않았습니다."
            }

    def run_performance_test(self, scenario: str) -> Dict[str, Any]:
        """성능 통합 테스트"""
        print(f"⚡ 성능 통합 테스트 시작 ({scenario})...")

        scenario_info = INTEGRATION_SCENARIOS.get(scenario)
        if not scenario_info:
            return {
                'success': False,
                'message': f"시나리오 '{scenario}'를 찾을 수 없습니다."
            }

        # 현재는 Chapter 01만으로 성능 테스트
        try:
            import psutil
            import os

            process = psutil.Process(os.getpid())
            initial_memory = process.memory_info().rss / 1024 / 1024  # MB

            start_time = time.time()

            # 실제 테스트 실행
            pipeline_result = self.run_pipeline_test()

            end_time = time.time()
            final_memory = process.memory_info().rss / 1024 / 1024  # MB

            duration = end_time - start_time
            memory_used = final_memory - initial_memory

            # 성능 기준 확인
            duration_ok = duration < scenario_info.get('expected_duration', 300)  # 기본 5분
            memory_ok = final_memory < scenario_info.get('memory_limit_mb', 500)  # 기본 500MB

            return {
                'success': pipeline_result['success'] and duration_ok and memory_ok,
                'duration': duration,
                'memory_used_mb': memory_used,
                'total_memory_mb': final_memory,
                'performance_ok': duration_ok and memory_ok,
                'message': f"성능 테스트 {'통과' if duration_ok and memory_ok else '실패'}"
            }

        except ImportError:
            return {
                'success': False,
                'message': "psutil 패키지가 필요합니다: pip install psutil"
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': f"성능 테스트 실패: {e}"
            }


def run_integration_test(category: str = "pipeline") -> Dict[str, Any]:
    """통합 테스트 실행"""
    runner = IntegrationTestRunner()

    if category == "pipeline":
        return runner.run_pipeline_test()
    elif category == "cross_chapter":
        return runner.run_cross_chapter_test([1])  # 현재는 Chapter 1만
    elif category == "performance":
        return runner.run_performance_test("core_concepts")
    else:
        return {
            'success': False,
            'message': f"알 수 없는 테스트 카테고리: {category}"
        }


def run_all_integration_tests() -> Dict[str, Dict[str, Any]]:
    """모든 통합 테스트 실행"""
    print("🚀 === 모든 통합 테스트 실행 ===\n")

    results = {}

    # 현재 구현된 테스트들만 실행
    available_tests = ["pipeline", "cross_chapter", "performance"]

    for test_category in available_tests:
        print(f"🔍 {test_category} 테스트 실행 중...")

        try:
            result = run_integration_test(test_category)
            results[test_category] = result

            status = "✅ 성공" if result['success'] else "❌ 실패"
            print(f"   {status}: {result.get('message', '완료')}")

        except Exception as e:
            results[test_category] = {
                'success': False,
                'error': str(e),
                'message': f"테스트 실행 중 예외: {e}"
            }
            print(f"   💥 예외: {e}")

        print()

    # 결과 요약
    success_count = sum(1 for result in results.values() if result['success'])
    total_count = len(results)

    print("📋 === 통합 테스트 결과 요약 ===")
    for category, result in results.items():
        status = "✅" if result['success'] else "❌"
        print(f"  {status} {category}: {result.get('message', '완료')}")

    print(f"\n🎯 총 결과: {success_count}/{total_count} 통합 테스트 통과")

    return results


if __name__ == "__main__":
    print("🔗 === 통합 테스트 패키지 정보 ===\n")
    list_integration_categories()
    print()
    list_integration_scenarios()