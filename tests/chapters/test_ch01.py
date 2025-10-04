"""
Chapter 01: 태초에 DataFrame 테스트
"태초에 말씀이 계시니라" (요 1:1) - 모든 분석의 시작점 검증
"""

import pytest
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import patch, MagicMock

from chapters.ch01.exodus_analysis import TwelveTribesAnalyzer
from chapters.ch01.john_analysis import JohnChapter1Analyzer
from chapters.ch01.spiritual_dna import PersonalSpiritualDNA
from chapters.ch01.visualizations import ChapterVisualizations
from chapters.ch01.__main__ import run_chapter01

@pytest.mark.chapter01
class TestTwelveTribesAnalyzer:
    """12지파 분석기 테스트"""

    def test_analyzer_initialization(self):
        """분석기 초기화 테스트"""
        analyzer = TwelveTribesAnalyzer()

        assert hasattr(analyzer, 'tribes_data'), "tribes_data 속성이 없습니다."
        assert isinstance(analyzer.tribes_data, pd.DataFrame), "tribes_data가 DataFrame이 아닙니다."
        assert len(analyzer.tribes_data) == 12, "12지파 데이터가 12개가 아닙니다."

    def test_create_basic_dataframe(self, suppress_stdout):
        """기본 DataFrame 생성 테스트"""
        analyzer = TwelveTribesAnalyzer()
        basic_df = analyzer.create_basic_dataframe()

        assert isinstance(basic_df, pd.DataFrame), "기본 DataFrame이 DataFrame 타입이 아닙니다."
        assert len(basic_df) == 4, "기본 DataFrame이 4행이 아닙니다."

        expected_columns = ['이름', '순서', '의미']
        for col in expected_columns:
            assert col in basic_df.columns, f"{col} 컬럼이 누락되었습니다."

    def test_create_complete_dataframe(self, suppress_stdout):
        """완전한 DataFrame 생성 테스트"""
        analyzer = TwelveTribesAnalyzer()
        complete_df = analyzer.create_complete_dataframe()

        assert len(complete_df) == 12, "완전한 DataFrame이 12행이 아닙니다."
        assert '이름' in complete_df.columns, "이름 컬럼이 없습니다."
        assert '어머니' in complete_df.columns, "어머니 컬럼이 없습니다."

    def test_analyze_mothers_distribution(self, suppress_stdout):
        """어머니별 분포 분석 테스트"""
        analyzer = TwelveTribesAnalyzer()
        distribution = analyzer.analyze_mothers_distribution()

        assert isinstance(distribution, pd.Series), "분포 결과가 Series가 아닙니다."
        assert distribution.sum() == 12, "총 아들 수가 12가 아닙니다."
        assert 'Leah' in distribution.index, "레아가 어머니 목록에 없습니다."

    def test_analyze_leah_spiritual_journey(self, suppress_stdout, biblical_assertions):
        """레아 신앙 여정 분석 테스트"""
        analyzer = TwelveTribesAnalyzer()
        result = analyzer.analyze_leah_spiritual_journey()

        assert isinstance(result, dict), "레아 분석 결과가 딕셔너리가 아닙니다."
        assert 'match_rate' in result, "일치율이 결과에 없습니다."
        assert 'is_biblical_pattern' in result, "성경적 패턴 여부가 결과에 없습니다."

        # 성경적 패턴 확인
        biblical_assertions.assert_leah_pattern_valid(result['actual_stages'])

    def test_get_leah_sons(self):
        """레아의 아들들 조회 테스트"""
        analyzer = TwelveTribesAnalyzer()
        leah_sons = analyzer.get_leah_sons()

        assert isinstance(leah_sons, pd.DataFrame), "레아의 아들들이 DataFrame이 아닙니다."
        assert len(leah_sons) == 6, "레아의 아들이 6명이 아닙니다."
        assert all(leah_sons['mother'] == 'Leah'), "레아가 아닌 아들이 포함되어 있습니다."

    def test_run_complete_analysis(self, suppress_stdout):
        """전체 분석 실행 테스트"""
        analyzer = TwelveTribesAnalyzer()
        results = analyzer.run_complete_analysis()

        assert isinstance(results, dict), "분석 결과가 딕셔너리가 아닙니다."

        required_keys = ['basic_dataframe', 'complete_dataframe', 'leah_analysis', 'spiritual_insights']
        for key in required_keys:
            assert key in results, f"{key}가 결과에 없습니다."

