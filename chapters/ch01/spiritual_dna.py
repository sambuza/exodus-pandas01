"""
개인 신앙 DNA 분석 모듈
레아의 패턴과 요한복음 빛/어둠 비율로 개인 신앙 여정 분석

"사람의 마음에는 많은 계획이 있어도 오직 여호와의 뜻이 완전히 서리라" (잠 19:21)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
from typing import List, Dict

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.bible_utils import SpiritualMetrics

class PersonalSpiritualDNA:
    """개인 신앙 DNA 분석 클래스
    
    개인의 신앙 여정을 성경적 패턴과 비교하여
    영적 성장 현황과 방향을 분석합니다.
    """
    
    def __init__(self, name: str = "신앙인"):
        """분석기 초기화
        
        Args:
            name: 분석 대상자 이름
        """
        self.name = name
        self.spiritual_journey = None
        self.light_balance = None
        self.grace_truth_balance = None
        
    def create_spiritual_journey_dataframe(self, 
                                         years: List[int] = None,
                                         experiences: List[str] = None,
                                         growth_scores: List[int] = None,
                                         gratitude_themes: List[str] = None) -> pd.DataFrame:
        """신앙 여정 DataFrame 생성 (책의 Step 1)
        
        Args:
            years: 연도 리스트
            experiences: 핵심 신앙 경험들
            growth_scores: 성장 점수들 (1-10)
            gratitude_themes: 감사 제목들
            
        Returns:
            DataFrame: 개인 신앙 여정 데이터
        """
        # 기본값 설정
        if years is None:
            years = [2020, 2021, 2022, 2023, 2024]
        if experiences is None:
            experiences = ['첫 교회 출석', '세례받음', '소그룹 리더', '단기선교', '큐티 시작']
        if growth_scores is None:
            growth_scores = [3, 5, 7, 8, 9]
        if gratitude_themes is None:
            gratitude_themes = ['새로운 시작', '거듭남', '섬김의 기쁨', '선교 경험', '말씀 사랑']
            
        self.spiritual_journey = pd.DataFrame({
            '연도': years,
            '핵심사건': experiences,
            '성장지수': growth_scores,
            '감사제목': gratitude_themes
        })
        
        print(f"📖 {self.name}의 신앙 여정:")
        print(self.spiritual_journey)
        
        return self.spiritual_journey
        
    def analyze_growth_pattern(self) -> Dict:
        """성장 패턴 분석 (책의 Step 2)
        
        Returns:
            dict: 성장 패턴 분석 결과
        """
        if self.spiritual_journey is None:
            raise ValueError("먼저 create_spiritual_journey_dataframe()을 실행하세요.")
            
        mean_growth = self.spiritual_journey['성장지수'].mean()
        max_growth_idx = self.spiritual_journey['성장지수'].idxmax()
        peak_experience = self.spiritual_journey.loc[max_growth_idx, '핵심사건']
        latest_state = self.spiritual_journey.iloc[-1]
        
        print(f"📈 신앙 성장 평균: {mean_growth:.1f}")
        print(f"🎯 최고 성장 시기: {peak_experience}")
        print(f"🌟 현재 상태: {latest_state['연도']}년 - {latest_state['핵심사건']} (성장지수: {latest_state['성장지수']})")
        
        return {
            'average_growth': mean_growth,
            'peak_experience': peak_experience,
            'current_state': latest_state.to_dict(),
            'growth_trend': self._calculate_growth_trend()
        }
        
    def _calculate_growth_trend(self) -> str:
        """성장 추세 계산"""
        growth_scores = self.spiritual_journey['성장지수'].tolist()
        
        if len(growth_scores) < 2:
            return "데이터 부족"
            
        recent_trend = growth_scores[-1] - growth_scores[-2]
        if recent_trend > 0:
            return "상승"
        elif recent_trend < 0:
            return "하락"
        else:
            return "평행"
            
    def add_future_vision(self, future_year: int = 2025, 
                         future_vision: str = "JesusBornd로 코딩과 신앙 통합",
                         target_growth: int = 10) -> pd.DataFrame:
        """미래 계획 추가 (책의 Step 3)
        
        Args:
            future_year: 미래 연도
            future_vision: 미래 비전
            target_growth: 목표 성장 지수
            
        Returns:
            DataFrame: 미래 계획이 포함된 완전한 여정
        """
        if self.spiritual_journey is None:
            raise ValueError("먼저 create_spiritual_journey_dataframe()을 실행하세요.")
            
        future_plan = pd.DataFrame({
            '연도': [future_year],
            '핵심사건': [future_vision],
            '성장지수': [target_growth],
            '감사제목': ['복음과 기술의 만남']
        })
        
        # 기존 데이터와 결합
        complete_journey = pd.concat([self.spiritual_journey, future_plan], ignore_index=True)
        
        print(f"\n🚀 완전한 신앙 여정 ({future_year} 계획 포함):")
        print(complete_journey)
        
        return complete_journey
        
    def analyze_leah_pattern_match(self, spiritual_stages: List[str] = None) -> Dict:
        """레아의 4단계 패턴과 비교 분석
        
        Args:
            spiritual_stages: 개인의 영적 단계들
            
        Returns:
            dict: 패턴 매칭 분석 결과
        """
        if spiritual_stages is None:
            # 기본 신앙 단계 (사용자 입력 받아야 함)
            spiritual_stages = ['관계', '소통', '연합', '예배']
            
        leah_pattern = ['관계', '소통', '연합', '예배']
        
        print(f"🔍 레아 패턴과의 일치도 분석:")
        print(f"   레아의 4단계: {' → '.join(leah_pattern)}")
        print(f"   {self.name}의 4단계: {' → '.join(spiritual_stages[:4])}")
        
        matches = sum(1 for i, stage in enumerate(spiritual_stages[:4]) 
                     if i < len(leah_pattern) and stage == leah_pattern[i])
        match_rate = matches / len(leah_pattern) * 100
        
        print(f"   일치율: {matches}/{len(leah_pattern)} = {match_rate:.0f}%")
        
        if match_rate >= 75:
            print("   ✅ 성경적 신앙 패턴을 따르고 있습니다!")
            recommendation = "✨ 레아와 같은 아름다운 신앙 여정을 걷고 계시네요!"
        elif match_rate >= 50:
            print("   ⚠️ 좀 더 체계적인 신앙 성장이 필요할 수 있습니다.")
            recommendation = "📚 성경적 신앙 성장을 위해 말씀 읽기와 기도를 늘려보세요."
        else:
            print("   🔄 신앙 여정을 다시 점검해보시기 바랍니다.")
            recommendation = "🙏 하나님과의 관계부터 차근차근 시작해보세요. 레아의 여정을 참고하세요."
            
        return {
            'leah_pattern': leah_pattern,
            'user_pattern': spiritual_stages[:4],
            'matches': matches,
            'match_rate': match_rate,
            'is_biblical': match_rate >= 75,
            'recommendation': recommendation
        }
        
    def analyze_light_darkness_balance(self, light_experiences: int = 7, 
                                     dark_experiences: int = 3) -> Dict:
        """빛과 어둠의 영적 균형 분석 (요한복음 패턴)
        
        Args:
            light_experiences: 빛의 경험 횟수 (최근 한달 기준)
            dark_experiences: 어둠의 경험 횟수
            
        Returns:
            dict: 빛/어둠 균형 분석 결과
        """
        self.light_balance = pd.DataFrame({
            '요소': ['빛의_경험', '어둠의_경험'],
            '내용': ['기쁨,감사,평안,사랑,희망', '의심,불안,원망,절망,분노'],
            '최근_빈도': [light_experiences, dark_experiences],
            '원하는_비율': [8, 2]
        })
        
        print("💡 나의 영적 빛과 어둠 비율:")
        print(self.light_balance)
        
        current_ratio = light_experiences / dark_experiences if dark_experiences > 0 else float('inf')
        john_ratio = 2.5  # 요한복음의 빛:어둠 비율
        
        print(f"\n📊 비율 비교:")
        print(f"   내 현재 비율: {current_ratio:.1f}:1")
        print(f"   요한복음 비율: {john_ratio:.1f}:1")
        
        if current_ratio >= john_ratio:
            result_message = "🌟 요한복음처럼 빛이 승리하는 삶을 살고 계세요!"
            spiritual_status = "승리"
        else:
            result_message = "🕯️ 더 많은 빛의 경험이 필요합니다. 말씀과 기도를 늘려보세요."
            spiritual_status = "성장 필요"
            
        print(f"   {result_message}")
        
        return {
            'light_frequency': light_experiences,
            'dark_frequency': dark_experiences,
            'current_ratio': current_ratio,
            'john_ratio': john_ratio,
            'spiritual_status': spiritual_status,
            'message': result_message
        }
        
    def analyze_grace_truth_balance(self, grace_actions: int = 4, 
                                  truth_studies: int = 4) -> Dict:
        """은혜와 진리 균형 자가 진단
        
        Args:
            grace_actions: 주간 은혜 실천 횟수
            truth_studies: 주간 진리 추구 횟수
            
        Returns:
            dict: 은혜/진리 균형 분석 결과
        """
        self.grace_truth_balance = pd.DataFrame({
            '영역': ['은혜_경험', '진리_추구'],
            '구체적_행동': ['용서,위로,격려,긍휼', '성경공부,교리학습,진리탐구'],
            '주간_횟수': [grace_actions, truth_studies],
            '만족도': [8, 7]  # 기본값
        })
        
        print("⚖️ 나의 은혜와 진리 균형 점검:")
        print(self.grace_truth_balance)
        
        grace_score = grace_actions * 8 / 10  # 만족도 가중
        truth_score = truth_studies * 7 / 10
        
        print(f"\n📈 종합 점수:")
        print(f"   은혜 점수: {grace_score:.1f}")
        print(f"   진리 점수: {truth_score:.1f}")
        
        balance_diff = abs(grace_score - truth_score)
        
        if balance_diff <= 1:
            balance_message = "✨ 은혜와 진리가 조화를 이루는 신앙생활을 하고 계세요!"
            balance_status = "균형"
        elif grace_score > truth_score:
            balance_message = "📚 진리 추구를 더 늘려보세요 (성경공부, 독서 등)"
            balance_status = "은혜 우세"
        else:
            balance_message = "💝 은혜 실천을 더 늘려보세요 (섬김, 위로, 용서 등)"
            balance_status = "진리 우세"
            
        print(f"   {balance_message}")
        
        return {
            'grace_score': grace_score,
            'truth_score': truth_score,
            'balance_status': balance_status,
            'is_balanced': balance_diff <= 1,
            'message': balance_message,
            'recommendation': self._get_balance_recommendation(balance_status)
        }
        
    def _get_balance_recommendation(self, balance_status: str) -> str:
        """균형 상태에 따른 추천사항"""
        recommendations = {
            "균형": "현재 상태를 유지하면서 더 깊이 있는 성장을 추구하세요.",
            "은혜 우세": "진리 공부를 늘려보세요: 성경 통독, 교리 학습, 신학 독서",
            "진리 우세": "은혜 실천을 늘려보세요: 섬김, 나눔, 위로, 용서"
        }
        return recommendations.get(balance_status, "지속적인 성장을 추구하세요.")
        
    def generate_spiritual_report(self) -> Dict:
        """종합 영적 리포트 생성
        
        Returns:
            dict: 전체 분석 결과 종합
        """
        if self.spiritual_journey is None:
            raise ValueError("먼저 create_spiritual_journey_dataframe()을 실행하세요.")
            
        # 기본 분석들 실행
        growth_analysis = self.analyze_growth_pattern()
        leah_analysis = self.analyze_leah_pattern_match()
        light_analysis = self.analyze_light_darkness_balance()
        grace_truth_analysis = self.analyze_grace_truth_balance()
        
        # 종합 점수 계산
        overall_score = self._calculate_overall_spiritual_score(
            growth_analysis, leah_analysis, light_analysis, grace_truth_analysis
        )
        
        print(f"\n📋 === {self.name}의 종합 영적 리포트 ===")
        print(f"🎯 종합 영적 성숙도: {overall_score:.1f}/10")
        print(f"📈 성장 추세: {growth_analysis['growth_trend']}")
        print(f"📖 성경적 패턴 일치: {leah_analysis['match_rate']:.0f}%")
        print(f"💡 영적 빛 우세도: {light_analysis['current_ratio']:.1f}:1")
        print(f"⚖️ 은혜-진리 균형: {grace_truth_analysis['balance_status']}")
        
        return {
            'overall_score': overall_score,
            'growth_analysis': growth_analysis,
            'leah_pattern_analysis': leah_analysis,
            'light_darkness_analysis': light_analysis,
            'grace_truth_analysis': grace_truth_analysis,
            'recommendations': self._get_comprehensive_recommendations(overall_score)
        }
        
    def _calculate_overall_spiritual_score(self, growth_analysis, leah_analysis, 
                                         light_analysis, grace_truth_analysis) -> float:
        """종합 영적 점수 계산"""
        # 각 영역별 점수 (0-10)
        growth_score = min(growth_analysis['average_growth'], 10)
        leah_score = leah_analysis['match_rate'] / 10
        light_score = min(light_analysis['current_ratio'] * 2, 10)  # 2.5:1 비율이 5점 기준
        balance_score = 10 if grace_truth_analysis['is_balanced'] else 7
        
        # 가중평균 (성장 30%, 패턴 25%, 빛 25%, 균형 20%)
        overall = (growth_score * 0.3 + leah_score * 0.25 + 
                  light_score * 0.25 + balance_score * 0.2)
        
        return min(overall, 10)
        
    def _get_comprehensive_recommendations(self, overall_score: float) -> List[str]:
        """종합 점수에 따른 추천사항들"""
        if overall_score >= 8.5:
            return [
                "🌟 탁월한 신앙 성장을 보이고 있습니다!",
                "🎓 이제 다른 사람들을 멘토링해보세요",
                "📚 더 깊은 신학 공부에 도전해보세요",
                "🌍 선교나 큰 사역에 참여를 고려해보세요"
            ]
        elif overall_score >= 7.0:
            return [
                "✨ 안정적인 신앙 성장을 하고 있어요",
                "📖 성경 통독이나 체계적 공부를 해보세요",
                "🤝 소그룹이나 봉사 활동을 늘려보세요",
                "🙏 기도 시간을 더 늘려보세요"
            ]
        elif overall_score >= 5.5:
            return [
                "🌱 꾸준한 성장이 필요해요",
                "📚 기초 신앙 교육에 참여해보세요",
                "💬 신앙 멘토를 찾아보세요",
                "⛪ 교회 공동체 참여를 늘려보세요"
            ]
        else:
            return [
                "🙏 하나님과의 관계부터 시작해보세요",
                "📖 매일 성경 읽기 습관을 만드세요",
                "⛪ 교회 출석을 규칙적으로 해보세요",
                "🤲 기도로 하나님께 도움을 구하세요"
            ]

def demo_personal_spiritual_dna(name: str = "데이브"):
    """개인 신앙 DNA 분석 데모"""
    analyzer = PersonalSpiritualDNA(name)
    
    # 1. 신앙 여정 생성
    journey_df = analyzer.create_spiritual_journey_dataframe()
    print("\n" + "="*50 + "\n")
    
    # 2. 성장 패턴 분석
    growth_result = analyzer.analyze_growth_pattern()
    print("\n" + "="*50 + "\n")
    
    # 3. 미래 비전 추가
    complete_journey = analyzer.add_future_vision()
    print("\n" + "="*50 + "\n")
    
    # 4. 레아 패턴 매칭
    leah_result = analyzer.analyze_leah_pattern_match()
    print("\n" + "="*50 + "\n")
    
    # 5. 빛/어둠 균형
    light_result = analyzer.analyze_light_darkness_balance()
    print("\n" + "="*50 + "\n")
    
    # 6. 은혜/진리 균형
    grace_truth_result = analyzer.analyze_grace_truth_balance()
    print("\n" + "="*50 + "\n")
    
    # 7. 종합 리포트
    comprehensive_report = analyzer.generate_spiritual_report()
    
    return comprehensive_report

if __name__ == "__main__":
    # 단독 실행 테스트
    print("🧬 개인 신앙 DNA 분석 모듈 테스트")
    demo_results = demo_personal_spiritual_dna()
    print("\n✅ 테스트 완료!")