import pandas as pd
import numpy as np
from pandas.io.formats.style import Styler

class DataFrameStyler:
    """
    데이터프레임에 시각적 스타일링을 적용하는 클래스.
    `DataFrame.style` 객체를 활용하여 데이터의 가독성과 시각적 매력을 높입니다.

    Class to apply visual styling to a DataFrame.
    Enhances data readability and visual appeal using the `DataFrame.style` object.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def highlight_max(self, s):
        """시리즈에서 최댓값을 하이라이트합니다."""
        is_max = s == s.max()
        return ['background-color: yellow' if v else '' for v in is_max]

    def color_negative_red(self, val):
        """음수 값을 빨간색으로 표시합니다."""
        color = 'red' if isinstance(val, (int, float)) and val < 0 else 'black'
        return f'color: {color}'

    def apply_styles(self) -> Styler:
        """
        데이터프레임에 다양한 스타일을 적용합니다.
        예: 최댓값 하이라이트, 특정 조건에 따른 색상 변경 등.

        Applies various styles to the DataFrame.
        E.g., highlighting max values, changing colors based on conditions.

        Returns:
            pd.io.formats.style.Styler: 스타일이 적용된 Styler 객체.
        """
        styled_df = self.df.style \
            .apply(self.highlight_max, subset=['material_quality', 'gemstone_count']) \
            .format({'color_purity': "{:.2f}"}) \
            .background_gradient(cmap='Blues', subset=['material_quality']) \
            .set_caption("제사장 옷 데이터 스타일링")

        print("DataFrameStyler: 데이터프레임 스타일링 적용 완료.")
        return styled_df

if __name__ == "__main__":
    # 샘플 데이터 생성
    data = {
        'priest_id': range(1, 6),
        'garment_type': ['Ephod', 'Robe', 'Ephod', 'Tunic', 'Robe'],
        'material_quality': [7, 8, 6, 9, 7],
        'color_purity': [0.8, 0.9, 0.7, 0.95, 0.85],
        'gemstone_count': [12, 8, 10, 11, 9],
        'status': ['Clean', 'Worn', 'New', 'Clean', 'Worn']
    }
    sample_df = pd.DataFrame(data)
    print("원본 데이터:")
    print(sample_df)

    styler = DataFrameStyler(sample_df)
    styled_df = styler.apply_styles()
    print("\n스타일링된 데이터 (HTML 출력):")
    print(styled_df.to_html(max_rows=5))
