import pandas as pd
from chapters.ch28.categorical_labeling import CategoricalLabeler
from chapters.ch28.dataframe_styling import DataFrameStyler

class StyledReportGenerator:
    """
    라벨링 및 스타일링이 적용된 데이터프레임을 기반으로 보고서를 생성하는 클래스.
    데이터의 의미를 효과적으로 전달하고 시각적 매력을 높입니다.

    Class to generate a report based on a labeled and styled DataFrame.
    Effectively communicates data meaning and enhances visual appeal.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def generate_report(self) -> str:
        """
        스타일링된 데이터프레임을 HTML 형식의 보고서로 생성합니다.

        Generates an HTML report from the styled DataFrame.

        Returns:
            str: HTML 형식의 보고서 내용.
        """
        # 1. 범주형 라벨링 적용 (이미 적용되었다고 가정하거나, 여기서 다시 적용)
        labeler = CategoricalLabeler(self.df)
        labeled_df = labeler.apply_categorical_labels()

        # 2. 스타일링 적용
        styler = DataFrameStyler(labeled_df)
        styled_df_styler = styler.apply_styles()

        # HTML 보고서 생성
        report_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>제사장 옷 데이터 분석 보고서</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>제사장 옷 데이터 분석 보고서</h1>
            <p>이 보고서는 제사장 옷 데이터의 라벨링 및 스타일링 결과를 보여줍니다.</p>
            {styled_df_styler.to_html()}
            <p>보고서 생성 시간: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </body>
        </html>
        """
        print("StyledReportGenerator: 스타일링된 보고서 생성 완료.")
        return report_html

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

    generator = StyledReportGenerator(sample_df)
    report = generator.generate_report()
    # HTML 보고서 내용을 파일로 저장하거나 출력
    with open("ch28_report.html", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n보고서가 'ch28_report.html' 파일로 저장되었습니다.")
