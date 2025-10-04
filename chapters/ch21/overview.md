# Chapter 21: 공의의 법도 - 분류와 범주형

## 개요 (Overview)
이번 챕터에서는 Pandas를 사용하여 데이터를 특정 기준에 따라 분류하고 범주형 데이터로 다루는 방법을 배웁니다. `pd.cut()`과 `pd.qcut()`을 활용하여 데이터를 구간으로 나누고, `category dtype`을 통해 범주형 데이터를 효율적으로 관리하는 기술을 탐구합니다. 출애굽기 21장의 공의의 법도와 요한복음 7장의 공의로운 판단 말씀을 통해, 데이터를 공의롭게 분류하고 범주형으로 다루어 하나님의 질서와 공의를 데이터적으로 이해하고 묵상합니다.

This chapter introduces how to classify data according to specific criteria and handle it as categorical data using Pandas. We will explore techniques for dividing data into bins using `pd.cut()` and `pd.qcut()`, and efficiently managing categorical data through `category dtype`. Through the ordinances of justice in Exodus 21 and the righteous judgment in John 7, we will understand and meditate on God's order and justice by classifying and handling data categorically.

---

## 📜 성경 본문 깊이 묵상

### 출애굽기 21장: 공의의 법도

십계명 이후 하나님께서는 이스라엘 백성에게 다양한 사회적, 도덕적 규례들을 주셨습니다. 이는 노예, 폭력, 재산, 배상 등 일상생활에서 발생할 수 있는 문제들에 대한 구체적인 법규들로, 하나님의 공의로운 통치를 반영합니다. 각 상황에 따라 명확한 기준과 분류가 적용되어야 했습니다.

- **노예에 대한 규례:** 히브리 종과 여종에 대한 대우 (출 21:1-11)
- **폭력에 대한 규례:** 살인, 상해, 낙태 등에 대한 처벌 (출 21:12-27)
- **재산 및 배상 규례:** 소유물에 대한 책임과 손해 배상 (출 21:28-36)

이 본문은 데이터를 분류하고 범주화하는 데 영감을 줍니다. 예를 들어, 범죄 유형을 `category dtype`으로 분류하고, 피해 정도를 `pd.cut()`이나 `pd.qcut()`으로 구간화하여 분석할 수 있습니다. 이는 각 법도(규례)가 적용되는 상황과 그에 따른 결과를 명확히 이해하는 데 도움을 줍니다.

### 요한복음 7:24: 공의로운 판단

예수님께서는 "외모로 판단하지 말고 공의롭게 판단하라"고 말씀하셨습니다. 이는 겉으로 드러나는 현상만을 보고 성급하게 결론을 내리지 말고, 본질과 상황을 깊이 이해하여 올바른 판단을 내릴 것을 촉구합니다. 데이터 분석에서도 겉으로 보이는 숫자나 문자열만을 볼 것이 아니라, 그 데이터가 속한 범주와 맥락을 이해하는 것이 중요합니다.

- **외모 판단 금지:** 겉모습이나 편견에 기반한 판단 지양
- **공의로운 판단:** 본질과 진실에 기반한 올바른 판단
- **데이터의 본질:** 데이터가 속한 범주와 맥락 이해

이 말씀은 데이터를 분류하고 범주화하는 과정에서 우리가 가져야 할 태도를 가르칩니다. `category dtype`은 데이터의 본질적인 범주를 명확히 하고, `pd.cut()`이나 `pd.qcut()`은 데이터를 공의로운 기준에 따라 나누어 편향되지 않은 분석을 가능하게 합니다. 이는 데이터의 외모가 아닌 본질을 보고 판단하는 데 도움을 줍니다.

---

## 🔍 숨겨진 질문 발견

**출애굽기에서 발견할 질문들:**

- 출애굽기 21장의 다양한 규례들을 `category dtype`으로 분류하면, 각 규례가 다루는 핵심 주제(예: 인명, 재산)는 무엇일까?
- `pd.cut()`을 사용하여 피해 정도를 '경미', '보통', '심각' 등으로 구간화하면, 각 구간에 해당하는 규례의 특징은 무엇일까?
- `pd.qcut()`을 사용하여 노예의 노동 시간을 동일한 빈도로 묶으면, 노동 시간 분포에 따른 규례의 적용 방식은 어떻게 달라질까?

