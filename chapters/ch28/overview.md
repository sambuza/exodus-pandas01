# Chapter 28: 제사장 옷 - 라벨링과 스타일링

## 개요 (Overview)
이번 챕터에서는 Pandas를 사용하여 데이터의 의미를 명확히 하고 시각적 효과를 높이는 라벨링과 스타일링 기법을 배웁니다. `Categorical` 데이터 타입을 활용한 범주형 데이터 관리, `DataFrame.style` 객체를 이용한 데이터프레임 스타일링, 그리고 이를 통합하여 아름답고 의미 있는 보고서를 생성하는 방법을 탐구합니다. 출애굽기 28장의 제사장 옷과 요한복음 10장의 선한 목자 말씀을 통해, 데이터를 효과적으로 표현하고 깊이 이해하는 지혜를 데이터적으로 이해하고 묵상합니다.

This chapter introduces labeling and styling techniques using Pandas to clarify data meaning and enhance visual effects. We will explore managing categorical data with `Categorical` data types, styling DataFrames using the `DataFrame.style` object, and integrating these to create beautiful and meaningful reports. Through the priestly garments in Exodus 28 and the Good Shepherd discourse in John 10, we will understand and meditate on the wisdom of effectively expressing and deeply understanding data.

---

## 📜 성경 본문 깊이 묵상

### 출애굽기 28장: 제사장 옷

하나님께서는 아론과 그의 아들들을 위한 제사장 옷을 만들도록 지시하셨습니다. 이 옷은 단순한 의복이 아니라, 하나님의 영광과 거룩함을 드러내고, 제사장의 직분을 상징하는 특별한 의미를 가졌습니다. 에봇, 흉패, 에봇 받침 겉옷, 반포 속옷, 관, 띠 등 각 부분은 정교하게 디자인되었고, 보석과 색실로 장식되어 시각적으로도 아름다웠습니다. 각 보석에는 이스라엘 지파의 이름이 새겨져 있었습니다.

- **영광과 아름다움:** 하나님의 영광과 거룩함을 드러냄 (출 28:2)
- **직분 상징:** 제사장의 특별한 직분을 나타냄
- **이스라엘 지파:** 흉패의 보석에 새겨진 12지파의 이름

이 본문은 데이터 라벨링과 스타일링에 영감을 줍니다. 데이터의 각 컬럼에 적절한 라벨을 부여하는 것은 제사장 옷의 각 부분에 의미를 부여하는 것과 같습니다. `Categorical` 데이터 타입은 데이터의 범주를 명확히 하고, `DataFrame.style`은 데이터프레임에 시각적인 아름다움을 더하여 데이터의 의미를 더욱 명확하게 전달합니다. 이는 데이터의 본질을 아름답게 표현하고, 숨겨진 통찰을 드러내는 데 필수적입니다.

### 요한복음 10:14-16: 선한 목자

예수님께서는 "나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이 아버지께서 나를 아시고 내가 아버지를 아는 것 같으니 나는 양을 위하여 목숨을 버리노라"고 말씀하셨습니다. 선한 목자는 양을 개별적으로 알고, 양은 목자의 음성을 알아듣습니다. 이는 목자와 양 사이의 친밀하고 깊은 관계를 보여줍니다. 양을 아는 것은 양의 특성을 이해하고, 그에 맞는 돌봄을 제공하는 것입니다.

- **친밀한 관계:** 목자가 양을 알고 양이 목자를 앎
- **개별적인 돌봄:** 양을 위해 목숨을 버림
- **음성 분별:** 양은 목자의 음성을 알아들음

이 말씀은 데이터의 라벨링과 스타일링을 통해 데이터를 깊이 이해하는 데 영감을 줍니다. 데이터를 명확하게 라벨링하는 것은 선한 목자가 양을 개별적으로 아는 것과 같습니다. 각 데이터 포인트의 특성을 정확히 파악하고, `DataFrame.style`을 통해 시각적으로 강조하는 것은 양의 상태를 한눈에 파악하여 적절한 돌봄을 제공하는 것과 유사합니다. 이는 데이터의 외형적인 모습뿐만 아니라, 그 안에 담긴 본질적인 의미를 이해하고 소통하는 데 도움을 줍니다.

