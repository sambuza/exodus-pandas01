"""
JesusBornd Pandas Edition - Chapter 02
나일강에서 건진 데이터 — read_csv 입문

"바로의 딸이 그를 아들로 삼고 그의 이름을 모세라 하여 이르되 
이는 내가 그를 물에서 건져내었음이라" (출 2:10)

이 챕터는 CSV 파일을 갈대상자에 비유하여,
데이터를 안전하게 저장하고 읽는 방법을 배웁니다.
"""

from pathlib import Path
import sys

__version__ = "1.0.0"
__author__ = "신동혁(Dave)"
__chapter__ = 2
__title__ = "나일강에서 건진 데이터 — read_csv 입문"

# 챕터 정보
CHAPTER_INFO = {
    'number': 2,
    'title': '나일강에서 건진 데이터 — read_csv 입문',
    'exodus': '출애굽기 2장 - 모세의 출생과 구원',
    'john': '요한복음 1:29 - 보라 하나님의 어린양',
    'skills': [
        'CSV 파일 읽기 (pd.read_csv)',
        '인코딩 처리 (utf-8, cp949 등)',
        '결측치 탐색과 처리',
        '구분자 설정과 옵션 활용'
    ],
    'key_concepts': [
        '갈대상자 = CSV 파일',
        '나일강 = 파일 시스템',
        '바로의 딸 = read_csv() 함수',
        '숨겨진 모세 = 결측치',
        '언어 장벽 = 인코딩 문제',
        '어린양 발견 = 데이터 인식'
    ],
    'status': '완료'
}

# 모듈 임포트 정리
from .moses_rescue import (
    MosesRescueAnalyzer,
    demo_moses_rescue
)

from .lamb_discovery import (
    LambDiscoveryAnalyzer,
    demo_lamb_discovery
)

from .csv_journey import (
    PersonalCSVJourney,
    demo_personal_csv_journey
)

from .__main__ import (
    run_chapter02,
    print_chapter_header,
    run_exodus_analysis,
    run_john_analysis,
    run_personal_analysis
)

# 챕터 실행 함수
def run():
    """챕터 02 실행"""
    from .__main__ import main
    return main()

def info():
    """챕터 정보 출력"""
    print(f"📚 === Chapter {CHAPTER_INFO['number']:02d} ===")
    print(f"제목: {CHAPTER_INFO['title']}")
    print(f"출애굽기: {CHAPTER_INFO['exodus']}")
    print(f"요한복음: {CHAPTER_INFO['john']}")
    print(f"\n🔧 학습할 기술:")
    for skill in CHAPTER_INFO['skills']:
        print(f"   • {skill}")
    print(f"\n💡 핵심 개념:")
    for concept in CHAPTER_INFO['key_concepts']:
        print(f"   • {concept}")
    print(f"\n상태: {CHAPTER_INFO['status']}")

def quick_start():
    """빠른 시작 가이드"""
    guide = """
🚀 === Chapter 02 빠른 시작 가이드 ===

1. 전체 챕터 실행:
   from chapters.ch02 import run
   run()

2. 개별 모듈 실행:
   from chapters.ch02 import demo_moses_rescue
   from chapters.ch02 import demo_lamb_discovery
   from chapters.ch02 import demo_personal_csv_journey
   
   # 각각 실행
   moses_results = demo_moses_rescue()
   lamb_results = demo_lamb_discovery()
   personal_results = demo_personal_csv_journey("내이름")

3. 분석기 직접 사용:
   from chapters.ch02 import MosesRescueAnalyzer
   analyzer = MosesRescueAnalyzer()
   results = analyzer.run_complete_analysis()

4. CSV 파일 실습:
   import pandas as pd
   
   # 갈대상자 만들기 (CSV 저장)
   df = pd.DataFrame({'name': ['Moses'], 'age': [80]})
   df.to_csv('basket.csv', index=False)
   
   # 나일강에서 건지기 (CSV 읽기)
   rescued_df = pd.read_csv('basket.csv')
   print(rescued_df.head())  # "보라!"
    """
    print(guide)