**요한복음에서 발견할 질문들:**

- 예수님께서 말씀하신 다양한 판단의 기준들을 `category dtype`으로 분류하면, 어떤 기준이 가장 중요하게 강조되었을까?
- 사람들의 외모 판단 경향을 `pd.cut()`으로 '낮음', '중간', '높음'으로 구간화하면, 각 구간에 따른 영적 통찰은 무엇일까?
- 공의로운 판단의 요소들을 `pd.qcut()`으로 동일한 빈도로 묶으면, 판단의 균형을 맞추는 데 어떤 도움이 될까?

이런 질문들은 데이터의 '분류와 범주형'이라는 관점으로 성경 본문을 더 깊이 이해하는 데 도움을 줄 것이다.

---

## 📊 판다스로 성경 탐구하기

### 탐구 1: 공의의 법도 분류 분석 (category dtype, pd.cut)

```python
import pandas as pd
import numpy as np
from chapters.ch21.justice_ordinances_data import JusticeOrdinancesDataGenerator

# 공의의 법도 데이터 생성
data_gen = JusticeOrdinancesDataGenerator()
df_ordinances = data_gen.generate_ordinances_data()

print("⚖️ 공의의 법도 데이터 요약:\n", df_ordinances.head())
print("데이터 타입:\n", df_ordinances.dtypes)

# 'offense_type' 컬럼을 category dtype으로 변환
df_ordinances['offense_type'] = df_ordinances['offense_type'].astype('category')
print("\n--- 'offense_type' 컬럼 변환 후 데이터 타입 ---")
print(df_ordinances.dtypes)

# 'damage_level'을 기준으로 데이터를 3개의 구간으로 나누어 분류 (pd.cut)
# labels를 명시하여 의미 있는 범주 이름 부여
df_ordinances['damage_category'] = pd.cut(df_ordinances['damage_level'], bins=3, labels=['Minor', 'Moderate', 'Severe'])
print("\n--- 'damage_level'을 3개 구간으로 분류 후 ---")
print(df_ordinances[['damage_level', 'damage_category']].head())
print(df_ordinances['damage_category'].value_counts())
```

### 탐구 2: 공의로운 판단 범주화 분석 (pd.qcut)

```python
import pandas as pd
import numpy as np
from chapters.ch21.classification_analysis import ClassificationAnalyzer

# 공의로운 판단 데이터 생성 (가정)
# ClassificationAnalyzer에서 데이터를 생성한다고 가정
analyzer = ClassificationAnalyzer()
df_judgment = analyzer.generate_judgment_data()

print("⚖️ 공의로운 판단 데이터 요약:\n", df_judgment.head())

# 'judgment_score'를 기준으로 데이터를 동일한 빈도로 4개의 구간으로 나누어 분류 (pd.qcut)
# labels를 명시하여 의미 있는 범주 이름 부여
df_judgment['judgment_quartile'] = pd.qcut(df_judgment['judgment_score'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print("\n--- 'judgment_score'를 4분위수로 분류 후 ---")
print(df_judgment[['judgment_score', 'judgment_quartile']].head())
print(df_judgment['judgment_quartile'].value_counts())
```

---

## ⭐ 놀라운 발견들

### 발견 1: `category dtype`을 통한 데이터의 본질적 분류

`category dtype`을 사용하여 데이터의 범주형 특성을 명확히 하면, 데이터의 본질적인 의미를 더 깊이 이해할 수 있습니다. 이는 출애굽기 21장의 공의의 법도가 각 상황과 대상에 따라 명확한 분류 기준을 가지고 있음을 데이터적으로 보여줍니다. 데이터의 외모가 아닌 본질을 보고 판단하는 공의로운 태도를 기르는 데 도움을 줍니다.

### 발견 2: `pd.cut()`을 통한 공의로운 구간 분류

