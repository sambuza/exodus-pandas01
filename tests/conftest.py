"""
pytest 공통 설정 및 fixtures
"주 앞에서 시험을 받아 인정함을 얻으라" (딤후 2:15)
"""

import pytest
import pandas as pd
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

@pytest.fixture(scope="session")
def project_root():
    """프로젝트 루트 경로 fixture"""
    return PROJECT_ROOT

@pytest.fixture(scope="session")
def test_data_path():
    """테스트 데이터 경로 fixture"""
    return PROJECT_ROOT / "data" / "examples"

@pytest.fixture(scope="session")
def config_path():
    """설정 파일 경로 fixture"""
    return PROJECT_ROOT / "config.yml"

@pytest.fixture
def sample_tribes_data():
    """샘플 12지파 데이터 fixture"""
    return pd.DataFrame({
        'name': ['Reuben', 'Simeon', 'Levi', 'Judah'],
        'korean_name': ['르우벤', '시므온', '레위', '유다'],
        'korean_meaning': ['보라 아들이다', '들으심', '연합', '찬송'],  # 추가
        'mother': ['Leah', 'Leah', 'Leah', 'Leah'],
        'birth_order': [1, 2, 3, 4],
        'spiritual_theme': ['관계', '소통', '연합', '예배']
    })

@pytest.fixture
def sample_john_concepts():
    """샘플 요한복음 개념 데이터 fixture"""
    return pd.DataFrame({
        'concept': ['Word', 'Light', 'Darkness', 'Grace', 'Truth'],
        'korean_name': ['말씀', '빛', '어둠', '은혜', '진리'],
        'greek_transliteration': ['logos', 'phos', 'skotos', 'charis', 'aletheia'],  # 추가
        'frequency_ch1': [3, 5, 2, 2, 2],
        'theological_importance': [10, 9, 3, 9, 9]
    })

@pytest.fixture
def spiritual_journey_data():
    """샘플 개인 신앙 여정 데이터 fixture"""
    return pd.DataFrame({
        '연도': [2020, 2021, 2022, 2023, 2024],
        '핵심사건': ['첫 교회 출석', '세례받음', '소그룹 참여', '헌신 결단', '큐티 시작'],
        '성장지수': [3, 5, 7, 8, 9],
        '감사제목': ['새로운 시작', '거듭남', '소속감', '헌신', '성숙']
    })

# 테스트 마커 정의
def pytest_configure(config):
    """pytest 설정"""
    config.addinivalue_line(
        "markers", "slow: 시간이 오래 걸리는 테스트"
    )
    config.addinivalue_line(
        "markers", "integration: 통합 테스트"
    )
    config.addinivalue_line(
        "markers", "visualization: 시각화 테스트"
    )
    config.addinivalue_line(
        "markers", "chapter01: Chapter 01 관련 테스트"
    )

# 테스트 전후 설정
@pytest.fixture(autouse=True)
def test_environment():
    """각 테스트마다 환경 초기화"""
    # 테스트 전 설정
    import matplotlib
    matplotlib.use('Agg')  # GUI 없이 matplotlib 사용

    yield

    # 테스트 후 정리
    import matplotlib.pyplot as plt
    plt.close('all')  # 모든 차트 창 닫기

@pytest.fixture
def suppress_stdout(capsys):
    """출력 억제 fixture"""
    return capsys

# 커스텀 assertion 헬퍼들
class BiblicalAssertions:
    """성경적 데이터를 위한 커스텀 assertion들"""

    @staticmethod
    def assert_twelve_tribes_complete(df):
        """12지파 데이터 완전성 확인"""
        assert len(df) == 12, f"12지파 데이터가 {len(df)}개입니다. 12개여야 합니다."
        assert 'korean_name' in df.columns, "korean_name 컬럼이 없습니다."
        assert 'mother' in df.columns, "mother 컬럼이 없습니다."
        assert df['birth_order'].nunique() == 12, "birth_order가 중복되거나 누락되었습니다."

    @staticmethod
    def assert_leah_pattern_valid(stages):
        """레아의 4단계 패턴 유효성 확인"""
        expected = ['관계', '소통', '연합', '예배']
        assert len(stages) >= 4, f"신앙 단계가 {len(stages)}개입니다. 최소 4개 필요합니다."
        first_four = stages[:4]
        matches = sum(1 for i, stage in enumerate(first_four) if stage == expected[i])
        assert matches >= 3, f"레아 패턴 일치율이 {matches}/4입니다. 최소 3/4 이상이어야 합니다."

    @staticmethod
    def assert_light_dominance(light_freq, dark_freq):
        """빛의 우세 확인 (요한복음 패턴)"""
        assert light_freq > dark_freq, f"빛({light_freq}) > 어둠({dark_freq})이어야 합니다."
        ratio = light_freq / dark_freq if dark_freq > 0 else float('inf')
        assert ratio >= 2.0, f"빛의 비율이 {ratio:.1f}:1입니다. 최소 2:1 이상이어야 합니다."

    @staticmethod
    def assert_grace_truth_balance(grace_freq, truth_freq, tolerance=1):
        """은혜와 진리의 균형 확인"""
        difference = abs(grace_freq - truth_freq)
        assert difference <= tolerance, f"은혜({grace_freq})와 진리({truth_freq})의 차이가 {difference}입니다. {tolerance} 이하여야 합니다."

@pytest.fixture
def biblical_assertions():
    """성경적 assertion 헬퍼 fixture"""
    return BiblicalAssertions()

# 성능 테스트용 fixture
@pytest.fixture
def performance_threshold():
    """성능 테스트 임계값들"""
    return {
        'data_load_time': 2.0,      # 데이터 로드 2초 이내
        'analysis_time': 5.0,       # 분석 5초 이내
        'visualization_time': 10.0,  # 시각화 10초 이내
        'memory_limit_mb': 500       # 메모리 500MB 이내
    }