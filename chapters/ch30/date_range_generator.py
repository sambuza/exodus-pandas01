import pandas as pd

class DateRangeGenerator:
    """
    Pandas의 `date_range` 기능을 시연하는 클래스.
    다양한 빈도(frequency)로 시계열 인덱스를 생성합니다.

    Class to demonstrate Pandas' `date_range` functionality.
    Generates time-series indices with various frequencies.
    """

    def generate_ranges(self) -> dict[str, pd.DatetimeIndex]:
        """
        다양한 `date_range`를 생성하여 반환합니다.

        Generates and returns various `date_range` objects.

        Returns:
            dict[str, pd.DatetimeIndex]: 생성된 date_range 객체들을 담은 딕셔너리.
        """
        daily_range = pd.date_range(start='2023-01-01', periods=7, freq='D')
        hourly_range = pd.date_range(start='2023-01-01 09:00', periods=5, freq='H')
        monthly_range = pd.date_range(start='2023-01-01', periods=3, freq='MS') # Month Start

        print("DateRangeGenerator: 다양한 date_range 생성 완료.")
        return {
            'daily': daily_range,
            'hourly': hourly_range,
            'monthly': monthly_range
        }

if __name__ == "__main__":
    generator = DateRangeGenerator()
    ranges = generator.generate_ranges()
    for name, dr in ranges.items():
        print(f"\n--- {name} range ---")
        print(dr)