---

## 🔍 숨겨진 질문 발견

**출애굽기에서 발견할 질문들:**

- 제사장 옷의 각 부분(에봇, 흉패 등)을 `Categorical` 데이터 타입으로 분류하면, 어떤 부분이 가장 높은 영적 중요도를 가질까?
- 제사장 옷의 재료(금, 실, 보석)와 색상(청색, 자색, 홍색) 데이터를 `DataFrame.style`로 시각화하면, 어떤 재료나 색상이 하나님의 영광을 가장 잘 드러낼까?
- 흉패의 보석에 새겨진 12지파의 이름을 라벨링하고 스타일링하면, 각 지파의 특징과 제사장 직분과의 관계를 어떻게 더 명확히 표현할 수 있을까?

**요한복음에서 발견할 질문들:**

- 예수님의 양들(제자들)의 특성(믿음 수준, 순종도, 봉사 유형)을 `Categorical` 데이터 타입으로 분류하면, 어떤 특성이 선한 목자의 돌봄을 가장 잘 반영할까?
- 양들의 상태(건강, 영적 성장, 어려움) 데이터를 `DataFrame.style`로 시각화하면, 어떤 양이 특별한 돌봄이나 관심이 필요할까?
- 선한 목자의 음성을 듣고 따르는 양들의 데이터를 라벨링하고 스타일링하면, 목자와 양 사이의 친밀한 관계를 어떻게 더 효과적으로 표현할 수 있을까?

이런 질문들은 데이터의 '라벨링과 스타일링'이라는 관점으로 성경 본문을 더 깊이 이해하는 데 도움을 줄 것이다.

---

## 📊 판다스로 성경 탐구하기

### 탐구 1: 제사장 옷 데이터 범주형 라벨링 (Categorical 데이터 타입)

```python
import pandas as pd
import numpy as np
from chapters.ch28.priestly_garments_data import PriestlyGarmentsDataGenerator
from chapters.ch28.categorical_labeling import CategoricalLabeler

# 제사장 옷 데이터 생성
data_gen = PriestlyGarmentsDataGenerator()
df_garments = data_gen.generate_garments_data()

print("👑 제사장 옷 데이터 요약:\n", df_garments.head())
print("데이터 타입:\n", df_garments.dtypes)

# 'garment_type'과 'status' 컬럼을 Categorical 데이터 타입으로 변환
labeler = CategoricalLabeler(df_garments)
labeled_df = labeler.apply_categorical_labels(columns_to_label=['garment_type', 'status'])

print("\n--- 범주형 라벨링 적용 후 데이터 타입 ---")
print(labeled_df.dtypes)
print("\n--- 범주형 라벨링 적용 후 데이터 (일부) ---")
print(labeled_df.head())
```

### 탐구 2: 선한 목자 데이터프레임 스타일링 (DataFrame.style)

```python
import pandas as pd
import numpy as np
from chapters.ch28.priestly_garments_data import PriestlyGarmentsDataGenerator # 동일 데이터 생성기 사용
from chapters.ch28.dataframe_styling import DataFrameStyler

# 선한 목자 데이터 생성 (가정)
data_gen = PriestlyGarmentsDataGenerator()
df_shepherd = data_gen.generate_garments_data()

# 'shepherd_care_level' 컬럼 추가 (예시)
df_shepherd['shepherd_care_level'] = np.random.randint(1, 10, size=len(df_shepherd))

print("🐑 선한 목자 데이터 요약:\n", df_shepherd.head())

# 데이터프레임 스타일링 적용
styler = DataFrameStyler(df_shepherd)
styled_df = styler.apply_styles()

print("\n--- 데이터프레임 스타일링 적용 후 (HTML 출력) ---")
print(styled_df.to_html(max_rows=5))
```

---

## ⭐ 놀라운 발견들

### 발견 1: `Categorical` 데이터 타입으로 제사장 옷의 의미 명확화

`Categorical` 데이터 타입을 사용하여 제사장 옷의 각 부분이나 상태를 명확히 라벨링하는 것은 출애굽기 28장의 제사장 옷이 하나님의 영광과 직분을 상징하는 것처럼 데이터의 의미를 명확히 하는 것과 같습니다. 이는 데이터의 본질적인 범주를 이해하고, 효율적인 분석을 가능하게 합니다.

