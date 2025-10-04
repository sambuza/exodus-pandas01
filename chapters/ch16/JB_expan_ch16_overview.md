# Chapter 16: 만나의 규례 — 윈도우와 롤링

## 개요 (Overview)
이번 챕터에서는 Pandas의 `rolling()`과 `expanding()` 함수를 사용하여 시계열 데이터에서 일정 기간 동안의 이동 평균, 이동 합계 등 윈도우(Window) 연산을 수행하는 방법을 배웁니다. 출애굽기 16장의 만나의 규례와 요한복음 6장의 생명의 떡 말씀을 통해, 시간의 흐름에 따른 하나님의 신실한 공급과 영원한 채움의 패턴을 탐구합니다.

This chapter introduces how to perform window operations like rolling mean and sum on time-series data over a specified period using Pandas' `rolling()` and `expanding()` functions. Through the manna ordinance in Exodus 16 and the Bread of Life discourse in John 6, we will explore patterns of God's faithful provision and eternal sustenance over time.

---

## 📜 성경 본문 깊이 묵상

### 출애굽기 16장: 만나와 메추라기

이스라엘 백성이 광야에서 배고픔을 호소하자, 하나님께서는 하늘에서 만나를 내려주시고 메추라기를 보내어 먹이셨습니다. 만나는 매일 아침 거두어야 했고, 안식일 전날에는 이틀 치를 거두게 하셨으며, 다음 날까지 남겨두면 벌레가 생기고 냄새가 났습니다. 이는 하나님의 매일의 공급과 순종의 규례를 보여줍니다.

- **매일의 공급:** 매일 아침 만나를 거둠 (출 16:4)
- **안식일 규례:** 안식일 전날에는 이틀 치를 거둠 (출 16:22-26)
- **순종의 시험:** 다음 날까지 남겨두지 말라는 명령 (출 16:19-20)

이 사건은 시간의 흐름에 따른 데이터의 변화를 분석하는 데 영감을 줍니다. `rolling()` 함수는 매일의 만나 수확량이나 이스라엘의 순종/불평 지수를 일정 기간(예: 7일) 동안의 이동 평균으로 분석하여 추세를 파악하는 데 사용될 수 있습니다. `expanding()`은 광야 여정 전체에 걸친 누적된 공급량이나 불평의 총합을 계산하는 데 유용합니다.

### 요한복음 6:31-35: 생명의 떡

예수님께서는 오병이어 기적 후 자신을 하늘에서 내려온 참된 떡, 곧 생명의 떡이라고 말씀하셨습니다. 이스라엘 백성이 광야에서 만나를 먹었으나 죽었지만, 예수님을 믿는 자는 영원히 주리지 않고 영생을 얻을 것이라고 선포하셨습니다. 이는 일시적인 육신의 양식과 영원한 생명의 양식을 대조합니다.

- **만나의 한계:** 만나를 먹었으나 죽었음 (요 6:49)
- **생명의 떡:** 예수님을 믿는 자는 영원히 주리지 않음 (요 6:35)
- **영원한 공급:** 예수님은 영원한 생명을 주시는 분 (요 6:40)

이 말씀은 영적 갈증과 채움의 지속적인 패턴을 분석하는 데 영감을 줍니다. `rolling()` 함수는 영적 갈증이나 채움의 지수를 일정 기간 동안의 이동 평균으로 분석하여 영적 상태의 단기적인 변화를 파적하는 데 사용될 수 있습니다. `expanding()`은 예수님을 믿은 후 누적되는 영적 만족도나 성장의 총합을 계산하는 데 유용합니다.

---

## 🔍 숨겨진 질문 발견

**출애굽기에서 발견할 질문들:**

