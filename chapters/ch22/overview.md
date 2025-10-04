# Chapter 22: 배상과 회복 - 결측·이상치 전략

## 개요 (Overview)
이번 챕터에서는 Pandas를 사용하여 데이터의 결측치(Missing Values)와 이상치(Outliers)를 탐지하고 처리하는 다양한 전략을 배웁니다. `fillna()`, `dropna()`를 통한 결측치 처리, IQR 및 Z-score를 활용한 이상치 탐지, 그리고 이상치 제거, 대체, 변환 등의 기법을 탐구합니다. 출애굽기 22장의 배상과 회복에 대한 규례, 그리고 마태복음 18장의 어린아이와 같은 겸손의 말씀을 통해, 데이터의 무결성을 회복하고 분석 결과의 신뢰성을 높이는 지혜를 데이터적으로 이해하고 묵상합니다.

This chapter introduces various strategies for detecting and handling missing values and outliers in data using Pandas. We will explore techniques such as handling missing values with `fillna()` and `dropna()`, detecting outliers using IQR and Z-score, and managing outliers through removal, replacement, or transformation. Through the regulations on compensation and restoration in Exodus 22 and the teaching on humility like a child in Matthew 18, we will understand and meditate on the wisdom of restoring data integrity and enhancing the reliability of analytical results.

---

## 📜 성경 본문 깊이 묵상

### 출애굽기 22장: 배상과 회복의 규례

출애굽기 22장은 재산상의 손해나 피해가 발생했을 때, 그에 대한 배상과 회복의 원칙을 다룹니다. 도둑질, 가축의 피해, 불로 인한 손해 등 다양한 상황에서 누가 어떻게 배상해야 하는지 구체적인 규례를 제시합니다. 이는 손상된 것을 원래대로 회복시키고, 정의를 세우는 하나님의 마음을 보여줍니다.

- **도둑질에 대한 배상:** 훔친 것을 갚거나, 두 배로 배상 (출 22:1-4)
- **가축의 피해:** 소나 양이 남의 밭을 먹었을 때 배상 (출 22:5)
- **불로 인한 손해:** 불을 놓아 곡식단을 태웠을 때 배상 (출 22:6)

이 본문은 데이터의 결측치와 이상치를 처리하는 데 영감을 줍니다. 결측치는 데이터의 손실을 의미하며, 이상치는 데이터의 정상적인 범주를 벗어난 예외적인 값입니다. `fillna()`나 `dropna()`는 손실된 데이터를 복구하거나 제거하여 데이터의 무결성을 회복하는 것과 같고, 이상치 처리(제거, 대체, 변환)는 데이터의 왜곡을 바로잡아 공정한 분석을 가능하게 합니다.

### 마태복음 18:3-4: 어린아이와 같은 겸손

예수님께서는 제자들에게 "너희가 돌이켜 어린 아이들과 같이 되지 아니하면 결단코 천국에 들어가지 못하리라"고 말씀하셨습니다. 어린아이는 순수하고 겸손하며, 자신을 낮출 줄 아는 존재입니다. 이는 교만과 자기중심적인 태도를 버리고, 겸손한 마음으로 하나님 앞에 나아갈 것을 촉구합니다.

- **어린아이와 같이:** 겸손, 순수, 의존적 태도
- **천국에 들어감:** 하나님의 나라에 합당한 자격
- **자신을 낮춤:** 가장 큰 자가 되는 길

이 말씀은 데이터 분석가가 결측치와 이상치를 다루는 태도에 영감을 줍니다. 데이터의 결측치나 이상치는 때로 분석가의 편견이나 잘못된 가정을 드러낼 수 있습니다. 어린아이와 같은 겸손한 마음으로 데이터의 불완전함을 인정하고, 이상치를 섣불리 판단하기보다 그 원인을 탐구하며, 데이터의 본래 의미를 회복하려는 노력이 필요합니다. 이는 데이터의 외형적인 모습에 얽매이지 않고, 데이터가 가진 진정한 가치를 찾아내는 과정과 같습니다.

