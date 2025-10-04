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
from math import pi

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

class ChapterVisualizations:
    """
    Chapter 01의 모든 시각화 기능을 포함하는 클래스
    """
    # 테스트가 요구하는 'colors' 속성 추가
    colors = COLORS

    @staticmethod
    def plot_mothers_distribution(tribes_df=None):
        """어머니별 12지파 분포 시각화"""

        print("👥 어머니별 분포 차트 생성...")
        if tribes_df is None:
            tribes_df = load_twelve_tribes()

        # 어머니별 집계
        mother_counts = tribes_df['mother'].value_counts()

        fig, ax = plt.subplots(figsize=(10, 8))

        # 막대 그래프
        colors_bar = [ChapterVisualizations.colors['gradient'][i % len(ChapterVisualizations.colors['gradient'])]
                    for i in range(len(mother_counts))]
        bars = ax.bar(mother_counts.index, mother_counts.values,
                    color=colors_bar, edgecolor='black', linewidth=1.5)

        # 값과 백분율 표시
        total_tribes = mother_counts.sum()
        for bar in bars:
            height = bar.get_height()
            percentage = (height / total_tribes) * 100
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}명\n({percentage:.1f}%)',
                    ha='center', va='bottom', fontweight='bold')

        ax.set_xlabel('어머니 이름', fontsize=12)
        ax.set_ylabel('아들 수', fontsize=12)
        ax.set_title('👥 이스라엘 12지파 - 어머니들의 분포', fontsize=14, fontweight='bold')
        ax.set_ylim(0, max(mother_counts.values) + 2)

        # 그리드 추가
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

        return fig

    @staticmethod
    def plot_leah_spiritual_journey(tribes_df=None):
        """레아의 신앙 여정 시각화"""

        print("💝 레아의 신앙 여정 차트 생성...")
        if tribes_df is None:
            tribes_df = load_twelve_tribes()

        journey = calculate_leah_spiritual_journey(tribes_df)

        fig, ax = plt.subplots(figsize=(12, 8))

        # 4단계 여정 곡선
        stages = journey['first_four_sons']
        x = np.arange(len(stages))

        # 신앙 성장 곡선 (임의의 성장 수치)
        growth_values = [3, 5, 7, 9]  # 점진적 성장

        # 곡선 그래프
        ax.plot(x, growth_values, 'o-', color=ChapterVisualizations.colors['primary'],
                linewidth=3, markersize=10, label='신앙 성장도')

        # 각 단계 표시
        for i, (name, theme) in enumerate(zip(stages, journey['actual_stages'])):
            match_text = "✓" if journey['expected_pattern'][i] == theme else "✗"
            ax.annotate(f"{name}\n({theme}) {match_text}",
                        xy=(i, growth_values[i]),
                        xytext=(0, 20),
                        textcoords='offset points',
                        ha='center',
                        bbox=dict(boxstyle='round,pad=0.5',
                                fc=ChapterVisualizations.colors['gradient'][i], alpha=0.7),
                        fontweight='bold')

        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(0, 10)
        ax.set_xticks(x)
        ax.set_xticklabels(['1단계', '2단계', '3단계', '4단계'])
        ax.set_ylabel('신앙 성장도', fontsize=12)
        ax.set_title('💝 레아의 4단계 신앙 여정', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()

        plt.suptitle('레아 - 사랑받지 못한 자의 승리 (패턴 일치율: %.1f%%)' % journey['match_rate'],
                    fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.show()

        return fig

    @staticmethod
    def plot_john_concepts_importance(john_df=None):
        """요한복음 핵심 개념 중요도 시각화"""

        print("🎯 요한복음 개념 중요도 차트 생성...")
        if john_df is None:
            john_df = load_john_concepts()

        # 중요도 순으로 정렬
        john_df_sorted = john_df.sort_values('theological_importance', ascending=True)

        fig, ax = plt.subplots(figsize=(10, 8))

        # 수평 막대 그래프
        y_pos = np.arange(len(john_df_sorted))
        bars = ax.barh(y_pos, john_df_sorted['theological_importance'].values,
                    color=ChapterVisualizations.colors['gradient'][:len(john_df_sorted)])

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

    @staticmethod
    def plot_light_vs_darkness(john_df=None):
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
                        color=ChapterVisualizations.colors['warning'], edgecolor='black')
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
        colors_donut = [ChapterVisualizations.colors['warning'], '#2C3E50']
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

    @staticmethod
    def plot_spiritual_growth_radar(scores):
        """개인 영적 성장 레이더 차트 시각화"""
        print("📈 영적 성장 레이더 차트 생성...")

        # 레이더 차트 데이터
        categories = ['관계', '소통', '연합', '예배', '성장']
        N = len(categories)
        values = scores
        values += values[:1]  # 첫 번째 값 반복하여 그래프 닫기

        # 각도 계산
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        fig, ax = plt.subplots(subplot_kw=dict(polar=True), figsize=(8, 8))
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        plt.xticks(angles[:-1], categories, color='grey', size=12)
        plt.yticks(np.arange(0, 11, 2), ["0", "2", "4", "6", "8", "10"], color="grey", size=8)
        plt.ylim(0, 10)

        ax.plot(angles, values, linewidth=2, linestyle='solid', label='나의 영적 성장')
        ax.fill(angles, values, 'b', alpha=0.25)
        ax.set_title("📈 개인 영적 성장 레이더 차트", size=16, color=ChapterVisualizations.colors['primary'], fontweight='bold', pad=20)
        ax.grid(True)
        ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        plt.tight_layout()
        plt.show()
        return fig

    @staticmethod
    def create_chapter_summary_dashboard(tribes_df=None, john_df=None, personal_scores=None):
        """종합 대시보드 생성"""

        print("📊 종합 대시보드 생성...")

        if tribes_df is None:
            tribes_df = load_twelve_tribes()
        if john_df is None:
            john_df = load_john_concepts()
        if personal_scores is None:
            personal_scores = [7, 8, 6, 9, 7] # 기본값

        fig = plt.figure(figsize=(16, 10))

        # 2x2 그리드 생성
        ax1 = plt.subplot(2, 2, 1)
        ax2 = plt.subplot(2, 2, 2)
        ax3 = plt.subplot(2, 2, 3)
        ax4 = plt.subplot(2, 2, 4)

        # 1. 12지파 어머니별 분포
        mother_counts = tribes_df['mother'].value_counts()
        colors_pie = [ChapterVisualizations.colors['gradient'][i % len(ChapterVisualizations.colors['gradient'])]
                    for i in range(len(mother_counts))]
        ax1.pie(mother_counts.values, labels=mother_counts.index,
                colors=colors_pie, autopct='%1.1f%%', startangle=90)
        ax1.set_title('👥 12지파 어머니별 분포', fontsize=12, fontweight='bold')

        # 2. 레아의 4단계
        leah_sons = tribes_df[tribes_df['mother'] == '레아'].head(4)
        stages = ['관계', '소통', '연합', '예배']
        x = np.arange(len(stages))
        ax2.bar(x, [1, 2, 3, 4], color=ChapterVisualizations.colors['gradient'][:4])
        ax2.set_xticks(x)
        ax2.set_xticklabels(stages)
        ax2.set_title('💝 레아의 4단계 신앙 여정', fontsize=12, fontweight='bold')
        ax2.set_ylabel('단계')

        # 3. 요한복음 핵심 개념
        top_concepts = john_df.nlargest(5, 'theological_importance')
        ax3.barh(range(5), top_concepts['theological_importance'].values,
                color=ChapterVisualizations.colors['gradient'][:5])
        ax3.set_yticks(range(5))
        ax3.set_yticklabels(top_concepts['korean_name'].values)
        ax3.set_title('🎯 요한복음 1장 핵심 개념', fontsize=12, fontweight='bold')
        ax3.set_xlabel('신학적 중요도')

        # 4. 빛과 어둠
        light_dark = [7, 3]  # 빛 70%, 어둠 30%
        ax4.pie(light_dark, labels=['빛', '어둠'],
                colors=[ChapterVisualizations.colors['warning'], '#2C3E50'],
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

    # 클래스를 통해 메서드 호출
    ChapterVisualizations.plot_mothers_distribution()
    ChapterVisualizations.plot_leah_spiritual_journey()
    ChapterVisualizations.plot_john_concepts_importance()
    ChapterVisualizations.plot_light_vs_darkness()
    ChapterVisualizations.plot_spiritual_growth_radar([7, 8, 6, 9, 7])
    ChapterVisualizations.create_chapter_summary_dashboard()

    print("🎉 시각화 데모 완료!")


if __name__ == "__main__":
    demo_all_visualizations()