- 이스라엘 백성의 만나 수확량이나 불평 지수를 7일 `rolling mean`으로 분석하면, 주간 단위의 순종/불순종 패턴을 발견할 수 있을까?
- 광야 여정 전체에 걸쳐 이스라엘 백성의 누적된 불평(`expanding sum`)은 어떻게 변화했을까?
- 만나의 공급량과 이스라엘 백성의 순종 수준 사이에 `rolling correlation`을 계산하면, 어떤 관계를 발견할 수 있을까?

**요한복음에서 발견할 질문들:**

- 예수님을 믿은 후 영적 갈증이나 채움의 지수를 30일 `rolling mean`으로 분석하면, 월별 영적 상태의 추세를 파악할 수 있을까?
- 예수님을 믿은 후 누적되는 영적 만족도(`expanding sum`)는 어떻게 변화했을까?
- 말씀 섭취량과 영적 성장 지수 사이에 `rolling correlation`을 계산하면, 어떤 관계를 발견할 수 있을까?

이런 질문들은 데이터의 '윈도우와 롤링'이라는 관점으로 성경 본문을 더 깊이 이해하는 데 도움을 줄 것이다.

---

## 📊 판다스로 성경 탐구하기

### 탐구 1: 만나의 규례 롤링/익스팬딩 분석 (rolling, expanding)

```python
import pandas as pd
from .manna_ordinance_data import MannaOrdinanceDataGenerator

# 만나 데이터 생성
data_gen = MannaOrdinanceDataGenerator()
df_manna = data_gen.generate_manna_data()

print("🍞 만나 데이터 요약:\n", df_manna)

# 7일 이동 평균 (rolling mean) 계산
print("\n--- 7일 이동 평균 만나 수확량 (7-Day Rolling Mean Manna Gathered) ---")
df_manna['rolling_mean_manna'] = df_manna['manna_gathered_kg'].rolling(window=7).mean()
print(df_manna[['day', 'manna_gathered_kg', 'rolling_mean_manna']].to_string(index=False))

# 누적 합계 (expanding sum) 계산
print("\n--- 누적 불평 지수 (Expanding Sum of Complaint Index) ---")
df_manna['expanding_sum_complaint'] = df_manna['israel_complaint'].expanding().sum()
print(df_manna[['day', 'israel_complaint', 'expanding_sum_complaint']].to_string(index=False))
```

### 탐구 2: 생명의 떡 윈도우 함수 분석 (rolling, window functions)

```python
import pandas as pd
from .bread_of_life_data import BreadOfLifeDataGenerator

# 생명의 떡 데이터 생성
data_gen = BreadOfLifeDataGenerator()
df_bread_of_life = data_gen.generate_bread_of_life_data()

print("🙏 생명의 떡 데이터 요약:\n", df_bread_of_life)

# 3일 이동 평균 영적 채움 (rolling mean) 계산
print("\n--- 3일 이동 평균 영적 채움 (3-Day Rolling Mean Spiritual Fulfillment) ---")
df_bread_of_life['rolling_mean_fulfillment'] = df_bread_of_life['spiritual_fulfillment'].rolling(window=3).mean()
print(df_bread_of_life[['date', 'spiritual_fulfillment', 'rolling_mean_fulfillment']].to_string(index=False))

# 5일 이동 표준편차 영적 갈증 (rolling std) 계산
print("\n--- 5일 이동 표준편차 영적 갈증 (5-Day Rolling Std Spiritual Hunger) ---")
df_bread_of_life['rolling_std_hunger'] = df_bread_of_life['spiritual_hunger'].rolling(window=5).std()
print(df_bread_of_life[['date', 'spiritual_hunger', 'rolling_std_hunger']].to_string(index=False))
```

---

## ⭐ 놀라운 발견들

### 발견 1: `rolling()`을 통한 만나 공급의 주기적 패턴