@pytest.mark.chapter01
class TestJohnChapter1Analyzer:
    """요한복음 1장 분석기 테스트"""

    def test_analyzer_initialization(self):
        """분석기 초기화 테스트"""
        analyzer = JohnChapter1Analyzer()

        assert hasattr(analyzer, 'john_concepts'), "john_concepts 속성이 없습니다."
        assert isinstance(analyzer.john_concepts, pd.DataFrame), "john_concepts가 DataFrame이 아닙니다."

    def test_create_theological_dataframe(self, suppress_stdout):
        """신학적 개념 DataFrame 생성 테스트"""
        analyzer = JohnChapter1Analyzer()
        theological_df = analyzer.create_theological_dataframe()

        assert isinstance(theological_df, pd.DataFrame), "신학적 DataFrame이 DataFrame이 아닙니다."
        assert not theological_df.empty, "신학적 DataFrame이 비어있습니다."

        expected_columns = ['개념', '헬라어', '등장빈도', '중요도']
        for col in expected_columns:
            assert col in theological_df.columns, f"{col} 컬럼이 누락되었습니다."

    def test_analyze_high_importance_concepts(self, suppress_stdout):
        """중요도 높은 개념 분석 테스트"""
        analyzer = JohnChapter1Analyzer()
        high_importance = analyzer.analyze_high_importance_concepts()

        assert isinstance(high_importance, pd.DataFrame), "중요 개념이 DataFrame이 아닙니다."
        assert all(high_importance['중요도'] >= 8), "중요도 8 미만인 개념이 포함되어 있습니다."

    def test_analyze_light_vs_darkness(self, suppress_stdout, biblical_assertions):
        """빛과 어둠 대조 분석 테스트"""
        analyzer = JohnChapter1Analyzer()
        result = analyzer.analyze_light_vs_darkness()

        assert isinstance(result, dict), "빛/어둠 분석 결과가 딕셔너리가 아닙니다."

        # 성경적 패턴 확인 (빛이 어둠을 압도해야 함)
        biblical_assertions.assert_light_dominance(
            result['light_frequency'],
            result['darkness_frequency']
        )

    def test_analyze_grace_truth_balance(self, suppress_stdout, biblical_assertions):
        """은혜와 진리 균형 분석 테스트"""
        analyzer = JohnChapter1Analyzer()
        result = analyzer.analyze_grace_truth_balance()

        assert isinstance(result, dict), "은혜/진리 분석 결과가 딕셔너리가 아닙니다."

        # 균형 확인
        biblical_assertions.assert_grace_truth_balance(
            result['grace_frequency'],
            result['truth_frequency']
        )

    def test_get_top_theological_concepts(self, suppress_stdout):
        """TOP 신학 개념 조회 테스트"""
        analyzer = JohnChapter1Analyzer()
        top_concepts = analyzer.get_top_theological_concepts(5)

        assert isinstance(top_concepts, pd.DataFrame), "TOP 개념이 DataFrame이 아닙니다."
        assert len(top_concepts) <= 5, "TOP 5개를 초과했습니다."

        # 중요도 순으로 정렬되어 있는지 확인
        importances = analyzer.john_concepts.nlargest(5, 'theological_importance')['theological_importance'].tolist()
        assert importances == sorted(importances, reverse=True), "중요도 순으로 정렬되지 않았습니다."

