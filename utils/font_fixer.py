"""
JesusBornd 한글 폰트 설정 자동화 스크립트
matplotlib 한글 깨짐 현상을 완벽하게 해결합니다.
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
from pathlib import Path


def setup_korean_font():
    """시스템에 맞는 한글 폰트를 자동으로 설정"""

    # matplotlib 캐시 초기화
    try:
        cache_dir = Path.home() / '.matplotlib'
        if cache_dir.exists():
            for cache_file in cache_dir.glob('*.cache'):
                cache_file.unlink()
            print("✅ matplotlib 캐시 초기화 완료")
    except:
        pass

    # 폰트 매니저 재구성
    fm._load_fontmanager(try_read_cache=False)

    # 사용 가능한 한글 폰트 찾기
    korean_fonts = []
    for font in fm.fontManager.ttflist:
        if 'malgun' in font.name.lower() or 'gothic' in font.name.lower():
            korean_fonts.append(font.name)

    # 중복 제거
    korean_fonts = list(set(korean_fonts))

    print("\n🔍 발견된 한글 폰트:")
    for i, font in enumerate(korean_fonts, 1):
        print(f"  {i}. {font}")

    # 우선순위대로 폰트 설정 시도
    font_priority = ['Malgun Gothic', 'NanumGothic', 'NanumBarunGothic',
                     'D2Coding', 'Gulim', 'Dotum', 'Batang']

    selected_font = None
    for priority_font in font_priority:
        if priority_font in korean_fonts:
            selected_font = priority_font
            break

    # 못 찾으면 첫 번째 한글 폰트 사용
    if not selected_font and korean_fonts:
        selected_font = korean_fonts[0]

    if selected_font:
        # matplotlib 설정 변경
        plt.rcParams['font.family'] = selected_font
        plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

        print(f"\n✅ '{selected_font}' 폰트로 설정 완료!")

        # 설정 파일 생성
        save_matplotlib_config(selected_font)

        return selected_font
    else:
        print("\n❌ 한글 폰트를 찾을 수 없습니다.")
        print("한글 폰트를 설치해주세요: https://hangeul.naver.com/font")
        return None


def save_matplotlib_config(font_name):
    """matplotlib 설정을 파일로 저장"""

    config_content = f"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# JesusBornd 한글 폰트 설정
plt.rcParams['font.family'] = '{font_name}'
plt.rcParams['axes.unicode_minus'] = False

print("✅ JesusBornd 한글 폰트 설정 로드 완료: {font_name}")
"""

    # utils 폴더에 설정 파일 저장
    utils_dir = Path('utils')
    utils_dir.mkdir(exist_ok=True)

    config_file = utils_dir / 'font_config.py'
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(config_content)

    print(f"📁 설정 파일 생성: {config_file}")

    # .matplotlibrc 파일도 생성
    rc_content = f"""
font.family : {font_name}
axes.unicode_minus : False
"""

    with open('.matplotlibrc', 'w', encoding='utf-8') as f:
        f.write(rc_content)

    print("📁 .matplotlibrc 파일 생성 완료")


def test_korean_font():
    """한글 폰트 테스트"""

    print("\n🧪 한글 폰트 테스트 시작...")

    # 테스트 그래프 생성
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 12지파 예시 데이터
    tribes = ['르우벤', '시므온', '레위', '유다', '단', '납달리']
    birth_order = [1, 2, 3, 4, 5, 6]

    # 막대 그래프
    ax1.bar(tribes, birth_order, color=['#800080', '#9B30FF', '#228B22',
                                        '#66CDAA', '#90EE90', '#C71585'])
    ax1.set_title('야곱의 12지파 - 출생 순서', fontsize=14, fontweight='bold')
    ax1.set_xlabel('지파명')
    ax1.set_ylabel('출생 순서')
    ax1.grid(True, alpha=0.3)

    # 요한복음 개념 파이차트
    concepts = ['말씀(λόγος)', '빛', '생명', '은혜', '진리']
    frequencies = [7, 5, 4, 3, 2]
    colors = ['#800080', '#9B30FF', '#228B22', '#66CDAA', '#90EE90']

    ax2.pie(frequencies, labels=concepts, colors=colors, autopct='%1.1f%%')
    ax2.set_title('요한복음 1장 핵심 개념', fontsize=14, fontweight='bold')

    plt.suptitle('JesusBornd 판다스 - 한글 폰트 테스트', fontsize=16, fontweight='bold')
    plt.tight_layout()

    # 테스트 이미지 저장
    output_file = 'korean_font_test.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n✅ 테스트 이미지 저장 완료: {output_file}")

    plt.show()

    print("\n🎉 한글이 정상적으로 표시되면 성공입니다!")


def main():
    print("=" * 60)
    print("    JesusBornd 한글 폰트 자동 설정 도구")
    print("    '태초에 말씀이 계시니라' - 한글도 아름답게!")
    print("=" * 60)

    # 한글 폰트 설정
    selected_font = setup_korean_font()

    if selected_font:
        # 테스트 실행
        test_korean_font()

        print("\n📌 이제 모든 파이썬 파일 상단에 다음 줄을 추가하세요:")
        print("    from utils.font_config import *")
        print("\n또는 각 파일에서 직접 설정:")
        print(f"    import matplotlib.pyplot as plt")
        print(f"    plt.rcParams['font.family'] = '{selected_font}'")
        print(f"    plt.rcParams['axes.unicode_minus'] = False")

    print("\n✅ 설정 완료!")
    print("다음 행동:")
    print("1. python font_fixer.py 실행하여 한글 폰트 설정")
    print("2. 생성된 korean_font_test.png 확인")
    print("3. 모든 분석 파일에 from utils.font_config import * 추가")


if __name__ == "__main__":
    main()