만나 수확량 데이터를 7일 `rolling mean`으로 분석하면, 안식일 전날 이틀 치를 거두게 하신 하나님의 규례로 인해 주간 단위의 패턴이 나타남을 확인할 수 있습니다. 이는 하나님의 공급이 일관되면서도 특정 주기를 가지고 있음을 데이터적으로 보여주며, `rolling()`이 시계열 데이터의 단기적인 추세나 패턴을 파악하는 데 유용함을 증명합니다.

### 발견 2: `expanding()`을 통한 광야 여정의 누적된 불평

이스라엘 백성의 불평 지수를 `expanding sum`으로 계산하면, 광야 여정이 길어질수록 불평이 누적되어 가는 경향을 볼 수 있습니다. 이는 인간의 연약함과 불순종이 시간이 지남에 따라 어떻게 쌓여가는지 데이터적으로 보여주며, `expanding()`이 전체 기간에 걸친 누적된 변화를 파악하는 데 필수적인 도구임을 증명합니다.

### 발견 3: 윈도우 함수를 통한 생명의 떡의 지속적인 채움

생명의 떡 데이터를 `rolling mean`이나 `rolling std`로 분석하면, 예수님을 믿는 자가 영원히 주리지 않고 영적 갈증이 해소되며 평안이 지속되는 패턴을 볼 수 있습니다. 이는 예수님께서 주시는 영원한 생명의 떡이 일시적인 만나와 달리 지속적이고 변함없는 채움을 제공함을 데이터적으로 묵상하게 합니다.

---

## 🎨 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰

|출애굽기 진리|요한복음 진리|판다스 도구|영적 발견|
|---|---|---|---|
|만나의 매일 공급과 주간 패턴|생명의 떡이신 예수님의 영원한 공급|`rolling()`|하나님의 신실한 공급과 지속적인 은혜|
|광야 여정의 누적된 불평|예수님을 믿지 않는 자의 누적된 갈증|`expanding()`|인간의 연약함과 하나님의 변함없는 사랑|
|만나 규례를 통한 순종의 시험|생명의 떡을 통한 믿음의 시험|윈도우 함수|하나님의 말씀에 대한 반응과 그 결과|
|일시적인 육신의 양식|영원한 생명의 양식|시계열 분석|세상적인 것과 영원한 것의 대조|
|하나님의 세밀한 인도하심|예수님의 지속적인 채움|데이터 추세 분석|시간의 흐름 속 하나님의 일하심의 패턴|

> **💎 블렌딩 결과**: `rolling()`과 `expanding()` 같은 윈도우 함수는 성경 속 시간의 흐름에 따른 하나님의 신실한 공급과 인간의 반응을 데이터적으로 분석하는 강력한 도구입니다. 만나의 규례와 생명의 떡 말씀을 통해, 하나님의 변함없는 사랑과 영원한 채움의 패턴을 시계열적으로 이해할 수 있습니다.

---

## 🛠️ 광야 생존 프로젝트: 나의 영적 상태 롤링 분석

**🎯 미션**: 내 삶의 영적 상태 데이터를 윈도우 함수로 분석하여 추세와 변화 파악하기
**📊 사용 기술**: DataFrame 생성, `rolling()`, `expanding()`, 윈도우 함수
**🕊️ 복음 포인트**: "내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라" (요한복음 6:35)

### Step 1: 나의 영적 활동 데이터 롤링 분석

```python
import pandas as pd

# 나의 영적 활동 데이터
df_my_spiritual_activity = pd.DataFrame({
    '날짜': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07']),
    '기도_시간_분': [30, 40, 20, 35, 50, 25, 45],
    '말씀_읽은_장수': [3, 4, 2, 3, 5, 2, 4],
    '감사_지수': [7, 8, 6, 7, 9, 6, 8] # 1-10 스케일
}).set_index('날짜')

print("🧬 나의 영적 활동 데이터:\n", df_my_spiritual_activity)

# 3일 이동 평균 기도 시간 계산
print("\n--- 3일 이동 평균 기도 시간 (3-Day Rolling Mean Prayer Time) ---")
df_my_spiritual_activity['rolling_mean_prayer'] = df_my_spiritual_activity['기도_시간_분'].rolling(window=3).mean()
print(df_my_spiritual_activity[['기도_시간_분', 'rolling_mean_prayer']].to_string())

# 누적 말씀 읽은 장수 계산
print("\n--- 누적 말씀 읽은 장수 (Expanding Sum of Chapters Read) ---")
df_my_spiritual_activity['expanding_sum_word'] = df_my_spiritual_activity['말씀_읽은_장수'].expanding().sum()
print(df_my_spiritual_activity[['말씀_읽은_장수', 'expanding_sum_word']].to_string())
```