`pd.cut()`을 사용하여 데이터를 특정 기준에 따라 구간으로 나누면, 데이터의 분포를 공의롭게 분류하고 각 구간의 특성을 분석할 수 있습니다. 이는 피해 정도나 상황의 심각성을 객관적인 기준으로 나누어, 하나님의 공의로운 법도가 어떻게 적용되는지 데이터적으로 탐구하는 것과 같습니다.

### 발견 3: `pd.qcut()`을 통한 균형 잡힌 판단

`pd.qcut()`을 사용하여 데이터를 동일한 빈도로 구간화하면, 데이터의 분포를 균형 있게 나누어 편향되지 않은 판단을 내리는 데 도움을 줍니다. 이는 예수님께서 외모로 판단하지 말고 공의롭게 판단하라고 하신 말씀처럼, 데이터의 특정 부분에 치우치지 않고 전체적인 분포를 고려하여 균형 잡힌 통찰을 얻는 데 유용합니다.

---

## 🎨 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰

|출애굽기 진리|요한복음 진리|판다스 도구|영적 발견|
|---|---|---|---|
|공의의 법도와 명확한 분류|외모로 판단하지 말고 공의롭게 판단|`category dtype`|데이터의 본질과 맥락 이해|
|각 상황에 따른 구체적인 규례|본질과 진실에 기반한 판단|`pd.cut()`|데이터를 공의로운 기준으로 분류|
|노예, 폭력, 재산에 대한 법규|데이터의 다양한 특성 이해|`pd.qcut()`|데이터 분포를 균형 있게 파악|
|하나님의 질서와 공의|예수님의 공의로운 통치|분류 및 범주화|데이터 속 하나님의 질서와 공의 발견|
|죄와 배상에 대한 기준|판단과 심판의 기준|데이터 구간화|영적 분별력과 올바른 판단력|

> **💎 블렌딩 결과**: `category dtype`, `pd.cut()`, `pd.qcut()`과 같은 분류 및 범주화 기술은 성경 속 공의의 법도와 공의로운 판단의 원리를 데이터적으로 분석하는 강력한 도구입니다. 데이터를 공의롭게 분류하고 범주형으로 다루어 하나님의 질서와 공의를 이해하고, 외모가 아닌 본질을 보고 판단하는 영적 통찰을 얻을 수 있습니다.

---

## 🛠️ 광야 생존 프로젝트: 나의 영적 상태 분류 분석

**🎯 미션**: 내 삶의 영적 상태 데이터를 분류하고 범주화하여 패턴 발견하기
**📊 사용 기술**: DataFrame 생성, `category dtype`, `pd.cut()`, `pd.qcut()`
**🕊️ 복음 포인트**: "외모로 판단하지 말고 공의의 판단으로 판단할지니라" (요한복음 7:24)

### Step 1: 나의 영적 상태 데이터 기록 및 범주형 변환

```python
import pandas as pd
import numpy as np

my_spiritual_state = pd.DataFrame({
    '날짜': pd.to_datetime(pd.date_range(start='2024-01-01', periods=30, freq='D')),
    '말씀_묵상_시간_분': np.random.randint(0, 60, size=30),
    '기도_시간_분': np.random.randint(0, 90, size=30),
    '봉사_참여_여부': np.random.choice(['Yes', 'No'], size=30, p=[0.3, 0.7]),
    '감사_지수': np.random.randint(1, 10, size=30)
})

print("🧬 나의 영적 상태 데이터:\n", my_spiritual_state.head())

# '봉사_참여_여부' 컬럼을 category dtype으로 변환
my_spiritual_state['봉사_참여_여부'] = my_spiritual_state['봉사_참여_여부'].astype('category')
print("\n--- '봉사_참여_여부' 컬럼 변환 후 데이터 타입 ---")
print(my_spiritual_state.dtypes)
```

### Step 2: 영적 성장 지표 구간 분류 분석

