"""
요한복음 1:29 분석 모듈
하나님의 어린양 발견과 데이터 발견의 평행 이론

"이튿날 요한이 예수께서 자기에게 나아오심을 보고 가로되 보라 세상 죄를 지고 가는 하나님의 어린 양이로다" (요 1:29)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.bible_utils import load_john_concepts

class LambDiscoveryAnalyzer:
    """어린양 발견과 데이터 발견 분석 클래스"""
    
    def __init__(self):
        """분석기 초기화"""
        self.lamb_references = None
        self.discovery_pattern = None
        self.create_lamb_data()
        
    def create_lamb_data(self):
        """어린양 관련 데이터 생성"""
        self.lamb_references = pd.DataFrame({
            'verse_ref': ['창 22:8', '출 12:3', '사 53:7', '요 1:29', '요 1:36', '계 5:6'],
            'korean_text': [
                '아브라함이 가로되 아들아 번제할 어린 양은 하나님이 자기를 위하여 친히 준비하시리라',
                '너희는 이스라엘 회중에게 고하여 이르라 이 달 열흘에 너희 매인이 어린 양을 취할찌니 각 가족대로 그 식구를 위하여 어린 양을 취하되',
                '그가 곤욕을 당하여 괴로울 때에도 그 입을 열지 아니하였음이여 마치 도수장으로 끌려가는 어린 양과 털 깎는 자 앞에 잠잠한 양 같이 그 입을 열지 아니하였도다',
                '이튿날 요한이 예수께서 자기에게 나아오심을 보고 가로되 보라 세상 죄를 지고 가는 하나님의 어린 양이로다',
                '예수의 다니심을 보고 말하되 보라 하나님의 어린 양이로다',
                '내가 또 보니 보좌와 네 생물과 장로들 사이에 어린 양이 섰는데 일찍 죽임을 당한것 같더라 일곱 뿔과 일곱 눈이 있으니 이 눈은 온 땅에 보내심을 입은 하나님의 일곱 영이더라'
            ],
            'lamb_type': ['예표', '유월절', '고난', '선포', '재확인', '승리'],
            'greek_word': [None, None, None, 'ἀμνὸς', 'ἀμνὸς', 'ἀρνίον'],
            'discovery_level': [1, 2, 3, 5, 5, 5],  # 발견의 명확성
            'csv_parallel': [
                'file.exists()',
                'pd.read_csv()',
                'encoding errors',
                'df.head() - 첫 발견',
                'df.info() - 재확인',
                'df.describe() - 완전한 이해'
            ]
        })
        
    def analyze_behold_pattern(self) -> pd.DataFrame:
        """'보라' 패턴 분석"""
        
        print("👁️ === '보라'(Ἴδε) 패턴 분석 ===\n")
        
        behold_data = pd.DataFrame({
            'context': ['바로의 딸이 상자를 열고', '세례 요한이 예수를 보고', 'pd.read_csv() 실행 후'],
            'hebrew_greek': ['וַתִּרְאֵהוּ', 'Ἴδε', 'df.head()'],
            'action': ['보다', '선포하다', '확인하다'],
            'result': ['모세 발견', '어린양 선포', '데이터 발견'],
            'significance': [
                '숨겨진 구원자 발견',
                '메시아 정체성 선포', 
                '데이터 본질 파악'
            ]
        })
        
        print(behold_data.to_string(index=False))
        
        print("\n💡 통찰:")
        print("   '보라'는 단순한 시각적 관찰이 아닌")
        print("   영적 인식과 선포의 순간입니다.")
        print("   read_csv()도 단순한 파일 읽기가 아닌")
        print("   데이터의 본질을 발견하는 계시의 도구입니다.")
        
        return behold_data
        
    def analyze_lamb_progression(self) -> dict:
        """어린양 계시의 점진적 발전"""
        
        print("\n🐑 === 어린양 계시의 점진성 ===\n")
        
        progression = {
            'stage1_shadow': {
                'period': '구약 예표',
                'example': '아브라함의 숫양',
                'csv_stage': '파일 존재 확인',
                'clarity': 30
            },
            'stage2_ritual': {
                'period': '의식법',
                'example': '유월절 어린양',
                'csv_stage': 'CSV 구조 파악',
                'clarity': 50
            },
            'stage3_prophecy': {
                'period': '예언',
                'example': '이사야 53장',
                'csv_stage': '컬럼 의미 이해',
                'clarity': 70
            },
            'stage4_revelation': {
                'period': '성육신',
                'example': '요한의 선포',
                'csv_stage': '데이터 완전 이해',
                'clarity': 100
            }
        }
        
        for stage_key, stage_info in progression.items():
            stage_num = stage_key.split('_')[0].replace('stage', '')
            print(f"단계 {stage_num}: {stage_info['period']}")
            print(f"   예시: {stage_info['example']}")
            print(f"   CSV 대응: {stage_info['csv_stage']}")
            print(f"   명확도: {stage_info['clarity']}%\n")
        
        self.discovery_pattern = progression
        return progression
        
    def compare_discoveries(self) -> pd.DataFrame:
        """발견의 비교 분석"""
        
        print("🔄 === 모세 발견 vs 어린양 발견 ===\n")
        
        comparison = pd.DataFrame({
            '구분': ['발견자', '장소', '시점', '도구', '의미'],
            '모세_발견': [
                '바로의 딸',
                '나일강',
                '3개월 후',
                '갈대상자',
                '민족의 구원자'
            ],
            '어린양_발견': [
                '세례 요한',
                '요단강',
                '30년 후',
                '성령의 계시',
                '인류의 구원자'
            ],
            'CSV_발견': [
                'Data Scientist',
                '파일시스템',
                '필요시',
                'pd.read_csv()',
                '숨겨진 통찰'
            ]
        })
        
        print(comparison.to_string(index=False))
        
        print("\n🔗 공통점:")
        print("   1. 물가에서의 발견 (데이터의 흐름)")
        print("   2. 준비된 발견자 (도구를 아는 자)")
        print("   3. 때가 찬 발견 (적절한 타이밍)")
        
        return comparison
        
    def analyze_sin_bearing_data(self) -> pd.DataFrame:
        """죄를 지고 가는 데이터 패턴"""
        
        print("\n⚖️ === '지고 가는' 데이터 패턴 ===\n")
        
        bearing_pattern = pd.DataFrame({
            'data_type': ['결측치', '이상치', '중복값', '인코딩 오류'],
            'sin_parallel': ['숨겨진 죄', '명백한 죄', '반복된 죄', '왜곡된 죄'],
            'lamb_action': ['드러내심', '담당하심', '제거하심', '바로잡으심'],
            'csv_solution': [
                'fillna()',
                'remove outliers',
                'drop_duplicates()',
                'correct encoding'
            ],
            'spiritual_meaning': [
                '은혜로 채움',
                '정결케 함',
                '새롭게 함',
                '진리로 인도'
            ]
        })
        
        print(bearing_pattern.to_string(index=False))
        
        print("\n✝️ 영적 통찰:")
        print("   어린양이 세상 죄를 지고 가듯,")
        print("   데이터 클렌징은 불완전한 데이터를")
        print("   완전하게 만드는 구속의 과정입니다.")
        
        return bearing_pattern
        
    def create_discovery_timeline(self) -> pd.DataFrame:
        """발견의 타임라인"""
        
        print("\n📅 === 발견의 타임라인 ===\n")
        
        timeline = pd.DataFrame({
            'event': [
                '모세 탄생',
                '갈대상자 제작',
                '나일강 투하',
                '바로의 딸 발견',
                '예수 탄생',
                '세례 요한 준비',
                '요단강 세례',
                '어린양 선포'
            ],
            'time_reference': [
                '0',
                '3개월',
                '3개월',
                '3개월',
                '0',
                '30년',
                '30년',
                '30년'
            ],
            'csv_parallel': [
                '데이터 생성',
                'CSV 파일 생성',
                '파일 저장',
                'read_csv()',
                '원본 데이터',
                '분석 준비',
                '데이터 로드',
                'insights 발견'
            ],
            'significance': [5, 7, 8, 10, 5, 7, 8, 10]
        })
        
        print(timeline.to_string(index=False))
        
        # 시각적 타임라인
        print("\n📊 중요도 시각화:")
        for idx, row in timeline.iterrows():
            bars = '█' * row['significance']
            print(f"{row['event'][:15]:<15} {bars}")
        
        return timeline
        
    def run_complete_analysis(self) -> dict:
        """전체 분석 실행"""
        
        print("🔍 === 요한복음 1:29: 어린양 발견과 데이터 인식 ===\n")
        
        # 1. 어린양 참조 구절들
        print("📖 어린양 관련 성경 구절:")
        print(self.lamb_references[['verse_ref', 'lamb_type', 'csv_parallel']])
        print("\n" + "="*50 + "\n")
        
        # 2. '보라' 패턴 분석
        behold_pattern = self.analyze_behold_pattern()
        print("\n" + "="*50 + "\n")
        
        # 3. 계시의 점진성
        progression = self.analyze_lamb_progression()
        print("\n" + "="*50 + "\n")
        
        # 4. 발견 비교
        comparison = self.compare_discoveries()
        print("\n" + "="*50 + "\n")
        
        # 5. 죄를 지고 가는 패턴
        sin_bearing = self.analyze_sin_bearing_data()
        print("\n" + "="*50 + "\n")
        
        # 6. 발견 타임라인
        timeline = self.create_discovery_timeline()
        
        print("\n🎉 요한복음 1:29 분석 완료!")
        
        return {
            'lamb_references': self.lamb_references,
            'behold_pattern': behold_pattern,
            'progression': progression,
            'comparison': comparison,
            'sin_bearing': sin_bearing,
            'timeline': timeline
        }

def demo_lamb_discovery():
    """어린양 발견 분석 데모 실행"""
    analyzer = LambDiscoveryAnalyzer()
    results = analyzer.run_complete_analysis()
    return results

if __name__ == "__main__":
    print("🐑 어린양 발견 분석 모듈 테스트")
    demo_results = demo_lamb_discovery()
    print("\n✅ 테스트 완료!")

la = LambDiscoveryAnalyzer()
la.create_discovery_timeline()