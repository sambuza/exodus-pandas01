# Chapter 34: 새 돌판 - 정규화와 표준화

## 개요 (Overview)
이번 챕터에서는 Pandas를 사용하여 데이터의 스케일을 조정하는 '정규화(Normalization)'와 '표준화(Standardization)' 기법을 배웁니다. Min-Max Scaling을 통한 정규화, Z-score Standardization을 통한 표준화, 그리고 문자열 정규화(`str.normalize`)와 같은 기술을 탐구합니다. 출애굽기 34장의 새 돌판에 십계명을 다시 받은 사건과 요한복음 1장의 은혜 위에 은혜 말씀을 통해, 데이터의 특성을 통일하고 모델의 성능을 향상시키는 지혜를 데이터적으로 이해하고 묵상합니다.

This chapter introduces data scaling techniques using Pandas: 'Normalization' (Min-Max Scaling) and 'Standardization' (Z-score Standardization), as well as string normalization (`str.normalize`). Through the event of receiving the Ten Commandments on new tablets in Exodus 34 and the message of grace upon grace in John 1, we will understand and meditate on the wisdom of unifying data characteristics and improving model performance.

---

## 📜 성경 본문 깊이 묵상

### 출애굽기 34장: 새 돌판과 언약 갱신

금송아지 사건으로 모세가 깨뜨렸던 처음 돌판 대신, 하나님께서는 모세에게 새 돌판 둘을 깎아 만들라고 지시하시고 그 위에 십계명을 다시 기록하셨습니다. 이는 깨어진 언약이 갱신되고, 하나님의 변치 않는 말씀이 다시 한번 확증되는 중요한 사건입니다. 새 돌판은 이전의 깨어진 돌판과 동일한 내용을 담고 있지만, 새로운 시작과 회복을 상징합니다. 이는 데이터의 스케일을 조정하여 본질적인 특성을 유지하면서도 새로운 관점으로 데이터를 바라보는 것과 유사합니다.

- **새 돌판:** 깨어진 언약의 회복과 갱신 (출 34:1)
- **동일한 말씀:** 처음 판에 쓴 말을 다시 기록 (출 34:1)
- **새로운 시작:** 데이터의 본질을 유지하며 스케일 조정

이 본문은 데이터 정규화와 표준화에 영감을 줍니다. 데이터의 스케일이 다르면 분석이나 모델링에 어려움이 있을 수 있습니다. 정규화(Min-Max Scaling)는 데이터를 특정 범위(예: 0~1)로 조정하여 모든 특성이 동일한 중요도를 가지도록 합니다. 표준화(Z-score Standardization)는 데이터를 평균 0, 표준편차 1로 조정하여 데이터의 분포를 통일합니다. 이는 새 돌판에 기록된 십계명처럼 데이터의 본질적인 특성을 유지하면서도, 분석에 적합한 형태로 데이터를 변환하는 것과 같습니다.

### 요한복음 1:16: 은혜 위에 은혜

"우리가 다 그의 충만한 데서 받으니 은혜 위에 은혜러라." 이 말씀은 예수 그리스도를 통해 우리가 받는 하나님의 은혜가 끊임없이 이어지고 풍성함을 의미합니다. 은혜는 단순히 한 번 주어지는 것이 아니라, 계속해서 더해지고 넘쳐나는 것입니다. 데이터 분석에서 정규화와 표준화는 데이터의 특성을 통일하여 모델이 더 많은 '은혜'(정보)를 효과적으로 받아들이고 활용할 수 있도록 돕습니다.

- **충만한 은혜:** 예수 그리스도를 통해 받는 풍성한 은혜
- **은혜 위에 은혜:** 끊임없이 더해지고 넘쳐나는 은혜
- **데이터의 통일성:** 모델이 은혜(정보)를 효과적으로 받아들임

이 말씀은 데이터 정규화와 표준화의 목적에 영감을 줍니다. 데이터의 스케일을 통일하는 것은 모델이 데이터의 모든 특성을 동일한 관점에서 바라보고, 편향되지 않은 학습을 할 수 있도록 돕습니다. 이는 은혜 위에 은혜를 더하는 것처럼 모델의 성능을 향상시키고, 데이터가 가진 모든 정보를 효과적으로 활용하여 더 깊은 통찰을 얻는 데 기여합니다. 문자열 정규화(`str.normalize`)는 텍스트 데이터의 다양한 표현을 통일하여 분석의 일관성을 확보하는 데 유용합니다.

