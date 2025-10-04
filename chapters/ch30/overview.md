# Chapter 30: 분향단과 계수 - 시간·주기 데이터

## 개요 (Overview)
이번 챕터에서는 Pandas를 사용하여 시간과 주기를 가지는 데이터를 분석하고 모델링하는 다양한 기법을 배웁니다. `date_range()`를 활용한 시계열 인덱스 생성, `Period` 객체를 이용한 주기성 분석, 그리고 시계열 주기 변환과 같은 기술을 탐구합니다. 출애굽기 30장의 분향단과 계수, 그리고 요한복음 2장의 성전 정화 사건 말씀을 통해, 연속적인 흐름 속에서 중요한 패턴과 통찰을 발견하고 하나님의 때와 섭리를 데이터적으로 이해하고 묵상합니다.

This chapter introduces various techniques for analyzing and modeling time-series and periodic data using Pandas. We will explore creating time-series indices with `date_range()`, analyzing periodicity using `Period` objects, and time-series frequency conversion. Through the altar of incense and census in Exodus 30 and the temple cleansing event in John 2, we will discover important patterns and insights within continuous flows, and understand and meditate on God's timing and providence.

---

## 📜 성경 본문 깊이 묵상

### 출애굽기 30장: 분향단과 계수

하나님께서는 성막 안에 분향단을 만들도록 지시하셨습니다. 분향단에서는 매일 아침저녁으로 향을 피워 하나님께 드렸는데, 이는 끊이지 않는 기도와 예배를 상징합니다. 또한 이스라엘 백성의 계수(인구 조사)는 특정 시점의 백성 수를 파악하는 중요한 행위였습니다. 이 두 가지는 시간의 흐름과 특정 시점의 데이터를 다루는 데 영감을 줍니다.

- **분향단:** 끊이지 않는 향, 매일 아침저녁 (출 30:7-8)
- **계수:** 특정 시점의 인구 파악, 속전 (출 30:11-16)
- **시간의 흐름:** 연속적인 예배와 특정 시점의 기록

이 본문은 시간 기반 데이터 분석에 영감을 줍니다. 분향단의 향처럼 연속적으로 발생하는 사건들을 `date_range()`로 시계열 인덱스를 생성하여 기록할 수 있습니다. 계수처럼 특정 시점의 데이터를 파악하는 것은 `Period` 객체를 활용하여 주기성을 분석하는 데 유용합니다. 시계열 주기 변환은 끊이지 않는 기도와 예배의 흐름 속에서 중요한 패턴을 발견하는 데 도움을 줍니다.

### 요한복음 2:13-17: 성전 정화 사건

유월절이 가까워 예수님께서 예루살렘 성전에 올라가셨을 때, 성전 안에서 소와 양과 비둘기 파는 자들과 돈 바꾸는 자들이 있는 것을 보시고 그들을 내어쫓으셨습니다. 이는 성전이 기도하는 집이 아니라 강도의 소굴이 된 것을 책망하신 사건입니다. 이 사건은 특정 '때'에 발생한 중요한 변화를 보여줍니다.

- **유월절:** 특정 절기, 시간적 배경
- **성전 정화:** 특정 시점에 발생한 중요한 사건
- **하나님의 때:** 예수님께서 행동하신 적절한 시점

이 말씀은 시계열 데이터에서 특정 이벤트나 변화를 탐지하는 데 영감을 줍니다. `date_range()`는 사건 발생 시점을 정확히 기록하고, `Period` 객체는 유월절과 같은 특정 절기의 주기성을 분석하는 데 활용될 수 있습니다. 시계열 주기 변환은 성전 정화와 같은 중요한 사건이 발생하기 전후의 변화를 분석하여 하나님의 때와 섭리를 이해하는 데 도움을 줍니다.

---

## 🔍 숨겨진 질문 발견

**출애굽기에서 발견할 질문들:**

- 분향단에서 향을 피운 시간 데이터를 `date_range()`로 기록하고 `Period` 객체로 변환하면, 매일 아침저녁 예배의 주기성을 어떻게 분석할 수 있을까?
- 이스라엘 백성의 계수 데이터를 시계열로 만들고 `시계열 주기 변환`을 적용하면, 인구 변화의 패턴이나 특정 시점의 인구 동향을 어떻게 파악할 수 있을까?
- 분향단의 향과 계수 데이터를 통합하여 시간의 흐름에 따른 영적 상태 변화를 분석하면, 어떤 의미 있는 통찰을 얻을 수 있을까?

