import pandas as pd
import numpy as np

def analyze_cana_miracle_datatypes():
    """요한복음 2:1-11 가나 혼인잔치 데이터타입 분석"""
    print("\n🍷 가나 혼인잔치: 물이 포도주로, 데이터 타입의 기적")
    print("=" * 50)

    miracle_data = pd.DataFrame({
        '요소': ['물', '포도주', '항아리 수', '용량(리터)', '주인 반응', '하인 반응'],
        '초기_상태': ['물', '없음', '6개', '40(x6)', '당황', '순종'],
        '최종_상태': ['포도주', '있음', '6개', '240', '놀람', '확신'],
        '초기_데이터_타입_비유': ['category', 'category', 'string', 'string', 'string', 'string'],
        '최종_데이터_타입_비유': ['category', 'category', 'integer', 'integer', 'string', 'string']
    })
    print(miracle_data)
    print("\n📊 가나 기적 DataFrame의 데이터 타입:\n", miracle_data.dtypes)

    # '용량(리터)' 초기 상태를 numeric으로 변환 시도
    miracle_data['용량_numeric_초기'] = pd.to_numeric(miracle_data['초기_상태'].str.extract(r'(\d+)', expand=False), errors='coerce')
    miracle_data['용량_numeric_최종'] = pd.to_numeric(miracle_data['최종_상태'].loc[3], errors='coerce')

    print("\n🔄 '용량(리터)' 초기/최종 상태를 numeric으로 변환 시도 후:\n", miracle_data[['용량_numeric_초기', '용량_numeric_최종']].dtypes)
    print(miracle_data[['요소', '초기_상태', '용량_numeric_초기', '최종_상태', '용량_numeric_최종']])
    print("   -> 초기 상태의 문자열에서 숫자를 추출하여 변환. 데이터 전처리의 중요성!")

    # 초기 상태와 최종 상태의 데이터 타입 변화 비유
    print("\n✨ 초기 상태와 최종 상태의 데이터 타입 변화 비유:")
    for i in range(len(miracle_data)):
        print(f"   {miracle_data.loc[i, '요소']}: {miracle_data.loc[i, '초기_데이터_타입_비유']} -> {miracle_data.loc[i, '최종_데이터_타입_비유']}")

    return miracle_data

def main():
    analyze_cana_miracle_datatypes()

if __name__ == "__main__":
    main()