### Step 2: 나의 영적 갈증/채움 롤링 분석

```python
my_spiritual_state = pd.DataFrame({
    '날짜': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']),
    '갈증_수준': [8, 7, 6, 4, 2],
    '채움_수준': [2, 3, 5, 7, 9]
}).set_index('날짜')

print("💡 나의 영적 갈증/채움 데이터:\n", my_spiritual_state)

# 2일 이동 평균 갈증 수준 계산
print("\n--- 2일 이동 평균 갈증 수준 (2-Day Rolling Mean Thirst Level) ---")
df_my_spiritual_state['rolling_mean_thirst'] = df_my_spiritual_state['갈증_수준'].rolling(window=2).mean()
print(df_my_spiritual_state[['갈증_수준', 'rolling_mean_thirst']].to_string())

# 3일 이동 표준편차 채움 수준 계산
print("\n--- 3일 이동 표준편차 채움 수준 (3-Day Rolling Std Fulfillment Level) ---")
df_my_spiritual_state['rolling_std_fulfillment'] = df_my_spiritual_state['채움_수준'].rolling(window=3).std()
print(df_my_spiritual_state[['채움_수준', 'rolling_std_fulfillment']].to_string())
```

---

## 📱 3×10초 광야 루틴

### 🌅 아침 10초: 말씀 묵상

"내가 곧 생명의 떡이니 내게 오는 자는 결코 주리지 아니할 터이요 나를 믿는 자는 영원히 목마르지 아니하리라." (요 6:35)
오늘도 생명의 떡이신 예수님으로 영적 갈증을 채웁니다.

### ☀️ 점심 1분: 롤링 기도

- 지난 며칠간(윈도우) 나의 영적 상태(기도, 말씀, 감사)의 평균은 어떠했는지 돌아봅니다.
- 나의 삶에서 누적되어(익스팬딩) 온 하나님의 은혜와 공급을 기억하며 감사드립니다.
- 주님, 매일매일의 삶 속에서 주님의 신실한 공급을 경험하게 하소서.

### 🌙 저녁 2분: 데이터 기도일기

**오늘의 영적 데이터:**
- 지난 7일간 나의 기도 시간 `rolling mean`은?
- 나의 영적 갈증 수준의 `rolling std`는 어떻게 변화했나?
- 주님, 시간의 흐름 속에서 변함없이 저를 먹이시고 입히시는 주님을 찬양합니다.

---

## ❓ FAQ & 체크리스트

### 깊이 있는 질문들

**Q1: `rolling()` 함수는 어떤 상황에서 유용하게 사용되나요?** A: `rolling()` 함수는 시계열 데이터에서 일정 크기의 윈도우(기간)를 이동시키면서 해당 윈도우 내의 데이터에 대해 통계량(평균, 합계, 표준편차 등)을 계산할 때 사용됩니다. 주식 가격의 이동 평균, 일별 판매량의 주간 추세 분석 등 단기적인 추세나 패턴을 파악하는 데 매우 유용합니다.