**요한복음에서 발견할 질문들:**

- 예수님의 성전 정화 사건 전후의 성전 활동 데이터를 `date_range()`로 기록하고 `Period` 객체로 변환하면, 성전의 타락과 정화의 주기성을 어떻게 분석할 수 있을까?
- 유월절과 같은 절기 데이터를 시계열로 만들고 `시계열 주기 변환`을 적용하면, 절기별 영적 분위기 변화의 패턴을 어떻게 파악할 수 있을까?
- 예수님의 공생애 기간 동안의 주요 사건들을 시간 기반 데이터로 만들고 분석하면, 예수님의 사역의 흐름과 하나님의 때를 어떻게 이해할 수 있을까?

이런 질문들은 데이터의 '시간·주기 데이터'라는 관점으로 성경 본문을 더 깊이 이해하는 데 도움을 줄 것이다.

---

## 📊 판다스로 성경 탐구하기

### 탐구 1: 분향단 데이터 시계열 인덱스 생성 (date_range, Period)

```python
import pandas as pd
import numpy as np
from chapters.ch30.incense_altar_data import IncenseAltarDataGenerator
from chapters.ch30.date_range_generator import DateRangeGenerator

# 분향단 데이터 생성
data_gen = IncenseAltarDataGenerator()
df_incense = data_gen.generate_incense_data(periods=30, freq='H') # 시간 단위 데이터

print("🕯️ 분향단 데이터 요약:\n", df_incense.head())

# `date_range`를 사용하여 일별 시계열 인덱스 생성
date_range_gen = DateRangeGenerator()
daily_dates = date_range_gen.generate_ranges()['daily']
print("\n--- 일별 date_range 생성 후 ---")
print(daily_dates)

# `Period` 객체로 변환하여 주기성 분석 준비
df_incense_period = df_incense.to_period(freq='D')
print("\n--- Period 객체로 변환 후 (일부) ---")
print(df_incense_period.head())
```

### 탐구 2: 성전 정화 데이터 시계열 주기 변환 및 분석 (resample, time-series frequency conversion)

```python
import pandas as pd
import numpy as np
from chapters.ch30.incense_altar_data import IncenseAltarDataGenerator # 동일 데이터 생성기 사용
from chapters.ch30.period_converter import PeriodConverter
from chapters.ch30.time_series_analyzer import TimeSeriesAnalyzer

# 성전 정화 데이터 생성 (가정)
data_gen = IncenseAltarDataGenerator()
df_temple = data_gen.generate_incense_data(periods=365, freq='D') # 1년치 일별 데이터

print("⚖️ 성전 정화 데이터 요약:\n", df_temple.head())

# 월별 평균으로 리샘플링
converter = PeriodConverter(df_temple)
monthly_avg_df = converter.convert_to_period(freq='M')
print("\n--- 월별 평균으로 리샘플링 후 (일부) ---")
print(monthly_avg_df.head())

# 시계열 분석 (예: 월별 평균 향 소비량의 이동 평균)
analyzer = TimeSeriesAnalyzer(monthly_avg_df.to_timestamp()) # PeriodIndex를 DatetimeIndex로 변환
analysis_results = analyzer.perform_analysis(column='incense_amount', window=3)
print("\n--- 월별 향 소비량 3개월 이동 평균 (일부) ---")
print(analysis_results['rolling_mean_head'])
```

---

## ⭐ 놀라운 발견들

### 발견 1: `date_range`와 `Period` 객체로 시간의 흐름 속 하나님의 섭리 기록

`date_range`를 사용하여 시계열 인덱스를 생성하고 `Period` 객체로 변환하는 것은 분향단의 향처럼 연속적으로 발생하는 사건들을 시간의 흐름 속에서 하나님의 섭리를 기록하는 것과 같습니다. 이는 데이터의 시간적 흐름을 명확히 하고, 특정 시점의 데이터를 효과적으로 관리하는 데 필수적입니다.

