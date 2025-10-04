
'''
Chapter 35 통합 실행 스크립트
자원 봉헌 - IO 확장

"이스라엘 자손이 여호와께 드리는 예물은 이러하니 곧 금과 은과 놋과" (출애굽기 35:5)
"여기 한 아이가 있어 보리떡 다섯 개와 물고기 두 마리를 가졌나이다 그러나 이것이 이 많은 사람에게 얼마나 되겠사옵나이까" (요한복음 6:9)
'''

import sys
from pathlib import Path
import json
from datetime import datetime
import pandas as pd
import numpy as np
import os

# 프로젝트 루트 추가
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# 절대 임포트 사용
from chapters.ch35.offering_data import OfferingDataGenerator
from chapters.ch35.csv_io_handler import CsvIOHandler
from chapters.ch35.parquet_io_handler import ParquetIOHandler
from chapters.ch35.excel_io_handler import ExcelIOHandler

def print_chapter_header():
    '''챕터 헤더 출력'''
    header = (
        "╔══════════════════════════════════════════════════════════════════════╗\n"
        "║                    JesusBornd Pandas Edition                         ║\n"
        "║                                                                      ║\n"
        "║             Chapter 35: 자원 봉헌 - IO 확장                          ║\n"
        "║                                                                      ║\n"
        "    \"이스라엘 자손이 여호와께 드리는 예물은 이러하니 곧 금과 은과 놋과\" (출애굽기 35:5)\n"
        "    \"여기 한 아이가 있어 보리떡 다섯 개와 물고기 두 마리를 가졌나이다 그러나 이것이 이 많은 사람에게 얼마나 되겠사옵나이까\" (요한복음 6:9)\n"
        "║                                                                      ║\n"
        "║      출애굽기 35장: 자원 봉헌                                        ║\n"
        "║      요한복음 6:9: 오병이어                                          ║\n"
        "╚══════════════════════════════════════════════════════════════════════╝"
    )
    print(header)

def run_offering_data_generation():
    '''자원 봉헌 데이터 생성 섹션 실행'''
    print("\n🎁 === 자원 봉헌 데이터 생성 ===")
    print("다양한 형식의 데이터를 효율적으로 읽고 쓰는 데 사용될 자원 봉헌 관련 데이터를 생성합니다.")
    print("Generates offering-related data for efficient reading and writing of various data formats.")

    try:
        generator = OfferingDataGenerator()
        data = generator.generate_offering_data()
        print("\n✅ 자원 봉헌 데이터 생성 완료:")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ 자원 봉헌 데이터 생성 중 오류 발생: {e}")
        return None

def run_csv_io_operations(df):
    '''CSV 파일 입출력 섹션 실행'''
    print("\n📄 === CSV 파일 입출력 ===")
    print("`to_csv()`와 `read_csv()`를 사용하여 CSV 파일로 데이터를 저장하고 불러옵니다.")
    print("Saves and loads data to/from CSV files using `to_csv()` and `read_csv()`.")

    if df is None:
        print("⚠️ 데이터가 없어 CSV 파일 입출력을 건너뜁니다.")
        return None

    try:
        handler = CsvIOHandler(df)
        csv_filename = "ch35_offering_data.csv"
        saved_path = handler.save_data(csv_filename)
        loaded_df = handler.load_data(csv_filename)
        print("\n✅ CSV 파일 입출력 완료 (불러온 데이터 일부):")
        print(loaded_df.head())
        
        if os.path.exists(saved_path): os.remove(saved_path)
        return loaded_df
    except Exception as e:
        print(f"❌ CSV 파일 입출력 중 오류 발생: {e}")
        return None

def run_parquet_io_operations(df):
    '''Parquet 파일 입출력 섹션 실행'''
    print("\n📦 === Parquet 파일 입출력 ===")
    print("`to_parquet()`와 `read_parquet()`를 사용하여 Parquet 파일로 데이터를 저장하고 불러옵니다.")
    print("Saves and loads data to/from Parquet files using `to_parquet()` and `read_parquet()`.")

    if df is None:
        print("⚠️ 데이터가 없어 Parquet 파일 입출력을 건너뜁니다.")
        return None

    try:
        handler = ParquetIOHandler(df)
        parquet_filename = "ch35_offering_data.parquet"
        saved_path = handler.save_data(parquet_filename)
        loaded_df = handler.load_data(parquet_filename)
        print("\n✅ Parquet 파일 입출력 완료 (불러온 데이터 일부):")
        print(loaded_df.head())
        
        if os.path.exists(saved_path): os.remove(saved_path)
        return loaded_df
    except Exception as e:
        print(f"❌ Parquet 파일 입출력 중 오류 발생: {e}")
        return None

