"""
시스템에 설치된 한글 폰트 확인
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def check_korean_fonts():
    """시스템에 설치된 한글 폰트 찾기"""
    font_list = fm.findSystemFonts()
    korean_fonts = []

    for font_path in font_list:
        try:
            font_prop = fm.FontProperties(fname=font_path)
            font_name = font_prop.get_name()

            # 한글 폰트 키워드로 필터링
            korean_keywords = [
                'Gothic', 'Malgun', 'Batang', 'Dotum', 'Gulim', 'Gungsuh',
                'Nanum', 'NotoSans', 'Apple', '맑은', '굴림', '바탕', '궁서'
            ]

            if any(keyword in font_name for keyword in korean_keywords):
                korean_fonts.append((font_name, font_path))

        except Exception:
            continue

    return korean_fonts


def test_fonts():
    """한글 폰트 테스트"""
    korean_fonts = check_korean_fonts()

    print("🔍 시스템에서 발견된 한글 폰트들:")
    for i, (name, path) in enumerate(korean_fonts[:10], 1):  # 상위 10개만
        print(f"  {i}. {name}")

    if korean_fonts:
        # 첫 번째 폰트로 테스트
        best_font = korean_fonts[0][0]
        print(f"\n✅ 추천 폰트: {best_font}")

        # 간단한 한글 테스트
        plt.rcParams['font.family'] = [best_font]
        plt.rcParams['axes.unicode_minus'] = False

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(0.5, 0.5, '한글 테스트: 레아의 신앙 여정',
                fontsize=16, ha='center', va='center')
        ax.set_title('한글 폰트 테스트')
        plt.tight_layout()
        plt.show()

        return best_font
    else:
        print("❌ 한글 폰트를 찾을 수 없습니다.")
        return None


if __name__ == "__main__":
    test_fonts()