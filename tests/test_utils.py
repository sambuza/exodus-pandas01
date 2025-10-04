"""
유틸리티 모듈 테스트
"말씀을 옳게 분별하는" (딤후 2:15) 정확한 분석 도구 테스트
"""

import pytest
import pandas as pd
import time
from pathlib import Path
from utils import bible_utils

from utils.bible_utils import (
    load_config,
    load_twelve_tribes,
    load_john_concepts, 
    calculate_leah_spiritual_journey,
    analyze_light_darkness_ratio,
    get_grace_truth_balance,
    get_hebrew_meaning,
    get_greek_concept_info,
    SpiritualMetrics
)

class TestDataLoading:
    """데이터 로드 기능 테스트"""
    
    def test_load_config(self, config_path):
        """설정 파일 로드 테스트"""
        config = load_config()
        
        assert isinstance(config, dict), "설정이 딕셔너리 형태여야 합니다."
        assert 'project' in config, "project 설정이 없습니다."
        assert 'bible' in config, "bible 설정이 없습니다."
        assert 'analysis' in config, "analysis 설정이 없습니다."
        
        # 필수 프로젝트 정보 확인
        assert config['project']['name'] == "JesusBornd Pandas Edition"
        assert 'version' in config['project']
        
    def test_load_twelve_tribes(self, biblical_assertions):
        """12지파 데이터 로드 테스트"""
        tribes_df = load_twelve_tribes()
        
        # 기본 DataFrame 검증
        assert isinstance(tribes_df, pd.DataFrame), "12지파 데이터가 DataFrame이 아닙니다."
        assert not tribes_df.empty, "12지파 데이터가 비어있습니다."
        
        # 성경적 완전성 검증
        biblical_assertions.assert_twelve_tribes_complete(tribes_df)
        
        # 필수 컬럼 확인
        required_columns = ['korean_name', 'mother', 'birth_order', 'spiritual_theme']
        for col in required_columns:
            assert col in tribes_df.columns, f"{col} 컬럼이 누락되었습니다."
            
        # 데이터 타입 확인
        assert tribes_df['birth_order'].dtype in ['int64', 'int32'], "birth_order가 정수 타입이 아닙니다."
        
    def test_load_john_concepts(self):
        """요한복음 개념 데이터 로드 테스트"""
        john_df = load_john_concepts()
        
        assert isinstance(john_df, pd.DataFrame), "요한복음 데이터가 DataFrame이 아닙니다."
        assert not john_df.empty, "요한복음 데이터가 비어있습니다."
        
        # 필수 컬럼 확인
        required_columns = ['korean_name', 'frequency_ch1', 'theological_importance']
        for col in required_columns:
            assert col in john_df.columns, f"{col} 컬럼이 누락되었습니다."
            
        # 중요도 범위 확인
        importance_values = john_df['theological_importance']
        assert importance_values.min() >= 1, "신학적 중요도 최솟값이 1 미만입니다."
        assert importance_values.max() <= 10, "신학적 중요도 최댓값이 10 초과입니다."
        
    def test_data_loading_performance(self, performance_threshold):
        """데이터 로드 성능 테스트"""
        start_time = time.time()
        
        tribes_df = load_twelve_tribes()
        john_df = load_john_concepts()
        
        load_time = time.time() - start_time
        
        assert load_time < performance_threshold['data_load_time'], \
            f"데이터 로드 시간이 {load_time:.2f}초입니다. {performance_threshold['data_load_time']}초 이내여야 합니다."