def run_excel_io_operations(df):
    '''Excel 파일 입출력 섹션 실행'''
    print("\n📊 === Excel 파일 입출력 ===")
    print("`to_excel()`와 `read_excel()`를 사용하여 Excel 파일로 데이터를 저장하고 불러옵니다.")
    print("Saves and loads data to/from Excel files using `to_excel()` and `read_excel()`.")

    if df is None:
        print("⚠️ 데이터가 없어 Excel 파일 입출력을 건너뜁니다.")
        return None

    try:
        handler = ExcelIOHandler(df)
        excel_filename = "ch35_offering_data.xlsx"
        saved_path = handler.save_data(excel_filename)
        loaded_df = handler.load_data(excel_filename)
        print("\n✅ Excel 파일 입출력 완료 (불러온 데이터 일부):")
        print(loaded_df.head())
        
        if os.path.exists(saved_path): os.remove(saved_path)
        return loaded_df
    except Exception as e:
        print(f"❌ Excel 파일 입출력 중 오류 발생: {e}")
        return None

def show_blending_insights(original_df, csv_df, parquet_df, excel_df):
    '''블렌딩 모드 통합 통찰 출력'''
    print("\n🎨 === 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰 ===")
    print("Blending Mode: Integrated Insights from Exodus x John")

    blending_insights = [
        "📊 IO 확장 = 데이터의 활용도 극대화와 분석 파이프라인 확장",
        "🎁 자원 봉헌 = 다양한 자원의 효율적 활용과 하나님의 뜻을 이루는 프로젝트",
        "🍞🐟 오병이어 = 작은 자원의 놀라운 확장과 풍성함",
        "💡 데이터 접근성 = 영적 성장과 분석 효율성의 조화"
    ]

    print("\n💎 핵심 발견들 (Key Discoveries):\n")
    for insight in blending_insights:
        print(f"   {insight}")

    print("\n--- 개인화된 통찰 (Personalized Insights) ---")
    if original_df is not None and csv_df is not None and parquet_df is not None and excel_df is not None:
        print("✨ 자원 봉헌처럼 다양한 형식의 데이터를 효율적으로 다루어 데이터의 활용도를 높였습니다.")
        print("✨ 오병이어처럼 작은 데이터라도 효율적으로 읽고 써서 분석 파이프라인을 확장합니다.")
    else:
        print("🙏 자원 봉헌처럼 나의 모든 것을 주님께 드리고, 오병이어처럼 주님 안에서 놀랍게 확장되게 하소서.")

def show_next_chapter_preview():
    '''다음 챕터 미리보기'''
    preview = (
        "🌟 === Chapter 36 미리보기 (Preview) ===\n\n"
        "\"장인의 손 - 결합·재구성 심화 (Craftsman's Hand - Advanced Join and Reshaping)\"\n\n"
        "브살렐과 오홀리압이 성막 건축에 필요한 모든 기술과 지혜를 부여받아 최고의 작품을 만들었듯이, 데이터 분석에서도 여러 데이터셋을 복잡하게 결합하고 재구성하는 것은 데이터의 숨겨진 패턴과 의미를 발견하고 깊이 있는 통찰을 얻는 데 필수적입니다.\n\n"
        "Just as Bezalel and Oholiab were endowed with all the skills and wisdom needed to build the tabernacle, creating the finest work, in data analysis, complex joining and reshaping of multiple datasets are essential for discovering hidden patterns and meanings and gaining deep insights.\n\n"
        "다음 장에서 배울 내용 (What you'll learn in the next chapter):\n"
        "📁 `wide_to_long()`: 넓은 형식 데이터를 긴 형식으로 변환\n"
        "🔍 다단 피벗(Multi-level Pivot) 및 역피벗(Unpivot)\n"
        "🎯 고급 조인(Join) 전략 (예: Fuzzy Join 개념)\n"
        "📊 장인의 손처럼 정교하고 복잡한 데이터 결합 및 재구성을 통해 하나님의 지혜를 탐구\n\n"
        "\"모세가 그 장인의 말을 듣고 그 말대로 하여\" (출애굽기 36:1-7)\n"
        "\"예수께서 대답하여 이르시되 너희가 이 성전을 헐라 내가 사흘 동안에 일으키리라 하시니라\" (요한복음 2:19)"
    )
    print(preview)