```python
# '감사_지수'를 기준으로 데이터를 4개의 구간으로 나누어 분류 (pd.cut)
my_spiritual_state['감사_레벨'] = pd.cut(my_spiritual_state['감사_지수'], bins=4, labels=['Low', 'Medium', 'High', 'Very High'])
print("\n--- '감사_지수'를 4개 구간으로 분류 후 ---")
print(my_spiritual_state[['감사_지수', '감사_레벨']].head())
print(my_spiritual_state['감사_레벨'].value_counts())

# '기도_시간_분'을 기준으로 데이터를 동일한 빈도로 3개의 구간으로 나누어 분류 (pd.qcut)
my_spiritual_state['기도_시간_그룹'] = pd.qcut(my_spiritual_state['기도_시간_분'], q=3, labels=['Short', 'Medium', 'Long'])
print("\n--- '기도_시간_분'을 3분위수로 분류 후 ---")
print(my_spiritual_state[['기도_시간_분', '기도_시간_그룹']].head())
print(my_spiritual_state['기도_시간_그룹'].value_counts())
```

---

## 📱 3×10초 광야 루틴

### 🌅 아침 10초: 말씀 묵상

"너는 외모를 보고 판단하지 말고 공의의 판단으로 판단할지니라." (요 7:24)
오늘도 겉모습이 아닌 본질을 보고 공의롭게 판단하는 하루를 시작합니다.

### ☀️ 점심 1분: 분류 기도

- 오늘 제가 마주한 사람이나 상황을 `category dtype`처럼 어떤 범주로 분류하고 있지는 않은지 돌아봅니다.
- `pd.cut()`이나 `pd.qcut()`처럼 편견 없이 공의로운 기준으로 사람과 상황을 이해할 지혜를 구합니다.

### 🌙 저녁 2분: 데이터 기도일기

**오늘의 영적 데이터:**
- 오늘 `category dtype`으로 분류해 본 나의 영적 활동은?
- `pd.cut()`으로 구간화해 본 나의 영적 상태 지표는?
- `pd.qcut()`으로 균형 있게 분류해 본 나의 판단 기준은?
- 주님, 공의로운 판단으로 저를 인도하시고, 모든 것을 바르게 분류하게 하소서.

---

## ❓ FAQ & 체크리스트

### 깊이 있는 질문들

**Q1: `category dtype`을 사용하는 주된 이유는 무엇인가요?** A: `category dtype`은 문자열과 같은 범주형 데이터를 효율적으로 저장하고 처리하기 위해 사용됩니다. 이는 메모리 사용량을 줄이고, 연산 속도를 향상시키며, 범주형 데이터에 특화된 기능을 제공합니다. 예를 들어, 성별, 지역, 등급과 같이 고정된 몇 가지 값만을 가지는 컬럼에 적합합니다.

**Q2: `pd.cut()`과 `pd.qcut()`의 차이점은 무엇인가요?** A: `pd.cut()`은 사용자가 지정한 경계값(bins)을 기준으로 데이터를 구간으로 나눕니다. 각 구간의 데이터 개수는 다를 수 있습니다. 반면, `pd.qcut()`은 데이터를 동일한 개수(빈도)로 나누어 각 구간에 거의 같은 수의 데이터가 포함되도록 합니다. 이는 데이터의 분포를 균등하게 나누고자 할 때 유용합니다.

**Q3: 공의의 법도를 `category dtype`으로 분류하는 것이 영적으로 어떤 의미가 있을까요?** A: 공의의 법도를 `category dtype`으로 분류하면, 각 법도가 다루는 핵심 주제(예: 인명, 재산)를 명확히 하고, 각 주제에 따른 하나님의 공의로운 기준을 체계적으로 이해할 수 있습니다. 이는 하나님의 질서와 공의가 혼란스러운 상황 속에서도 명확한 분류와 기준을 가지고 있음을 보여줍니다.

**Q4: `pd.cut()`과 `pd.qcut()`을 공의로운 판단에 적용하는 것이 왜 중요한가요?** A: `pd.cut()`은 우리가 정한 기준(bins)에 따라 데이터를 분류하므로, 우리가 어떤 기준으로 판단해야 할지 고민하게 합니다. `pd.qcut()`은 데이터의 분포를 균등하게 나누어 편향되지 않은 시각으로 데이터를 바라보게 합니다. 이는 외모로 판단하지 않고 공의롭게 판단하라는 말씀처럼, 객관적이고 균형 잡힌 판단을 돕는 데 영감을 줍니다.