---

## 🔍 숨겨진 질문 발견

**출애굽기에서 발견할 질문들:**

- 이스라엘 백성의 순종 지수와 불순종 지수 데이터를 만들고, `정규화`를 적용하여 0과 1 사이의 값으로 조정하면, 두 지표의 상대적인 변화를 어떻게 더 명확히 비교할 수 있을까?
- 재앙의 강도 데이터와 파라오의 완악함 지수 데이터를 만들고, `표준화`를 적용하여 평균 0, 표준편차 1로 조정하면, 두 지표의 분포를 어떻게 더 효과적으로 비교할 수 있을까?
- 십계명 텍스트 데이터를 만들고 `문자열 정규화`를 적용하면, 다양한 표현의 십계명 구절들을 어떻게 통일하여 분석할 수 있을까?

**요한복음에서 발견할 질문들:**

- 제자들의 믿음 수준과 영적 성장 점수 데이터를 만들고, `정규화`를 적용하여 0과 1 사이의 값으로 조정하면, 각 제자의 영적 성장을 어떻게 더 명확히 비교할 수 있을까?
- 예수님의 가르침에 대한 사람들의 반응 데이터(긍정, 부정)를 만들고, `표준화`를 적용하여 평균 0, 표준편차 1로 조정하면, 반응의 분포를 어떻게 더 효과적으로 비교할 수 있을까?
- 예수님의 말씀 텍스트 데이터를 만들고 `문자열 정규화`를 적용하면, 다양한 표현의 말씀 구절들을 어떻게 통일하여 분석할 수 있을까?

이런 질문들은 데이터의 '정규화와 표준화'라는 관점으로 성경 본문을 더 깊이 이해하는 데 도움을 줄 것이다.

---

## 📊 판다스로 성경 탐구하기

### 탐구 1: 새 돌판 데이터 정규화 및 표준화 (Min-Max Scaling, Z-score Standardization)

```python
import pandas as pd
import numpy as np
from chapters.ch34.new_tablets_data import NewTabletsDataGenerator
from chapters.ch34.min_max_normalizer import MinMaxNormalizer
from chapters.ch34.zscore_standardizer import ZscoreStandardizer

# 새 돌판 데이터 생성
data_gen = NewTabletsDataGenerator()
df_new_tablets = data_gen.generate_tablets_data()

print("📜 새 돌판 데이터 요약:\n", df_new_tablets.head())

# 'obedience_score' 컬럼 Min-Max 정규화
normalizer = MinMaxNormalizer(df_new_tablets)
normalized_df = normalizer.apply_min_max_scaling('obedience_score')
print("\n--- 'obedience_score' Min-Max 정규화 후 ---")
print(normalized_df.head())

# 'divine_favor' 컬럼 Z-score 표준화
standardizer = ZscoreStandardizer(df_new_tablets)
standardized_df = standardizer.apply_zscore_standardization('divine_favor')
print("\n--- 'divine_favor' Z-score 표준화 후 ---")
print(standardized_df.head())
```

### 탐구 2: 은혜 위에 은혜 데이터 문자열 정규화 (str.normalize)

```python
import pandas as pd
import numpy as np
from chapters.ch34.new_tablets_data import NewTabletsDataGenerator # 동일 데이터 생성기 사용
from chapters.ch34.string_normalizer import StringNormalizer

# 은혜 데이터 생성 (가정)
data_gen = NewTabletsDataGenerator()
df_grace = data_gen.generate_tablets_data()

# 'commandment_text' 컬럼에 다양한 문자열 표현 추가 (예시)
df_grace.loc[0, 'commandment_text'] = "Thou shalt not kill."
df_grace.loc[1, 'commandment_text'] = "Thou shalt not steal."
df_grace.loc[2, 'commandment_text'] = "Thou shalt not kill!"
df_grace.loc[3, 'commandment_text'] = "Thou shalt not steal."

print("🙏 은혜 데이터 요약:\n", df_grace.head())

# 'commandment_text' 컬럼 문자열 정규화
normalizer = StringNormalizer(df_grace)
normalized_string_df = normalizer.apply_string_normalization('commandment_text')

print("\n--- 'commandment_text' 문자열 정규화 후 ---")
print(normalized_string_df.head())
```

---

## ⭐ 놀라운 발견들

### 발견 1: 정규화(Min-Max Scaling)를 통한 새 돌판의 통일된 기준

