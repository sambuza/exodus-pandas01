"""
요한복음 1장 분석 모듈  
λόγος(로고스)의 신학적 구조와 문학적 정교함 분석

"In the beginning was the Word, and the Word was with God, and the Word was God." (John 1:1 KJV)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.bible_utils import (
    load_john_concepts, 
    analyze_light_darkness_ratio,
    get_grace_truth_balance
)

class JohnChapter1Analyzer:
    """요한복음 1장 분석 클래스
    
    말씀(λόγος), 빛(φῶς), 생명(ζωή)의 신학적 구조와
    요한의 의도적 문학 설계를 분석합니다.
    """
    
    def __init__(self):
        """분석기 초기화"""
        self.john_concepts = load_john_concepts()
        self.light_analysis = None
        self.grace_truth_analysis = None
        
    def create_theological_dataframe(self) -> pd.DataFrame:
        """신학적 개념 DataFrame 생성 (책의 5.1절)
        
        Returns:
            DataFrame: 요한복음 1장 핵심 개념들
        """
        # KJV 기반 핵심 개념만 선별 (저작권 안전)
        core_concepts = self.john_concepts[[
            'korean_name', 'greek_transliteration', 'frequency_ch1', 'theological_importance'
        ]].copy()
        
        core_concepts = core_concepts.rename(columns={
            'korean_name': '개념',
            'greek_transliteration': '헬라어',
            'frequency_ch1': '등장빈도', 
            'theological_importance': '중요도'
        })
        
        print("📜 요한복음 1장 핵심 개념:")
        print(core_concepts)
        
        # 가장 중요한 개념 찾기
        most_important_idx = core_concepts['중요도'].idxmax()
        most_important = core_concepts.loc[most_important_idx]
        print(f"\n⭐ 가장 중요한 개념: {most_important['개념']} ({most_important['헬라어']})")
        
        return core_concepts
        
    def analyze_high_importance_concepts(self) -> pd.DataFrame:
        """중요도 높은 개념들 필터링 (책의 5.2절 - 초급+알파)
        
        Returns:
            DataFrame: 중요도 8 이상인 개념들
        """
        high_importance = self.john_concepts[
            self.john_concepts['theological_importance'] >= 8
        ][['korean_name', 'greek_transliteration', 'frequency_ch1', 'theological_importance']]
        
        high_importance = high_importance.rename(columns={
            'korean_name': '개념',
            'greek_transliteration': '헬라어', 
            'frequency_ch1': '등장빈도',
            'theological_importance': '중요도'
        })
        
        print("🌟 중요도 8 이상인 핵심 개념들:")
        print(high_importance)
        
        return high_importance
        
    def analyze_light_vs_darkness(self) -> dict:
        """빛과 어둠 대조 분석 (책의 5.2절)
        
        Returns:
            dict: 빛 vs 어둠 분석 결과
        """
        self.light_analysis = analyze_light_darkness_ratio(self.john_concepts)
        
        print("💡 빛과 어둠의 대조:")
        print(f"  빛: 빈도 {self.light_analysis['light_frequency']}회, 중요도 {self.light_analysis['light_importance']}/10")
        print(f"  어둠: 빈도 {self.light_analysis['darkness_frequency']}회, 중요도 {self.light_analysis['darkness_importance']}/10")
        print(f"  📈 {self.light_analysis['spiritual_insight']}")
        
        return self.light_analysis
        
    def analyze_grace_truth_balance(self) -> dict:
        """은혜와 진리의 완벽한 균형 분석
        
        Returns:
            dict: 은혜와 진리 균형 분석 결과
        """
        self.grace_truth_analysis = get_grace_truth_balance(self.john_concepts)
        
        print("⚖️ 은혜와 진리의 완벽한 균형:")
        grace_freq = self.grace_truth_analysis['grace_frequency']
        truth_freq = self.grace_truth_analysis['truth_frequency']
        grace_imp = self.grace_truth_analysis['grace_importance']
        truth_imp = self.grace_truth_analysis['truth_importance']
        
        print(f"  은혜: 빈도 {grace_freq}회, 중요도 {grace_imp}/10")
        print(f"  진리: 빈도 {truth_freq}회, 중요도 {truth_imp}/10")
        
        print(f"\n📊 구약 vs 신약 대조:")
        print(f"   율법 시대(모세): 규범과 심판")
        print(f"   은혜 시대(예수): 은혜 {grace_freq}회 + 진리 {truth_freq}회 = 완전한 조화")
        
        if self.grace_truth_analysis['is_balanced']:
            print("   ✨ 완벽한 균형을 이루고 있습니다!")
            
        return self.grace_truth_analysis
        
    def get_top_theological_concepts(self, top_n: int = 5) -> pd.DataFrame:
        """신학적 중요도 TOP N 개념들
        
        Args:
            top_n: 상위 N개 개념
            
        Returns:
            DataFrame: TOP N 개념들
        """
        top_concepts = self.john_concepts.nlargest(top_n, 'theological_importance')
        
        print(f"🎯 신학적 중요도 TOP {top_n}:")
        for idx, concept in top_concepts.iterrows():
            print(f"   {concept['korean_name']} ({concept['greek_transliteration']}): {concept['theological_importance']}/10")
            
        return top_concepts[['korean_name', 'greek_transliteration', 'theological_importance']]
        
    def analyze_literary_structure(self) -> dict:
        """요한복음 1장 문학적 구조 분석
        
        Returns:
            dict: 문학적 구조 분석 결과
        """
        # 섹션별 개념 분포
        sections = self.john_concepts['section_position'].value_counts()
        contrasts = self.john_concepts[['korean_name', 'contrast_pair']].dropna()
        
        print("📚 요한복음 1장 문학적 구조:")
        print("   섹션별 개념 분포:")
        for section, count in sections.items():
            print(f"     {section}: {count}개 개념")
            
        print("\n   주요 대조 구조:")
        for idx, row in contrasts.iterrows():
            if row['contrast_pair'] != row['korean_name']:  # 자기 자신과의 대조 제외
                print(f"     {row['korean_name']} ↔ {row['contrast_pair']}")
                
        return {
            'sections': sections.to_dict(),
            'contrasts': contrasts.to_dict('records'),
            'literary_insight': "요한은 의도적으로 대조법을 사용하여 예수님의 정체성을 부각시켰습니다."
        }
        
    def get_spiritual_discoveries(self) -> list:
        """영적 발견 정리
        
        Returns:
            list: 주요 영적 발견들
        """
        discoveries = [
            "📜 λόγος(말씀)가 모든 신학의 시작점임을 확인",
            "💡 빛이 어둠을 2.5:1로 압도하는 의도적 설계", 
            "⚖️ 은혜와 진리의 완벽한 수치적 균형",
            "🔍 요한의 정교한 대조법 구조",
            "✨ 창세기 1장과의 의도적 메아리 효과"
        ]
        
        if self.light_analysis:
            ratio = self.light_analysis['ratio']
            discoveries.append(f"📊 빛의 절대 우세: {ratio:.1f}:1 비율로 복음의 승리 예증")
            
        if self.grace_truth_analysis and self.grace_truth_analysis['is_balanced']:
            discoveries.append("🎯 예수님 = 은혜와 진리의 완벽한 통합체")
            
        return discoveries
        
    def run_complete_analysis(self) -> dict:
        """전체 분석 실행
        
        Returns:
            dict: 종합 분석 결과
        """
        print("📜 === 요한복음 1장: 말씀(λόγος) 분석 시작 ===\n")
        
        # 1. 신학적 개념 DataFrame
        theological_df = self.create_theological_dataframe()
        print("\n" + "="*50 + "\n")
        
        # 2. 중요도 높은 개념들
        high_importance_df = self.analyze_high_importance_concepts()
        print("\n" + "="*50 + "\n")
        
        # 3. 빛 vs 어둠 대조
        light_result = self.analyze_light_vs_darkness()
        print("\n" + "="*50 + "\n")
        
        # 4. 은혜와 진리 균형
        grace_truth_result = self.analyze_grace_truth_balance()
        print("\n" + "="*50 + "\n")
        
        # 5. TOP 5 개념들
        top_concepts = self.get_top_theological_concepts()
        print("\n" + "="*50 + "\n")
        
        # 6. 문학적 구조
        literary_structure = self.analyze_literary_structure()
        print("\n" + "="*50 + "\n")
        
        # 7. 영적 발견
        discoveries = self.get_spiritual_discoveries()
        print("🌟 주요 영적 발견:")
        for discovery in discoveries:
            print(f"   {discovery}")
            
        print(f"\n🎉 요한복음 1장 분석 완료!")
        
        return {
            'theological_dataframe': theological_df,
            'high_importance_concepts': high_importance_df,
            'light_darkness_analysis': light_result,
            'grace_truth_analysis': grace_truth_result,
            'top_concepts': top_concepts,
            'literary_structure': literary_structure,
            'spiritual_discoveries': discoveries
        }

def demo_john_chapter1():
    """요한복음 1장 분석 데모 실행"""
    analyzer = JohnChapter1Analyzer()
    results = analyzer.run_complete_analysis()
    return results

if __name__ == "__main__":
    # 단독 실행 테스트
    print("📜 요한복음 1장 분석 모듈 테스트")
    demo_results = demo_john_chapter1()
    print("\n✅ 테스트 완료!")