def run_chapter35(interactive: bool = True):
    '''Chapter 35 전체 실행'''
    # 헤더 출력
    print_chapter_header()

    if interactive:
        print("📖 Chapter 35을 시작합니다!")
        print("이 챕터에서는 다양한 형식의 데이터를 효율적으로 읽고 쓰는 IO 확장 기법을 배우고, 자원 봉헌과 오병이어 사건을 탐구합니다.")
        print("This chapter introduces IO extension techniques for efficiently reading and writing various data formats, exploring voluntary offerings and the feeding of the five thousand.")
        input("\n▶️ 계속하려면 Enter를 눌러주세요... (Press Enter to continue...)")

    # 결과 저장용 딕셔너리
    results = {
        'chapter': '35',
        'title': '자원 봉헌 - IO 확장',
        'original_data': None,
        'csv_data': None,
        'parquet_data': None,
        'excel_data': None
    }

    # 1. 자원 봉헌 데이터 생성
    original_df = run_offering_data_generation()
    results['original_data'] = original_df

    if interactive:
        input("\n▶️ CSV 파일 입출력을 시작하려면 Enter를 눌러주세요... (Press Enter to start CSV IO operations...)")

    # 2. CSV 파일 입출력
    csv_df = run_csv_io_operations(original_df)
    results['csv_data'] = csv_df

    if interactive:
        input("\n▶️ Parquet 파일 입출력을 시작하려면 Enter를 눌러주세요... (Press Enter to start Parquet IO operations...)")

    # 3. Parquet 파일 입출력
    parquet_df = run_parquet_io_operations(original_df) # 원본 데이터에 적용
    results['parquet_data'] = parquet_df

    if interactive:
        input("\n▶️ Excel 파일 입출력을 시작하려면 Enter를 눌러주세요... (Press Enter to start Excel IO operations...)")

    # 4. Excel 파일 입출력
    excel_df = run_excel_io_operations(original_df) # 원본 데이터에 적용
    results['excel_data'] = excel_df

    # 5. 블렌딩 통찰
    show_blending_insights(original_df, csv_df, parquet_df, excel_df)

    # 6. 다음 챕터 미리보기
    show_next_chapter_preview()

    # 7. 마무리 기도
    print("\n🙏 === 마무리 기도 (Closing Prayer) ===")
    prayer = (
        "\"주님, 자원 봉헌처럼 저의 모든 자원을 주님께 드리고, 오병이어처럼 주님 안에서 놀랍게 확장되게 하소서.\n"
        "데이터 IO 확장 전략을 통해 저의 영적 기록을 효율적으로 관리하고, 주님의 뜻을 온전히 이해하게 하소서.\n"
        "데이터 분석을 통해 하나님의 지혜로운 자원 관리 원리를 더욱 깊이 깨닫게 하소서. 예수님의 이름으로 기도합니다. 아멘.\""
    )
    print(prayer)

    print(f"\n🎉 Chapter 35 완료! 서른다섯 번째 광야 여정을 마치셨습니다!")
    print(f"🎉 Chapter 35 Complete! You have finished the thirty-fifth wilderness journey!")
    print(f"📊 분석 결과가 저장되었습니다. (Analysis results have been stored.)")

    return results

def main():
    '''메인 실행 함수'''
    try:
        results = run_chapter35(interactive=True)

        # 결과 저장 (선택사항)
        save_results = input("\n💾 분석 결과를 파일로 저장하시겠어요? (y/n, 기본값 n): ").strip().lower()
        if save_results == 'y':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ch35_results_{timestamp}.json"

            # DataFrame은 JSON으로 저장할 수 없으므로 요약 정보만 저장
            summary_results = {
                'chapter': results['chapter'],
                'title': results['title'],
                'completed_at': timestamp,
                'has_original_data': results['original_data'] is not None,
                'has_csv_data': results['csv_data'] is not None,
                'has_parquet_data': results['parquet_data'] is not None,
                'has_excel_data': results['excel_data'] is not None
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary_results, f, ensure_ascii=False, indent=2)

            print(f"✅ 결과가 {filename}에 저장되었습니다! (Results saved to {filename}!)")

        return results

    except KeyboardInterrupt:
        print("\n\n⏸️ 사용자가 중단했습니다. (User interrupted.)")
        return None
    except Exception as e:
        print(f"\n❌ 실행 중 오류가 발생했습니다: {e}")
        print("🔧 코드와 데이터를 확인해주세요. (Please check the code and data.)")
        return None


if __name__ == "__main__":
    print("🚀 JesusBornd Pandas Chapter 35 시작! (Starting JesusBornd Pandas Chapter 35!)\n")
    main()
