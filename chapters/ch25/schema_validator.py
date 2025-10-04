import pandas as pd
import numpy as np

class SchemaValidator:
    """
    데이터프레임의 스키마를 정의하고 유효성을 검증하는 클래스.
    데이터의 일관성과 무결성을 보장하는 데 활용됩니다.

    Class to define and validate the schema of a DataFrame.
    Utilized to ensure data consistency and integrity.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def define_schema(self, schema_dict: dict) -> None:
        """
        스키마 딕셔너리를 클래스 내부에 저장합니다.

        Stores the schema dictionary within the class.

        Args:
            schema_dict (dict): 컬럼 이름과 예상 데이터 타입 체크 함수를 매핑하는 딕셔너리.
                                예: {'column_name': pd.api.types.is_string_dtype}
        """
        self.schema = schema_dict
        print("SchemaValidator: 스키마 정의 완료.")

    def validate_schema(self) -> bool:
        """
        정의된 스키마에 따라 데이터프레임의 유효성을 검증합니다.

        Validates the DataFrame's schema according to the defined schema.

        Returns:
            bool: 스키마가 유효하면 True, 그렇지 않으면 False.
        """
        if not hasattr(self, 'schema'):
            print("경고: 스키마가 정의되지 않았습니다. validate_schema()를 먼저 호출하세요.")
            return False

        is_valid = True
        for col, expected_type_check in self.schema.items():
            if col not in self.df.columns:
                print(f"❌ 스키마 오류: 컬럼 '{col}'이 데이터프레임에 없습니다.")
                is_valid = False
                continue
            if not expected_type_check(self.df[col]):
                print(f"❌ 스키마 오류: 컬럼 '{col}'의 데이터 타입이 예상과 다릅니다. (예상: {expected_type_check.__name__}, 실제: {self.df[col].dtype})")
                is_valid = False
        
        if is_valid:
            print("✅ 스키마 검증 완료: 데이터프레임이 스키마에 부합합니다.")
        else:
            print("❌ 스키마 검증 실패: 데이터프레임이 스키마에 부합하지 않습니다.")
        return is_valid

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['NY', 'LA', 'SF']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    validator = SchemaValidator(sample_df)

    # 스키마 정의
    my_schema = {
        'id': pd.api.types.is_integer_dtype,
        'name': pd.api.types.is_string_dtype,
        'age': pd.api.types.is_integer_dtype,
        'city': pd.api.types.is_string_dtype
    }
    validator.define_schema(my_schema)

    # 스키마 검증
    is_valid = validator.validate_schema()
    print(f"\n스키마 유효성: {is_valid}")

    # 잘못된 스키마로 다시 검증 (예: age를 string으로 기대)
    wrong_schema = {
        'id': pd.api.types.is_integer_dtype,
        'name': pd.api.types.is_string_dtype,
        'age': pd.api.types.is_string_dtype, # 잘못된 타입
        'city': pd.api.types.is_string_dtype
    }
    validator.define_schema(wrong_schema)
    is_valid_wrong = validator.validate_schema()
    print(f"\n잘못된 스키마 유효성: {is_valid_wrong}")