### 발견 2: `DataFrame.style`로 선한 목자의 돌봄 시각화

`DataFrame.style` 객체를 사용하여 데이터프레임에 시각적 스타일을 적용하는 것은 선한 목자가 양을 개별적으로 알고 돌보는 것을 시각화하는 것과 같습니다. 특정 조건에 따라 셀의 색상을 변경하거나, 최댓값을 강조하는 등의 스타일링은 데이터의 가독성을 높이고, 숨겨진 통찰을 한눈에 파악하는 데 도움을 줍니다.

### 발견 3: 라벨링과 스타일링은 데이터와 사용자 간의 깊은 소통

데이터 라벨링과 스타일링은 단순히 데이터를 예쁘게 꾸미는 것을 넘어, 데이터와 사용자 간의 깊은 소통을 가능하게 합니다. 이는 선한 목자가 양을 알고 양이 목자를 아는 친밀한 관계처럼, 분석가가 데이터를 깊이 이해하고, 그 의미를 다른 사람들에게 효과적으로 전달하는 데 필수적입니다. 제사장 옷이 하나님의 영광을 드러내듯, 잘 라벨링되고 스타일링된 데이터는 그 안에 담긴 진리를 명확하게 보여줍니다.

---

## 🎨 블렌딩 모드: 출애굽 × 요한복음의 통합 통찰

|출애굽기 진리|요한복음 진리|판다스 도구|영적 발견|
|---|---|---|---|
|제사장 옷의 영광과 아름다움|선한 목자가 양을 알고 돌봄|`Categorical` 데이터 타입|데이터의 본질적 의미와 효율적 관리|
|각 부분의 상징적 의미|양을 개별적으로 아는 친밀함|`DataFrame.style`|데이터의 시각적 아름다움과 통찰력|
|이스라엘 지파의 이름 새김|양의 음성을 알아듣는 관계|라벨링 기법|데이터와 사용자 간의 깊은 소통|
|하나님의 영광을 드러냄|예수님의 사랑과 희생|스타일링 전략|데이터의 가치 극대화와 효과적인 표현|
|거룩함과 직분의 명확성|진정한 리더십의 본질|데이터 시각화|영적 분별력과 지혜로운 의사결정|

> **💎 블렌딩 결과**: `Categorical` 데이터 타입, `DataFrame.style` 객체와 같은 라벨링과 스타일링 기술은 성경 속 제사장 옷과 선한 목자 말씀을 데이터적으로 분석하는 강력한 도구입니다. 데이터의 의미를 명확히 하고 시각적 효과를 높이는 과정을 통해, 데이터를 효과적으로 표현하고 깊이 이해하며 하나님의 지혜로운 데이터 관리 원리를 깨달을 수 있습니다.

---

## 🛠️ 광야 생존 프로젝트: 나의 영적 상태 라벨링 및 스타일링 분석

**🎯 미션**: 내 삶의 영적 상태 데이터를 라벨링하고 스타일링하여 패턴 발견하기
**📊 사용 기술**: DataFrame 생성, `Categorical` 데이터 타입, `DataFrame.style`
**🕊️ 복음 포인트**: "나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이" (요한복음 10:14)

### Step 1: 나의 영적 상태 데이터 기록 및 라벨링

```python
import pandas as pd
import numpy as np

my_spiritual_state = pd.DataFrame({
    '날짜': pd.to_datetime(pd.date_range(start='2024-01-01', periods=10, freq='D')),
    '기도_시간_분': np.random.randint(0, 60, size=10),
    '말씀_묵상_시간_분': np.random.randint(0, 60, size=10),
    '감사_지수': np.random.randint(1, 10, size=10),
    '영적_상태_평가': np.random.choice(['좋음', '보통', '나쁨'], size=10, p=[0.5, 0.3, 0.2])
})

print("🧬 나의 영적 상태 데이터:\n", my_spiritual_state.head())

# '영적_상태_평가' 컬럼을 Categorical 데이터 타입으로 변환
my_spiritual_state['영적_상태_평가'] = my_spiritual_state['영적_상태_평가'].astype('category')
print("\n--- '영적_상태_평가' 컬럼 변환 후 데이터 타입 ---")
print(my_spiritual_state.dtypes)
```

