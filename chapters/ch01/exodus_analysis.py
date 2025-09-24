"""
출애굽기 1장 분석 모듈
12지파의 영적 패턴과 하나님의 섭리 분석

"이스라엘의 아들들의 이름은 이러하니라" (출 1:1)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.bible_utils import load_twelve_tribes, calculate_leah_spiritual_journey,load_exodus

class TwelveTribesAnalyzer:
    """12지파 분석 클래스

    야곱의 12아들에서 발견되는 하나님의 설계와
    레아의 신앙 여정을 분석합니다.
    """

    def __init__(self):
        """분석기 초기화"""
        self.tribes_data = load_twelve_tribes()
        self.leah_analysis = None
        self.haha = load_exodus().head(100)

    def create_basic_dataframe(self) -> pd.DataFrame:
        """기본 12지파 DataFrame 생성 (책의 4.1절)

        Returns:
            DataFrame: 기본 4지파 정보
        """


        basic_four = self.tribes_data.head(4)[['korean_name', 'birth_order', 'korean_meaning']]

        basic_four = basic_four.rename(columns={
            'korean_name': '이름',
            'birth_order': '순서',
            'korean_meaning': '의미'
        })

        print("✨ 첫 번째 DataFrame이 창조되었습니다!")
        print(basic_four)
        print(f"\n📊 총 인원: {len(basic_four)}명")

        return basic_four

    def create_complete_dataframe(self) -> pd.DataFrame:
        """완전한 12지파 DataFrame (책의 4.2절)

        Returns:
            DataFrame: 전체 12지파 정보
        """

        complete_tribes = self.tribes_data[[
            'korean_name', 'mother', 'birth_order', 'egypt_residence'
        ]].copy()

        complete_tribes = complete_tribes.rename(columns={
            'korean_name': '이름',
            'mother': '어머니',
            'birth_order': '출생순서',
            'egypt_residence': '애굽거주'
        })

        print("🏺 12지파 데이터가 완성되었습니다!")
        print(complete_tribes.head())
        print(f"\n📊 총 지파 수: {len(complete_tribes)}개 (완전수 12)")

        return complete_tribes

    def analyze_data_structure(self) -> None:
        """DataFrame 구조 분석 (책의 4.3절)"""
        complete_df = self.create_complete_dataframe()

        print("📋 데이터 구조 정보:")
        complete_df.info()

        print("\n📊 기본 통계:")
        print(complete_df.describe(include='all'))

    def analyze_mothers_distribution(self) -> pd.Series:
        """어머니별 아들 수 분석 - 하나님의 공평하심

        Returns:
            Series: 어머니별 아들 수
        """
        mothers_count = self.tribes_data['mother'].value_counts()

        print("👥 어머니별 아들 수:")
        print(mothers_count)

        return mothers_count

    def analyze_leah_spiritual_journey(self) -> dict:
        """레아의 4단계 신앙 여정 분석

        Returns:
            dict: 레아 신앙 여정 분석 결과
        """
        self.leah_analysis = calculate_leah_spiritual_journey(self.tribes_data)

        print(f"\n💝 레아의 신앙 여정 (총 {len(self.get_leah_sons())}명):")

        leah_sons = self.get_leah_sons()
        for _, son in leah_sons.iterrows():
            print(f"  {son['birth_order']}. {son['korean_name']}: {son['korean_meaning']} → {son['spiritual_theme']}")

        # 첫 4아들의 특별한 패턴
        first_four_themes = leah_sons.head(4)['spiritual_theme'].tolist()
        print(f"\n✨ 레아의 첫 4아들이 보여주는 신앙 성숙 과정:")
        print(f"   {' → '.join(first_four_themes)}")
        print(f"   일치율: {self.leah_analysis['match_rate']:.1f}%")

        if self.leah_analysis['is_biblical_pattern']:
            print("   🎉 완벽한 성경적 신앙 패턴입니다!")

        return self.leah_analysis

    def get_leah_sons(self) -> pd.DataFrame:
        """레아의 아들들 반환

        Returns:
            DataFrame: 레아의 아들들 정보
        """
        return self.tribes_data[self.tribes_data['mother'] == 'Leah'].sort_values('birth_order')

    def get_spiritual_insights(self) -> list:
        """영적 통찰 정리

        Returns:
            list: 주요 영적 통찰들
        """
        insights = [
            "🔍 12지파는 하나님의 완전한 설계 (완전수 12)",
            "💝 레아의 고난이 완벽한 신앙 성숙 과정을 보여줌",
            "⚖️ 어머니별 분배에서 하나님의 공의와 사랑 발견",
            "📈 개인의 아픔이 전체의 축복이 되는 섭리",
            "🏺 각 이름에 담긴 하나님의 뜻과 계획"
        ]

        if self.leah_analysis and self.leah_analysis['is_biblical_pattern']:
            insights.append("✨ 레아의 여정 = 모든 신자의 표준 성장 패턴")

        return insights

    def run_complete_analysis(self) -> dict:
        """전체 분석 실행

        Returns:
            dict: 종합 분석 결과
        """
        print("🏺 === 출애굽기 1장: 12지파 분석 시작 ===\n")

        # 1. 기본 DataFrame
        basic_df = self.create_basic_dataframe()
        print("\n" + "="*50 + "\n")

        # 2. 완전한 DataFrame
        complete_df = self.create_complete_dataframe()
        print("\n" + "="*50 + "\n")

        # 3. 데이터 구조 분석
        self.analyze_data_structure()
        print("\n" + "="*50 + "\n")

        # 4. 어머니별 분포
        mothers_dist = self.analyze_mothers_distribution()
        print("\n" + "="*50 + "\n")

        # 5. 레아의 신앙 여정
        leah_result = self.analyze_leah_spiritual_journey()
        print("\n" + "="*50 + "\n")

        # 6. 영적 통찰
        insights = self.get_spiritual_insights()
        print("🌟 주요 영적 통찰:")
        for insight in insights:
            print(f"   {insight}")

        print(f"\n🎉 출애굽기 1장 분석 완료!")

        return {
            'basic_dataframe': basic_df,
            'complete_dataframe': complete_df,
            'mothers_distribution': mothers_dist,
            'leah_analysis': leah_result,
            'spiritual_insights': insights
        }

def demo_twelve_tribes():
    """12지파 분석 데모 실행"""
    analyzer = TwelveTribesAnalyzer()
    results = analyzer.run_complete_analysis()
    return results

if __name__ == "__main__":
    # 단독 실행 테스트
    print("🏺 12지파 분석 모듈 테스트")
    demo_results = demo_twelve_tribes()
    print("\n✅ 테스트 완료!")
