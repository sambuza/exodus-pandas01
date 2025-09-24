"""
Chapter 01 시각화 모듈 - 한글 폰트 수정 버전
출애굽기 × 요한복음의 시각적 표현

"말씀이 육신이 되어" - 데이터가 그래프가 되다
"""

# ===== 한글 폰트 설정 (가장 중요!) =====
from matplotlib import rc
rc('font', family='Malgun Gothic')  # Windows에서 가장 확실한 방법

import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

import numpy as np
from pathlib import Path
import sys


# 프로젝트 루트 경로 설정
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))
# ================== 시각화 설정 ==================
# 색상 팔레트 (프로젝트 브랜드 컬러)
COLORS = {
    'primary': '#800080',      # Purple - 왕권
    'secondary': '#228B22',    # Green - 생명
    'accent': '#9B30FF',       # Violet - 성령
    'warning': '#FF6B35',      # Orange - 경고
    'success': '#4CAF50',      # Green - 성공
    'gradient': ['#800080', '#9B30FF', '#C71585', '#228B22', '#66CDAA', '#90EE90']
}

# 시각화 기본 설정

plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['figure.dpi'] = 100

# utils 임포트
from utils.bible_utils import (
    load_twelve_tribes,
    load_john_concepts,
    calculate_leah_spiritual_journey
)