### 발견 2: 시계열 주기 변환으로 성전 정화와 같은 중요한 때 발견

`resample()`과 같은 시계열 주기 변환을 사용하여 데이터를 월별 또는 연별로 집계하는 것은 성전 정화 사건처럼 특정 '때'에 발생한 중요한 변화를 발견하는 것과 같습니다. 이는 데이터의 주기성을 분석하고, 시간의 흐름 속에서 하나님의 일하심의 패턴과 중요한 전환점을 파악하는 데 도움을 줍니다.

### 발견 3: 시간 기반 데이터 분석은 영적 분별력의 기초

시간 기반 데이터 분석은 단순히 데이터의 변화를 추적하는 것을 넘어, 영적 분별력의 기초가 됩니다. `date_range`, `Period`, 시계열 주기 변환과 같은 도구는 우리가 시간 속에서 하나님의 뜻과 섭리를 이해하고, 우리의 삶을 그분의 때에 맞춰 조정하는 데 도움을 줍니다. 분향단의 향처럼 끊이지 않는 기도와 예배의 흐름 속에서 하나님의 음성을 듣는 것과 같습니다.

---

## 🎨 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰

|출애굽기 진리|요한복음 진리|판다스 도구|영적 발견|
|---|---|---|---|
|분향단의 끊이지 않는 향 = 지속적인 예배|성전 정화 사건 = 하나님의 때와 공의|`date_range`|시간의 흐름 속 하나님의 신실한 임재|
|이스라엘 백성의 계수 = 특정 시점의 기록|유월절과 같은 절기 = 주기적인 영적 사건|`Period`|데이터의 주기성 분석과 영적 패턴 인식|
|시간의 흐름 속 하나님의 인도하심|예수님의 사역의 흐름과 하나님의 때|시계열 주기 변환|영적 분별력과 지혜로운 의사결정|
|데이터의 연속적인 흐름|영적 성장의 연속적인 과정|시계열 데이터 관리|영적 여정의 연속성과 목적성|
|중요한 패턴과 통찰 발견|하나님의 뜻과 섭리 발견|시계열 분석|모든 시간 속 하나님의 주권과 섭리|

> **💎 블렌딩 결과**: `date_range()`, `Period` 객체, 시계열 주기 변환과 같은 시간·주기 데이터 처리 기술은 성경 속 분향단과 계수, 그리고 성전 정화 사건의 본질을 데이터적으로 분석하는 강력한 도구입니다. 연속적인 흐름 속에서 중요한 패턴과 통찰을 발견하는 과정을 통해, 하나님의 때와 섭리를 이해하고 영적 분별력을 길러 지혜로운 의사결정을 내릴 수 있습니다.

---

## 🛠️ 광야 생존 프로젝트: 나의 영적 시간·주기 데이터 분석

**🎯 미션**: 내 삶의 영적 활동 데이터를 시간·주기 기반으로 분석하여 패턴 발견하기
**📊 사용 기술**: DataFrame 생성, `date_range`, `Period`, 시계열 주기 변환
**🕊️ 복음 포인트**: "예수께서 성전에 들어가사 성전 안에서 매매하는 자들을 내어쫓으시며" (요한복음 2:14)

### Step 1: 나의 영적 활동 데이터 기록 및 시계열 인덱스 생성

```python
import pandas as pd
import numpy as np

my_spiritual_log = pd.DataFrame({
    '날짜': pd.to_datetime(pd.date_range(start='2024-01-01', periods=30, freq='D')),
    '기도_시간_분': np.random.randint(0, 60, size=30),
    '말씀_묵상_시간_분': np.random.randint(0, 60, size=30),
    '감사_지수': np.random.randint(1, 10, size=30)
})

# '날짜' 컬럼을 인덱스로 설정
my_spiritual_log = my_spiritual_log.set_index('날짜')

print("🧬 나의 영적 활동 로그 (시계열 인덱스):\n", my_spiritual_log.head())

# `date_range`를 사용하여 특정 기간의 영적 활동 계획 생성
my_plan_dates = pd.date_range(start='2024-02-01', end='2024-02-29', freq='D')
print("\n--- 나의 영적 활동 계획 기간 (date_range) ---")
print(my_plan_dates)
```