**Q5: 데이터 분류 및 범주화가 영적 분별력과 어떻게 연결될 수 있을까요?** A: 데이터 분류 및 범주화는 복잡한 정보 속에서 핵심을 파악하고, 유사한 것들을 묶어 이해하며, 다른 것들을 구별하는 과정입니다. 이는 영적 분별력과 유사합니다. 우리가 영적으로 무엇이 옳고 그른지, 무엇이 중요한지 덜 중요한지, 무엇이 하나님의 뜻인지 아닌지를 분류하고 범주화하는 지혜를 기르는 데 도움을 줍니다.

### ✅ 체크리스트

**성경 이해 체크:**

- [ ] 출애굽기 21장의 공의의 법도와 각 규례의 의미 이해
- [ ] 요한복음 7장의 공의로운 판단의 중요성 이해
- [ ] 데이터를 공의롭게 분류하고 범주형으로 다루어 하나님의 질서와 공의를 이해

**DataFrame 기초 체크:**

- [ ] `df.astype('category')`를 사용하여 범주형 데이터 타입으로 변환 성공
- [ ] `pd.cut()` 함수를 사용하여 데이터를 지정된 구간으로 나누어 분류 성공
- [ ] `pd.qcut()` 함수를 사용하여 데이터를 동일한 빈도로 나누어 분류 성공
- [ ] `bins`와 `q` 파라미터의 역할 이해

**영적 적용 체크:**

- [ ] 내 삶의 영적 상태 데이터를 분류하고 범주화하여 패턴 발견 시도 완료
- [ ] 나의 판단 기준을 `pd.cut()`과 `pd.qcut()` 원리에 따라 공의롭게 점검 시도 완료
- [ ] 데이터 분류 및 범주화 원리를 통해 영적 분별력 향상 고민

**발견 기록 체크:**

- [ ] `category dtype`을 통한 데이터의 본질적 분류 확인
- [ ] `pd.cut()`을 통한 공의로운 구간 분류 통찰
- [ ] `pd.qcut()`을 통한 균형 잡힌 판단 확인

---

## 🧠 미니 퀴즈

**1. 문자열과 같은 범주형 데이터를 효율적으로 저장하고 처리하기 위해 사용되는 Pandas 데이터 타입은?**
a) `object`
b) `int64`
c) `category`

**2. 사용자가 지정한 경계값(bins)을 기준으로 데이터를 구간으로 나누는 함수는?**
a) `pd.qcut()`
b) `pd.cut()`
c) `df.groupby()`

**3. 데이터를 동일한 개수(빈도)로 나누어 각 구간에 거의 같은 수의 데이터가 포함되도록 하는 함수는?**
a) `pd.cut()`
b) `pd.qcut()`
c) `df.resample()`

**4. `pd.cut()` 함수에서 각 구간에 의미 있는 이름을 부여하기 위해 사용되는 파라미터는?**
a) `bins`
b) `labels`
c) `right`

**5. 공의로운 판단을 위해 데이터를 분류하고 범주화하는 영적 의미로 가장 적절하지 않은 것은?**
a) 데이터의 외모가 아닌 본질을 보고 판단
b) 편향되지 않고 균형 잡힌 시각으로 데이터 이해
c) 데이터의 특정 부분에만 집중하여 빠른 결론 도출

_(정답: 1-c, 2-b, 3-b, 4-b, 5-c)_

---

## 🎯 깊이 탐구 과제 (선택)

### 초급 과제

1.  **성경 인물 특성 범주화**: 성경 인물 데이터(이름, 시대, 역할, 성별)를 만들고, `역할`과 `성별` 컬럼을 `category dtype`으로 변환해보기
2.  **성경 구절 길이 구간화**: 성경 구절 데이터(구절 ID, 구절 내용, 글자 수)를 만들고, `pd.cut()`을 사용하여 `글자 수`를 '짧음', '중간', '김'으로 구간화해보기

