
import matplotlib
matplotlib.use('Agg') # Set backend before importing pyplot

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 프로젝트 루트 추가 (필요시)
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

from font_checker import check_korean_fonts

def set_korean_font():
    font_found = False

    # 1. Malgun Gothic 시도 (Windows 기본 한글 폰트)
    if sys.platform == 'win32':
        if 'Malgun Gothic' in [f.name for f in fm.fontManager.ttflist]:
            plt.rcParams['font.family'] = ['Malgun Gothic']
            print("✅ JesusBornd 한글 폰트 설정 로드 완료: Malgun Gothic")
            font_found = True

    # 2. NanumGothic 시도 (리눅스/맥 등에서 흔히 사용되는 오픈소스 한글 폰트)
    if not font_found:
        if 'NanumGothic' in [f.name for f in fm.fontManager.ttflist]:
            plt.rcParams['font.family'] = ['NanumGothic']
            print("✅ JesusBornd 한글 폰트 설정 로드 완료: NanumGothic")
            font_found = True

    # 3. 시스템에서 사용 가능한 다른 한글 폰트 찾기
    if not font_found:
        korean_fonts = check_korean_fonts()
        if korean_fonts:
            best_font_name = korean_fonts[0][0] # 첫 번째 찾은 폰트 사용
            plt.rcParams['font.family'] = [best_font_name]
            print(f"✅ JesusBornd 한글 폰트 설정 로드 완료: {best_font_name}")
            font_found = True

    # 4. 모든 시도 실패 시 기본 폰트 사용
    if not font_found:
        print("❌ 시스템에서 한글 폰트를 찾을 수 없습니다. 기본 폰트로 설정됩니다.")
        plt.rcParams['font.family'] = ['sans-serif']
    
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 부호 깨짐 방지

# 함수 호출
set_korean_font()
