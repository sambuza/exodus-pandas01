'''
Chapter 34 통합 실행 스크립트
새 돌판 - 정규화와 표준화

"여호와께서 모세에게 이르시되 너는 돌판 둘을 처음 것과 같이 깎아 만들라 네가 깨뜨린 처음 판에 쓴 말을 내가 그 판에 쓰리라" (출애굽기 34:1)
"우리가 다 그의 충만한 데서 받으니 은혜 위에 은혜러라" (요한복음 1:16)
'''

import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd
import numpy as np

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch34.new_tablets_data import NewTabletsDataGenerator
from chapters.ch34.min_max_normalizer import MinMaxNormalizer
from chapters.ch34.zscore_standardizer import ZscoreStandardizer
from chapters.ch34.string_normalizer import StringNormalizer

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        "╔══════════════════════════════════════════════════════════════════════╗\n"
        "║                    JesusBornd Pandas Edition                         ║\n"
        "║                                                                      ║\n"
        "║             Chapter 34: 새 돌판 - 정규화와 표준화                    ║\n"
        "║                                                                      ║\n"
        "║    \"여호와께서 모세에게 이르시되 너는 돌판 둘을 처음 것과 같이 깎아 만들라 네가 깨뜨린 처음 판에 쓴 말을 내가 그 판에 쓰리라\" (출애굽기 34:1)\n"
        "║    \"우리가 다 그의 충만한 데서 받으니 은혜 위에 은혜러라\" (요한복음 1:16)\n"
        "║                                                                      ║\n"
        "║      출애굽기 34장: 새 돌판과 언약 갱신                               ║\n"
        "║      요한복음 1:16: 은혜 위에 은혜                                     ║\n"
        "╚══════════════════════════════════════════════════════════════════════╝"
    )
    print(header)

def run_new_tablets_data_generation():
    '''새 돌판 데이터 생성 섹션 실행'''
    print("\n📜 === 새 돌판 데이터 생성 ===")
    print("정규화와 표준화에 사용될 새 돌판 관련 데이터를 생성합니다.")
    print("Generates New Tablets related data for normalization and standardization.")

    try:
        generator = NewTabletsDataGenerator()
        data = generator.generate_tablets_data()
        print("\n✅ 새 돌판 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 새 돌판 데이터 생성 중 오류 발생: {e}")
        return None

def run_min_max_normalization(df):
    '''Min-Max 정규화 섹션 실행'''
    print("\n📈 === Min-Max 정규화 ===")
    print("데이터를 특정 범위(예: 0~1)로 조정하여 모든 특성이 동일한 중요도를 가지도록 합니다.")
    print("Adjusts data to a specific range (e.g., 0-1) so that all features have equal importance.")

    if df is None:
        print("⚠️ 데이터가 없어 Min-Max 정규화를 건너뜁니다.")
        return None

    try:
        normalizer = MinMaxNormalizer(df)
        normalized_df = normalizer.apply_min_max_scaling('obedience_score')
        print("\n✅ Min-Max 정규화 적용 완료 (일부):")
        print(normalized_df.head())
        return normalized_df
    except Exception as e:
        print(f"❌ Min-Max 정규화 중 오류 발생: {e}")
        return None

def run_zscore_standardization(df):
    '''Z-score 표준화 섹션 실행'''
    print("\n📊 === Z-score 표준화 ===")
    print("데이터를 평균 0, 표준편차 1로 조정하여 데이터의 분포를 통일합니다.")
    print("Adjusts data to have a mean of 0 and a standard deviation of 1, unifying data distribution.")

    if df is None:
        print("⚠️ 데이터가 없어 Z-score 표준화를 건너뜁니다.")
        return None

    try:
        standardizer = ZscoreStandardizer(df)
        standardized_df = standardizer.apply_zscore_standardization('divine_favor')
        print("\n✅ Z-score 표준화 적용 완료 (일부):")
        print(standardized_df.head())
        return standardized_df
    except Exception as e:
        print(f"❌ Z-score 표준화 중 오류 발생: {e}")
        return None