### Step 2: 영적 상태 데이터 스타일링

```python
# '감사_지수'가 7 이상이면 초록색, 4 이하면 빨간색으로 강조
def highlight_spiritual_state(s):
    is_high = s['감사_지수'] >= 7
    is_low = s['감사_지수'] <= 4
    return ['background-color: lightgreen' if v else ('background-color: lightcoral' if w else '') for v, w in zip(is_high, is_low)]

styled_spiritual_state = my_spiritual_state.style \
    .apply(highlight_spiritual_state, axis=1) \
    .format({'기도_시간_분': "{:.0f}분", '말씀_묵상_시간_분': "{:.0f}분"}) \
    .set_caption("나의 영적 상태 분석")

print("\n--- 스타일링된 나의 영적 상태 데이터 (HTML 출력) ---")
print(styled_spiritual_state.to_html(max_rows=10))
```

---

## 📱 3×10초 광야 루틴

### 🌅 아침 10초: 말씀 묵상

"나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이." (요 10:14)
오늘도 선한 목자이신 주님을 따르며 하루를 시작합니다.

### ☀️ 점심 1분: 라벨링 기도

- 오늘 제가 만나는 사람들을 `Categorical` 데이터처럼 어떤 편견으로 라벨링하고 있지는 않은지 돌아봅니다.
- `DataFrame.style`처럼 주님께서 각 사람을 아름답게 창조하셨음을 기억하며, 그들의 본질적인 가치를 보게 하소서.

### 🌙 저녁 2분: 데이터 기도일기

**오늘의 영적 데이터:**
- 오늘 `Categorical` 데이터처럼 분류해 본 나의 영적 상태는?
- `DataFrame.style`처럼 시각적으로 강조해 본 나의 영적 성장 지표는?
- 주님, 제사장 옷처럼 아름답고 선한 목자처럼 친밀하게 데이터를 이해하고 표현하는 지혜를 구합니다.

---

## ❓ FAQ & 체크리스트

### 깊이 있는 질문들

**Q1: `Categorical` 데이터 타입은 어떤 장점이 있으며, 언제 사용해야 하나요?** A: `Categorical` 데이터 타입은 문자열과 같은 범주형 데이터를 효율적으로 저장하고 처리하기 위해 사용됩니다. 이는 메모리 사용량을 줄이고, 연산 속도를 향상시키며, 범주형 데이터에 특화된 기능을 제공합니다. 성별, 지역, 등급과 같이 고정된 몇 가지 값만을 가지는 컬럼에 적합하며, 특히 데이터의 고유한 범주 수가 적을 때 큰 이점을 가집니다.

**Q2: `DataFrame.style` 객체는 무엇이며, 어떤 기능을 제공하나요?** A: `DataFrame.style` 객체는 Pandas DataFrame의 시각적 표현을 커스터마이징하는 데 사용됩니다. 셀 배경색, 텍스트 색상, 글꼴, 조건부 서식 등을 적용하여 데이터의 가독성을 높이고, 특정 패턴이나 중요한 값을 시각적으로 강조할 수 있습니다. 이는 데이터 분석 결과를 보고서나 대시보드 형태로 공유할 때 매우 유용합니다.

**Q3: 라벨링과 스타일링이 데이터 분석에서 중요한 이유는 무엇인가요?** A: 라벨링은 데이터의 각 요소에 명확한 의미를 부여하여 데이터의 이해도를 높입니다. 스타일링은 데이터를 시각적으로 매력적이고 가독성 있게 만들어, 분석 결과를 효과적으로 전달하고 중요한 통찰을 빠르게 파악할 수 있도록 돕습니다. 이는 복잡한 데이터를 단순화하고, 사용자에게 친숙하게 다가가는 데 필수적입니다.

**Q4: 제사장 옷이 라벨링과 스타일링과 어떤 영적 의미로 연결될 수 있을까요?** A: 제사장 옷은 하나님의 영광과 거룩함을 드러내고, 제사장의 직분을 상징하는 특별한 의미를 가졌습니다. 데이터 라벨링과 스타일링은 데이터의 본질적인 의미를 명확히 하고, 시각적으로 아름답게 표현하여 데이터가 가진 진리를 드러내는 것과 같습니다. 이는 하나님의 창조 질서와 말씀의 아름다움을 데이터적으로 묵상하게 합니다.