**Q2: `expanding()` 함수는 `rolling()`과 어떻게 다른가요?** A: `rolling()`이 고정된 크기의 윈도우를 이동시키는 반면, `expanding()`은 윈도우의 크기가 데이터의 시작점부터 현재 시점까지 점차 확장됩니다. 즉, `expanding()`은 누적 합계, 누적 평균 등 전체 기간에 걸친 누적된 통계량을 계산할 때 사용됩니다. 광야 여정 전체에 걸친 누적된 불평 등을 분석할 때 유용합니다.

**Q3: 만나의 규례에서 `rolling mean`을 사용하면 어떤 통찰을 얻을 수 있을까요?** A: 만나 수확량 데이터를 7일 `rolling mean`으로 분석하면, 안식일 전날 이틀 치를 거두게 하신 하나님의 규례로 인해 주간 단위의 패턴이 나타남을 확인할 수 있습니다. 이는 하나님의 공급이 일관되면서도 특정 주기를 가지고 있음을 데이터적으로 보여줍니다.

**Q4: 생명의 떡 데이터를 `rolling std`로 분석하는 것이 영적으로 어떤 의미가 있을까요?** A: 영적 갈증이나 채움 수준의 `rolling std`를 계산하면, 영적 상태의 변동성(불안정성)을 파악할 수 있습니다. 표준편차가 높다면 영적 상태의 기복이 심하다는 의미이고, 낮다면 안정적이라는 의미입니다. 이는 예수님께서 주시는 생명의 떡이 영적 상태를 안정적으로 유지하게 하는 힘이 있음을 데이터적으로 묵상하게 합니다.

**Q5: 윈도우 함수를 사용할 때 `min_periods` 파라미터는 어떤 역할을 하나요?** A: `min_periods`는 윈도우 내에 최소한 몇 개의 유효한 데이터가 있어야 연산을 수행할지 지정하는 파라미터입니다. 예를 들어, `window=7`이고 `min_periods=1`이면, 7일 윈도우 내에 데이터가 1개만 있어도 연산을 수행합니다. 초기 데이터가 부족한 시점에 유용하게 사용될 수 있습니다.

### ✅ 체크리스트

**성경 이해 체크:**

- [ ] 출애굽기 16장의 만나의 규례와 하나님의 매일의 공급 이해
- [ ] 요한복음 6장의 생명의 떡이신 예수님의 영원한 채움 이해
- [ ] 만나와 생명의 떡 말씀 속에서 하나님의 신실한 공급과 영원한 생명을 이해

**DataFrame 기초 체크:**

- [ ] `df.rolling()` 함수를 사용하여 이동 평균, 이동 합계 등 계산 성공
- [ ] `df.expanding()` 함수를 사용하여 누적 합계, 누적 평균 등 계산 성공
- [ ] `window` 파라미터의 역할 이해
- [ ] `min_periods` 파라미터의 역할 이해

**영적 적용 체크:**

- [ ] 내 삶의 영적 상태 데이터를 윈도우 함수로 분석하여 추세와 변화 파악 시도 완료
- [ ] 나의 영적 활동과 갈증/채움 수준을 `rolling()`과 `expanding()`으로 분석 시도 완료
- [ ] 윈도우 함수 원리를 통해 시간의 흐름 속에서 하나님의 신실한 공급과 나의 영적 성장을 묵상

**발견 기록 체크:**

- [ ] `rolling()`을 통한 만나 공급의 주기적 패턴 확인
- [ ] `expanding()`을 통한 광야 여정의 누적된 불평 확인
- [ ] 윈도우 함수를 통한 생명의 떡의 지속적인 채움 확인

---

## 🧠 미니 퀴즈

**1. 시계열 데이터에서 일정 크기의 윈도우를 이동시키면서 통계량을 계산하는 함수는?**
a) `df.expanding()`
b) `df.rolling()`
c) `df.groupby()`

**2. 시계열 데이터에서 윈도우의 크기가 데이터의 시작점부터 현재 시점까지 점차 확장되면서 통계량을 계산하는 함수는?**
a) `df.rolling()`
b) `df.expanding()`
c) `df.pivot_table()`