Min-Max 정규화를 통해 데이터를 특정 범위(예: 0~1)로 조정하는 것은 새 돌판에 십계명을 다시 기록하여 모든 백성에게 통일된 기준을 제시하는 것과 같습니다. 이는 데이터의 스케일이 다를 때 발생하는 분석의 어려움을 해소하고, 모든 특성이 동일한 중요도를 가지도록 하여 공정한 분석을 가능하게 합니다.

### 발견 2: 표준화(Z-score Standardization)를 통한 은혜 위에 은혜의 분포 통일

Z-score 표준화를 통해 데이터를 평균 0, 표준편차 1로 조정하는 것은 은혜 위에 은혜를 더하는 것처럼 데이터의 분포를 통일하여 모델이 더 많은 정보를 효과적으로 받아들이고 활용할 수 있도록 돕습니다. 이는 데이터의 특성을 통일하여 모델의 성능을 향상시키고, 데이터가 가진 모든 정보를 효과적으로 활용하여 더 깊은 통찰을 얻는 데 기여합니다.

### 발견 3: 문자열 정규화는 말씀의 본질을 흐리지 않는 지혜

문자열 정규화(`str.normalize`)는 텍스트 데이터의 다양한 표현을 통일하여 분석의 일관성을 확보하는 것과 같습니다. 이는 십계명의 말씀이 다양한 언어나 형태로 번역될지라도 그 본질적인 의미는 변하지 않는 것처럼, 데이터의 다양한 표현을 통일하여 분석의 정확성을 높이고, 말씀의 본질을 흐리지 않는 지혜를 제공합니다.

---

## 🎨 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰

|출애굽기 진리|요한복음 진리|판다스 도구|영적 발견|
|---|---|---|---|
|새 돌판에 십계명 = 통일된 기준|은혜 위에 은혜 = 풍성한 정보 활용|정규화 (Min-Max Scaling)|데이터의 특성 통일과 공정한 분석|
|깨어진 언약의 회복|예수님의 충만한 은혜|표준화 (Z-score Standardization)|데이터 분포 통일과 모델 성능 향상|
|하나님의 변치 않는 말씀|진리의 불변성|문자열 정규화 (str.normalize)|데이터의 일관성 확보와 말씀의 본질 유지|
|데이터의 스케일 조정|모델의 성능 향상|정규화/표준화 전략|영적 분별력과 지혜로운 의사결정|
|데이터의 본질 유지|새로운 관점으로 데이터 바라봄|데이터 변환|영적 성장과 분석 효율성의 조화|

> **💎 블렌딩 결과**: 정규화(Min-Max Scaling), 표준화(Z-score Standardization), 문자열 정규화(`str.normalize`)와 같은 데이터 스케일 조정 기술은 성경 속 새 돌판에 십계명을 다시 받은 사건과 은혜 위에 은혜 말씀을 데이터적으로 분석하는 강력한 도구입니다. 데이터의 특성을 통일하고 모델의 성능을 향상시키는 과정을 통해, 하나님의 변치 않는 말씀과 풍성한 은혜를 이해하고 영적 분별력을 길러 지혜로운 의사결정을 내릴 수 있습니다.

---

## 🛠️ 광야 생존 프로젝트: 나의 영적 성장 지표 정규화 및 표준화

**🎯 미션**: 내 삶의 영적 성장 데이터를 정규화하고 표준화하여 분석하기
**📊 사용 기술**: DataFrame 생성, Min-Max Scaling, Z-score Standardization, 문자열 정규화
**🕊️ 복음 포인트**: "우리가 다 그의 충만한 데서 받으니 은혜 위에 은혜러라" (요한복음 1:16)

### Step 1: 나의 영적 성장 데이터 기록 및 정규화

```python
import pandas as pd
import numpy as np

my_spiritual_growth = pd.DataFrame({
    '날짜': pd.to_datetime(pd.date_range(start='2024-01-01', periods=10, freq='D')),
    '기도_시간_분': np.random.randint(0, 120, size=10),
    '말씀_묵상_시간_분': np.random.randint(0, 90, size=10),
    '감사_지수': np.random.randint(1, 10, size=10),
    '영적_상태_평가': np.random.choice(['좋음', '보통', '나쁨'], size=10)
})

print("🧬 나의 영적 성장 기록:\n", my_spiritual_growth.head())

# '기도_시간_분' 컬럼 Min-Max 정규화
min_max_scaled_prayer = my_spiritual_growth.copy()
min_max_scaled_prayer['기도_시간_분_정규화'] = (min_max_scaled_prayer['기도_시간_분'] - min_max_scaled_prayer['기도_시간_분'].min()) /
                                        (min_max_scaled_prayer['기도_시간_분'].max() - min_max_scaled_prayer['기도_시간_분'].min())
print("\n--- '기도_시간_분' Min-Max 정규화 후 ---")
print(min_max_scaled_prayer[['기도_시간_분', '기도_시간_분_정규화']].head())
```