@pytest.mark.chapter01
class TestPersonalSpiritualDNA:
    """개인 신앙 DNA 분석기 테스트"""

    def test_analyzer_initialization(self):
        """분석기 초기화 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")

        assert analyzer.name == "테스트유저", "이름이 올바르게 설정되지 않았습니다."
        assert hasattr(analyzer, 'spiritual_journey'), "spiritual_journey 속성이 없습니다."

    def test_create_spiritual_journey_dataframe(self, suppress_stdout):
        """신앙 여정 DataFrame 생성 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")
        journey_df = analyzer.create_spiritual_journey_dataframe()

        assert isinstance(journey_df, pd.DataFrame), "신앙 여정이 DataFrame이 아닙니다."
        assert not journey_df.empty, "신앙 여정이 비어있습니다."

        expected_columns = ['연도', '핵심사건', '성장지수', '감사제목']
        for col in expected_columns:
            assert col in journey_df.columns, f"{col} 컬럼이 누락되었습니다."

    def test_analyze_growth_pattern(self, suppress_stdout):
        """성장 패턴 분석 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")
        analyzer.create_spiritual_journey_dataframe()  # 먼저 데이터 생성

        result = analyzer.analyze_growth_pattern()

        assert isinstance(result, dict), "성장 패턴 결과가 딕셔너리가 아닙니다."
        assert 'average_growth' in result, "평균 성장이 결과에 없습니다."
        assert 'peak_experience' in result, "최고 경험이 결과에 없습니다."
        assert 'growth_trend' in result, "성장 추세가 결과에 없습니다."

    def test_add_future_vision(self, suppress_stdout):
        """미래 비전 추가 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")
        analyzer.create_spiritual_journey_dataframe()  # 먼저 데이터 생성

        complete_journey = analyzer.add_future_vision(2025, "새로운 목표", 10)

        assert isinstance(complete_journey, pd.DataFrame), "완전한 여정이 DataFrame이 아닙니다."
        assert len(complete_journey) == 6, "미래 계획이 추가되지 않았습니다."  # 기본 5개 + 미래 1개

    def test_analyze_leah_pattern_match(self, suppress_stdout):
        """레아 패턴 매칭 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")

        # 완벽한 패턴으로 테스트
        perfect_pattern = ['관계', '소통', '연합', '예배']
        result = analyzer.analyze_leah_pattern_match(perfect_pattern)

        assert isinstance(result, dict), "패턴 매칭 결과가 딕셔너리가 아닙니다."
        assert result['match_rate'] == 100, "완벽한 패턴의 일치율이 100%가 아닙니다."
        assert result['is_biblical'], "완벽한 패턴이 성경적이지 않다고 판정되었습니다."

    def test_analyze_light_darkness_balance(self, suppress_stdout, biblical_assertions):
        """빛/어둠 균형 분석 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")

        # 빛이 우세한 상황으로 테스트
        result = analyzer.analyze_light_darkness_balance(8, 2)

        assert isinstance(result, dict), "빛/어둠 균형 결과가 딕셔너리가 아닙니다."
        assert result['spiritual_status'] == '승리', "빛이 우세한데 승리 상태가 아닙니다."

        # 성경적 패턴 확인
        biblical_assertions.assert_light_dominance(
            result['light_frequency'],
            result['dark_frequency']
        )

    def test_generate_spiritual_report(self, suppress_stdout):
        """종합 영적 리포트 생성 테스트"""
        analyzer = PersonalSpiritualDNA("테스트유저")
        analyzer.create_spiritual_journey_dataframe()  # 먼저 데이터 생성

        report = analyzer.generate_spiritual_report()

        assert isinstance(report, dict), "영적 리포트가 딕셔너리가 아닙니다."
        assert 'overall_score' in report, "종합 점수가 없습니다."
        assert 'recommendations' in report, "추천사항이 없습니다."

        # 점수 범위 확인
        score = report['overall_score']
        assert 0 <= score <= 10, f"종합 점수가 {score}입니다. 0-10 범위여야 합니다."

@pytest.mark.chapter01
@pytest.mark.visualization
class TestChapterVisualizations:
    """시각화 모듈 테스트"""

    def test_visualization_initialization(self):
        """시각화 객체 초기화 테스트"""
        viz = ChapterVisualizations()

        assert hasattr(viz, 'colors'), "색상 팔레트가 없습니다."
        assert isinstance(viz.colors, dict), "색상 팔레트가 딕셔너리가 아닙니다."

        required_colors = ['primary', 'secondary', 'accent']
        for color in required_colors:
            assert color in viz.colors, f"{color} 색상이 팔레트에 없습니다."

    def test_plot_mothers_distribution(self, sample_tribes_data):
        """어머니별 분포 차트 테스트"""
        viz = ChapterVisualizations()
        fig = viz.plot_mothers_distribution(sample_tribes_data)

        assert fig is not None, "차트가 생성되지 않았습니다."
        assert len(fig.axes) == 1, "축이 1개가 아닙니다."

        plt.close(fig)  # 메모리 정리

    def test_plot_leah_spiritual_journey(self, sample_tribes_data):
        """레아 신앙 여정 차트 테스트"""
        viz = ChapterVisualizations()
        fig = viz.plot_leah_spiritual_journey(sample_tribes_data)

        assert fig is not None, "신앙 여정 차트가 생성되지 않았습니다."
        assert len(fig.axes) == 1, "축이 1개가 아닙니다."

        plt.close(fig)

    def test_plot_john_concepts_importance(self, sample_john_concepts):
        """요한복음 개념 중요도 차트 테스트"""
        viz = ChapterVisualizations()
        fig = viz.plot_john_concepts_importance(sample_john_concepts)

        assert fig is not None, "중요도 차트가 생성되지 않았습니다."
        plt.close(fig)

    def test_plot_light_vs_darkness(self, sample_john_concepts):
        """빛 vs 어둠 차트 테스트"""
        viz = ChapterVisualizations()
        fig = viz.plot_light_vs_darkness(sample_john_concepts)

        assert fig is not None, "빛/어둠 차트가 생성되지 않았습니다."
        assert len(fig.axes) == 2, "서브플롯이 2개가 아닙니다."

        plt.close(fig)

    def test_plot_spiritual_growth_radar(self):
        """영적 성장 레이더 차트 테스트"""
        viz = ChapterVisualizations()
        growth_scores = [7, 8, 6, 9, 7]
        fig = viz.plot_spiritual_growth_radar(growth_scores)

        assert fig is not None, "레이더 차트가 생성되지 않았습니다."
        plt.close(fig)

    def test_create_chapter_summary_dashboard(self, sample_tribes_data, sample_john_concepts):
        """종합 대시보드 테스트"""
        viz = ChapterVisualizations()
        personal_scores = [7, 8, 6, 9, 7]
        fig = viz.create_chapter_summary_dashboard(
            sample_tribes_data, sample_john_concepts, personal_scores
        )

        assert fig is not None, "대시보드가 생성되지 않았습니다."
        assert len(fig.axes) == 4, "서브플롯이 4개가 아닙니다."

        plt.close(fig)

