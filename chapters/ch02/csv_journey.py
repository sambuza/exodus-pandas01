"""
개인 CSV 여정 모듈
나만의 갈대상자 만들고 건지기

"믿음으로 모세가 났을 때에 그 부모가 아름다운 아이임을 보고 석달 동안 숨겨 임금의 명령을 무서워 아니하였으며" (히 11:23)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import random

class PersonalCSVJourney:
    """개인의 CSV 여정 클래스"""
    
    def __init__(self, name: str = "신앙인"):
        """초기화
        
        Args:
            name: 사용자 이름
        """
        self.name = name
        self.journey_data = None
        self.rescued_data = None
        self.encoding_attempts = []
        
    def create_faith_basket(self) -> pd.DataFrame:
        """신앙 기록 갈대상자 만들기"""
        
        print(f"\n🧺 === {self.name}의 갈대상자 만들기 ===\n")
        
        # 7일간의 신앙 기록 생성
        dates = pd.date_range(start='2024-01-01', periods=7, freq='D')
        
        # 랜덤하게 결측치 포함
        bible_reading = ['창세기 1장', '창세기 2장', None, '출애굽기 1장', 
                        '출애굽기 2장', None, '요한복음 1장']
        
        prayer_minutes = [30, 45, 15, None, 60, 20, 40]
        
        thanks_items = ['건강', '가족', '일용할양식', None, '구원의 은혜', 
                       '성령충만', '새로운 깨달음']
        
        spiritual_state = ['평안', '기쁨', '연약함', '회복', '감사', None, '충만']
        
        # 데이터프레임 생성
        self.journey_data = pd.DataFrame({
            '날짜': dates,
            '성경읽기': bible_reading,
            '기도시간(분)': prayer_minutes,
            '감사제목': thanks_items,
            '영적상태': spiritual_state,
            '주일예배': [True, False, False, False, False, False, True],
            '새벽기도': [True, True, False, True, False, True, True]
        })
        
        print("📝 원본 기록 (갈대상자 내용물):")
        print(self.journey_data)

        
        # CSV로 저장 (갈대상자에 담기)
        filename = f'{self.name}_faith_journey.csv'
        self.journey_data.to_csv(filename, index=False, encoding='utf-8-sig')
        
        print(f"\n✅ 갈대상자가 '{filename}'으로 저장되었습니다!")
        
        # 파일 정보
        file_info = {
            'size': Path(filename).stat().st_size,
            'encoding': 'utf-8-sig',
            'rows': len(self.journey_data),
            'columns': len(self.journey_data.columns)
        }
        
        print(f"📦 상자 정보:")
        print(f"   크기: {file_info['size']} bytes")
        print(f"   행: {file_info['rows']}개, 열: {file_info['columns']}개")
        
        return self.journey_data
        
    def rescue_from_river(self, filename: str = None) -> pd.DataFrame:
        """나일강에서 갈대상자 건지기 (CSV 읽기)"""
        
        if filename is None:
            filename = f'{self.name}_faith_journey.csv'
            
        print(f"\n🌊 === 나일강에서 건지기 (CSV 읽기) ===\n")
        
        # 여러 인코딩 시도 (바로의 딸의 시녀들처럼)
        encodings_to_try = [
            ('utf-8-sig', '표준 UTF-8 (BOM)'),
            ('utf-8', '표준 UTF-8'),
            ('cp949', '한국어 CP949'),
            ('euc-kr', '한국어 EUC-KR'),
            ('latin-1', '서구 Latin-1')
        ]
        
        for encoding, description in encodings_to_try:
            try:
                print(f"🔍 시도: {description} ({encoding})")
                self.rescued_data = pd.read_csv(filename, encoding=encoding)
                self.encoding_attempts.append({
                    'encoding': encoding,
                    'success': True,
                    'description': description
                })
                print(f"✅ 성공! {description}로 데이터를 건졌습니다!")
                break
            except Exception as e:
                self.encoding_attempts.append({
                    'encoding': encoding,
                    'success': False,
                    'error': str(e)[:50]
                })
                print(f"❌ 실패: {encoding}")
                continue
        
        if self.rescued_data is not None:
            print(f"\n📊 건져낸 데이터 확인:")
            print(f"   행: {len(self.rescued_data)}개")
            print(f"   열: {self.rescued_data.columns.tolist()}")
            
            # 날짜 컬럼 파싱
            self.rescued_data['날짜'] = pd.to_datetime(self.rescued_data['날짜'])
            
        return self.rescued_data
    
    def find_hidden_moses_in_data(self) -> dict:
        """데이터에서 숨겨진 모세 찾기 (결측치 분석)"""
        
        print(f"\n🔎 === {self.name}의 숨겨진 데이터 찾기 ===\n")
        
        if self.rescued_data is None:
            print("⚠️ 먼저 데이터를 건져야 합니다!")
            return None
        
        # 결측치 분석
        missing_analysis = {}
        
        for column in self.rescued_data.columns:
            null_count = self.rescued_data[column].isnull().sum()
            null_ratio = (null_count / len(self.rescued_data)) * 100
            
            if null_count > 0:
                missing_analysis[column] = {
                    'count': null_count,
                    'ratio': null_ratio,
                    'missing_days': self.rescued_data[
                        self.rescued_data[column].isnull()
                    ]['날짜'].dt.strftime('%Y-%m-%d').tolist()
                }
        
        print("🕳️ 결측치 현황 (숨겨진 모세):")
        for col, info in missing_analysis.items():
            print(f"\n📍 {col}:")
            print(f"   결측: {info['count']}개 ({info['ratio']:.1f}%)")
            print(f"   날짜: {', '.join(info['missing_days'])}")
        
        # 결측치 패턴 분석
        print("\n🎯 결측치 패턴 분석:")
        missing_pattern = self.rescued_data.isnull().astype(int)
        
        for idx, row in missing_pattern.iterrows():
            date_str = self.rescued_data.loc[idx, '날짜'].strftime('%Y-%m-%d')
            visual = ""
            for col in ['성경읽기', '기도시간(분)', '감사제목', '영적상태']:
                if col in missing_pattern.columns:
                    visual += "□ " if row[col] == 1 else "■ "
            print(f"{date_str}: {visual}")
        
        print("\n💡 (■=데이터있음, □=결측치)")
        
        return missing_analysis
    
    def rescue_hidden_moses(self, strategy: str = 'grace') -> pd.DataFrame:
        """숨겨진 모세 구출하기 (결측치 처리)"""
        
        print(f"\n⛑️ === 결측치 구출 작전: {strategy} ===\n")
        
        if self.rescued_data is None:
            print("⚠️ 먼저 데이터를 건져야 합니다!")
            return None
        
        filled_data = self.rescued_data.copy()
        
        if strategy == 'grace':  # 은혜로 채우기
            print("✨ 은혜의 전략: 기본값으로 채우기")
            fill_values = {
                '성경읽기': '시편 23편',  # 기본 말씀
                '기도시간(분)': 30,  # 기본 기도시간
                '감사제목': '일용할 양식',  # 기본 감사
                '영적상태': '평안'  # 기본 상태
            }
            filled_data = filled_data.fillna(value=fill_values)
            
        elif strategy == 'wisdom':  # 지혜로 채우기
            print("🧠 지혜의 전략: 평균/최빈값으로 채우기")
            # 숫자형: 평균
            filled_data['기도시간(분)'] = filled_data['기도시간(분)'].fillna(
                filled_data['기도시간(분)'].mean()
            )
            # 문자형: 최빈값
            for col in ['성경읽기', '감사제목', '영적상태']:
                mode_val = filled_data[col].mode()
                if not mode_val.empty:
                    filled_data[col] = filled_data[col].fillna(mode_val[0])
                    
        elif strategy == 'faith':  # 믿음으로 채우기
            print("🙏 믿음의 전략: 앞의 값으로 채우기")
            filled_data = filled_data.fillna(method='ffill')
            
        elif strategy == 'truth':  # 진리로 대하기
            print("⚖️ 진리의 전략: 결측치 제거")
            filled_data = filled_data.dropna()
        
        # 결과 확인
        remaining_nulls = filled_data.isnull().sum().sum()
        print(f"\n📊 구출 결과:")
        print(f"   원래 결측치: {self.rescued_data.isnull().sum().sum()}개")
        print(f"   남은 결측치: {remaining_nulls}개")
        print(f"   구출 성공: {self.rescued_data.isnull().sum().sum() - remaining_nulls}개")
        
        return filled_data
    
    def analyze_spiritual_journey(self) -> dict:
        """영적 여정 분석"""
        
        print(f"\n📈 === {self.name}의 영적 여정 분석 ===\n")
        
        if self.rescued_data is None:
            print("⚠️ 먼저 데이터를 건져야 합니다!")
            return None
        
        analysis = {}
        
        # 1. 기도 통계
        prayer_stats = {
            'total': self.rescued_data['기도시간(분)'].sum(),
            'average': self.rescued_data['기도시간(분)'].mean(),
            'max': self.rescued_data['기도시간(분)'].max(),
            'consistency': self.rescued_data['기도시간(분)'].notna().sum() / len(self.rescued_data) * 100
        }
        
        print("🙏 기도 생활:")
        print(f"   총 기도시간: {prayer_stats['total']:.0f}분")
        print(f"   평균 기도시간: {prayer_stats['average']:.1f}분")
        print(f"   최대 기도시간: {prayer_stats['max']:.0f}분")
        print(f"   기도 일관성: {prayer_stats['consistency']:.1f}%")
        
        # 2. 성경읽기 패턴
        bible_count = self.rescued_data['성경읽기'].notna().sum()
        bible_rate = bible_count / len(self.rescued_data) * 100
        
        print(f"\n📖 성경읽기:")
        print(f"   읽은 날: {bible_count}일 / {len(self.rescued_data)}일")
        print(f"   읽기율: {bible_rate:.1f}%")
        
        # 3. 영적 상태 분포
        if '영적상태' in self.rescued_data.columns:
            state_counts = self.rescued_data['영적상태'].value_counts()
            print(f"\n😇 영적 상태 분포:")
            for state, count in state_counts.items():
                print(f"   {state}: {count}일")
        
        # 4. 주일/새벽 참여
        sunday_rate = self.rescued_data['주일예배'].sum() / len(self.rescued_data) * 100
        dawn_rate = self.rescued_data['새벽기도'].sum() / len(self.rescued_data) * 100
        
        print(f"\n⛪ 예배 참여:")
        print(f"   주일예배: {sunday_rate:.1f}%")
        print(f"   새벽기도: {dawn_rate:.1f}%")
        
        # 5. 종합 점수 (모세 구출 지수)
        rescue_index = (
            prayer_stats['consistency'] * 0.3 +
            bible_rate * 0.3 +
            sunday_rate * 0.2 +
            dawn_rate * 0.2
        )
        
        print(f"\n🏆 모세 구출 지수: {rescue_index:.1f}/100")
        
        if rescue_index >= 80:
            print("   ⭐ 탁월함! 바로의 딸처럼 사명을 잘 감당하고 있습니다!")
        elif rescue_index >= 60:
            print("   🌱 성장 중! 갈대상자를 잘 지키고 있습니다!")
        else:
            print("   🙏 더 힘내세요! 하나님이 함께하십니다!")
        
        analysis['prayer_stats'] = prayer_stats
        analysis['bible_rate'] = bible_rate
        analysis['sunday_rate'] = sunday_rate
        analysis['dawn_rate'] = dawn_rate
        analysis['rescue_index'] = rescue_index
        
        return analysis
    
    def create_comparison_report(self) -> pd.DataFrame:
        """모세와 나의 여정 비교"""
        
        print(f"\n📊 === 모세와 {self.name}의 여정 비교 ===\n")
        
        comparison = pd.DataFrame({
            '항목': [
                '준비 기간',
                '숨겨진 기간',
                '발견 방법',
                '구출자',
                '사명'
            ],
            '모세': [
                '3개월 (갈대상자 준비)',
                '나일강 갈대숲',
                '바로의 딸이 발견',
                '이방인 공주',
                '이스라엘 구원'
            ],
            f'{self.name}': [
                '7일 (데이터 수집)',
                'CSV 파일',
                'pd.read_csv()',
                'Python/Pandas',
                '영적 성장'
            ],
            'CSV_의미': [
                '데이터 구조화',
                '파일 시스템',
                '데이터 로드',
                '분석 도구',
                'insights 발견'
            ]
        })
        
        print(comparison.to_string(index=False))
        
        return comparison

def demo_personal_csv_journey(name: str = None):
    """개인 CSV 여정 데모 실행"""
    
    if name is None:
        name = "데이브"
    
    print(f"🚀 === {name}의 CSV 여정 시작 ===")
    
    journey = PersonalCSVJourney(name)
    
    # 1. 갈대상자 만들기
    faith_data = journey.create_faith_basket()
    print("\n" + "="*50 + "\n")
    
    # 2. 나일강에서 건지기
    rescued_data = journey.rescue_from_river()
    print("\n" + "="*50 + "\n")
    
    # 3. 숨겨진 데이터 찾기
    missing_analysis = journey.find_hidden_moses_in_data()
    print("\n" + "="*50 + "\n")
    
    # 4. 결측치 구출 (은혜의 전략)
    filled_data = journey.rescue_hidden_moses('grace')
    print("\n" + "="*50 + "\n")
    
    # 5. 영적 여정 분석
    spiritual_analysis = journey.analyze_spiritual_journey()
    print("\n" + "="*50 + "\n")
    
    # 6. 모세와 비교
    comparison = journey.create_comparison_report()
    
    print(f"\n🎉 {name}의 CSV 여정 완료!")
    
    return {
        'faith_data': faith_data,
        'rescued_data': rescued_data,
        'missing_analysis': missing_analysis,
        'filled_data': filled_data,
        'spiritual_analysis': spiritual_analysis,
        'comparison': comparison
    }

if __name__ == "__main__":
     print("📚 개인 CSV 여정 모듈 테스트")
     demo_results = demo_personal_csv_journey("테스트유저")
     print("\n✅ 테스트 완료!")

