
import pandas as pd
from .song_of_sea_data import SongOfTheSeaDataGenerator

class SongPivotReshapeAnalyzer:
    """
    출애굽기 15장의 바다의 노래 데이터를 `pivot_table()`과 `melt()`를 사용하여 분석하는 클래스.
    하나님의 구원 역사를 다양한 관점으로 재구성하고 탐구합니다.

    Class to analyze Song of the Sea data from Exodus Chapter 15 using `pivot_table()` and `melt()`.
    Reconfigures and explores God's salvation history from various perspectives.
    """

    def __init__(self):
        """
        분석기 초기화 및 데이터 생성.
        Initializes the analyzer and generates data.
        """
        self.data_generator = SongOfTheSeaDataGenerator()
        self.song_df = self.data_generator.generate_song_of_sea_data()

    def analyze_pivot_table(self):
        """
        `pivot_table()`을 사용하여 하나님의 속성별 이스라엘의 반응을 교차 분석합니다.
        Uses `pivot_table()` to cross-analyze Israel's response by God's attributes.

        - KJV: Exodus 15:11 - "Who is like unto thee, O LORD, among the gods? who is like thee, glorious in holiness, fearful in praises, doing wonders?"
        - ESV: Exodus 15:11 - "Who is like you, O LORD, among the gods? Who is like you, majestic in holiness, awesome in glorious deeds, doing wonders?"
        - 개역한글: 출애굽기 15:11 - "여호와여 신 중에 주와 같은 자 누구니이까 주와 같이 거룩함에 영광스러우며 찬송 중에 심히 두려우며 기사를 행하는 자 누구니이까"
        """
        print("\n📊 === 하나님의 속성별 이스라엘 반응 Pivot Table (Israel's Response by God's Attribute) ===")
        print("하나님의 속성과 이스라엘의 반응을 교차 분석하여 구원 역사를 다각도로 이해합니다.")
        print("Cross-analyzing God's attributes and Israel's response to understand salvation history from multiple angles.")

        # 'attribute_of_God'를 인덱스로, 'israel_response'를 컬럼으로 하는 pivot_table 생성
        pivoted_song = pd.pivot_table(self.song_df, values='intensity', index='attribute_of_God', columns='israel_response', aggfunc='sum', fill_value=0)
        print(pivoted_song.to_string())

        print("\n💡 통찰 (Insight): `pivot_table()`은 하나님의 위대한 속성이 이스라엘 백성의 어떤 반응을 이끌어냈는지 요약하여 보여줍니다.")
        print("Insight: `pivot_table()` summarizes how God's great attributes elicited specific responses from the Israelites.")
        return pivoted_song

    def analyze_melt(self):
        """
        데이터를 넓은(wide) 형식에서 긴(long) 형식으로 `melt()`하여 변화를 추적합니다.
        Uses `melt()` to transform data from wide to long format, tracking changes.

        - KJV: Exodus 15:1 - "...I will sing unto the LORD, for he hath triumphed gloriously: the horse and his rider hath he thrown into the sea."
        - ESV: Exodus 15:1 - "...I will sing to the LORD, for he has triumphed gloriously; the horse and his rider he has thrown into the sea."
        - 개역한글: 출애굽기 15:1 - "...내가 여호와를 찬송하리니 그는 높고 영화로우심이요 말과 그 탄 자를 바다에 던지셨음이로다"
        """
        print("\n📈 === 데이터 Melt (Melting Data from Wide to Long Format) ===")
        print("바다의 노래 데이터를 `melt()`하여 각 사건의 다양한 측면을 긴 형식으로 변환합니다.")
        print("Melting the Song of the Sea data to transform various aspects of each event into a long format.")

        # 'event_id', 'event_type'을 고정하고 나머지 컬럼을 'category'와 'value'로 melt
        melted_song = self.song_df.melt(id_vars=['event_id', 'event_type'], var_name='category', value_name='value')
        print(melted_song.head().to_string(index=False))

        print("\n💡 통찰 (Insight): `melt()`는 구원 역사의 각 요소(하나님의 속성, 이스라엘 반응, 애굽 운명)를 개별적으로 분석하여 하나님의 일하심의 세밀함을 추적하게 합니다.")
        print("Insight: `melt()` allows individual analysis of each element (God's attributes, Israel's response, Egypt's fate) in salvation history, tracking the meticulousness of God's work.")
        return melted_song

    def run_all_analyses(self) -> dict:
        """
        모든 피벗 및 형태변환 분석을 실행하고 결과를 반환합니다.
        Runs all pivot and reshaping analyses and returns the results.
        """
        print("\n--- 출애굽기 15장: 바다의 노래 피벗/형태변환 분석 시작 ---")
        print("--- Exodus Chapter 15: Song of the Sea Pivot/Reshaping Analysis Started ---")

        results = {
            'pivoted_song': self.analyze_pivot_table(),
            'melted_song': self.analyze_melt()
        }

        print("\n--- 출애굽기 15장: 바다의 노래 피벗/형태변환 분석 완료 ---")
        print("--- Exodus Chapter 15: Song of the Sea Pivot/Reshaping Analysis Completed ---")
        return results

def demo_song_pivot_reshape_analyzer():
    """
    SongPivotReshapeAnalyzer 클래스의 데모 실행 함수.
    Demonstration function for SongPivotReshapeAnalyzer class.
    """
    print("\n=== Song of the Sea Pivot/Reshape Analyzer Demo ===")
    analyzer = SongPivotReshapeAnalyzer()
    results = analyzer.run_all_analyses()
    return results

if __name__ == "__main__":
    demo_song_pivot_reshape_analyzer()
