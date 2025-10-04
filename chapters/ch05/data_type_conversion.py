import pandas as pd
import numpy as np

def demo_dtype_inspection():
    """데이터 타입 점검 데모: 성경 인물 속성 데이터"""
    print("\n🔎 데이터 타입 점검: 성경 인물 속성")
    print("=" * 50)

    character_attributes = pd.DataFrame({
        '이름': ['모세', '아론', '파라오', '안드레', '나다나엘'],
        '나이': [80, 83, 60, 30, 35], # integer
        '믿음_수준': [9.5, 7.0, 1.0, 8.0, 8.5], # float
        '직분': ['선지자', '대변자', '왕', '제자', '제자'], # object (string)
        '활동_여부': [True, True, True, True, True] # boolean
    })
    print(character_attributes)
    print("\n📊 DataFrame의 데이터 타입 (dtypes):\n", character_attributes.dtypes)

    # 특정 열의 데이터 타입 확인
    print("\n✅ '나이' 열의 데이터 타입:\n", character_attributes['나이'].dtype)
    print("\n✅ '직분' 열의 데이터 타입:\n", character_attributes['직분'].dtype)

    return character_attributes

def demo_astype_conversion():
    """astype() 변환 데모: 광야 여정 통계"""
    print("\n🔄 astype() 변환 데모: 광야 여정 통계")
    print("=" * 50)

    journey_stats = pd.DataFrame({
        '여정_단계': ['애굽 탈출', '시내산 도착', '가나안 입성'],
        '기간_일': [430, '약 60', '약 14600'], # 40년 * 365 = 14600
        '기적_횟수': [10, 5, 3],
        '주요_사건': ['유월절', '십계명', '여리고']
    })
    print(journey_stats)
    print("\n📊 초기 DataFrame의 데이터 타입:\n", journey_stats.dtypes)

    # '기간_일'을 숫자형으로 변환 시도 (오류 발생 예정: '약 60'이 문자열)
    # 먼저 문자열에서 숫자 부분만 추출
    journey_stats['기간_일_숫자'] = journey_stats['기간_일'].astype(str).str.extract(r'(\d+)', expand=False)
    journey_stats['기간_일_int'] = pd.to_numeric(journey_stats['기간_일_숫자'], errors='coerce').astype(pd.Int64Dtype()) # Nullable Integer

    print("\n🔄 '기간_일'을 숫자형(Int64)으로 변환 후:\n", journey_stats[['기간_일', '기간_일_int']].dtypes)
    print(journey_stats[['여정_단계', '기간_일', '기간_일_int']])
    print("   -> 문자열에서 숫자만 추출 후 Int64로 변환, 결측치는 <NA>로 표시")

    # '기적_횟수'를 float으로 변환
    journey_stats['기적_횟수_float'] = journey_stats['기적_횟수'].astype(float)
    print("\n🔄 '기적_횟수'를 float으로 변환 후:\n", journey_stats[['기적_횟수', '기적_횟수_float']].dtypes)

    return journey_stats

def demo_to_numeric_conversion():
    """pd.to_numeric() 데모: 믿음 고백 강도 분석"""
    print("\n🔢 pd.to_numeric() 데모: 믿음 고백 강도")
    print("=" * 50)

    faith_confession = pd.DataFrame({
        '인물': ['베드로', '도마', '백부장', '사울'],
        '고백_강도_점수': ['8', '의심 후 9', '7.5', '초기0 후10'], # Mixed types
        '고백_내용': ['주는 그리스도시요', '나의 주 나의 하나님', '참으로 하나님의 아들이었도다', '누구시니이까']
    })
    print(faith_confession)
    print("\n📊 초기 DataFrame의 데이터 타입:\n", faith_confession.dtypes)

    # '고백_강도_점수'를 숫자형으로 변환 (errors='coerce' 적용)
    faith_confession['고백_강도_numeric'] = pd.to_numeric(faith_confession['고백_강도_점수'], errors='coerce')
    print("\n🔄 '고백_강도_점수'를 numeric으로 변환 후 (오류 처리):\n", faith_confession['고백_강도_numeric'].dtypes)
    print(faith_confession[['인물', '고백_강도_점수', '고백_강도_numeric']])
    print("   -> 숫자가 아닌 값은 NaN으로 변환되어 float 타입이 됨. 결측치 발생!")

    # 숫자형으로 잘 변환된 데이터만 필터링하여 평균 강도 계산
    valid_scores = faith_confession[faith_confession['고백_강도_numeric'].notna()]
    if not valid_scores.empty:
        print(f"\n⭐ 유효한 고백 강도 평균: {valid_scores['고백_강도_numeric'].mean():.2f}")

    return faith_confession

def main():
    demo_dtype_inspection()
    demo_astype_conversion()
    demo_to_numeric_conversion()

if __name__ == "__main__":
    main()