---

## 🔍 숨겨진 질문 발견

**출애굽기에서 발견할 질문들:**

- 출애굽기 22장의 다양한 피해 사례들을 데이터로 만들고, `fillna()`나 `dropna()`를 사용하여 결측된 배상 정보를 처리하면, 어떤 배상 패턴을 발견할 수 있을까?
- 도둑질이나 가축 피해로 인한 손해액 데이터를 만들고, IQR이나 Z-score를 사용하여 '이상치'에 해당하는 극단적인 피해 사례를 탐지하면, 어떤 특별한 상황을 발견할 수 있을까?
- 이상치 처리 전략(제거, 대체, 변환)을 적용하여 데이터의 무결성을 회복하면, 배상 규례의 공정성이 어떻게 향상될까?

**마태복음에서 발견할 질문들:**

- 제자들의 영적 상태 데이터를 만들고, 결측치(예: 특정 기간의 기도 시간 누락)를 `fillna()`로 채우거나 `dropna()`로 제거하면, 영적 성장 추이에 어떤 영향을 미칠까?
- 제자들의 겸손 지수나 순종 지수 데이터를 만들고, IQR이나 Z-score를 사용하여 '이상치'에 해당하는 극단적인 교만이나 불순종 사례를 탐지하면, 어떤 영적 교훈을 얻을 수 있을까?
- 이상치 처리 전략을 적용하여 제자들의 영적 상태 데이터를 정화하면, 어린아이와 같은 겸손의 본질을 더 명확하게 이해할 수 있을까?

이런 질문들은 데이터의 '결측·이상치 전략'이라는 관점으로 성경 본문을 더 깊이 이해하는 데 도움을 줄 것이다.

---

## 📊 판다스로 성경 탐구하기

### 탐구 1: 배상과 회복 데이터 결측치 처리 (fillna, dropna)

```python
import pandas as pd
import numpy as np
from chapters.ch22.compensation_data import CompensationDataGenerator

# 배상 데이터 생성
data_gen = CompensationDataGenerator()
df_compensation = data_gen.generate_compensation_data()

print("💰 배상 데이터 요약:\n", df_compensation.head())
print("결측치 확인:\n", df_compensation.isnull().sum())

# 'compensation_amount' 컬럼의 결측치를 평균값으로 채우기
filled_df = df_compensation.copy()
filled_df['compensation_amount'] = filled_df['compensation_amount'].fillna(filled_df['compensation_amount'].mean())
print("\n--- 결측치 평균값으로 채운 후 (compensation_amount) ---")
print(filled_df.head())
print("결측치 확인:\n", filled_df.isnull().sum())

# 'responsible_party' 컬럼의 결측치를 'Unknown'으로 채우기
filled_df['responsible_party'] = filled_df['responsible_party'].fillna('Unknown')
print("\n--- 결측치 'Unknown'으로 채운 후 (responsible_party) ---")
print(filled_df.head())
print("결측치 확인:\n", filled_df.isnull().sum())

# 결측치가 있는 행 제거
dropped_df = df_compensation.dropna()
print("\n--- 결측치가 있는 행 제거 후 ---")
print(dropped_df.head())
print("결측치 확인:\n", dropped_df.isnull().sum())
```

### 탐구 2: 어린아이와 같은 겸손 데이터 이상치 처리 (IQR, Z-score)