def run_string_normalization(df):
    '''문자열 정규화 섹션 실행'''
    print("\n📝 === 문자열 정규화 ===")
    print("텍스트 데이터의 다양한 표현을 통일하여 분석의 일관성을 확보합니다.")
    print("Ensures consistency in text analysis by unifying various representations of text data.")

    if df is None:
        print("⚠️ 데이터가 없어 문자열 정규화를 건너뜁니다.")
        return None

    try:
        normalizer = StringNormalizer(df)
        # 'commandment_text' 컬럼에 다양한 문자열 표현 추가 (예시)
        df_temp = df.copy()
        df_temp.loc[0, 'commandment_text'] = "Thou shalt not kill."
        df_temp.loc[1, 'commandment_text'] = "Thou shalt not steal."
        df_temp.loc[2, 'commandment_text'] = "Thou shalt not kill!"
        df_temp.loc[3, 'commandment_text'] = "Thou shalt not steal."
        
        normalized_string_df = normalizer.apply_string_normalization('commandment_text')
        print("\n✅ 문자열 정규화 적용 완료 (일부):")
        print(normalized_string_df.head())
        return normalized_string_df
    except Exception as e:
        print(f"❌ 문자열 정규화 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, normalized_df, standardized_df, string_normalized_df):
    '''블렌딩 모드 통합 통찰 출력'''
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 정규화와 표준화 = 데이터의 특성 통일과 모델 성능 향상",
        "📜 새 돌판 = 깨어진 언약의 회복과 하나님의 변치 않는 말씀",
        "🙏 은혜 위에 은혜 = 예수님의 충만한 은혜와 데이터의 풍성한 정보 활용",
        "💡 데이터 스케일 조정 = 영적 분별력과 지혜로운 의사결정"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and normalized_df is not None and standardized_df is not None and string_normalized_df is not None:
        print("✨ 새 돌판에 십계명을 다시 받은 것처럼, 데이터의 스케일을 조정하여 본질적인 특성을 유지합니다.")
        print("✨ 은혜 위에 은혜를 더하는 것처럼, 정규화와 표준화를 통해 데이터의 모든 정보를 효과적으로 활용합니다.")
    else:
        print("🙏 새 돌판처럼 저의 마음을 새롭게 하시고, 주님의 은혜 위에 은혜를 더하게 하소서.")

def show_next_chapter_preview():
    """다음 챕터 미리보기"""
    preview = (
        "🌟 === Chapter 35 미리보기 (Preview) ===\n\n"
        "\"브살렐과 오홀리압, 그리고 마음이 지혜로운 자\" (출애굽기 35:30)\n\n"
        "다음 장에서는 성막 건축을 위한 거룩한 장인, 브살렐과 오홀리압의 이야기를 통해\n"
        "데이터 시각화의 장인을 만나봅니다. Matplotlib와 Seaborn을 사용하여\n"
        "하나님의 영광을 데이터로 그려내는 방법을 배웁니다.\n\n"
        "🎨 데이터 시각화 기초: Matplotlib와 Seaborn 소개\n"
        "🔨 다양한 플롯 유형: 라인, 바, 산점도 등\n"
        "✨ 미적 감각: 플롯 스타일링과 커스터마이징"
    )
    print(preview)

def run_chapter34(interactive: bool = True):
    """Chapter 34 전체 실행"""
    print_chapter_header()

    if interactive:
        input("\n▶️ Chapter 34을 시작하려면 Enter를 눌러주세요...")

    results = {
        'chapter': '34',
        'title': '새 돌판 - 정규화와 표준화',
        'original_data': None,
        'normalized_data': None,
        'standardized_data': None,
        'string_normalized_data': None
    }

    original_df = run_new_tablets_data_generation()
    if original_df is not None:
        results['original_data'] = original_df.to_dict()

        if interactive:
            input("\n▶️ Min-Max 정규화를 시작하려면 Enter를 눌러주세요...")
        
        normalized_df = run_min_max_normalization(original_df.copy())
        if normalized_df is not None:
            results['normalized_data'] = normalized_df.to_dict()

        if interactive:
            input("\n▶️ Z-score 표준화를 시작하려면 Enter를 눌러주세요...")

        standardized_df = run_zscore_standardization(original_df.copy())
        if standardized_df is not None:
            results['standardized_data'] = standardized_df.to_dict()

        if interactive:
            input("\n▶️ 문자열 정규화를 시작하려면 Enter를 눌러주세요...")

        string_normalized_df = run_string_normalization(original_df.copy())
        if string_normalized_df is not None:
            results['string_normalized_data'] = string_normalized_df.to_dict()

        show_blending_insights(original_df, normalized_df, standardized_df, string_normalized_df)
    
    show_next_chapter_preview()

    print("\n🙏 === 마무리 기도 ===")
    prayer = """
"하나님 아버지, 깨어진 돌판을 새롭게 하시고 다시 언약을 새겨주신 주님의 은혜에 감사합니다.
우리의 불완전한 데이터를 정규화하고 표준화하는 과정을 통해,
모든 것을 새롭게 하시고 질서를 부여하시는 주님의 손길을 느낍니다.
은혜 위에 은혜를 더하시듯, 우리의 삶도 주님의 기준에 맞춰 아름답게 다듬어주소서.
예수님의 이름으로 기도합니다. 아멘."
    """
    print(prayer)

    print(f"\n🎉 Chapter 34 완료! 새 돌판에 새겨진 언약을 마음에 새기는 여정이었습니다.")
    return results

def main():
    """메인 실행 함수"""
    try:
        results = run_chapter34(interactive=True)

        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch34_results_{timestamp}.json"
            
            # DataFrame을 JSON으로 직접 저장하기 어려우므로 to_dict() 사용
            serializable_results = {}
            for key, value in results.items():
                if isinstance(value, pd.DataFrame):
                    serializable_results[key] = value.to_dict(orient='split')
                else:
                    serializable_results[key] = value

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(serializable_results, f, ensure_ascii=False, indent=2)
            
            print(f"✅ 결과가 {filename}에 저장되었습니다!")

    except KeyboardInterrupt:
        print("\n\n⏸️ 사용자가 중단했습니다.")
    except Exception as e:
        print(f"\n❌ 실행 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    print("🚀 JesusBornd Pandas Chapter 34 시작!\n")
    main()

        