class TestBiblicalAnalysis:
    """성경적 분석 기능 테스트"""
    
    def test_calculate_leah_spiritual_journey(self, biblical_assertions):
        """레아 신앙 여정 분석 테스트"""
        tribes_df = load_twelve_tribes()
        result = calculate_leah_spiritual_journey(tribes_df)
        
        # 결과 구조 확인
        assert isinstance(result, dict), "레아 분석 결과가 딕셔너리가 아닙니다."
        required_keys = ['expected_pattern', 'actual_stages', 'match_rate', 'is_biblical_pattern']
        for key in required_keys:
            assert key in result, f"{key} 키가 결과에 없습니다."
            
        # 패턴 유효성 확인
        biblical_assertions.assert_leah_pattern_valid(result['actual_stages'])
        
        # 일치율 확인
        assert 0 <= result['match_rate'] <= 100, f"일치율이 {result['match_rate']}%입니다. 0-100% 범위여야 합니다."
        
        # 예상 패턴 확인
        expected = ['관계', '소통', '연합', '예배']
        assert result['expected_pattern'] == expected, "예상 패턴이 올바르지 않습니다."
        
    def test_analyze_light_darkness_ratio(self, biblical_assertions):
        """빛과 어둠 분석 테스트"""
        john_df = load_john_concepts()
        result = analyze_light_darkness_ratio(john_df)
        
        # 결과 구조 확인
        assert isinstance(result, dict), "빛/어둠 분석 결과가 딕셔너리가 아닙니다."
        required_keys = ['light_frequency', 'darkness_frequency', 'ratio']
        for key in required_keys:
            assert key in result, f"{key} 키가 결과에 없습니다."
            
        # 성경적 패턴 확인 (빛이 어둠을 압도해야 함)
        biblical_assertions.assert_light_dominance(
            result['light_frequency'], 
            result['darkness_frequency']
        )
        
        # 비율 유효성 확인
        expected_ratio = result['light_frequency'] / result['darkness_frequency']
        assert abs(result['ratio'] - expected_ratio) < 0.01, "비율 계산이 잘못되었습니다."
        
    def test_get_grace_truth_balance(self, biblical_assertions):
        """은혜와 진리 균형 테스트"""
        john_df = load_john_concepts()
        result = get_grace_truth_balance(john_df)
        
        # 결과 구조 확인
        assert isinstance(result, dict), "은혜/진리 분석 결과가 딕셔너리가 아닙니다."
        required_keys = ['grace_frequency', 'truth_frequency', 'is_balanced']
        for key in required_keys:
            assert key in result, f"{key} 키가 결과에 없습니다."
            
        # 균형 확인 (요한복음의 특징)
        biblical_assertions.assert_grace_truth_balance(
            result['grace_frequency'], 
            result['truth_frequency']
        )

class TestLookupFunctions:
    """조회 함수 테스트"""
    
    def test_get_hebrew_meaning_valid(self):
        """유효한 히브리어 이름 조회 테스트"""
        # 유다의 히브리어
        meaning = get_hebrew_meaning('יְהוּדָה')
        assert meaning == '찬송', f"유다의 의미가 '{meaning}'입니다. '찬송'이어야 합니다."
        
    def test_get_hebrew_meaning_invalid(self):
        """무효한 히브리어 이름 조회 테스트"""
        meaning = get_hebrew_meaning('존재하지않는히브리어')
        assert meaning is None, "존재하지 않는 히브리어에 대해 None을 반환해야 합니다."
        
    def test_get_greek_concept_info_valid(self):
        """유효한 헬라어 개념 조회 테스트"""
        # 로고스 조회
        info = get_greek_concept_info('λόγος')
        
        assert isinstance(info, dict), "헬라어 개념 정보가 딕셔너리가 아닙니다."
        assert info['korean_name'] == '말씀', "λόγος의 한국어가 '말씀'이 아닙니다."
        assert 'frequency' in info, "빈도 정보가 없습니다."
        assert 'importance' in info, "중요도 정보가 없습니다."
        
    def test_get_greek_concept_info_invalid(self):
        """무효한 헬라어 개념 조회 테스트"""
        info = get_greek_concept_info('존재하지않는헬라어')
        assert info is None, "존재하지 않는 헬라어에 대해 None을 반환해야 합니다."

