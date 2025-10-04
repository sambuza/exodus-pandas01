import pytest
from chapters.ch01.visualizations import ChapterVisualizations
from chapters.ch01.exodus_analysis import TwelveTribesAnalyzer
from chapters.ch01.john_analysis import JohnChapter1Analyzer
import pandas as pd
import numpy as np


# # 1. 간단한 함수 테스트
# def test_add_numbers():
#     """아주 간단한 덧셈 함수 테스트"""
#     result = 2 + 3
#     assert result == 5, "2 + 3은 5가 되어야 합니다."
#

# 2. 피스쳐(fixture)를 사용한 공통 데이터 준비
@pytest.fixture
def sample_tribes_data():
    """테스트용 가상 12지파 DataFrame 제공"""
    data = {
        'name': ['Reuben', 'Simeon', 'Levi', 'Judah'],
        'korean_name': ['르우벤', '시므온', '레위', '유다'],
        'mother': ['Leah', 'Leah', 'Leah', 'Leah'],
        'birth_order': [1, 2, 3, 4]
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_john_concepts():
    """테스트용 요한복음 개념 DataFrame 제공"""
    data = {
        'concept': ['Word', 'Life', 'Light', 'Darkness', 'Truth'],
        'korean_name': ['말씀', '생명', '빛', '어둠', '진리'],
        'theological_importance': [10, 8, 9, 5, 9],
        'frequency_ch1': [1, 2, 3, 4, 5]
    }
    return pd.DataFrame(data)


# 3. 클래스 기반의 테스트
class TestChapterVisualizations:
    """ChapterVisualizations 클래스의 여러 메서드를 테스트하는 클래스"""

    def test_visualization_initialization(self):
        """시각화 객체 초기화 및 속성 확인"""
        viz = ChapterVisualizations()
        assert hasattr(viz, 'colors'), "colors 속성이 존재해야 합니다."

    def test_plot_mothers_distribution(self, sample_tribes_data):
        """plot_mothers_distribution 메서드 테스트"""
        viz = ChapterVisualizations()
        fig = viz.plot_mothers_distribution(sample_tribes_data)
        assert fig is not None, "함수가 matplotlib figure 객체를 반환해야 합니다."
        assert len(fig.axes) == 1, "그래프는 단일 축(axes)을 가져야 합니다."

    def test_plot_john_concepts(self, sample_john_concepts):
        """plot_john_concepts_importance 메서드 테스트"""
        viz = ChapterVisualizations()
        fig = viz.plot_john_concepts_importance(sample_john_concepts)
        assert fig is not None, "함수가 matplotlib figure 객체를 반환해야 합니다."
        assert len(fig.axes) == 1, "그래프는 단일 축(axes)을 가져야 합니다."

    def test_create_dashboard_with_all_data(self, sample_tribes_data, sample_john_concepts):
        """종합 대시보드 생성 테스트"""
        viz = ChapterVisualizations()
        personal_scores = [7, 8, 6, 9, 7]
        fig = viz.create_chapter_summary_dashboard(
            tribes_df=sample_tribes_data,
            john_df=sample_john_concepts,
            personal_scores=personal_scores
        )
        assert fig is not None, "대시보드 함수는 figure 객체를 반환해야 합니다."
        assert len(fig.axes) == 4, "대시보드는 4개의 축(axes)을 가져야 합니다."