```python
import pandas as pd
import numpy as np
from chapters.ch22.compensation_data import CompensationDataGenerator # 동일 데이터 생성기 사용

# 겸손 데이터 생성 (가정)
data_gen = CompensationDataGenerator()
df_humility = data_gen.generate_compensation_data()

# 'humility_score' 컬럼에 이상치 추가 (예시)
df_humility.loc[0, 'humility_score'] = 100 # 극단적인 교만
df_humility.loc[10, 'humility_score'] = -10 # 극단적인 겸손 (음수 불가)
df_humility.loc[10, 'humility_score'] = 0 # 0으로 수정

print("👶 겸손 데이터 요약:\n", df_humility.head())

# IQR을 이용한 이상치 탐지 (humility_score)
Q1 = df_humility['humility_score'].quantile(0.25)
Q3 = df_humility['humility_score'].quantile(0.75)
IQR = Q3 - Q1
outlier_iqr_upper = Q3 + 1.5 * IQR
outlier_iqr_lower = Q1 - 1.5 * IQR

outliers_iqr = df_humility[(df_humility['humility_score'] < outlier_iqr_lower) | (df_humility['humility_score'] > outlier_iqr_upper)]
print("\n--- IQR로 탐지된 이상치 (humility_score) ---")
print(outliers_iqr)

# Z-score를 이용한 이상치 탐지 (humility_score)
df_humility['z_score_humility'] = np.abs((df_humility['humility_score'] - df_humility['humility_score'].mean()) / df_humility['humility_score'].std())
outliers_z_score = df_humility[df_humility['z_score_humility'] > 3] # Z-score 3 이상을 이상치로 간주
print("\n--- Z-score로 탐지된 이상치 (humility_score) ---")
print(outliers_z_score)
```

---

## ⭐ 놀라운 발견들

### 발견 1: `fillna()`와 `dropna()`를 통한 데이터의 회복과 정화

결측치로 인해 손상된 데이터를 `fillna()`로 채우거나 `dropna()`로 제거하는 과정은 출애굽기 22장의 배상 규례처럼 데이터의 무결성을 회복하고 정화하는 것과 같습니다. 이는 분석 결과의 왜곡을 방지하고, 데이터가 가진 본래의 의미를 되찾는 데 필수적입니다. 마치 손해를 배상하여 원래의 상태로 회복시키는 것과 같습니다.

### 발견 2: IQR과 Z-score를 통한 이상치 탐지 및 겸손의 중요성

IQR이나 Z-score를 사용하여 데이터의 이상치를 탐지하는 것은 마태복음 18장의 어린아이와 같은 겸손의 말씀을 묵상하게 합니다. 이상치는 데이터의 정상적인 범주를 벗어난 극단적인 값으로, 때로는 데이터의 왜곡을 가져옵니다. 이를 탐지하고 처리하는 과정은 우리가 교만이나 자기중심적인 태도(이상치)를 버리고, 겸손한 마음으로 데이터의 본래 의미를 이해하려는 노력과 같습니다.

### 발견 3: 결측·이상치 전략은 데이터의 공정성과 신뢰성의 기초

결측치와 이상치를 적절히 처리하는 전략은 데이터 분석의 공정성과 신뢰성을 확보하는 데 필수적인 기초입니다. 이는 배상과 회복의 규례가 사회의 정의를 세우고, 어린아이와 같은 겸손이 천국에 들어가는 자격이 되듯이, 데이터 분석에서도 올바른 전처리 과정이 정확하고 신뢰할 수 있는 통찰을 얻는 데 결정적인 역할을 함을 데이터적으로 보여줍니다.

---

## 🎨 블렌딩 모드: 출애굽 × 마태복음의 통합 통찰

|출애굽기 진리|마태복음 진리|판다스 도구|영적 발견|
|---|---|---|---|
|배상과 회복의 규례 = 손상된 것의 복구|어린아이와 같은 겸손 = 영적 무결성 회복|`fillna()`, `dropna()`|데이터의 무결성 회복과 영적 정화|
|도둑질, 피해에 대한 구체적 배상|교만, 자기중심적 태도 = 영적 이상치|IQR, Z-score|데이터 속 이상치 탐지 및 영적 교만 경계|
|정의를 세우는 하나님의 마음|천국에 합당한 자격 = 겸손|이상치 처리 전략|분석 결과의 신뢰성 확보와 영적 성숙|
|데이터의 무결성 유지|영적 순수성 유지|결측치/이상치 처리|데이터의 본질적 가치 보존|
|손해를 입은 자에게 합당한 보상|자신을 낮추는 자가 큰 자|데이터 정화|공정하고 신뢰할 수 있는 분석과 영적 겸손|