### Step 2: 영적 성장 지표 표준화 및 문자열 정규화

```python
# '말씀_묵상_시간_분' 컬럼 Z-score 표준화
zscore_standardized_word = my_spiritual_growth.copy()
zscore_standardized_word['말씀_묵상_시간_분_표준화'] = (zscore_standardized_word['말씀_묵상_시간_분'] - zscore_standardized_word['말씀_묵상_시간_분'].mean()) /
                                                zscore_standardized_word['말씀_묵상_시간_분'].std()
print("\n--- '말씀_묵상_시간_분' Z-score 표준화 후 ---")
print(zscore_standardized_word[['말씀_묵상_시간_분', '말씀_묵상_시간_분_표준화']].head())

# '영적_상태_평가' 컬럼 문자열 정규화 (예: 공백 제거, 소문자 변환)
my_spiritual_growth['영적_상태_평가_정규화'] = my_spiritual_growth['영적_상태_평가'].str.strip().str.lower()
print("\n--- '영적_상태_평가' 문자열 정규화 후 ---")
print(my_spiritual_growth[['영적_상태_평가', '영적_상태_평가_정규화']].head())
```

---

## 📱 3×10초 광야 루틴

### 🌅 아침 10초: 말씀 묵상

"우리가 다 그의 충만한 데서 받으니 은혜 위에 은혜러라." (요 1:16)
오늘도 주님의 충만한 은혜 속에서 하루를 시작합니다.

### ☀️ 점심 1분: 스케일 조정 기도

- 나의 삶에서 `정규화`처럼 너무 크거나 작은 부분은 없는지 돌아봅니다.
- `표준화`처럼 나의 생각과 행동이 주님의 기준에 맞게 통일되어야 할 부분은 없는지 점검합니다.
- 주님, `문자열 정규화`처럼 나의 모든 표현이 주님의 말씀의 본질을 흐리지 않게 하소서.

### 🌙 저녁 2분: 데이터 기도일기

**오늘의 영적 데이터:**
- 오늘 `정규화`해 본 나의 영적 성장 지표는?
- `표준화`해 본 나의 영적 상태 분포는?
- `문자열 정규화`로 본 나의 언어생활은?
- 주님, 새 돌판처럼 저의 마음을 새롭게 하시고, 주님의 은혜 위에 은혜를 더하게 하소서.

---

## ❓ FAQ & 체크리스트

### 깊이 있는 질문들

**Q1: 정규화(Normalization)와 표준화(Standardization)의 주요 차이점은 무엇인가요?** A: **정규화(Normalization)**는 데이터를 특정 범위(예: 0~1)로 조정하여 모든 특성이 동일한 스케일을 가지도록 합니다. 이는 Min-Max Scaling이 대표적입니다. **표준화(Standardization)**는 데이터를 평균 0, 표준편차 1을 가지도록 조정하여 데이터의 분포를 통일합니다. 이는 Z-score Standardization이 대표적입니다. 정규화는 데이터의 최댓값과 최솟값에 민감하고, 표준화는 이상치에 덜 민감합니다.

**Q2: Min-Max Scaling은 어떻게 작동하며, 어떤 상황에서 사용되나요?** A: Min-Max Scaling은 데이터의 최솟값을 0, 최댓값을 1로 만들고, 모든 데이터를 이 범위 안에 비례적으로 조정합니다. `(x - min(x)) / (max(x) - min(x))` 공식을 사용합니다. 이는 데이터의 스케일을 특정 범위로 제한해야 할 때(예: 신경망 입력 데이터) 유용합니다.

**Q3: Z-score Standardization은 어떻게 작동하며, 어떤 상황에서 사용되나요?** A: Z-score Standardization은 데이터에서 평균을 빼고 표준편차로 나누어 데이터를 평균 0, 표준편차 1을 가지도록 조정합니다. `(x - mean(x)) / std(x)` 공식을 사용합니다. 이는 데이터의 분포가 정규 분포를 따를 때 효과적이며, 이상치에 덜 민감하여 모델의 성능을 향상시키는 데 자주 사용됩니다.