def get_sample_code():
    """샘플 코드 반환"""
    sample = """
# Chapter 02 핵심 코드 예제

import pandas as pd

# 1. 기본 CSV 읽기 (갈대상자 열기)
df = pd.read_csv('data.csv')

# 2. 인코딩 처리 (언어 장벽 극복)
df_korean = pd.read_csv('korean.csv', encoding='utf-8-sig')

# 3. 결측치 찾기 (숨겨진 모세)
missing_count = df.isnull().sum()
print(f"결측치: {missing_count}")

# 4. 결측치 처리 (은혜로 채우기)
df_filled = df.fillna('기본값')  # 은혜
df_filled = df.fillna(method='ffill')  # 믿음
df_dropped = df.dropna()  # 진리

# 5. 첫 발견 (보라!)
print(df.head())  # 데이터의 첫 5행
print(df.info())  # 데이터 정보
print(df.describe())  # 통계 요약
    """
    return sample

def chapter_summary():
    """챕터 요약"""
    summary = {
        'chapter': 2,
        'title': CHAPTER_INFO['title'],
        'main_function': 'pd.read_csv()',
        'spiritual_parallel': '모세의 구출 = 데이터의 구출',
        'key_learning': [
            'CSV 파일은 갈대상자처럼 데이터를 보호한다',
            'read_csv()는 바로의 딸처럼 데이터를 발견한다',
            '결측치는 숨겨진 모세처럼 찾아야 한다',
            '인코딩은 언어 장벽처럼 극복해야 한다'
        ],
        'practice_files': [
            'moses_family.csv',
            'faith_journey.csv',
            'biblical_genealogy.csv'
        ],
        'next_chapter': {
            'number': 3,
            'title': '불타는 떨기나무와 인덱스의 부름',
            'preview': '인덱스를 통한 정확한 데이터 선택'
        }
    }
    return summary

# 전역 상수
CSV_ENCODINGS = ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr', 'latin-1']
FILL_STRATEGIES = ['grace', 'wisdom', 'faith', 'truth']
MOSES_RESCUE_STAGES = ['preparation', 'placement', 'discovery', 'identification']

# 유틸리티 함수
def test_encoding(filepath, encodings=None):
    """여러 인코딩 테스트"""
    if encodings is None:
        encodings = CSV_ENCODINGS
    
    results = []
    for encoding in encodings:
        try:
            pd.read_csv(filepath, encoding=encoding)
            results.append((encoding, True, 'Success'))
        except Exception as e:
            results.append((encoding, False, str(e)[:50]))
    
    return results

def analyze_missing_data(df):
    """결측치 분석 헬퍼"""
    analysis = {
        'total_missing': df.isnull().sum().sum(),
        'missing_by_column': df.isnull().sum().to_dict(),
        'missing_ratio': (df.isnull().sum() / len(df) * 100).to_dict(),
        'complete_rows': len(df.dropna()),
        'incomplete_rows': len(df) - len(df.dropna())
    }
    return analysis

# 챕터 진입점
def main():
    """메인 실행 함수"""
    from .__main__ import main as chapter_main
    return chapter_main()

# 모든 내보내기
__all__ = [
    # 메인 실행
    'run',
    'run_chapter02',
    'main',
    
    # 분석기 클래스
    'MosesRescueAnalyzer',
    'LambDiscoveryAnalyzer', 
    'PersonalCSVJourney',
    
    # 데모 함수
    'demo_moses_rescue',
    'demo_lamb_discovery',
    'demo_personal_csv_journey',
    
    # 유틸리티
    'info',
    'quick_start',
    'get_sample_code',
    'chapter_summary',
    'test_encoding',
    'analyze_missing_data',
    
    # 상수
    'CSV_ENCODINGS',
    'FILL_STRATEGIES',
    'MOSES_RESCUE_STAGES',
    'CHAPTER_INFO'
]

if __name__ == "__main__":
    info()
    print("\n" + "="*50 + "\n")
    quick_start()