**Q5: 선한 목자가 양을 아는 것이 데이터 라벨링과 스타일링과 어떤 영적 의미로 연결될 수 있을까요?** A: 선한 목자는 양을 개별적으로 알고, 양의 특성을 이해하여 그에 맞는 돌봄을 제공합니다. 데이터 라벨링은 데이터의 각 요소를 정확히 파악하고, 스타일링은 양의 상태를 한눈에 파악하여 적절한 돌봄을 제공하는 것과 유사합니다. 이는 데이터의 외형적인 모습뿐만 아니라, 그 안에 담긴 본질적인 의미를 이해하고 소통하는 데 도움을 줍니다.

### ✅ 체크리스트

**성경 이해 체크:**

- [ ] 출애굽기 28장의 제사장 옷의 영광과 아름다움 이해
- [ ] 요한복음 10장의 선한 목자와 양의 친밀한 관계 이해
- [ ] 데이터 라벨링과 스타일링을 통해 데이터를 효과적으로 표현하고 깊이 이해

**DataFrame 기초 체크:**

- [ ] `df.astype('category')`를 사용하여 범주형 데이터 타입으로 변환 성공
- [ ] `df.style` 객체를 사용하여 데이터프레임에 시각적 스타일 적용 성공
- [ ] `apply()`, `format()`, `background_gradient()`, `set_caption()` 등 스타일링 메서드 활용
- [ ] `to_html()`을 사용하여 스타일링된 데이터프레임을 HTML로 출력 성공

**영적 적용 체크:**

- [ ] 내 삶의 영적 상태 데이터를 라벨링하고 스타일링하여 패턴 발견 시도 완료
- [ ] 나의 영적 상태를 `Categorical` 데이터처럼 분류하고, `DataFrame.style`처럼 시각적으로 강조 시도 완료
- [ ] 라벨링과 스타일링 원리를 통해 영적 분별력과 지혜로운 의사결정 노력

**발견 기록 체크:**

- [ ] `Categorical` 데이터 타입으로 제사장 옷의 의미 명확화 확인
- [ ] `DataFrame.style`로 선한 목자의 돌봄 시각화 통찰
- [ ] 라벨링과 스타일링이 데이터와 사용자 간의 깊은 소통임을 확인

---

## 🧠 미니 퀴즈

**1. 문자열과 같은 범주형 데이터를 효율적으로 저장하고 처리하기 위해 사용되는 Pandas 데이터 타입은?**
a) `object`
b) `int64`
c) `category`

**2. Pandas DataFrame의 시각적 표현을 커스터마이징하는 데 사용되는 객체는?**
a) `df.plot()`
b) `df.style`
c) `df.visualize()`

**3. `DataFrame.style` 객체에서 특정 조건에 따라 셀의 배경색을 변경하는 데 사용되는 메서드는?**
a) `style.highlight_max()`
b) `style.apply()`
c) `style.format()`

**4. 제사장 옷이 라벨링과 스타일링과 연결되는 영적 의미로 가장 적절한 것은?**
a) 데이터의 양을 늘려 하나님의 풍성함을 표현
b) 데이터의 본질적인 의미를 명확히 하고 시각적으로 아름답게 표현
c) 데이터의 복잡성을 숨겨 분석을 단순화

**5. 선한 목자가 양을 아는 것이 데이터 라벨링과 스타일링과 연결되는 영적 의미로 가장 적절하지 않은 것은?**
a) 데이터의 각 요소를 정확히 파악하고 특성을 이해
b) 데이터의 상태를 한눈에 파악하여 적절한 돌봄 제공
c) 데이터의 외형적인 모습만을 중요시하여 본질을 간과함

_(정답: 1-c, 2-b, 3-b, 4-b, 5-c)_

---

## 🎯 깊이 탐구 과제 (선택)

### 초급 과제

