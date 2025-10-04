import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

class ClassificationAnalyzer:
    """
    분류 및 범주형 데이터를 활용하여 기본적인 분류 분석을 수행하는 클래스.
    의사결정나무 모델을 사용하여 데이터의 패턴을 학습하고 예측합니다.

    Class to perform basic classification analysis using categorical and binned data.
    Learns and predicts data patterns using a Decision Tree Classifier.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def perform_classification(self, feature_columns: list, target_column: str, random_state: int = 21) -> dict:
        """
        지정된 특성 컬럼과 타겟 컬럼을 사용하여 분류 분석을 수행합니다.
        데이터 분할, 모델 학습, 예측 및 평가를 포함합니다.

        Performs classification analysis using specified feature and target columns.
        Includes data splitting, model training, prediction, and evaluation.

        Args:
            feature_columns (list): 특성으로 사용할 컬럼 이름 리스트.
            target_column (str): 타겟(예측 대상) 컬럼 이름.
            random_state (int): 재현 가능한 데이터 분할 및 모델 학습을 위한 시드.

        Returns:
            dict: 분류 분석 결과를 담은 딕셔너리 (정확도, 분류 보고서 등).
        """
        for col in feature_columns + [target_column]:
            if col not in self.df.columns:
                raise ValueError(f"컬럼 '{col}'이 데이터프레임에 존재하지 않습니다.")

        # 범주형 데이터를 숫자형으로 변환 (원-핫 인코딩)
        # 여기서는 간단히 factorize를 사용하거나, 이미 category dtype으로 변환된 것을 가정
        # 실제 ML에서는 OneHotEncoder 등을 사용
        processed_df = self.df.copy()
        for col in feature_columns:
            if pd.api.types.is_categorical_dtype(processed_df[col]) or pd.api.types.is_object_dtype(processed_df[col]):
                processed_df[col] = pd.factorize(processed_df[col])[0]
        
        if pd.api.types.is_categorical_dtype(processed_df[target_column]) or pd.api.types.is_object_dtype(processed_df[target_column]):
            processed_df[target_column] = pd.factorize(processed_df[target_column])[0]


        X = processed_df[feature_columns]
        y = processed_df[target_column]

        # 훈련 세트와 테스트 세트 분할
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)

        # 의사결정나무 모델 학습
        model = DecisionTreeClassifier(random_state=random_state)
        model.fit(X_train, y_train)

        # 예측
        y_pred = model.predict(X_test)

        # 평가
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        print("ClassificationAnalyzer: 분류 분석 완료.")
        return {
            'accuracy': accuracy,
            'classification_report': report,
            'model': model # 모델 자체도 반환 가능
        }

if __name__ == "__main__":
    # 샘플 데이터 생성 (JusticeOrdinancesDataGenerator에서 생성된 데이터와 유사)
    data = {
        'case_id': range(1, 101),
        'offense_type': np.random.choice(['Theft', 'Assault', 'Property Damage', 'Dispute'], size=100, p=[0.3, 0.3, 0.2, 0.2]),
        'damage_level': np.random.randint(1, 10, size=100),
        'witness_count': np.random.randint(0, 5, size=100),
        'judge_bias_score': np.random.rand(100) * 10,
        'judgment_outcome': np.random.choice(['Guilty', 'Not Guilty', 'Settled'], size=100, p=[0.4, 0.3, 0.3])
    }
    sample_df = pd.DataFrame(data)

    # 범주형 변환 및 구간화 (분석을 위해 미리 처리)
    sample_df['offense_type'] = sample_df['offense_type'].astype('category')
    sample_df['damage_category'] = pd.cut(sample_df['damage_level'], bins=3, labels=['Low', 'Medium', 'High'])
    sample_df['damage_category'] = sample_df['damage_category'].astype('category') # cut 결과도 category로

    print("원본 데이터 (일부):")
    print(sample_df.head())
    print(sample_df.dtypes)

    analyzer = ClassificationAnalyzer(sample_df)
    results = analyzer.perform_classification(
        feature_columns=['offense_type', 'damage_level', 'witness_count', 'judge_bias_score'],
        target_column='judgment_outcome'
    )
    print("\n분류 분석 결과:")
    print(f"정확도: {results['accuracy']:.2f}")
    print("분류 보고서:")
    print(pd.DataFrame(results['classification_report']).transpose())
