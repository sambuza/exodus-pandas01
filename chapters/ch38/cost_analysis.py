import pandas as pd

class CostAnalysis:
    """
    비용 분석을 위한 클래스.
    `groupby`와 `agg`를 사용하여 데이터를 그룹화하고 집계합니다.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze_costs_by_item(self):
        """
        항목별 비용을 분석합니다.
        """
        try:
            # 총 비용 계산
            self.df['total_cost'] = self.df['cost_shekels'] * self.df['quantity']
            
            # 항목별 비용 집계
            cost_summary = self.df.groupby('item').agg(
                total_cost=('total_cost', 'sum'),
                avg_quantity=('quantity', 'mean')
            ).reset_index()
            
            print("CostAnalysis: 항목별 비용 분석 완료.")
            return cost_summary
        except Exception as e:
            print(f"항목별 비용 분석 중 오류 발생: {e}")
            return None