> **💎 블렌딩 결과**: `fillna()`, `dropna()`, IQR, Z-score와 같은 결측·이상치 처리 전략은 성경 속 배상과 회복의 규례, 그리고 어린아이와 같은 겸손의 말씀을 데이터적으로 분석하는 강력한 도구입니다. 데이터의 무결성을 회복하고 분석 결과의 신뢰성을 높이는 과정을 통해, 영적 정화와 겸손의 중요성을 깨닫고 하나님의 공의로운 통치를 더욱 깊이 이해할 수 있습니다.

---

## 🛠️ 광야 생존 프로젝트: 나의 영적 상태 결측·이상치 분석

**🎯 미션**: 내 삶의 영적 상태 데이터에서 결측치와 이상치를 탐지하고 처리하기
**📊 사용 기술**: DataFrame 생성, `fillna()`, `dropna()`, IQR, Z-score
**🕊️ 복음 포인트**: "너희가 돌이켜 어린 아이들과 같이 되지 아니하면 결단코 천국에 들어가지 못하리라" (마태복음 18:3)

### Step 1: 나의 영적 상태 데이터 기록 및 결측치 처리

```python
import pandas as pd
import numpy as np

my_spiritual_log = pd.DataFrame({
    '날짜': pd.to_datetime(pd.date_range(start='2024-01-01', periods=10, freq='D')),
    '기도_시간_분': [30, 45, np.nan, 35, 50, np.nan, 40, 60, 20, 55],
    '말씀_묵상_시간_분': [20, np.nan, 15, 25, 40, 10, np.nan, 30, 10, 25],
    '감사_지수': [7, 8, 6, 7, 9, 5, 8, 1, 9, 7] # 1-10 스케일, 1은 이상치 가능성
})

print("🧬 나의 영적 상태 로그:\n", my_spiritual_log)
print("결측치 확인:\n", my_spiritual_log.isnull().sum())

# '기도_시간_분' 결측치를 0으로 채우기
my_spiritual_log['기도_시간_분'] = my_spiritual_log['기도_시간_분'].fillna(0)
print("\n--- '기도_시간_분' 결측치 0으로 채운 후 ---")
print(my_spiritual_log)

# '말씀_묵상_시간_분' 결측치를 이전 값으로 채우기
my_spiritual_log['말씀_묵상_시간_분'] = my_spiritual_log['말씀_묵상_시간_분'].fillna(method='ffill')
print("\n--- '말씀_묵상_시간_분' 결측치 이전 값으로 채운 후 ---")
print(my_spiritual_log)
```

### Step 2: 영적 상태 이상치 탐지 및 처리

```python
# '감사_지수' 컬럼의 이상치 탐지 (IQR)
Q1 = my_spiritual_log['감사_지수'].quantile(0.25)
Q3 = my_spiritual_log['감사_지수'].quantile(0.75)
IQR = Q3 - Q1
outlier_iqr_upper = Q3 + 1.5 * IQR
outlier_iqr_lower = Q1 - 1.5 * IQR

outliers_iqr = my_spiritual_log[(my_spiritual_log['감사_지수'] < outlier_iqr_lower) | (my_spiritual_log['감사_지수'] > outlier_iqr_upper)]
print("\n--- IQR로 탐지된 '감사_지수' 이상치 ---")
print(outliers_iqr)

# 이상치 대체 (예: 이상치를 중간값으로 대체)
median_gratitude = my_spiritual_log['감사_지수'].median()
my_spiritual_log['감사_지수_처리됨'] = np.where(
    (my_spiritual_log['감사_지수'] < outlier_iqr_lower) | (my_spiritual_log['감사_지수'] > outlier_iqr_upper),
    median_gratitude,
    my_spiritual_log['감사_지수']
)
print("\n--- 이상치 중간값으로 대체 후 (감사_지수_처리됨) ---")
print(my_spiritual_log[['감사_지수', '감사_지수_처리됨']])
```