**Q4: 문자열 정규화(`str.normalize`)는 왜 필요하며, 어떤 종류가 있나요?** A: 문자열 정규화는 텍스트 데이터에서 동일한 의미를 가지지만 표현 방식이 다른 문자열들을 통일하는 과정입니다. 예를 들어, 유니코드 문자열에서 결합 문자(combining characters)를 표준 형태로 변환하거나, 대소문자 통일, 공백 제거 등을 포함합니다. 이는 텍스트 분석에서 데이터의 일관성을 확보하고 정확한 비교를 가능하게 합니다.

**Q5: 새 돌판에 십계명을 다시 받은 사건이 정규화와 표준화와 어떤 영적 의미로 연결될 수 있을까요?** A: 새 돌판에 십계명을 다시 받은 것은 깨어진 언약이 갱신되고, 하나님의 변치 않는 말씀이 다시 확증되는 사건입니다. 정규화와 표준화는 데이터의 스케일을 조정하여 본질적인 특성을 유지하면서도, 분석에 적합한 새로운 관점으로 데이터를 바라보는 것과 같습니다. 이는 하나님의 말씀의 불변성과 회복의 은혜를 데이터적으로 묵상하게 합니다.

### ✅ 체크리스트

**성경 이해 체크:**

- [ ] 출애굽기 34장의 새 돌판과 언약 갱신의 의미 이해
- [ ] 요한복음 1장의 은혜 위에 은혜 말씀의 풍성함 이해
- [ ] 데이터 스케일 조정을 통해 하나님의 변치 않는 말씀과 풍성한 은혜를 이해

**DataFrame 기초 체크:**

- [ ] Min-Max Scaling을 통한 정규화 구현 성공
- [ ] Z-score Standardization을 통한 표준화 구현 성공
- [ ] `str.normalize()`를 이용한 문자열 정규화 개념 이해
- [ ] `df.min()`, `df.max()`, `df.mean()`, `df.std()` 등 통계 함수 활용

**영적 적용 체크:**

- [ ] 내 삶의 영적 성장 데이터를 정규화하고 표준화하여 분석 시도 완료
- [ ] 나의 생각과 행동이 주님의 기준에 맞게 통일되어야 할 부분 점검 시도 완료
- [ ] 정규화와 표준화 원리를 통해 영적 분별력과 지혜로운 의사결정 노력

**발견 기록 체크:**

- [ ] 정규화(Min-Max Scaling)를 통한 새 돌판의 통일된 기준 확인
- [ ] 표준화(Z-score Standardization)를 통한 은혜 위에 은혜의 분포 통일 통찰
- [ ] 문자열 정규화가 말씀의 본질을 흐리지 않는 지혜임을 확인

---

## 🧠 미니 퀴즈

**1. 데이터를 특정 범위(예: 0~1)로 조정하여 모든 특성이 동일한 스케일을 가지도록 하는 기법은?**
a) 표준화
b) 정규화
c) 스케일링

**2. 데이터를 평균 0, 표준편차 1을 가지도록 조정하여 데이터의 분포를 통일하는 기법은?**
a) 정규화
b) 표준화
c) Min-Max Scaling

**3. 텍스트 데이터에서 동일한 의미를 가지지만 표현 방식이 다른 문자열들을 통일하는 과정은?**
a) 문자열 인코딩
b) 문자열 파싱
c) 문자열 정규화

**4. 새 돌판에 십계명을 다시 받은 사건이 정규화와 표준화와 연결되는 영적 의미로 가장 적절한 것은?**
a) 데이터의 스케일을 조정하여 본질적인 특성을 유지하면서 새로운 관점으로 데이터를 바라봄
b) 데이터의 양을 늘려 하나님의 풍성함을 표현
c) 데이터의 시각적 아름다움을 강조하여 사람들의 관심을 유도

**5. 은혜 위에 은혜 말씀이 정규화와 표준화와 연결되는 영적 의미로 가장 적절하지 않은 것은?**
a) 데이터의 특성을 통일하여 모델이 더 많은 정보를 효과적으로 받아들임
b) 모델의 성능을 향상시키고 더 깊은 통찰을 얻음
c) 데이터의 불필요한 부분을 제거하여 분석을 단순화함

_(정답: 1-b, 2-b, 3-c, 4-a, 5-c)_

---

## 🎯 깊이 탐구 과제 (선택)

### 초급 과제