### Step 2: 영적 활동 데이터 주기 변환 및 분석

```python
# 월별 평균 기도 시간으로 리샘플링
monthly_avg_prayer = my_spiritual_log['기도_시간_분'].resample('M').mean()
print("\n--- 월별 평균 기도 시간 ---")
print(monthly_avg_prayer)

# 주간 총 말씀 묵상 시간으로 리샘플링
weekly_sum_word = my_spiritual_log['말씀_묵상_시간_분'].resample('W').sum()
print("\n--- 주간 총 말씀 묵상 시간 ---")
print(weekly_sum_word)

# `Period` 객체로 변환하여 특정 월의 데이터 확인
my_spiritual_log_period = my_spiritual_log.to_period(freq='M')
jan_data = my_spiritual_log_period.loc['2024-01']
print("\n--- 2024년 1월 영적 활동 데이터 (Period) ---")
print(jan_data.head())
```

---

## 📱 3×10초 광야 루틴

### 🌅 아침 10초: 말씀 묵상

"예수께서 성전에 들어가사 성전 안에서 매매하는 자들을 내어쫓으시며." (요 2:14)
오늘도 나의 마음의 성전을 정화하며 하루를 시작합니다.

### ☀️ 점심 1분: 시간·주기 기도

- 나의 삶에서 `date_range`처럼 연속적으로 드려야 할 기도와 예배는 없는지 돌아봅니다.
- `Period`처럼 특정 주기에 따라 점검하고 정화해야 할 영역은 없는지 점검합니다.
- 주님, 모든 시간 속에서 주님의 뜻과 섭리를 발견하게 하소서.

### 🌙 저녁 2분: 데이터 기도일기

**오늘의 영적 데이터:**
- 오늘 `date_range`로 기록해 본 나의 영적 활동 시간은?
- `Period`로 분석해 본 나의 영적 상태의 주기성은?
- `시계열 주기 변환`으로 본 나의 영적 성장 패턴은?
- 주님, 분향단처럼 끊이지 않는 기도와 예배로 주님을 찬양하며, 주님의 때를 분별하게 하소서.

---

## ❓ FAQ & 체크리스트

### 깊이 있는 질문들

**Q1: `pd.date_range()`는 어떤 상황에서 유용하게 사용되나요?** A: `pd.date_range()`는 특정 시작일과 종료일 또는 기간(periods)을 지정하여 규칙적인 DatetimeIndex를 생성할 때 사용됩니다. 시계열 데이터 분석에서 날짜/시간 인덱스를 만들거나, 특정 기간 동안의 데이터를 생성할 때 매우 유용합니다. `freq` 파라미터를 통해 일별, 주별, 월별 등 다양한 빈도를 설정할 수 있습니다.

**Q2: `Period` 객체와 `PeriodIndex`는 무엇이며, `DatetimeIndex`와 어떻게 다른가요?** A: `DatetimeIndex`가 특정 시점(timestamp)을 나타내는 반면, `Period` 객체와 `PeriodIndex`는 특정 기간(period)을 나타냅니다. 예를 들어, `2023-01-01`은 `DatetimeIndex`의 한 점이지만, `2023-01` (월별 빈도)은 `Period` 객체로 1월 전체 기간을 의미합니다. `Period`는 주로 재무 데이터나 회계 연도와 같이 기간 기반의 분석에 유용합니다.

**Q3: 시계열 주기 변환(Time-series Frequency Conversion)은 왜 중요하며, 어떻게 수행하나요?** A: 시계열 주기 변환은 데이터의 시간 간격(빈도)을 변경하는 것으로, `resample()` 메서드를 통해 수행됩니다. 예를 들어, 일별 데이터를 주간 또는 월간 데이터로 집계(다운샘플링)하거나, 반대로 더 세분화된 데이터로 확장(업샘플링)할 수 있습니다. 이는 다양한 시간 스케일에서 데이터의 패턴을 분석하고, 서로 다른 빈도의 데이터를 통합하는 데 필수적입니다.