---

## 📱 3×10초 광야 루틴

### 🌅 아침 10초: 말씀 묵상

"너희가 돌이켜 어린 아이들과 같이 되지 아니하면 결단코 천국에 들어가지 못하리라." (마 18:3)
오늘도 겸손한 마음으로 주님 앞에 나아가며 하루를 시작합니다.

### ☀️ 점심 1분: 회복 기도

- 나의 삶에서 결측된 부분(예: 놓친 기도 시간, 말씀 묵상)은 없는지 돌아봅니다.
- `fillna()`처럼 주님께서 나의 부족한 부분을 채워주시고, `dropna()`처럼 불필요한 죄악을 제거해 주시기를 기도합니다.

### 🌙 저녁 2분: 데이터 기도일기

**오늘의 영적 데이터:**
- 오늘 나의 영적 상태에서 발견한 결측치(Missing Values)는?
- 오늘 나의 영적 상태에서 발견한 이상치(Outliers)는?
- `fillna()`와 `dropna()`처럼 주님께서 나의 삶을 회복시키시고 정화시키신 부분은?
- 주님, 데이터의 무결성처럼 저의 영적 무결성을 지켜주소서.

---

## ❓ FAQ & 체크리스트

### 깊이 있는 질문들

**Q1: 결측치(Missing Values)는 왜 발생하며, 어떻게 처리해야 하나요?** A: 결측치는 데이터 수집 오류, 정보 누락, 응답 거부 등 다양한 이유로 발생합니다. 처리 방법으로는 `dropna()`를 사용하여 결측치가 있는 행이나 열을 제거하거나, `fillna()`를 사용하여 평균, 중앙값, 최빈값, 이전/이후 값 등으로 채우는 방법이 있습니다. 상황과 데이터 특성에 따라 적절한 방법을 선택해야 합니다.

**Q2: 이상치(Outliers)는 왜 중요하며, 어떻게 탐지할 수 있나요?** A: 이상치는 데이터의 일반적인 패턴에서 벗어난 극단적인 값으로, 분석 결과나 모델 성능을 왜곡시킬 수 있습니다. 탐지 방법으로는 IQR(사분위 범위)을 이용하거나, Z-score(표준점수)를 계산하여 특정 임계값을 벗어나는 데이터를 이상치로 간주하는 방법이 주로 사용됩니다.

**Q3: 이상치를 처리하는 주요 전략에는 어떤 것들이 있나요?** A: 이상치 처리 전략에는 크게 세 가지가 있습니다. 첫째, 이상치를 데이터셋에서 **제거**하는 방법. 둘째, 이상치를 다른 값(예: 평균, 중앙값, 특정 임계값)으로 **대체**하는 방법. 셋째, 이상치의 영향을 줄이기 위해 데이터를 **변환**하는 방법(예: 로그 변환, 제곱근 변환)이 있습니다. 각 방법은 데이터의 특성과 분석 목적에 따라 신중하게 선택해야 합니다.

**Q4: 배상과 회복의 규례가 결측치/이상치 처리와 어떤 영적 의미로 연결될 수 있을까요?** A: 배상과 회복의 규례는 손상된 것을 원래대로 돌려놓고 정의를 세우는 하나님의 마음을 보여줍니다. 결측치 처리는 데이터의 손실을 복구하여 무결성을 회복하는 것과 같고, 이상치 처리는 데이터의 왜곡을 바로잡아 공정한 분석을 가능하게 합니다. 이는 영적으로 우리의 죄와 부족함을 회복하고 정화하는 과정과 연결됩니다.