@pytest.mark.chapter01
@pytest.mark.integration
class TestChapterIntegration:
    """Chapter 01 통합 테스트"""

    def test_run_chapter01_non_interactive(self, suppress_stdout):
        """비대화형 모드 전체 실행 테스트"""
        results = run_chapter01(interactive=False, user_name="테스트유저")

        assert isinstance(results, dict), "실행 결과가 딕셔너리가 아닙니다."
        assert results['chapter'] == '01', "챕터 번호가 올바르지 않습니다."

        # 각 분석 섹션이 실행되었는지 확인
        assert 'exodus_analysis' in results, "출애굽기 분석이 없습니다."
        assert 'john_analysis' in results, "요한복음 분석이 없습니다."
        assert 'personal_analysis' in results, "개인 분석이 없습니다."

    @patch('builtins.input')
    def test_run_chapter01_interactive_skip_personal(self, mock_input, suppress_stdout):
        """대화형 모드에서 개인 분석 건너뛰기 테스트"""
        # 사용자 입력 시뮬레이션: Enter, Enter, 'n' (개인 분석 건너뛰기)
        mock_input.side_effect = ['', '', 'n']

        results = run_chapter01(interactive=True)

        assert results is not None, "대화형 모드 실행 결과가 None입니다."
        assert results['personal_analysis'] is None, "개인 분석을 건너뛰었는데 결과가 있습니다."

    def test_chapter_components_integration(self, suppress_stdout):
        """챕터 구성요소들의 통합 동작 테스트"""
        # 각 분석기가 서로 호환되는지 확인
        tribes_analyzer = TwelveTribesAnalyzer()
        john_analyzer = JohnChapter1Analyzer()
        personal_analyzer = PersonalSpiritualDNA("통합테스트유저")
        viz = ChapterVisualizations()

        # 데이터 생성
        tribes_data = tribes_analyzer.tribes_data
        john_data = john_analyzer.john_concepts
        personal_journey = personal_analyzer.create_spiritual_journey_dataframe()

        # 시각화에서 모든 데이터 사용 가능한지 확인
        dashboard = viz.create_chapter_summary_dashboard(
            tribes_data, john_data, [7, 8, 6, 9, 7]
        )

        assert dashboard is not None, "통합 대시보드 생성에 실패했습니다."
        plt.close(dashboard)

@pytest.mark.chapter01
@pytest.mark.slow
class TestChapterPerformance:
    """Chapter 01 성능 테스트"""

    def test_full_chapter_performance(self, performance_threshold, suppress_stdout):
        """전체 챕터 실행 성능 테스트"""
        import time

        start_time = time.time()
        results = run_chapter01(interactive=False, user_name="성능테스트유저")
        execution_time = time.time() - start_time

        assert results is not None, "성능 테스트 실행에 실패했습니다."
        assert execution_time < 30, f"전체 실행 시간이 {execution_time:.2f}초입니다. 30초 이내여야 합니다."

    def test_visualization_performance(self, sample_tribes_data, sample_john_concepts, performance_threshold):
        """시각화 성능 테스트"""
        import time

        viz = ChapterVisualizations()

        start_time = time.time()

        # 모든 차트 생성
        fig1 = viz.plot_mothers_distribution(sample_tribes_data)
        fig2 = viz.plot_leah_spiritual_journey(sample_tribes_data)
        fig3 = viz.plot_john_concepts_importance(sample_john_concepts)
        fig4 = viz.plot_light_vs_darkness(sample_john_concepts)
        fig5 = viz.plot_spiritual_growth_radar([7, 8, 6, 9, 7])

        visualization_time = time.time() - start_time

        # 메모리 정리
        for fig in [fig1, fig2, fig3, fig4, fig5]:
            plt.close(fig)

        assert visualization_time < performance_threshold['visualization_time'], \
            f"시각화 시간이 {visualization_time:.2f}초입니다. {performance_threshold['visualization_time']}초 이내여야 합니다."

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])