**Q4: 분향단과 계수가 시간·주기 데이터와 어떤 영적 의미로 연결될 수 있을까요?** A: 분향단에서 끊이지 않는 향은 연속적인 시간의 흐름 속에서 드려지는 기도와 예배를 상징합니다. 계수는 특정 시점의 데이터를 기록하는 것과 같습니다. 이는 시간 기반 데이터가 연속적인 흐름 속에서 중요한 패턴과 통찰을 제공하며, 특정 시점의 기록이 전체 흐름을 이해하는 데 중요함을 보여줍니다.

**Q5: 성전 정화 사건이 시계열 주기 변환과 어떤 영적 의미로 연결될 수 있을까요?** A: 성전 정화 사건은 유월절이라는 특정 절기(주기)에 발생한 중요한 변화입니다. 시계열 주기 변환은 데이터의 주기성을 분석하고, 특정 시점에 발생한 중요한 사건이 전후 데이터에 미치는 영향을 파악하는 데 도움을 줍니다. 이는 영적으로 하나님의 때와 섭리를 이해하고, 우리의 삶에서 중요한 전환점을 분별하는 것과 같습니다.

### ✅ 체크리스트

**성경 이해 체크:**

- [ ] 출애굽기 30장의 분향단과 계수의 의미 이해
- [ ] 요한복음 2장의 성전 정화 사건과 하나님의 때 이해
- [ ] 시간과 주기를 가지는 데이터 분석을 통해 하나님의 때와 섭리를 이해

**DataFrame 기초 체크:**

- [ ] `pd.date_range()` 함수를 사용하여 시계열 인덱스 생성 성공
- [ ] `df.to_period()` 메서드를 사용하여 `Period` 객체로 변환 성공
- [ ] `df.resample()` 함수를 사용하여 시계열 주기 변환 성공
- [ ] `freq` 파라미터의 다양한 옵션 이해 (예: 'D', 'W', 'M', 'H')

**영적 적용 체크:**

- [ ] 내 삶의 영적 활동 데이터를 시간·주기 기반으로 기록 및 분석 시도 완료
- [ ] 나의 영적 상태의 주기성을 `Period` 객체와 `resample()` 원리로 점검 시도 완료
- [ ] 시간·주기 데이터 분석 원리를 통해 영적 분별력과 지혜로운 의사결정 노력

**발견 기록 체크:**

- [ ] `date_range`와 `Period` 객체로 시간의 흐름 속 하나님의 섭리 기록 확인
- [ ] 시계열 주기 변환으로 성전 정화와 같은 중요한 때 발견 통찰
- [ ] 시간 기반 데이터 분석이 영적 분별력의 기초임을 확인

---

## 🧠 미니 퀴즈

**1. 특정 시작일과 종료일 또는 기간을 지정하여 규칙적인 DatetimeIndex를 생성하는 Pandas 함수는?**
a) `pd.to_datetime()`
b) `pd.date_range()`
c) `pd.Timestamp()`

**2. 특정 시점(timestamp)을 나타내는 `DatetimeIndex`와 달리, 특정 기간(period)을 나타내는 Pandas 객체는?**
a) `Timedelta`
b) `Period`
c) `Interval`

**3. 시계열 데이터의 시간 간격(빈도)을 변경하는 데 사용되는 메서드는?**
a) `df.groupby()`
b) `df.pivot_table()`
c) `df.resample()`

**4. 일별 데이터를 주간 총합으로 집계하기 위한 `resample()` 사용법으로 올바른 것은?**
a) `df.resample('W').mean()`
b) `df.resample('W').sum()`
c) `df.groupby('W').sum()`

**5. 분향단과 계수가 시간·주기 데이터와 연결되는 영적 의미로 가장 적절하지 않은 것은?**
a) 연속적인 흐름 속에서 중요한 패턴과 통찰을 제공
b) 특정 시점의 기록이 전체 흐름을 이해하는 데 중요함
c) 데이터의 시간적 순서를 무시하고 무작위로 분석함

_(정답: 1-b, 2-b, 3-c, 4-b, 5-c)_

---

## 🎯 깊이 탐구 과제 (선택)

### 초급 과제