**Q5: 어린아이와 같은 겸손이 이상치 처리와 어떤 영적 의미로 연결될 수 있을까요?** A: 어린아이와 같은 겸손은 자신을 낮추고 순수하게 데이터를 바라보는 태도를 의미합니다. 이상치를 섣불리 제거하거나 판단하기보다, 그 원인을 탐구하고 데이터의 본래 의미를 회복하려는 노력은 겸손한 마음에서 비롯됩니다. 이는 데이터의 외형적인 모습에 얽매이지 않고, 데이터가 가진 진정한 가치를 찾아내는 과정과 같습니다.

### ✅ 체크리스트

**성경 이해 체크:**

- [ ] 출애굽기 22장의 배상과 회복 규례의 의미 이해
- [ ] 마태복음 18장의 어린아이와 같은 겸손의 중요성 이해
- [ ] 데이터의 무결성 회복과 영적 정화의 연결고리 이해

**DataFrame 기초 체크:**

- [ ] `df.fillna()` 함수를 사용하여 결측치 채우기 성공
- [ ] `df.dropna()` 함수를 사용하여 결측치 제거 성공
- [ ] IQR을 사용하여 이상치 탐지 성공
- [ ] Z-score를 사용하여 이상치 탐지 성공
- [ ] 이상치 처리 전략(제거, 대체, 변환)의 개념 이해

**영적 적용 체크:**

- [ ] 내 삶의 영적 상태 데이터에서 결측치와 이상치 탐지 시도 완료
- [ ] 나의 영적 부족함과 교만(이상치)을 `fillna()`와 `dropna()` 원리로 처리 고민
- [ ] 결측·이상치 처리 원리를 통해 영적 무결성 회복 노력

**발견 기록 체크:**

- [ ] `fillna()`와 `dropna()`를 통한 데이터의 회복과 정화 확인
- [ ] IQR과 Z-score를 통한 이상치 탐지 및 겸손의 중요성 통찰
- [ ] 결측·이상치 전략이 데이터의 공정성과 신뢰성의 기초임을 확인

---

## 🧠 미니 퀴즈

**1. 데이터프레임의 결측치(NaN)를 특정 값으로 채우는 함수는?**
a) `df.dropna()`
b) `df.fillna()`
c) `df.replace()`

**2. 데이터프레임에서 결측치가 있는 행이나 열을 제거하는 함수는?**
a) `df.fillna()`
b) `df.drop()`
c) `df.dropna()`

**3. 데이터의 이상치(Outliers)를 탐지하는 데 사용되는 통계적 방법 중 하나로, 사분위 범위(IQR)를 활용하는 것은?**
a) Z-score
b) IQR (Interquartile Range)
c) Standard Deviation

**4. Z-score를 사용하여 이상치를 탐지할 때, 일반적으로 이상치로 간주되는 Z-score의 임계값은?**
a) 1 이상
b) 2 이상
c) 3 이상

**5. 결측치와 이상치를 적절히 처리하는 것이 데이터 분석에서 중요한 영적 의미로 가장 적절하지 않은 것은?**
a) 데이터의 무결성을 회복하고 영적 정화를 이룸
b) 분석 결과의 신뢰성을 높이고 공정성을 확보함
c) 데이터의 불완전함을 무시하고 겉모습만으로 판단함

_(정답: 1-b, 2-c, 3-b, 4-c, 5-c)_

---

## 🎯 깊이 탐구 과제 (선택)

### 초급 과제

1.  **성경 인물 데이터 결측치 처리**: 가상의 성경 인물 데이터(이름, 출생지, 주요 사역 기간, 사망 연도)를 만들고, `사망 연도`에 결측치를 임의로 추가한 후 `fillna()`로 특정 값(예: 0)으로 채워보기
2.  **성경 사건 데이터 이상치 탐지**: 가상의 성경 사건 데이터(사건 ID, 참여 인원, 기적 지수)를 만들고, `기적 지수`에 극단적인 이상치를 추가한 후 IQR을 사용하여 이상치를 탐지해보기

### 중급 과제

