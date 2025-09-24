"""
Chapter 01 시각화 모듈
성경 데이터의 아름다운 패턴을 시각적으로 표현

"하나님이 지으신 그것을 보시니 보기에 좋았더라" (창 1:25)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 한글 폰트 설정
plt.rcParams['font.family'] = ['NanumGothic', 'Malgun Gothic', 'AppleGothic', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

class ChapterVisualizations:
    """Chapter 01 시각화 클래스
    
    12지파 패턴과 요한복음 구조를 아름다운 차트로 표현합니다.
    """
    
    def __init__(self):
        """시각화 설정 초기화"""
        # JesusBornd 컬러 팔레트
        self.colors = {
            'primary': '#800080',    # Purple - 왕권
            'secondary': '#228B22',  # Green - 생명  
            'accent': '#9B30FF',     # Violet - 성령
            'warning': '#FF6B35',    # Orange - 경고
            'success': '#4CAF50',    # Green - 성공
            'light': '#E8F5E8',     # Light green
            'dark': '#2F4F2F'       # Dark green
        }
        
        # 기본 스타일 설정
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_palette([self.colors['primary'], self.colors['secondary'], 
                        self.colors['accent'], self.colors['warning']])
        
    def plot_mothers_distribution(self, tribes_df: pd.DataFrame, save_path: str = None) -> plt.Figure:
        """어머니별 아들 분포 차트
        
        Args:
            tribes_df: 12지파 DataFrame
            save_path: 저장 경로 (선택사항)
            
        Returns:
            Figure: matplotlib 차트 객체
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        mothers_count = tribes_df['mother'].value_counts()
        
        # 파이 차트 생성
        colors = [self.colors['primary'], self.colors['secondary'], 
                 self.colors['accent'], self.colors['warning']]
        
        wedges, texts, autotexts = ax.pie(
            mothers_count.values, 
            labels=mothers_count.index,
            autopct=lambda pct: f'{pct:.0f}%\n({int(pct/100*len(tribes_df))}명)',
            colors=colors[:len(mothers_count)],
            startangle=90,
            textprops={'fontsize': 12}
        )

        ax.set_title('👥 어머니별 아들 분포 - 하나님의 공평하심\n"하나님은 사람의 외모를 보지 아니하시느니라" (갈 2:6)',
                    fontsize=14, fontweight='bold', pad=20)

        # 레이블 개선
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_leah_spiritual_journey(self, tribes_df: pd.DataFrame, save_path: str = None) -> plt.Figure:
        """레아의 4단계 신앙 여정 시각화

        Args:
            tribes_df: 12지파 DataFrame
            save_path: 저장 경로

        Returns:
            Figure: 신앙 여정 차트
        """
        leah_sons = tribes_df[tribes_df['mother'] == 'Leah'].sort_values('birth_order').head(4)

        fig, ax = plt.subplots(figsize=(12, 8))

        # 막대 차트 생성
        bars = ax.bar(range(len(leah_sons)), [1, 2, 3, 4],
                     color=[self.colors['primary'], self.colors['secondary'],
                           self.colors['accent'], self.colors['success']],
                     alpha=0.8, width=0.6)

        # 각 막대에 정보 표시
        for i, (idx, son) in enumerate(leah_sons.iterrows()):
            ax.text(i, i + 1.2, son['korean_name'], ha='center', va='bottom',
                   fontsize=14, fontweight='bold')
            ax.text(i, i + 0.9, f"'{son['korean_meaning']}'", ha='center', va='bottom',
                   fontsize=10, style='italic')
            ax.text(i, i + 0.6, son['spiritual_theme'], ha='center', va='bottom',
                   fontsize=12, color='white', fontweight='bold')

        # 화살표로 순서 표시
        for i in range(len(leah_sons) - 1):
            ax.annotate('', xy=(i + 0.8, 2.5), xytext=(i + 0.2, 2.5),
                       arrowprops=dict(arrowstyle='->', color=self.colors['dark'], lw=2))

        ax.set_xlim(-0.5, len(leah_sons) - 0.5)
        ax.set_ylim(0, 5)
        ax.set_xticks([])
        ax.set_yticks([])

        # 축 제거
        for spine in ax.spines.values():
            spine.set_visible(False)

        ax.set_title('💝 레아의 4단계 신앙 여정\n"내가 이제는 여호와를 찬송하리로다" (창 29:35)',
                    fontsize=16, fontweight='bold', pad=30)

        # 하단에 설명 추가
        journey_text = "관계 → 소통 → 연합 → 예배: 모든 신자의 성장 패턴"
        ax.text(1.5, -0.5, journey_text, ha='center', va='top',
               fontsize=12, style='italic', color=self.colors['dark'])

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_john_concepts_importance(self, john_df: pd.DataFrame, save_path: str = None) -> plt.Figure:
        """요한복음 1장 신학적 중요도 차트

        Args:
            john_df: 요한복음 개념 DataFrame
            save_path: 저장 경로

        Returns:
            Figure: 중요도 차트
        """
        # 중요도 상위 8개 개념
        top_concepts = john_df.nlargest(8, 'theological_importance')

        fig, ax = plt.subplots(figsize=(12, 8))

        # 수평 막대 차트
        bars = ax.barh(range(len(top_concepts)), top_concepts['theological_importance'],
                      color=[self.colors['primary'] if x == 10 else
                            self.colors['secondary'] if x >= 9 else
                            self.colors['accent'] for x in top_concepts['theological_importance']])

        # Y축 라벨 설정
        ax.set_yticks(range(len(top_concepts)))
        ax.set_yticklabels([f"{row['korean_name']}\n({row['greek_transliteration']})"
                           for _, row in top_concepts.iterrows()], fontsize=11)

        # 막대 끝에 점수 표시
        for i, (_, concept) in enumerate(top_concepts.iterrows()):
            ax.text(concept['theological_importance'] + 0.1, i, f"{concept['theological_importance']}/10",
                   va='center', fontsize=10, fontweight='bold')

        ax.set_xlabel('신학적 중요도', fontsize=12, fontweight='bold')
        ax.set_title('🎯 요한복음 1장 핵심 개념 중요도\n"태초에 말씀이 계시니라" (요 1:1)',
                    fontsize=14, fontweight='bold', pad=20)

        ax.set_xlim(0, 11)
        ax.grid(axis='x', alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_light_vs_darkness(self, john_df: pd.DataFrame, save_path: str = None) -> plt.Figure:
        """빛 vs 어둠 대조 시각화

        Args:
            john_df: 요한복음 개념 DataFrame
            save_path: 저장 경로

        Returns:
            Figure: 빛/어둠 대조 차트
        """
        light_data = john_df[john_df['concept'] == 'Light'].iloc[0]
        darkness_data = john_df[john_df['concept'] == 'Darkness'].iloc[0]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # 빈도 비교 (막대 차트)
        concepts = ['빛 (φῶς)', '어둠 (σκότος)']
        frequencies = [light_data['frequency_ch1'], darkness_data['frequency_ch1']]
        colors = ['#FFD700', '#2F2F2F']  # 금색과 어두운 회색

        bars1 = ax1.bar(concepts, frequencies, color=colors, alpha=0.8)
        ax1.set_ylabel('등장 빈도', fontsize=12)
        ax1.set_title('💡 등장 빈도 비교', fontsize=13, fontweight='bold')

        # 막대 위에 숫자 표시
        for bar, freq in zip(bars1, frequencies):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{freq}회', ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax1.set_ylim(0, max(frequencies) + 1)

        # 중요도 비교 (도넛 차트)
        importances = [light_data['theological_importance'], darkness_data['theological_importance']]
        total_importance = sum(importances)

        wedges, texts, autotexts = ax2.pie(importances, labels=concepts, autopct='%1.1f',
                                          colors=colors, startangle=90,
                                          wedgeprops=dict(width=0.5))

        ax2.set_title('⚖️ 신학적 중요도 비교', fontsize=13, fontweight='bold')

        # 전체 제목
        ratio = light_data['frequency_ch1'] / darkness_data['frequency_ch1']
        fig.suptitle(f'빛 vs 어둠의 압도적 대조\n"빛이 어둠에 비치되 어둠이 깨닫지 못하더라" (요 1:5)\n빛의 승리: {ratio:.1f}:1',
                    fontsize=16, fontweight='bold', y=0.95)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_grace_truth_balance(self, john_df: pd.DataFrame, save_path: str = None) -> plt.Figure:
        """은혜와 진리의 완벽한 균형 시각화

        Args:
            john_df: 요한복음 개념 DataFrame
            save_path: 저장 경로

        Returns:
            Figure: 은혜/진리 균형 차트
        """
        grace_data = john_df[john_df['concept'] == 'Grace'].iloc[0]
        truth_data = john_df[john_df['concept'] == 'Truth'].iloc[0]

        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))

        # 극좌표 차트로 균형 표현
        categories = ['빈도', '중요도', '위치', '대조성']

        grace_values = [
            grace_data['frequency_ch1'] / 2 * 10,  # 정규화
            grace_data['theological_importance'],
            8,  # 문단 위치 점수
            9   # 대조 효과 점수
        ]

        truth_values = [
            truth_data['frequency_ch1'] / 2 * 10,  # 정규화
            truth_data['theological_importance'],
            8,  # 문단 위치 점수
            9   # 대조 효과 점수
        ]

        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)

        # 은혜 라인
        ax.plot(angles, grace_values, 'o-', linewidth=2, label='은혜 (χάρις)',
               color=self.colors['secondary'])
        ax.fill(angles, grace_values, alpha=0.25, color=self.colors['secondary'])

        # 진리 라인
        ax.plot(angles, truth_values, 's-', linewidth=2, label='진리 (ἀλήθεια)',
               color=self.colors['primary'])
        ax.fill(angles, truth_values, alpha=0.25, color=self.colors['primary'])

        ax.set_xticks(angles)
        ax.set_xticklabels(categories, fontsize=12)
        ax.set_ylim(0, 10)
        ax.set_title('⚖️ 은혜와 진리의 완벽한 조화\n"은혜와 진리가 함께 온지라" (요 1:14)',
                    fontsize=14, fontweight='bold', pad=30)

        ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
        ax.grid(True)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def plot_spiritual_growth_radar(self, growth_scores: list, categories: list = None,
                                   save_path: str = None) -> plt.Figure:
        """개인 영적 성장 레이더 차트

        Args:
            growth_scores: 영역별 성장 점수 리스트
            categories: 영역 이름들
            save_path: 저장 경로

        Returns:
            Figure: 영적 성장 레이더 차트
        """
        if categories is None:
            categories = ['관계', '소통', '연합', '예배', '성숙']

        # 데이터 길이 맞추기
        if len(growth_scores) != len(categories):
            growth_scores = growth_scores[:len(categories)]

        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))

        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
        growth_scores = growth_scores + [growth_scores[0]]  # 닫힌 도형 만들기
        angles = np.concatenate((angles, [angles[0]]))

        # 레이더 차트 그리기
        ax.plot(angles, growth_scores, 'o-', linewidth=3, color=self.colors['primary'])
        ax.fill(angles, growth_scores, alpha=0.25, color=self.colors['primary'])

        # 각 축에 점수 표시
        for angle, score, category in zip(angles[:-1], growth_scores[:-1], categories):
            ax.text(angle, score + 0.5, f'{score}', ha='center', va='center',
                   fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=12)
        ax.set_ylim(0, 10)
        ax.set_title('🧬 개인 영적 성장 DNA\n"영광에서 영광에 이르니" (고후 3:18)',
                    fontsize=14, fontweight='bold', pad=30)

        # 격자 커스터마이징
        ax.grid(True, alpha=0.3)
        ax.set_yticks([2, 4, 6, 8, 10])
        ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=9)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

    def create_chapter_summary_dashboard(self, tribes_df: pd.DataFrame, john_df: pd.DataFrame,
                                       personal_scores: list = None, save_path: str = None) -> plt.Figure:
        """Chapter 01 종합 대시보드

        Args:
            tribes_df: 12지파 DataFrame
            john_df: 요한복음 개념 DataFrame
            personal_scores: 개인 성장 점수들
            save_path: 저장 경로

        Returns:
            Figure: 종합 대시보드
        """
        fig = plt.figure(figsize=(16, 12))

        # 2x2 그리드 레이아웃
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

        # 1. 어머니별 분포 (좌상)
        ax1 = fig.add_subplot(gs[0, 0])
        mothers_count = tribes_df['mother'].value_counts()
        colors = [self.colors['primary'], self.colors['secondary'],
                 self.colors['accent'], self.colors['warning']]
        ax1.pie(mothers_count.values, labels=mothers_count.index, autopct='%1.0f명',
               colors=colors[:len(mothers_count)], startangle=90)
        ax1.set_title('👥 12지파 어머니별 분포', fontweight='bold')

        # 2. 레아의 신앙 여정 (우상)
        ax2 = fig.add_subplot(gs[0, 1])
        leah_sons = tribes_df[tribes_df['mother'] == 'Leah'].head(4)
        stages = leah_sons['spiritual_theme'].tolist()
        ax2.barh(range(len(stages)), [1, 2, 3, 4],
                color=[self.colors['primary'], self.colors['secondary'],
                      self.colors['accent'], self.colors['success']])
        ax2.set_yticks(range(len(stages)))
        ax2.set_yticklabels(stages)
        ax2.set_title('💝 레아의 4단계 신앙 여정', fontweight='bold')

        # 3. 빛 vs 어둠 (좌하)
        ax3 = fig.add_subplot(gs[1, 0])
        light_freq = john_df[john_df['concept'] == 'Light']['frequency_ch1'].iloc[0]
        dark_freq = john_df[john_df['concept'] == 'Darkness']['frequency_ch1'].iloc[0]
        ax3.bar(['빛 (φῶς)', '어둠 (σκότος)'], [light_freq, dark_freq],
               color=['#FFD700', '#2F2F2F'])
        ax3.set_title('💡 빛 vs 어둠 대조', fontweight='bold')
        ax3.set_ylabel('등장 빈도')

        # 4. 개인 성장 레이더 (우하)
        if personal_scores:
            ax4 = fig.add_subplot(gs[1, 1], projection='polar')
            categories = ['관계', '소통', '연합', '예배', '성숙']
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
            scores = personal_scores + [personal_scores[0]]
            angles = np.concatenate((angles, [angles[0]]))

            ax4.plot(angles, scores, 'o-', linewidth=2, color=self.colors['primary'])
            ax4.fill(angles, scores, alpha=0.25, color=self.colors['primary'])
            ax4.set_xticks(angles[:-1])
            ax4.set_xticklabels(categories)
            ax4.set_title('🧬 개인 영적 성장', fontweight='bold')
        else:
            ax4 = fig.add_subplot(gs[1, 1])
            ax4.text(0.5, 0.5, '개인 분석\n데이터 없음', ha='center', va='center',
                    fontsize=14, transform=ax4.transAxes)
            ax4.set_title('🧬 개인 영적 성장', fontweight='bold')
            ax4.axis('off')

        # 전체 제목
        fig.suptitle('📊 Chapter 01: 태초에 DataFrame — 데이터의 탄생\n"태초에 말씀이 계시니라" (요 1:1)',
                    fontsize=18, fontweight='bold', y=0.95)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        return fig