1.  **성경 인물 특성 정규화**: 성경 인물 데이터(이름, 나이, 영향력 점수)를 만들고, `나이`와 `영향력 점수`를 Min-Max Scaling으로 정규화해보기
2.  **성경 구절 길이 표준화**: 성경 구절 데이터(구절 ID, 내용, 글자 수)를 만들고, `글자 수`를 Z-score Standardization으로 표준화해보기

### 중급 과제

1.  **교회 봉사자 헌신도 스케일 조정**: 가상의 교회 봉사자 데이터(봉사자 ID, 봉사 시간, 헌신도 점수)를 만들고, `봉사 시간`과 `헌신도 점수`를 각각 정규화와 표준화하여 두 지표의 상대적인 중요도를 비교 분석해보기
2.  **영적 성장 지표 문자열 통일**: 개인의 영적 성장 지표(예: 영적 상태 평가 - '좋음', 'Good', 'good') 데이터를 만들고, `str.normalize()`와 `str.lower()` 등을 사용하여 문자열을 통일해보기

### 고급 과제

1.  **텍스트 데이터 전처리 파이프라인 설계**: 성경 텍스트 데이터(구절 ID, 내용)를 대상으로 `str.normalize()`를 포함한 문자열 정규화, 불용어 제거, 표제어 추출 등을 포함하는 텍스트 전처리 파이프라인을 구축하여 텍스트 분석의 정확도를 높이는 시스템(개념) 설계해보기
2.  **다중 특성 스케일 조정 및 모델 성능 비교**: 가상의 데이터셋(다양한 스케일의 숫자형 특성 포함)을 만들고, 정규화와 표준화를 각각 적용한 후 머신러닝 모델(예: 로지스틱 회귀)을 학습시켜 모델 성능(정확도)을 비교 분석하는 보고서 작성해보기

---

## 🌟 다음 여정 예고

**Chapter 35: "자원 봉헌 - IO 확장 (Offering of Resources - IO Extension)"**

이스라엘 백성이 성막 건축을 위해 자원하여 예물을 봉헌했듯이, 데이터 분석에서도 다양한 형식의 데이터를 효율적으로 읽고 쓰는(IO) 것은 데이터의 활용도를 높이고 분석 파이프라인을 확장하는 데 필수적입니다.

Just as the Israelites voluntarily offered gifts for the construction of the Tabernacle, in data analysis, efficiently reading and writing data in various formats (IO) is essential for enhancing data usability and extending analytical pipelines.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `to_csv()`, `read_csv()`: CSV 파일 입출력
🔍 `to_parquet()`, `read_parquet()`: Parquet 파일 입출력
🎯 `to_excel()`, `read_excel()`: Excel 파일 입출력
📊 자원 봉헌처럼 다양한 형식의 데이터를 효율적으로 다루어 데이터 분석 파이프라인을 확장하는 전략

"이스라엘 자손이 여호와께 드리는 예물은 이러하니 곧 금과 은과 놋과" (출애굽기 35:5)
"여기 한 아이가 있어 보리떡 다섯 개와 물고기 두 마리를 가졌나이다 그러나 이것이 이 많은 사람에게 얼마나 되겠사옵나이까" (요한복음 6:9)

---

## 🙏 한 줄 기도

_"주님, 새 돌판처럼 저의 마음을 새롭게 하시고, 정규화와 표준화 전략을 통해 저의 삶의 모든 영역이 주님의 기준에 맞게 통일되게 하소서.
데이터의 특성을 통일하고 모델의 성능을 향상시키는 과정을 통해 주님의 변치 않는 말씀과 풍성한 은혜를 더욱 깊이 깨닫게 하소서. 예수님의 이름으로 기도합니다. 아멘."_

---

**🎊 서른네 번째 광야 여정을 완주하신 것을 축하합니다!**

_"여호와께서 모세에게 이르시되 너는 돌판 둘을 처음 것과 같이 깎아 만들라 네가 깨뜨린 처음 판에 쓴 말을 내가 그 판에 쓰리라" (출애굽기 34:1)_

여러분은 이제 데이터 속에서 정규화(Min-Max Scaling), 표준화(Z-score Standardization), 문자열 정규화(`str.normalize`)를 통해 데이터의 스케일을 조정하고 특성을 통일하는 방법을 알게 되었습니다. 주님께서 주신 지혜로 모든 데이터 속에서 하나님의 공의와 은혜의 원리를 발견하시길 기도합니다.

**다음 여정에서 만나요! 🌈**
