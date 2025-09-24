"""
JesusBornd Pandas Edition - 챕터 패키지
출애굽기 × 요한복음 = 40일 데이터 여정

"태초에 말씀이 계시니라" (요 1:1) - 모든 분석의 시작점

이 패키지는 40개 챕터로 구성된 성경적 데이터사이언스 여정을 제공합니다.
각 챕터는 출애굽기의 한 장과 요한복음의 구절을 블렌딩하여
판다스의 기능을 배우면서 동시에 영적 통찰을 얻을 수 있도록 설계되었습니다.
"""

from pathlib import Path
import importlib
import sys

__version__ = "1.0.0"
__author__ = "신동혁(Dave)"
__series__ = "JesusBornd Pandas Edition"
__total_chapters__ = 40

# 현재 구현된 챕터들
AVAILABLE_CHAPTERS = [1]  # Chapter 01만 현재 구현됨

# 챕터 정보
CHAPTER_INFO = {
    1: {
        "title": "태초에 DataFrame — 데이터의 탄생",
        "exodus": "출애굽기 1장 - 이스라엘이 애굽에서 번성하다",
        "john": "요한복음 1:1-14 - 태초에 말씀이 계시니라",
        "skills": ["DataFrame 생성", "기본 탐색", "패턴 분석"],
        "status": "완료"
    },
    2: {
        "title": "나일강에서 건진 데이터 — read_csv 입문",
        "exodus": "출애굽기 2장 - 모세의 출생과 구원",
        "john": "요한복음 1:29 - 보라 하나님의 어린양",
        "skills": ["CSV 읽기", "인코딩 처리", "구분자 설정"],
        "status": "계획됨"
    },
    3: {
        "title": "불붙는 떨기나무와 인덱스의 부름",
        "exodus": "출애굽기 3장 - 하나님의 부르심",
        "john": "요한복음 1:35-39 - 와서 보라",
        "skills": ["인덱스 설정", "재설정", "다중인덱스"],
        "status": "계획됨"
    }
    # ... 나머지 37개 챕터는 미래 구현
}

def list_chapters():
    """사용 가능한 챕터들 목록 출력"""
    print("🗂️ === JesusBornd 챕터 목록 ===\n")

    for ch_num in sorted(CHAPTER_INFO.keys()):
        info = CHAPTER_INFO[ch_num]
        status_emoji = "✅" if ch_num in AVAILABLE_CHAPTERS else "📋"

        print(f"{status_emoji} Chapter {ch_num:02d}: {info['title']}")
        print(f"   📖 {info['exodus']}")
        print(f"   📜 {info['john']}")
        print(f"   🔧 기술: {', '.join(info['skills'])}")
        print(f"   📊 상태: {info['status']}\n")

def get_chapter(chapter_num: int):
    """특정 챕터 모듈 동적 임포트"""
    if chapter_num not in AVAILABLE_CHAPTERS:
        available = ', '.join(map(str, AVAILABLE_CHAPTERS))
"""
JesusBornd Pandas Edition - 챕터 패키지
출애굽기 × 요한복음 = 40일 데이터 여정

"태초에 말씀이 계시니라" (요 1:1) - 모든 분석의 시작점

이 패키지는 40개 챕터로 구성된 성경적 데이터사이언스 여정을 제공합니다.
각 챕터는 출애굽기의 한 장과 요한복음의 구절을 블렌딩하여
판다스의 기능을 배우면서 동시에 영적 통찰을 얻을 수 있도록 설계되었습니다.
"""

from pathlib import Path
import importlib
import sys

__version__ = "1.0.0"
__author__ = "신동혁(Dave)"
__series__ = "JesusBornd Pandas Edition"
__total_chapters__ = 40

# 현재 구현된 챕터들
AVAILABLE_CHAPTERS = [1]  # Chapter 01만 현재 구현됨

# 챕터 정보
CHAPTER_INFO = {
    1: {
        "title": "태초에 DataFrame — 데이터의 탄생",
        "exodus": "출애굽기 1장 - 이스라엘이 애굽에서 번성하다",
        "john": "요한복음 1:1-14 - 태초에 말씀이 계시니라",
        "skills": ["DataFrame 생성", "기본 탐색", "패턴 분석"],
        "status": "완료"
    },
    2: {
        "title": "나일강에서 건진 데이터 — read_csv 입문",
        "exodus": "출애굽기 2장 - 모세의 출생과 구원",
        "john": "요한복음 1:29 - 보라 하나님의 어린양",
        "skills": ["CSV 읽기", "인코딩 처리", "구분자 설정"],
        "status": "계획됨"
    },
    3: {
        "title": "불붙는 떨기나무와 인덱스의 부름",
        "exodus": "출애굽기 3장 - 하나님의 부르심",
        "john": "요한복음 1:35-39 - 와서 보라",
        "skills": ["인덱스 설정", "재설정", "다중인덱스"],
        "status": "계획됨"
    }
    # ... 나머지 37개 챕터는 미래 구현
}

def list_chapters():
    """사용 가능한 챕터들 목록 출력"""
    print("🗂️ === JesusBornd 챕터 목록 ===\n")

    for ch_num in sorted(CHAPTER_INFO.keys()):
        info = CHAPTER_INFO[ch_num]
        status_emoji = "✅" if ch_num in AVAILABLE_CHAPTERS else "📋"

        print(f"{status_emoji} Chapter {ch_num:02d}: {info['title']}")
        print(f"   📖 {info['exodus']}")
        print(f"   📜 {info['john']}")
        print(f"   🔧 기술: {', '.join(info['skills'])}")
        print(f"   📊 상태: {info['status']}\n")

def get_chapter(chapter_num: int):
    """특정 챕터 모듈 동적 임포트"""
    if chapter_num not in AVAILABLE_CHAPTERS:
        available = ', '.join(map(str, AVAILABLE_CHAPTERS))
        raise ImportError(f"Chapter {chapter_num:02d}는 아직 구현되지 않았습니다. 사용 가능: {available}")

    module_name = f"chapters.ch{chapter_num:02d}"
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        raise ImportError(f"Chapter {chapter_num:02d} 모듈을 불러올 수 없습니다: {e}")

def run_chapter(chapter_num: int, **kwargs):
    """특정 챕터 실행"""
    chapter_module = get_chapter(chapter_num)

    if hasattr(chapter_module, f'run_chapter{chapter_num:02d}'):
        run_func = getattr(chapter_module, f'run_chapter{chapter_num:02d}')
        return run_func(**kwargs)
    else:
        raise AttributeError(f"Chapter {chapter_num:02d}에 실행 함수가 없습니다.")

# 빠른 접근 함수들
def ch01(**kwargs):
    """Chapter 01 빠른 실행"""
    return run_chapter(1, **kwargs)

# 전체 시리즈 정보 출력
def series_info():
    """시리즈 전체 정보 출력"""
    print("📚 === JesusBornd Pandas Edition ===")
    print(f"   버전: {__version__}")
    print(f"   저자: {__author__}")
    print(f"   총 챕터: {__total_chapters}개")
    print(f"   구현됨: {len(AVAILABLE_CHAPTERS)}개")
    print(f"   진행률: {len(AVAILABLE_CHAPTERS)/__total_chapters*100:.1f}%")

    print(f"\n🎯 목적: 복음과 코딩을 통합한 학습 여정")
    print(f"📖 구조: 출애굽기(스토리) × 요한복음(데이터) × 판다스(도구)")

    list_chapters()

if __name__ == "__main__":
    series_info()