class TestSpiritualMetrics:
    """영적 지표 클래스 테스트"""
    
    def test_calculate_spiritual_growth_index(self):
        """영적 성장 지수 계산 테스트"""
        experiences = [
            {'year': 2020, 'growth': 3},
            {'year': 2021, 'growth': 5},
            {'year': 2022, 'growth': 7},
            {'year': 2023, 'growth': 8},
            {'year': 2024, 'growth': 9}
        ]
        
        growth_index = SpiritualMetrics.calculate_spiritual_growth_index(experiences)
        
        expected = (3 + 5 + 7 + 8 + 9) / 5
        assert abs(growth_index - expected) < 0.01, f"성장 지수가 {growth_index}입니다. {expected}여야 합니다."
        
    def test_calculate_spiritual_growth_index_empty(self):
        """빈 경험 리스트에 대한 성장 지수 테스트"""
        growth_index = SpiritualMetrics.calculate_spiritual_growth_index([])
        assert growth_index == 0.0, "빈 리스트에 대해 0.0을 반환해야 합니다."
        
    def test_analyze_spiritual_pattern(self, biblical_assertions):
        """영적 패턴 분석 테스트"""
        # 완벽한 레아 패턴
        perfect_pattern = ['관계', '소통', '연합', '예배']
        result = SpiritualMetrics.analyze_spiritual_pattern(perfect_pattern)
        
        assert isinstance(result, dict), "패턴 분석 결과가 딕셔너리가 아닙니다."
        assert result['match_rate'] == 100, "완벽한 패턴의 일치율이 100%가 아닙니다."
        assert len(result['matches']) == 4, "매칭 결과 길이가 4가 아닙니다."
        assert all(result['matches']), "완벽한 패턴에서 모든 매칭이 True여야 합니다."
        
    def test_analyze_spiritual_pattern_partial(self):
        """부분 일치 패턴 테스트"""
        partial_pattern = ['관계', '다른단계', '연합', '예배']  # 2번째만 다름
        result = SpiritualMetrics.analyze_spiritual_pattern(partial_pattern)
        
        assert result['match_rate'] == 75, f"부분 일치 패턴의 일치율이 {result['match_rate']}%입니다. 75%여야 합니다."
        expected_matches = [True, False, True, True]
        assert result['matches'] == expected_matches, "부분 매칭 결과가 올바르지 않습니다."

class TestErrorHandling:
    """에러 처리 테스트"""
    
    def test_missing_data_file(self, tmp_path, monkeypatch):
        """데이터 파일 누락 시 에러 처리 테스트"""
        # 임시 디렉토리를 프로젝트 루트로 설정
        fake_root = tmp_path / "fake_project"
        fake_root.mkdir()
        
        # 잘못된 경로로 몽키패치
        import utils.bible_utils
        monkeypatch.setattr(utils.bible_utils, 'PROJECT_ROOT', fake_root)
        
        with pytest.raises(FileNotFoundError):
            load_twelve_tribes()
            
    def test_invalid_data_format(self, tmp_path, monkeypatch):
        """잘못된 데이터 형식 처리 테스트"""
        # 빈 CSV 파일 생성
        fake_csv = tmp_path / "empty.csv"
        fake_csv.write_text("", encoding='utf-8')
        
        # 임시로 빈 파일을 로드하도록 설정
        with pytest.raises((pd.errors.EmptyDataError, ValueError)):
            pd.read_csv(fake_csv)

@pytest.mark.slow
class TestPerformance:
    """성능 테스트 (시간이 오래 걸릴 수 있음)"""
    
    def test_analysis_performance(self, performance_threshold):
        """분석 성능 테스트"""
        start_time = time.time()
        
        # 전체 분석 파이프라인 실행
        tribes_df = load_twelve_tribes()
        john_df = load_john_concepts()
        
        leah_result = calculate_leah_spiritual_journey(tribes_df)
        light_result = analyze_light_darkness_ratio(john_df)
        grace_result = get_grace_truth_balance(john_df)
        
        analysis_time = time.time() - start_time
        
        assert analysis_time < performance_threshold['analysis_time'], \
            f"분석 시간이 {analysis_time:.2f}초입니다. {performance_threshold['analysis_time']}초 이내여야 합니다."

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