def plot_tribes_by_mother():
    """어머니별 12지파 분포 시각화"""

    print("👥 어머니별 분포 차트 생성...")

    tribes_df = load_twelve_tribes()

    # 어머니별 집계
    mother_counts = tribes_df['mother'].value_counts()

    # 파이 차트
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # 파이차트
    colors_pie = [COLORS['gradient'][i % len(COLORS['gradient'])]
                  for i in range(len(mother_counts))]
    wedges, texts, autotexts = ax1.pie(mother_counts.values,
                                        labels=mother_counts.index,
                                        colors=colors_pie,
                                        autopct='%1.1f%%',
                                        startangle=90)

    # 폰트 크기 조정
    for text in texts:
        text.set_fontsize(12)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        autotext.set_weight('bold')

    ax1.set_title('👥 어머니별 아들 분포', fontsize=14, fontweight='bold')

    # 막대 그래프
    bars = ax2.bar(mother_counts.index, mother_counts.values,
                   color=colors_pie, edgecolor='black', linewidth=1.5)

    # 값 표시
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}명',
                ha='center', va='bottom', fontweight='bold')

    ax2.set_xlabel('어머니 이름', fontsize=12)
    ax2.set_ylabel('아들 수', fontsize=12)
    ax2.set_title('하나님의 공평하심은 사람을 통해', fontsize=14, fontweight='bold')
    ax2.set_ylim(0, max(mother_counts.values) + 1)

    # 그리드 추가
    ax2.grid(True, alpha=0.3)

    plt.suptitle('이스라엘 12지파 - 어머니들의 이야기',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

    return fig

def plot_leah_spiritual_journey():
    """레아의 신앙 여정 시각화"""

    print("💝 레아의 신앙 여정 차트 생성...")

    tribes_df = load_twelve_tribes()
    journey = calculate_leah_spiritual_journey(tribes_df)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # 상단: 4단계 여정 곡선
    stages = journey['first_four_sons']
    x = np.arange(len(stages))

    # 신앙 성장 곡선 (임의의 성장 수치)
    growth_values = [3, 5, 7, 9]  # 점진적 성장

    # 곡선 그래프
    ax1.plot(x, growth_values, 'o-', color=COLORS['primary'],
             linewidth=3, markersize=10)

    # 각 단계 표시
    for i, (name, theme) in enumerate(zip(stages, journey['actual_stages'])):
        ax1.annotate(f"{name}\n({theme})",
                    xy=(i, growth_values[i]),
                    xytext=(0, 20),
                    textcoords='offset points',
                    ha='center',
                    bbox=dict(boxstyle='round,pad=0.5',
                             fc=COLORS['gradient'][i], alpha=0.7),
                    fontweight='bold')

    ax1.set_xlim(-0.5, 3.5)
    ax1.set_ylim(0, 10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(['1단계', '2단계', '3단계', '4단계'])
    ax1.set_ylabel('신앙 성장도', fontsize=12)
    ax1.set_title('💝 레아의 4단계 신앙 여정', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # 하단: 패턴 매칭 시각화
    expected = journey['expected_pattern']
    actual = journey['actual_stages']

    # 매칭 결과
    categories = ['관계', '소통', '연합', '예배']
    x_pos = np.arange(len(categories))

    # 기대값과 실제값 비교
    match_colors = ['green' if e == a else 'red'
                   for e, a in zip(expected, actual)]

    bars = ax2.bar(x_pos, [1]*4, color=match_colors, alpha=0.6,
                   edgecolor='black', linewidth=2)

    # 레이블 추가
    for i, (exp, act) in enumerate(zip(expected, actual)):
        match_text = "✓" if exp == act else "✗"
        ax2.text(i, 0.5, f"{match_text}\n{act}",
                ha='center', va='center',
                fontsize=11, fontweight='bold')

    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(categories)
    ax2.set_ylim(0, 1.2)
    ax2.set_ylabel('패턴 일치도', fontsize=12)
    ax2.set_title(f"레아의 신앙 패턴 vs 기대 패턴 (일치율: {journey['match_rate']:.1f}%)",
                  fontsize=14, fontweight='bold')
    ax2.set_yticks([])

    plt.suptitle('레아 - 사랑받지 못한 자의 승리',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

    return fig

def plot_john_concepts_importance():
    """요한복음 핵심 개념 중요도 시각화"""

    print("🎯 요한복음 개념 중요도 차트 생성...")

    john_df = load_john_concepts()

    # 중요도 순으로 정렬
    john_df_sorted = john_df.sort_values('theological_importance', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 8))

    # 수평 막대 그래프
    y_pos = np.arange(len(john_df_sorted))
    bars = ax.barh(y_pos, john_df_sorted['theological_importance'].values,
                   color=COLORS['gradient'][:len(john_df_sorted)])

    # 값 표시
    for i, (idx, row) in enumerate(john_df_sorted.iterrows()):
        value = row['theological_importance']
        freq = row['frequency_ch1']
        ax.text(value + 0.1, i, f'{value:.0f} (빈도: {freq})',
               va='center', fontweight='bold')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(john_df_sorted['korean_name'].values)
    ax.set_xlabel('신학적 중요도', fontsize=12)
    ax.set_title('🎯 요한복음 1장 핵심 개념들', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 11)

    # 중요도 구간 표시
    ax.axvline(x=5, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=8, color='red', linestyle='--', alpha=0.5)
    ax.text(2.5, len(john_df_sorted)-0.5, '보통', ha='center', fontweight='bold')
    ax.text(6.5, len(john_df_sorted)-0.5, '중요', ha='center', fontweight='bold')
    ax.text(9.5, len(john_df_sorted)-0.5, '핵심', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.show()

    return fig

def plot_light_darkness_contrast():
    """빛과 어둠의 대조 시각화"""

    print("💡 빛 vs 어둠 대조 차트 생성...")

    # 요한복음 1장의 빛/어둠 등장 빈도 (예시 데이터)
    verses = ['1:4-5', '1:7-8', '1:9']
    light_freq = [2, 3, 1]
    darkness_freq = [1, 0, 1]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # 막대 그래프 - 비교
    x = np.arange(len(verses))
    width = 0.35

    bars1 = ax1.bar(x - width/2, light_freq, width, label='빛',
                    color=COLORS['warning'], edgecolor='black')
    bars2 = ax1.bar(x + width/2, darkness_freq, width, label='어둠',
                    color='#2C3E50', edgecolor='black')

    ax1.set_xlabel('구절', fontsize=12)
    ax1.set_ylabel('등장 빈도', fontsize=12)
    ax1.set_title('💡 빛과 어둠의 대조', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(verses)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 도넛 차트 - 비율
    total_light = sum(light_freq)
    total_darkness = sum(darkness_freq)

    sizes = [total_light, total_darkness]
    colors_donut = [COLORS['warning'], '#2C3E50']
    explode = (0.1, 0)

    ax2.pie(sizes, explode=explode, labels=['빛', '어둠'],
            colors=colors_donut, autopct='%1.1f%%',
            shadow=True, startangle=90)

    # 도넛 효과
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    ax2.add_artist(centre_circle)

    ax2.set_title('⚖️ 빛과 어둠의 비율', fontsize=14, fontweight='bold')

    # 중앙 텍스트
    ax2.text(0, 0, '신학적\n중요도', ha='center', va='center',
            fontsize=12, fontweight='bold')

    plt.suptitle('"빛이 어둠에 비치되 어둠이 깨닫지 못하더라" (요 1:5)',
                 fontsize=14, style='italic', y=1.02)
    plt.tight_layout()
    plt.show()

    return fig

def create_comprehensive_dashboard():
    """종합 대시보드 생성"""

    print("📊 종합 대시보드 생성...")

    tribes_df = load_twelve_tribes()
    john_df = load_john_concepts()

    fig = plt.figure(figsize=(16, 10))

    # 2x2 그리드 생성
    ax1 = plt.subplot(2, 2, 1)
    ax2 = plt.subplot(2, 2, 2)
    ax3 = plt.subplot(2, 2, 3)
    ax4 = plt.subplot(2, 2, 4)

    # 1. 12지파 어머니별 분포
    mother_counts = tribes_df['mother'].value_counts()
    colors_pie = [COLORS['gradient'][i % len(COLORS['gradient'])]
                  for i in range(len(mother_counts))]
    ax1.pie(mother_counts.values, labels=mother_counts.index,
            colors=colors_pie, autopct='%1.1f%%', startangle=90)
    ax1.set_title('👥 12지파 어머니별 분포', fontsize=12, fontweight='bold')

    # 2. 레아의 4단계
    leah_sons = tribes_df[tribes_df['mother'] == '레아'].head(4)
    stages = ['관계', '소통', '연합', '예배']
    x = np.arange(len(stages))
    ax2.bar(x, [1, 2, 3, 4], color=COLORS['gradient'][:4])
    ax2.set_xticks(x)
    ax2.set_xticklabels(stages)
    ax2.set_title('💝 레아의 4단계 신앙 여정', fontsize=12, fontweight='bold')
    ax2.set_ylabel('단계')

    # 3. 요한복음 핵심 개념
    top_concepts = john_df.nlargest(5, 'theological_importance')
    ax3.barh(range(5), top_concepts['theological_importance'].values,
             color=COLORS['gradient'][:5])
    ax3.set_yticks(range(5))
    ax3.set_yticklabels(top_concepts['korean_name'].values)
    ax3.set_title('🎯 요한복음 1장 핵심 개념', fontsize=12, fontweight='bold')
    ax3.set_xlabel('신학적 중요도')

    # 4. 빛과 어둠
    light_dark = [7, 3]  # 빛 70%, 어둠 30%
    ax4.pie(light_dark, labels=['빛', '어둠'],
            colors=[COLORS['warning'], '#2C3E50'],
            autopct='%1.1f%%', explode=(0.1, 0))
    ax4.set_title('💡 빛과 어둠의 대조', fontsize=12, fontweight='bold')

    plt.suptitle('🧬 개인 영적 DNA 성숙도 - 태초에 DataFrame',
                 fontsize=16, fontweight='bold', y=1.02)

    # 전체 설명 추가
    fig.text(0.5, 0.02,
             '📊 "태초에 말씀이 계시니라" - 데이터로 본 하나님의 계획',
             ha='center', fontsize=12, style='italic')

    plt.tight_layout()
    plt.show()

    return fig

def demo_all_visualizations():
    """모든 시각화 데모 실행"""

    print("🎨 Chapter 01 시각화 데모 시작...")

    # 1. 어머니별 분포
    plot_tribes_by_mother()

    # 2. 레아의 신앙 여정
    plot_leah_spiritual_journey()

    # 3. 요한복음 개념 중요도
    plot_john_concepts_importance()

    # 4. 빛과 어둠 대조
    plot_light_darkness_contrast()

    # 5. 종합 대시보드
    create_comprehensive_dashboard()

    print("🎉 시각화 데모 완료!")

if __name__ == "__main__":
    demo_all_visualizations()