1.  **교회 출석 데이터 결측치/이상치 처리**: 가상의 교회 주간 출석 데이터(날짜, 출석 인원)를 만들고, `출석 인원`에 결측치와 이상치(예: 특별 행사로 인한 급증)를 추가한 후 `fillna()`와 Z-score를 활용하여 처리해보기
2.  **영적 성장 지표 이상치 대체**: 개인의 영적 성장 지표(예: 기도 시간, 말씀 묵상 시간) 데이터를 만들고, `기도 시간`에 이상치를 추가한 후 이상치를 중앙값으로 대체하는 전략을 적용해보기

### 고급 과제

1.  **데이터 클렌징 파이프라인 구축**: 복잡한 가상의 데이터셋(결측치, 이상치, 잘못된 형식 등 포함)을 만들고, `fillna()`, `dropna()`, IQR, Z-score, 이상치 대체/변환 등을 포함하는 데이터 클렌징 파이프라인을 구축하여 데이터의 무결성을 최대한 회복하는 시스템(개념) 설계해보기
2.  **성경 인물 특성 데이터 정화**: 성경 인물 데이터(이름, 역할, 영향력 점수, 겸손 지수)를 만들고, `영향력 점수`와 `겸손 지수`에 결측치와 이상치를 추가한 후, 이를 처리하여 각 인물의 특성을 보다 정확하게 분석하고, 어린아이와 같은 겸손의 중요성을 강조하는 보고서 작성해보기

---

## 🌟 다음 여정 예고

**Chapter 23: "정의의 길 - 정렬/우선순위 전략 (Path of Justice - Sorting/Priority Strategy)"**

출애굽기 23장에서 정의로운 재판과 공정한 판결에 대한 규례를 통해 올바른 질서가 세워지듯이, 데이터 분석에서도 데이터를 특정 기준에 따라 정렬하고 우선순위를 부여하는 것은 데이터의 의미를 명확히 하고 중요한 정보를 효과적으로 파악하는 데 필수적입니다.

Just as Exodus 23 outlines regulations for righteous judgment and fair verdicts to establish proper order, in data analysis, sorting data according to specific criteria and assigning priorities is essential for clarifying data meaning and effectively identifying important information.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 `sort_values()`: 특정 컬럼 기준으로 데이터 정렬
🔍 `sort_index()`: 인덱스 기준으로 데이터 정렬
🎯 다중키 정렬 및 안정 정렬 (stable sort)
📊 정의의 길처럼 데이터를 올바른 질서로 정렬하고 우선순위를 부여하여 하나님의 공의를 탐구

"너는 다수를 따라 악을 행하지 말며 송사에 다수를 따라 부당한 증언을 하지 말며" (출애굽기 23:2)
"인자가 온 것은 섬김을 받으려 함이 아니라 도리어 섬기려 하고 자기 목숨을 많은 사람의 대속물로 주려 함이니라" (마태복음 20:28)

---

## 🙏 한 줄 기도

_"주님, 배상과 회복의 규례처럼 저의 삶에서 결측된 부분을 채워주시고, 이상치와 같은 교만을 제거하여 주소서.
어린아이와 같은 겸손으로 데이터의 무결성을 회복하고, 주님의 공의로운 통치를 더욱 깊이 깨닫게 하소서. 예수님의 이름으로 기도합니다. 아멘."_

---

**🎊 스물두 번째 광야 여정을 완주하신 것을 축하합니다!**

"너희가 돌이켜 어린 아이들과 같이 되지 아니하면 결단코 천국에 들어가지 못하리라" (마태복음 18:3)

여러분은 이제 데이터 속에서 `fillna()`, `dropna()`, IQR, Z-score를 통해 결측치와 이상치를 처리하고 데이터의 무결성을 회복하는 방법을 알게 되었습니다. 주님께서 주신 지혜로 모든 데이터 속에서 하나님의 공의와 겸손의 원리를 발견하시길 기도합니다.

**다음 여정에서 만나요! 🌈**