**3. 만나 수확량 데이터를 7일 이동 평균으로 분석하여 주간 패턴을 파악하는 데 가장 적합한 함수는?**
a) `df.expanding(window=7).mean()`
b) `df.rolling(window=7).mean()`
c) `df.groupby(freq='W').mean()`

**4. 광야 여정 전체에 걸쳐 이스라엘 백성의 누적된 불평을 계산하는 데 가장 적합한 함수는?**
a) `df.rolling().sum()`
b) `df.expanding().sum()`
c) `df.cumsum()`

**5. 윈도우 함수를 통한 영적 의미로 가장 적절하지 않은 것은?**
a) 하나님의 매일의 신실한 공급 패턴 발견
b) 영적 상태의 단기적 추세와 장기적 누적 변화 파악
c) 모든 데이터를 개별적으로 분석하여 전체적인 흐름 무시

_(정답: 1-b, 2-b, 3-b, 4-b, 5-c)_

---

## 🎯 깊이 탐구 과제 (선택)

### 초급 과제

1.  **성경 인물 감정 변화 롤링 분석**: 성경 인물(예: 다윗)의 감정 변화(기쁨, 슬픔, 분노) 데이터를 시계열로 만들고, 3일 `rolling mean`으로 감정의 단기적 추세를 분석해보기
2.  **성경 구절 읽기 누적 분석**: 매일 읽은 성경 구절 수를 기록한 데이터를 만들고, `expanding sum`으로 누적 읽은 구절 수를 계산하여 영적 성장의 누적량을 파악해보기

### 중급 과제

1.  **만나 공급과 순종 지수 롤링 상관관계**: 만나 수확량과 이스라엘 백성의 순종 지수 데이터를 만들고, 7일 `rolling correlation`을 계산하여 두 지표 간의 관계 변화를 분석해보기
2.  **영적 갈증/채움 롤링 표준편차**: 개인의 영적 갈증과 채움 수준 데이터를 만들고, 5일 `rolling std`를 계산하여 영적 상태의 변동성(기복)을 분석해보기

### 고급 과제

1.  **영적 성장 대시보드 (롤링/익스팬딩 포함)**: 개인의 영적 활동(기도, 말씀, 봉사) 데이터를 시계열로 기록하고, `rolling mean`, `expanding sum` 등을 활용하여 영적 성장 추세와 누적량을 보여주는 대시보드를 만들고 시각화해보기
2.  **교회 출석률/헌금 추세 분석**: 가상의 교회 출석률 및 헌금 데이터를 시계열로 만들고, 월별 `rolling mean`과 연간 `expanding sum`을 계산하여 교회의 성장 추세와 재정 상태를 분석하는 보고서 작성해보기

---

## 🙏 한 줄 기도

_"주님, 광야에서 만나를 주시고 생명의 떡이신 예수님으로 저희를 먹이시니 감사합니다.
시간의 흐름 속에서 `rolling()`과 `expanding()`처럼 주님의 신실한 공급과 영원한 채움을 발견하게 하시고,
매일매일 주님 안에서 영적으로 성장하게 하소서. 예수님의 이름으로 기도합니다. 아멘."_

---

**🎊 열여섯 번째 광야 여정을 완주하신 것을 축하합니다!**

_"여호와께서 모세에게 이르시되 하늘에서 너희를 위하여 양식을 비같이 내리리니 백성이 나가서 일용할 것을 날마다 거둘 것이라" (출애굽기 16:4)_

여러분은 이제 데이터 속에서 `rolling()`과 `expanding()` 같은 윈도우 함수를 통해 시간의 흐름에 따른 추세와 변화를 파악하는 방법을 알게 되었습니다. 주님께서 주신 지혜로 모든 시간 속에서 하나님의 신실한 공급을 발견하시길 기도합니다.

**다음 여정에서 만나요! 🌈**
