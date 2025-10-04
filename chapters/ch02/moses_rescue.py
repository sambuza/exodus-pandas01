"""
출애굽기 2장 분석 모듈
모세의 구출과 CSV 파일 읽기의 평행 이론

"더 숨길 수 없이 되매 그를 위하여 갈 상자를 가져다가 역청과 나무 진을 칠하고 아이를 거기 담아 하숫가 갈대 사이에 두고" (출 2:3)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from utils.bible_utils import get_hebrew_meaning

class MosesRescueAnalyzer:
    """모세 구출 스토리와 CSV 읽기 분석 클래스"""
    
    def __init__(self):
        """분석기 초기화"""
        self.moses_family_data = None
        self.rescue_process = None
        self.create_moses_family_data()
        
    def create_moses_family_data(self):
        """모세 가족 데이터 생성"""
        self.moses_family_data = pd.DataFrame({
            'name': ['Amram', 'Jochebed', 'Miriam', 'Aaron', 'Moses', None],
            'korean_name': ['아므람', '요게벳', '미리암', '아론', '모세', None],
            'hebrew': ['עַמְרָם', 'יוֹכֶבֶד', 'מִרְיָם', 'אַהֲרֹן', 'מֹשֶׁה', None],
            'role': ['레위인 아버지', '레위인 어머니', '선지자', '대제사장', '지도자', '알 수 없음'],
            'age_at_exodus': [137, 127, None, 83, 80, None],
            'calling_age': [None, None, 7, 83, 80, None],
            'key_event': ['모세의 아버지', '갈대상자에 담음', '구원의 노래', '금송아지 사건', '홍해 가르기', None]
        })
        
    def simulate_csv_creation(self) -> pd.DataFrame:
        """CSV 파일 생성 시뮬레이션 (갈대 상자 만들기)"""
        
        print("🧺 === 갈대 상자 준비 (CSV 생성) ===\n")
        
        # CSV로 저장
        filepath = 'moses_family.csv'
        self.moses_family_data.to_csv(filepath, index=False, encoding='utf-8-sig')
        
        print(f"✅ 갈대 상자가 준비되었습니다: {filepath}")
        print(f"📦 담긴 데이터:")
        print(self.moses_family_data)
        
        # 파일 정보
        file_size = Path(filepath).stat().st_size
        print(f"\n📏 상자 크기: {file_size} bytes")
        print(f"🏷️ 인코딩: UTF-8 with BOM (히브리어 보호)")
        
        return self.moses_family_data
        
    def analyze_rescue_process(self) -> dict:
        """구출 과정 분석 (CSV 읽기 과정)"""
        
        print("\n🌊 === 나일강에서 건지기 (CSV 읽기) ===\n")
        
        rescue_steps = {
            '1_preparation': {
                'hebrew': 'הֲכָנָה',
                'korean': '준비',
                'csv_equivalent': 'pd.read_csv() 준비',
                'description': '갈대상자에 역청을 바르듯, 인코딩 설정'
            },
            '2_placement': {
                'hebrew': 'הַנָּחָה',
                'korean': '배치',
                'csv_equivalent': '파일 경로 지정',
                'description': '나일강 갈대 사이에 두듯, 파일 위치 확인'
            },
            '3_discovery': {
                'hebrew': 'גִּלּוּי',
                'korean': '발견',
                'csv_equivalent': 'DataFrame 로드',
                'description': '바로의 딸이 발견하듯, 데이터 발견'
            },
            '4_identification': {
                'hebrew': 'זִהוּי',
                'korean': '확인',
                'csv_equivalent': 'df.info(), df.head()',
                'description': '히브리 아이임을 알듯, 데이터 타입 확인'
            }
        }
        
        for step_key, step_info in rescue_steps.items():
            step_num = step_key.split('_')[0]
            print(f"단계 {step_num}: {step_info['korean']} ({step_info['hebrew']})")
            print(f"   CSV 대응: {step_info['csv_equivalent']}")
            print(f"   의미: {step_info['description']}\n")
        
        self.rescue_process = rescue_steps
        return rescue_steps
        
    def find_hidden_moses(self) -> pd.DataFrame:
        """숨겨진 모세 찾기 (결측치 탐색)"""
        
        print("🔍 === 숨겨진 데이터 찾기 ===\n")
        
        # 결측치 현황
        null_counts = self.moses_family_data.isnull().sum()
        null_percentages = (null_counts / len(self.moses_family_data)) * 100
        
        missing_report = pd.DataFrame({
            '컬럼명': null_counts.index,
            '결측치_개수': null_counts.values,
            '결측치_비율(%)': null_percentages.values.round(1)
        })
        
        missing_report = missing_report[missing_report['결측치_개수'] > 0]
        
        print("⚠️ 발견된 결측치 (숨겨진 모세):")
        print(missing_report)
        
        print("\n💭 영적 통찰:")
        print("   갈대 숲에 숨겨진 모세처럼,")
        print("   결측치도 존재하지만 아직 보이지 않는 데이터입니다.")
        print("   때로는 '없음'도 중요한 정보가 됩니다.")
        
        return missing_report
        
    def demonstrate_encoding_issues(self) -> dict:
        """인코딩 문제 시연 (언어 장벽)"""
        
        print("\n🗣️ === 언어 장벽 극복 (인코딩 처리) ===\n")
        
        encoding_results = {}
        encodings = ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr', 'latin-1']
        
        for encoding in encodings:
            try:
                df = pd.read_csv('moses_family.csv', encoding=encoding)
                encoding_results[encoding] = {
                    'success': True,
                    'rows': len(df),
                    'hebrew_readable': '히브리어' in str(df.values)
                }
                print(f"✅ {encoding}: 성공 (히브리어 읽기: {encoding_results[encoding]['hebrew_readable']})")
            except Exception as e:
                encoding_results[encoding] = {
                    'success': False,
                    'error': str(e)
                }
                print(f"❌ {encoding}: 실패")
        
        print("\n📌 최적 인코딩: utf-8-sig (BOM으로 히브리어 보호)")
        return encoding_results
        
    def analyze_name_meanings(self) -> pd.DataFrame:
        """이름의 의미 분석"""
        
        print("\n📜 === 이름의 의미 (정체성 발견) ===\n")
        
        name_meanings = pd.DataFrame({
            '이름': ['모세', '미리암', '아론', '아므람', '요게벳'],
            '히브리어': ['מֹשֶׁה', 'מִרְיָם', 'אַהֲרֹן', 'עַמְרָם', 'יוֹכֶבֶד'],
            '의미': [
                '물에서 건진 자',
                '쓴물/반역',
                '빛을 가진 자',
                '고귀한 백성',
                '여호와는 영광'
            ],
            'CSV_의미': [
                'read_csv()로 건진 데이터',
                '잘못된 인코딩(쓴물)',
                'info()로 밝혀진 정보',
                'DataFrame의 귀중함',
                'pandas의 영광스런 기능'
            ]
        })
        
        print(name_meanings.to_string(index=False))
        
        print("\n✨ 통찰: 각 이름이 데이터 처리 과정의 한 단계를 상징합니다.")
        
        return name_meanings
        
    def run_complete_analysis(self) -> dict:
        """전체 분석 실행"""
        
        print("🎭 === 출애굽기 2장: 모세 구출과 CSV 읽기 ===\n")
        
        # 1. CSV 생성 (갈대상자 만들기)
        csv_data = self.simulate_csv_creation()
        print("\n" + "="*50 + "\n")
        
        # 2. 구출 과정 분석
        rescue_process = self.analyze_rescue_process()
        print("\n" + "="*50 + "\n")
        
        # 3. 숨겨진 데이터 찾기
        missing_data = self.find_hidden_moses()
        print("\n" + "="*50 + "\n")
        
        # 4. 인코딩 문제 시연
        encoding_results = self.demonstrate_encoding_issues()
        print("\n" + "="*50 + "\n")
        
        # 5. 이름의 의미 분석
        name_meanings = self.analyze_name_meanings()
        
        print("\n🎉 출애굽기 2장 분석 완료!")
        
        return {
            'csv_data': csv_data,
            'rescue_process': rescue_process,
            'missing_data': missing_data,
            'encoding_results': encoding_results,
            'name_meanings': name_meanings
        }

def demo_moses_rescue():
    """모세 구출 분석 데모 실행"""
    analyzer = MosesRescueAnalyzer()
    results = analyzer.run_complete_analysis()
    return results

if __name__ == "__main__":
    print("📚 모세 구출 분석 모듈 테스트")
    demo_results = demo_moses_rescue()
    print("\n✅ 테스트 완료!")