1.  **성경 인물 특성 범주화**: 성경 인물 데이터(이름, 시대, 역할, 성별)를 만들고, `역할`과 `성별` 컬럼을 `category dtype`으로 변환해보기
2.  **성경 구절 중요도 스타일링**: 성경 구절 데이터(구절 ID, 내용, 중요도 점수)를 만들고, `중요도 점수`에 따라 배경색을 다르게 하는 `DataFrame.style`을 적용해보기

### 중급 과제

1.  **교회 봉사자 현황 보고서**: 가상의 교회 봉사자 데이터(봉사자 ID, 봉사 유형, 헌신도, 참여 횟수)를 만들고, `봉사 유형`을 `category dtype`으로 변환한 후, `헌신도`가 높은 봉사자를 강조하는 `DataFrame.style`을 적용하여 보고서(HTML) 생성해보기
2.  **영적 성장 지표 대시보드**: 개인의 영적 성장 지표(예: 기도 시간, 말씀 묵상 시간, 감사 지수) 데이터를 만들고, `영적 상태 평가` 컬럼을 `category dtype`으로 변환한 후, `감사 지수`에 따라 색상을 다르게 하는 `DataFrame.style`을 적용하여 대시보드(개념) 설계해보기

### 고급 과제

1.  **성경 인물 관계도 시각화**: 성경 인물 데이터(이름, 관계, 영향력)를 만들고, `관계` 컬럼을 `category dtype`으로 변환한 후, `DataFrame.style`과 `networkx` 라이브러리(선택)를 활용하여 인물 간의 관계도를 시각적으로 아름답게 표현하는 시스템(개념) 설계해보기
2.  **교회 공동체 영적 건강 지표 대시보드**: 가상의 교회 공동체 데이터(교인 ID, 영적 성장 지수, 봉사 참여도, 헌금액)를 만들고, `영적 성장 지수`와 `봉사 참여도`를 `category dtype`으로 변환한 후, `DataFrame.style`을 활용하여 교인별 영적 건강 상태를 한눈에 파악할 수 있는 대시보드를 구축하고, 선한 목자의 돌봄 원리를 적용한 통찰 보고서 작성해보기

---

## 🌟 다음 여정 예고

**Chapter 29: "위임식 - 테스트 데이터 세팅 (Ordination - Test Data Setting)"**

제사장 위임식이 제사장의 직분을 공식적으로 시작하는 것처럼, 데이터 분석에서도 테스트 데이터 세팅은 모델의 성능을 검증하고 신뢰성을 확보하는 데 필수적입니다.

Just as the ordination of priests officially begins their ministry, in data analysis, setting up test data is essential for validating model performance and ensuring reliability.

다음 장에서 배울 내용 (What you'll learn in the next chapter):
📁 데이터 샘플링 기법
🔍 훈련/테스트 데이터 분할의 중요성
🎯 재현 가능한 데이터 분할을 위한 시드(seed) 설정
📊 위임식처럼 견고하고 신뢰할 수 있는 모델 검증 환경 구축

"모세가 그 장인의 말을 듣고 그 말대로 하여" (출애굽기 29:1-9)
"내가 비옵는 것은 이 사람들을 위함이요 세상은 위함이 아니요 내게 주신 자들을 위함이니이다" (요한복음 17:9)

---

## 🙏 한 줄 기도

_"주님, 제사장 옷처럼 데이터의 본질을 아름답게 표현하고, 선한 목자가 양을 알듯 데이터를 깊이 이해하는 분석가가 되게 하소서.
라벨링과 스타일링을 통해 데이터의 가치를 높이고, 통찰을 명확하게 전달하게 하소서.
예수님의 이름으로 기도합니다. 아멘."

---

**🎊 스물여덟 번째 광야 여정을 완주하신 것을 축하합니다!**

"나는 선한 목자라 나는 내 양을 알고 양도 나를 아는 것이" (요한복음 10:14)

여러분은 이제 데이터 속에서 `Categorical` 데이터 타입과 `DataFrame.style` 객체를 통해 데이터를 효과적으로 표현하고 깊이 이해하는 방법을 알게 되었습니다. 주님께서 주신 지혜로 모든 데이터 속에서 하나님의 영광과 선한 목자의 돌봄 원리를 발견하시길 기도합니다.

**다음 여정에서 만나요! 🌈**