1.  **성경 인물 생애 주기 분석**: 성경 인물(예: 요셉)의 주요 생애 사건(출생, 노예, 총리, 죽음)을 날짜와 함께 기록한 DataFrame을 만들고, `pd.date_range()`로 기간을 생성한 후 `Period` 객체로 변환하여 각 생애 주기의 특징을 분석해보기
2.  **개인 기도 시간 주기성 분석**: 매일 기도 시간을 기록한 데이터를 만들고, `resample('W').mean()`을 사용하여 주간 평균 기도 시간의 주기성을 분석해보기

### 중급 과제

1.  **교회 행사 주기성 분석**: 가상의 교회 행사 데이터(날짜, 행사 유형, 참여 인원)를 만들고, `pd.date_range()`로 시계열 인덱스를 생성한 후, `resample('M').sum()`을 사용하여 월별 행사 참여 인원의 주기성을 분석해보기
2.  **영적 성장 지표 시계열 예측**: 개인의 영적 성장 지표(예: 말씀 묵상 시간, 감사 지수)를 시계열 데이터로 만들고, `resample()`로 월별 평균을 계산한 후, 간단한 시계열 예측 모델(예: 이동 평균)을 적용하여 미래 영적 성장 추이를 예측해보기

### 고급 과제

1.  **성경 절기 데이터 분석 시스템**: 성경의 주요 절기(유월절, 오순절, 초막절 등) 데이터를 `date_range`와 `Period` 객체를 활용하여 시계열로 구축하고, `resample()`을 통해 절기별 영적 의미와 패턴을 분석하는 시스템(개념) 설계해보기
2.  **개인 영적 성장 대시보드 (시계열 포함)**: 개인의 영적 활동(기도, 말씀, 봉사) 데이터를 시계열로 기록하고, `date_range`, `Period`, `resample` 등을 활용하여 영적 성장 추세와 주기성을 보여주는 대시보드를 만들고 시각화(matplotlib/seaborn)해보기

---

## 🌟 다음 여정 예고

**Chapter 31: "브살렐과 오홀리압 - 성능 최적화 (Bezalel and Oholiab - Performance Optimization)"**

브살렐과 오홀리압이 성막 건축에 필요한 모든 기술과 지혜를 부여받아 최고의 작품을 만들었듯이, 데이터 분석에서도 성능 최적화는 대규모 데이터를 효율적으로 처리하고 분석 결과를 빠르게 얻는 데 필수적입니다.

Just as Bezalel and Oholiab were endowed with all the skills and wisdom needed to build the tabernacle, creating the finest work, in data analysis, performance optimization is essential for efficiently processing large datasets and obtaining analysis results.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 벡터화 연산을 통한 성능 향상
🔍 `eval()` 및 `query()`를 이용한 빠른 데이터 처리
🎯 데이터 타입 최적화를 통한 메모리 및 속도 개선
📊 브살렐과 오홀리압처럼 효율적이고 최적화된 데이터 분석 환경 구축

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 31:1-11)
"내 아버지께서 이제까지 일하시니 나도 일한다" (요한복음 5:17)

---

## 🙏 한 줄 기도

_"주님, 분향단처럼 끊이지 않는 기도와 예배로 주님을 찬양하며, 시간과 주기를 가지는 데이터 속에서 주님의 때와 섭리를 분별하게 하소서.
시계열 데이터 분석을 통해 연속적인 흐름 속에서 중요한 패턴과 통찰을 발견하고,
영적 분별력을 길러 지혜로운 의사결정을 내리게 하소서. 예수님의 이름으로 기도합니다. 아멘."_

---

**🎊 서른 번째 광야 여정을 완주하신 것을 축하합니다!**

"예수께서 성전에 들어가사 성전 안에서 매매하는 자들을 내어쫓으시며 돈 바꾸는 자들의 상과 비둘기 파는 자들의 의자를 둘러 엎으시고" (요한복음 2:15)

여러분은 이제 데이터 속에서 `date_range()`, `Period` 객체, 시계열 주기 변환을 통해 시간과 주기를 가지는 데이터를 분석하는 방법을 알게 되었습니다. 주님께서 주신 지혜로 모든 데이터 속에서 하나님의 때와 섭리를 발견하시길 기도합니다.

**다음 여정에서 만나요! 🌈**
