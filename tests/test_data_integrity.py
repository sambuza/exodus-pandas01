"""
데이터 무결성 테스트
"진리의 말씀을 옳게 분별하라" (딤후 2:15)

모든 성경 데이터의 정확성과 일관성을 검증합니다.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

class TestDataFiles:
    """데이터 파일 존재성 및 형식 테스트"""
    
    def test_required_data_files_exist(self, test_data_path):
        """필수 데이터 파일들 존재 확인"""
        required_files = [
            "ch01_tribes.csv",
            "ch01_john_concepts.csv"
        ]
        
        for filename in required_files:
            file_path = test_data_path / filename
            assert file_path.exists(), f"{filename} 파일이 존재하지 않습니다."
            assert file_path.stat().st_size > 0, f"{filename} 파일이 비어있습니다."
            
    def test_config_file_exists(self, config_path):
        """설정 파일 존재 확인"""
        assert config_path.exists(), "config.yml 파일이 존재하지 않습니다."
        assert config_path.stat().st_size > 0, "config.yml 파일이 비어있습니다."

class TestTwelveTribesData:
    """12지파 데이터 무결성 테스트"""
    
    @pytest.fixture
    def tribes_data(self, test_data_path):
        """12지파 데이터 로드"""
        return pd.read_csv(test_data_path / "ch01_tribes.csv", encoding='utf-8')
    
    def test_tribes_data_structure(self, tribes_data, biblical_assertions):
        """12지파 데이터 구조 검증"""
        # 기본 구조 확인
        assert isinstance(tribes_data, pd.DataFrame), "12지파 데이터가 DataFrame이 아닙니다."
        biblical_assertions.assert_twelve_tribes_complete(tribes_data)
        
    def test_tribes_required_columns(self, tribes_data):
        """필수 컬럼 존재 확인"""
        required_columns = [
            'name', 'korean_name', 'hebrew', 'korean_meaning', 
            'mother', 'birth_order', 'spiritual_theme'
        ]
        
        for col in required_columns:
            assert col in tribes_data.columns, f"{col} 컬럼이 누락되었습니다."
            
    def test_tribes_data_types(self, tribes_data):
        """데이터 타입 검증"""
        # 숫자형 컬럼 확인
        assert tribes_data['birth_order'].dtype in ['int64', 'int32'], "birth_order가 정수형이 아닙니다."
        
        # 문자열 컬럼 확인
        string_columns = ['name', 'korean_name', 'hebrew', 'korean_meaning', 'mother', 'spiritual_theme']
        for col in string_columns:
            assert tribes_data[col].dtype == 'object', f"{col}이 문자열 타입이 아닙니다."
            
    def test_tribes_birth_order_sequence(self, tribes_data):
        """출생 순서 연속성 확인"""
        birth_orders = sorted(tribes_data['birth_order'].tolist())
        expected = list(range(1, 13))  # 1부터 12까지
        
        assert birth_orders == expected, f"출생 순서가 {birth_orders}입니다. 1-12 연속이어야 합니다."
        
    def test_tribes_mothers_valid(self, tribes_data):
        """어머니 이름 유효성 확인"""
        valid_mothers = {'Leah', 'Rachel', 'Bilhah', 'Zilpah'}
        actual_mothers = set(tribes_data['mother'].unique())
        
        assert actual_mothers.issubset(valid_mothers), f"유효하지 않은 어머니 이름: {actual_mothers - valid_mothers}"
        
    def test_tribes_no_missing_values(self, tribes_data):
        """결측값 확인"""
        missing_counts = tribes_data.isnull().sum()
        missing_columns = missing_counts[missing_counts > 0]
        
        assert len(missing_columns) == 0, f"결측값이 있는 컬럼: {missing_columns.to_dict()}"
        
    def test_tribes_leah_sons_pattern(self, tribes_data, biblical_assertions):
        """레아의 아들들 패턴 검증"""
        leah_sons = tribes_data[tribes_data['mother'] == 'Leah'].sort_values('birth_order')
        first_four_themes = leah_sons.head(4)['spiritual_theme'].tolist()
        
        biblical_assertions.assert_leah_pattern_valid(first_four_themes)
        
    def test_tribes_hebrew_names_validity(self, tribes_data):
        """히브리어 이름 유효성 확인"""
        hebrew_names = tribes_data['hebrew'].tolist()
        
        # 히브리어 문자 확인 (기본적인 유니코드 범위)
        for name in hebrew_names:
            # 히브리어 유니코드 범위: U+0590-U+05FF
            has_hebrew = any('\u0590' <= char <= '\u05FF' for char in name)
            assert has_hebrew, f"히브리어 이름 '{name}'에 히브리어 문자가 없습니다."

class TestJohnConceptsData:
    """요한복음 개념 데이터 무결성 테스트"""
    
    @pytest.fixture
    def john_data(self, test_data_path):
        """요한복음 개념 데이터 로드"""
        return pd.read_csv(test_data_path / "ch01_john_concepts.csv", encoding='utf-8')
    
    def test_john_data_structure(self, john_data):
        """요한복음 데이터 구조 검증"""
        assert isinstance(john_data, pd.DataFrame), "요한복음 데이터가 DataFrame이 아닙니다."
        assert not john_data.empty, "요한복음 데이터가 비어있습니다."
        
    def test_john_required_columns(self, john_data):
        """필수 컬럼 존재 확인"""
        required_columns = [
            'concept', 'korean_name', 'greek_word', 'greek_transliteration',
            'frequency_ch1', 'theological_importance'
        ]
        
        for col in required_columns:
            assert col in john_data.columns, f"{col} 컬럼이 누락되었습니다."
            
    def test_john_data_types(self, john_data):
        """데이터 타입 검증"""
        # 숫자형 컬럼 확인
        numeric_columns = ['frequency_ch1', 'theological_importance']
        for col in numeric_columns:
            assert john_data[col].dtype in ['int64', 'int32', 'float64'], f"{col}이 숫자형이 아닙니다."
            
    def test_john_theological_importance_range(self, john_data):
        """신학적 중요도 범위 확인"""
        importance_values = john_data['theological_importance']
        
        assert importance_values.min() >= 1, f"신학적 중요도 최솟값이 {importance_values.min()}입니다. 1 이상이어야 합니다."
        assert importance_values.max() <= 10, f"신학적 중요도 최댓값이 {importance_values.max()}입니다. 10 이하여야 합니다."
        
    def test_john_frequency_positive(self, john_data):
        """빈도 값 양수 확인"""
        frequencies = john_data['frequency_ch1']
        
        assert all(frequencies > 0), "모든 빈도 값은 양수여야 합니다."
        assert frequencies.dtype in ['int64', 'int32'], "빈도는 정수여야 합니다."
        
    def test_john_light_darkness_contrast(self, john_data, biblical_assertions):
        """빛과 어둠의 대조 확인"""
        light_row = john_data[john_data['concept'] == 'Light']
        darkness_row = john_data[john_data['concept'] == 'Darkness']
        
        assert len(light_row) == 1, "Light 개념이 정확히 하나 있어야 합니다."
        assert len(darkness_row) == 1, "Darkness 개념이 정확히 하나 있어야 합니다."
        
        light_freq = light_row['frequency_ch1'].iloc[0]
        darkness_freq = darkness_row['frequency_ch1'].iloc[0]
        
        biblical_assertions.assert_light_dominance(light_freq, darkness_freq)
        
    def test_john_grace_truth_balance(self, john_data, biblical_assertions):
        """은혜와 진리의 균형 확인"""
        grace_row = john_data[john_data['concept'] == 'Grace']
        truth_row = john_data[john_data['concept'] == 'Truth']
        
        assert len(grace_row) == 1, "Grace 개념이 정확히 하나 있어야 합니다."
        assert len(truth_row) == 1, "Truth 개념이 정확히 하나 있어야 합니다."
        
        grace_freq = grace_row['frequency_ch1'].iloc[0]
        truth_freq = truth_row['frequency_ch1'].iloc[0]
        
        biblical_assertions.assert_grace_truth_balance(grace_freq, truth_freq)
        
    def test_john_key_concepts_present(self, john_data):
        """핵심 개념들 존재 확인"""
        key_concepts = {'Word', 'Light', 'Life', 'Grace', 'Truth', 'Darkness'}
        actual_concepts = set(john_data['concept'])
        
        missing_concepts = key_concepts - actual_concepts
        assert len(missing_concepts) == 0, f"핵심 개념이 누락됨: {missing_concepts}"
        
    def test_john_greek_words_validity(self, john_data):
        """헬라어 단어 유효성 확인"""
        greek_words = john_data['greek_word'].dropna().tolist()
        
        for word in greek_words:
            # 헬라어 유니코드 범위: U+0370-U+03FF
            has_greek = any('\u0370' <= char <= '\u03FF' for char in word)
            assert has_greek, f"헬라어 단어 '{word}'에 헬라어 문자가 없습니다."

class TestDataConsistency:
    """데이터 일관성 테스트"""
    
    def test_encoding_consistency(self, test_data_path):
        """모든 CSV 파일의 인코딩 일관성 확인"""
        csv_files = list(test_data_path.glob("*.csv"))
        
        for csv_file in csv_files:
            try:
                # UTF-8로 읽기 시도
                df = pd.read_csv(csv_file, encoding='utf-8')
                assert not df.empty, f"{csv_file.name}이 비어있습니다."
            except UnicodeDecodeError:
                pytest.fail(f"{csv_file.name}이 UTF-8 인코딩이 아닙니다.")
                
    def test_column_naming_consistency(self, test_data_path):
        """컬럼명 명명 규칙 일관성 확인"""
        csv_files = list(test_data_path.glob("*.csv"))
        
        for csv_file in csv_files:
            df = pd.read_csv(csv_file, encoding='utf-8')
            
            for col in df.columns:
                # 컬럼명에 공백이나 특수문자 확인
                assert not col.startswith(' '), f"{csv_file.name}의 '{col}' 컬럼명이 공백으로 시작합니다."
                assert not col.endswith(' '), f"{csv_file.name}의 '{col}' 컬럼명이 공백으로 끝납니다."

class TestBiblicalAccuracy:
    """성경적 정확성 테스트"""
    
    def test_twelve_tribes_biblical_accuracy(self, test_data_path):
        """12지파 성경적 정확성 확인"""
        tribes_data = pd.read_csv(test_data_path / "ch01_tribes.csv", encoding='utf-8')
        
        # 성경에 기록된 순서대로 확인 (창세기 29-30, 35장 기준)
        biblical_order = [
            ('Reuben', 'Leah', 1), ('Simeon', 'Leah', 2), ('Levi', 'Leah', 3), ('Judah', 'Leah', 4),
            ('Dan', 'Bilhah', 5), ('Naphtali', 'Bilhah', 6), ('Gad', 'Zilpah', 7), ('Asher', 'Zilpah', 8),
            ('Issachar', 'Leah', 9), ('Zebulun', 'Leah', 10), ('Joseph', 'Rachel', 11), ('Benjamin', 'Rachel', 12)
        ]
        
        for name, mother, order in biblical_order:
            row = tribes_data[tribes_data['name'] == name]
            assert len(row) == 1, f"{name} 지파를 찾을 수 없습니다."
            
            actual_mother = row['mother'].iloc[0]
            actual_order = row['birth_order'].iloc[0]
            
            assert actual_mother == mother, f"{name}의 어머니가 {actual_mother}입니다. {mother}여야 합니다."
            assert actual_order == order, f"{name}의 출생순서가 {actual_order}입니다. {order}여야 합니다."
            
    def test_john_gospel_theological_accuracy(self, test_data_path):
        """요한복음 신학적 정확성 확인"""
        john_data = pd.read_csv(test_data_path / "ch01_john_concepts.csv", encoding='utf-8')
        
        # 요한복음 1장의 신학적 중요도 검증
        word_importance = john_data[john_data['concept'] == 'Word']['theological_importance'].iloc[0]
        assert word_importance == 10, f"'말씀'의 중요도가 {word_importance}입니다. 10이어야 합니다."
        
        # 빛이 어둠보다 중요해야 함
        light_importance = john_data[john_data['concept'] == 'Light']['theological_importance'].iloc[0]
        darkness_importance = john_data[john_data['concept'] == 'Darkness']['theological_importance'].iloc[0]
        assert light_importance > darkness_importance, "빛이 어둠보다 신학적으로 더 중요해야 합니다."

class TestDataPerformance:
    """데이터 로드 성능 테스트"""
    
    @pytest.mark.slow
    def test_data_loading_speed(self, test_data_path, performance_threshold):
        """데이터 로딩 속도 테스트"""
        import time
        
        csv_files = list(test_data_path.glob("*.csv"))
        
        for csv_file in csv_files:
            start_time = time.time()
            df = pd.read_csv(csv_file, encoding='utf-8')
            load_time = time.time() - start_time
            
            assert load_time < performance_threshold['data_load_time'], \
                f"{csv_file.name} 로딩이 {load_time:.2f}초 걸렸습니다. {performance_threshold['data_load_time']}초 이내여야 합니다."
                
    def test_data_memory_usage(self, test_data_path):
        """데이터 메모리 사용량 테스트"""
        csv_files = list(test_data_path.glob("*.csv"))
        
        total_memory = 0
        for csv_file in csv_files:
            df = pd.read_csv(csv_file, encoding='utf-8')
            memory_usage = df.memory_usage(deep=True).sum()
            total_memory += memory_usage
            
            # 개별 파일이 10MB를 초과하지 않아야 함 (예시 데이터이므로)
            assert memory_usage < 10 * 1024 * 1024, \
                f"{csv_file.name}이 {memory_usage / (1024*1024):.1f}MB를 사용합니다. 10MB 이하여야 합니다."
        
        # 전체 메모리 사용량이 50MB를 초과하지 않아야 함
        assert total_memory < 50 * 1024 * 1024, \
            f"전체 데이터가 {total_memory / (1024*1024):.1f}MB를 사용합니다. 50MB 이하여야 합니다."

if __name__ == "__main__":
    pytest.main([__file__, "-v"])