### 중급 과제

1.  **교회 봉사 유형 분류**: 가상의 교회 봉사 데이터(봉사자 ID, 봉사 유형, 봉사 시간)를 만들고, `봉사 유형`을 `category dtype`으로 변환한 후, `봉사 시간`을 `pd.qcut()`으로 3분위수로 나누어 각 봉사 유형별 시간 분포 분석해보기
2.  **영적 성장 단계 분류**: 개인의 영적 성장 지표(예: 말씀 묵상 시간, 기도 시간, 감사 지수)를 종합하여 `pd.cut()`으로 '초급', '중급', '고급' 영적 성장 단계로 분류하고, 각 단계의 특징 분석해보기

### 고급 과제

1.  **사회 문제 공의로운 분류 시스템**: 가상의 사회 문제 데이터(문제 유형, 심각도, 영향 범위, 해결 난이도)를 만들고, `category dtype`, `pd.cut()`, `pd.qcut()`을 조합하여 문제를 공의로운 기준으로 분류하고, 각 분류에 따른 해결 방안을 제안하는 시스템(개념) 설계해보기
2.  **성경 인물 리더십 유형 분석**: 성경 인물 데이터(이름, 리더십 스타일, 영향력, 시대)를 만들고, `리더십 스타일`을 `category dtype`으로, `영향력`을 `pd.qcut()`으로 분류한 후, 각 리더십 유형의 특징과 시대별 분포를 분석하여 보고서 작성해보기

---

## 🌟 다음 여정 예고

**Chapter 22: "배상과 회복 - 결측·이상치 전략 (Compensation and Restoration - Missing/Outlier Strategy)"**

출애굽기 22장에서 배상과 회복에 대한 규례를 통해 손해를 입은 자에게 합당한 보상이 이루어지듯이, 데이터 분석에서도 결측치(Missing Values)와 이상치(Outliers)를 적절히 처리하는 것은 데이터의 무결성을 회복하고 분석 결과의 신뢰성을 높이는 데 필수적입니다.

Just as Exodus 22 outlines regulations for compensation and restoration to ensure proper recompense for damages, in data analysis, appropriately handling missing values and outliers is essential for restoring data integrity and enhancing the reliability of analytical results.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 결측치 탐지 및 처리 전략 (fillna, dropna)
🔍 이상치 탐지 기법 (IQR, Z-score)
🎯 이상치 처리 방법 (제거, 대체, 변환)
📊 배상과 회복처럼 데이터의 무결성을 지키고 신뢰성을 높이는 전략

"사람이 밭에나 포도원에 불을 놓아 곡식단을 사르거나 밭을 태우면 불 놓은 자가 반드시 배상할지니라" (출애굽기 22:5)
"예수께서 이르시되 내가 너희에게 이르노니 너희가 돌이켜 어린 아이들과 같이 되지 아니하면 결단코 천국에 들어가지 못하리라" (마태복음 18:3)

---

## 🙏 한 줄 기도

_"주님, 공의의 법도처럼 데이터를 공의롭게 분류하고 범주형으로 다루어 하나님의 질서와 공의를 이해하게 하소서.
외모로 판단하지 않고 본질을 보고 판단하는 영적 분별력을 주시고,
데이터 분석을 통해 주님의 공의로운 통치를 더욱 깊이 깨닫게 하소서. 예수님의 이름으로 기도합니다. 아멘."_

---

**🎊 스물한 번째 광야 여정을 완주하신 것을 축하합니다!**

"너는 외모를 보고 판단하지 말고 공의의 판단으로 판단할지니라" (요한복음 7:24)

여러분은 이제 데이터 속에서 `category dtype`, `pd.cut()`, `pd.qcut()`을 통해 데이터를 공의롭게 분류하고 범주형으로 다루는 방법을 알게 되었습니다. 주님께서 주신 지혜로 모든 정보 속에서 하나님의 질서와 공의를 발견하시길 기도합니다.

**다음 여정에서 만나요! 🌈**
