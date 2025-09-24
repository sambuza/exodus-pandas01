# utils/font_config.py
"""
JesusBornd 프로젝트 한글 폰트 설정
모든 시각화 파일에서 이 설정을 import하여 사용
"""

from matplotlib import rc
rc('font', family='Malgun Gothic')

import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False

print("✅ 한글 폰트 설정 로드 (Malgun Gothic)")