def demo_visualizations():
    """시각화 데모 실행"""
    from utils.bible_utils import load_twelve_tribes, load_john_concepts

    print("🎨 Chapter 01 시각화 데모 시작...")

    # 데이터 로드
    tribes_df = load_twelve_tribes()
    john_df = load_john_concepts()

    # 시각화 객체 생성
    viz = ChapterVisualizations()

    # 1. 어머니별 분포 차트
    print("👥 어머니별 분포 차트 생성...")
    fig1 = viz.plot_mothers_distribution(tribes_df)
    plt.show()

    # 2. 레아의 신앙 여정
    print("💝 레아의 신앙 여정 차트 생성...")
    fig2 = viz.plot_leah_spiritual_journey(tribes_df)
    plt.show()

    # 3. 요한복음 개념 중요도
    print("🎯 요한복음 개념 중요도 차트 생성...")
    fig3 = viz.plot_john_concepts_importance(john_df)
    plt.show()

    # 4. 빛 vs 어둠
    print("💡 빛 vs 어둠 대조 차트 생성...")
    fig4 = viz.plot_light_vs_darkness(john_df)
    plt.show()

    # 5. 종합 대시보드
    print("📊 종합 대시보드 생성...")
    personal_scores = [7, 8, 6, 9, 7]  # 예시 점수
    fig5 = viz.create_chapter_summary_dashboard(tribes_df, john_df, personal_scores)
    plt.show()

    print("🎉 시각화 데모 완료!")

if __name__ == "__main__":
    demo_visualizations()