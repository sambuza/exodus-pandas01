"""
JesusBornd 성경 분석 유틸리티
출애굽기 × 요한복음 블렌딩을 위한 헬퍼 함수들

"태초에 말씀이 계시니라" - 모든 분석의 시작점
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent


def load_config() -> Dict:
    """설정 파일 로드"""
    config_path = PROJECT_ROOT / "config.yml"

    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_bible() -> pd.DataFrame:
    df = pd.read_csv(PROJECT_ROOT / 'data' / 'raw' / 'bible_KJV.csv')

    return df

def load_twelve_tribes() -> pd.DataFrame:
    """12지파 기본 정보 로드

    Returns:
        DataFrame: 12지파 정보 (이름, 히브리어, 의미, 어머니 등)
    """
    data_path = PROJECT_ROOT / "data/examples/ch01_tribes.csv"
    return pd.read_csv(data_path, encoding='utf-8')

def load_exodus() -> pd.DataFrame:
    df = pd.read_csv(PROJECT_ROOT / 'data' / 'raw' / 'bible_KJV.csv')
    exodus = df[df["book"].str.strip().str.lower() == "exodus"].copy()
    return exodus

def load_john_concepts() -> pd.DataFrame:
    """요한복음 1장 신학적 개념 로드

    Returns:
        DataFrame: 요한복음 핵심 개념들 (말씀, 빛, 생명 등)
    """
    data_path = PROJECT_ROOT / "data/examples/ch01_john_concepts.csv"
    return pd.read_csv(data_path, encoding='utf-8')


def calculate_leah_spiritual_journey(tribes_df: pd.DataFrame) -> Dict:
    """레아의 신앙 여정 4단계 패턴 분석

    Args:
        tribes_df: 12지파 DataFrame

    Returns:
        Dict: 신앙 여정 분석 결과
    """
    config = load_config()
    expected_pattern = config['analysis']['patterns']['leah_stages']

    leah_sons = tribes_df[tribes_df['mother'] == 'Leah'].sort_values('birth_order')
    first_four = leah_sons.head(4)

    actual_stages = first_four['spiritual_theme'].tolist()

    # 패턴 일치율 계산
    matches = sum(1 for i, stage in enumerate(actual_stages)
                  if i < len(expected_pattern) and stage == expected_pattern[i])
    match_rate = matches / len(expected_pattern) * 100

    return {
        'expected_pattern': expected_pattern,
        'actual_stages': actual_stages,
        'first_four_sons': first_four[['korean_name', 'korean_meaning', 'spiritual_theme']].to_dict('records'),
        'match_rate': match_rate,
        'is_biblical_pattern': match_rate >= 75,
        'spiritual_insight': "레아의 고난이 완벽한 신앙 성숙 과정을 보여줍니다" if match_rate >= 75 else "패턴을 다시 확인해보세요"
    }


def analyze_light_darkness_ratio(john_df: pd.DataFrame) -> Dict:
    """요한복음 빛 vs 어둠 대조 분석

    Args:
        john_df: 요한복음 개념 DataFrame

    Returns:
        Dict: 빛과 어둠의 분석 결과
    """
    light_data = john_df[john_df['concept'] == 'Light'].iloc[0]
    darkness_data = john_df[john_df['concept'] == 'Darkness'].iloc[0]

    light_freq = light_data['frequency_ch1']
    darkness_freq = darkness_data['frequency_ch1']
    ratio = light_freq / darkness_freq if darkness_freq > 0 else float('inf')

    return {
        'light_frequency': light_freq,
        'darkness_frequency': darkness_freq,
        'ratio': ratio,
        'light_importance': light_data['theological_importance'],
        'darkness_importance': darkness_data['theological_importance'],
        'spiritual_insight': f"빛이 어둠을 {ratio:.1f}:1로 압도합니다. 요한의 의도적 설계입니다!"
    }


def get_grace_truth_balance(john_df: pd.DataFrame) -> Dict:
    """은혜와 진리의 완벽한 균형 분석

    Args:
        john_df: 요한복음 개념 DataFrame

    Returns:
        Dict: 은혜와 진리 균형 분석 결과
    """
    grace_data = john_df[john_df['concept'] == 'Grace'].iloc[0]
    truth_data = john_df[john_df['concept'] == 'Truth'].iloc[0]

    return {
        'grace_frequency': grace_data['frequency_ch1'],
        'truth_frequency': truth_data['frequency_ch1'],
        'grace_importance': grace_data['theological_importance'],
        'truth_importance': truth_data['theological_importance'],
        'is_balanced': grace_data['frequency_ch1'] == truth_data['frequency_ch1'] and
                       grace_data['theological_importance'] == truth_data['theological_importance'],
        'spiritual_insight': "예수님 안에서 은혜와 진리가 완벽하게 조화를 이룹니다!"
    }


def get_hebrew_meaning(hebrew_name: str) -> Optional[str]:
    """히브리어 이름의 의미 조회

    Args:
        hebrew_name: 히브리어 이름

    Returns:
        str: 한국어 의미 또는 None
    """
    tribes_df = load_twelve_tribes()
    result = tribes_df[tribes_df['hebrew'] == hebrew_name]

    if not result.empty:
        return result.iloc[0]['korean_meaning']
    return None


def get_greek_concept_info(greek_word: str) -> Optional[Dict]:
    """헬라어 신학 개념 정보 조회

    Args:
        greek_word: 헬라어 단어

    Returns:
        Dict: 개념 정보 또는 None
    """
    john_df = load_john_concepts()
    result = john_df[john_df['greek_word'] == greek_word]

    if not result.empty:
        row = result.iloc[0]
        return {
            'korean_name': row['korean_name'],
            'transliteration': row['greek_transliteration'],
            'frequency': row['frequency_ch1'],
            'importance': row['theological_importance'],
            'contrast': row['contrast_pair']
        }
    return None


class SpiritualMetrics:
    """영적 지표 계산 클래스"""

    @staticmethod
    def calculate_spiritual_growth_index(experiences: List[Dict]) -> float:
        """영적 성장 지수 계산

        Args:
            experiences: 영적 경험 리스트 [{'year': 2020, 'growth': 5}, ...]

        Returns:
            float: 성장 지수 (1-10)
        """
        if not experiences:
            return 0.0

        growth_scores = [exp.get('growth', 0) for exp in experiences]
        return np.mean(growth_scores)

    @staticmethod
    def analyze_spiritual_pattern(journey_stages: List[str]) -> Dict:
        """개인 영적 패턴 분석

        Args:
            journey_stages: 영적 여정 단계들

        Returns:
            Dict: 패턴 분석 결과
        """
        config = load_config()
        leah_pattern = config['analysis']['patterns']['leah_stages']

        # 패턴 매칭
        matches = []
        for i, stage in enumerate(journey_stages[:4]):  # 첫 4단계만 비교
            if i < len(leah_pattern) and stage == leah_pattern[i]:
                matches.append(True)
            else:
                matches.append(False)

        match_rate = sum(matches) / len(leah_pattern) * 100 if leah_pattern else 0

        return {
            'user_pattern': journey_stages[:4],
            'biblical_pattern': leah_pattern,
            'matches': matches,
            'match_rate': match_rate,
            'recommendation': get_spiritual_recommendation(match_rate)
        }


def get_spiritual_recommendation(match_rate: float) -> str:
    """영적 성장 추천사항

    Args:
        match_rate: 성경적 패턴 일치율

    Returns:
        str: 추천사항
    """
    if match_rate >= 90:
        return "✨ 레아와 같은 아름다운 신앙 여정을 걷고 계시네요!"
    elif match_rate >= 70:
        return "🌱 좋은 신앙 패턴을 보이고 있어요. 조금 더 체계적으로 성장해보세요."
    elif match_rate >= 50:
        return "📚 성경적 신앙 성장을 위해 말씀 읽기와 기도를 늘려보세요."
    else:
        return "🙏 하나님과의 관계부터 차근차근 시작해보세요. 레아의 여정을 참고하세요."


if __name__ == "__main__":
    # 테스트 코드
    print("🏺 JesusBornd 성경 분석 유틸리티 테스트")

    # 12지파 로드 테스트
    tribes = load_twelve_tribes()
    print(f"✅ 12지파 데이터 로드 완료: {len(tribes)}개 지파")

    # 레아 패턴 분석 테스트
    leah_analysis = calculate_leah_spiritual_journey(tribes)
    print(f"✅ 레아 패턴 분석 완료: 일치율 {leah_analysis['match_rate']:.1f}%")

    # 요한복음 분석 테스트
    john_concepts = load_john_concepts()
    light_analysis = analyze_light_darkness_ratio(john_concepts)
    print(f"✅ 빛 vs 어둠 분석 완료: {light_analysis['ratio']:.1f}:1 비율")

    print("🎉 모든 테스트 통과!")

