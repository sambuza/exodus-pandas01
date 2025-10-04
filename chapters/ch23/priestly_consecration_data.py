import pandas as pd

def get_priestly_consecration_steps():
    """제사장 위임식 절차 데이터를 생성합니다."""
    data = {
        'step_id': [1, 2, 3, 4, 5, 6],
        'ritual': ['Washing', 'Anointing', 'Garments', 'Bull Offering', 'Ram Offering', 'Consecration Offering'],
        'purpose': ['Purification', 'Sanctification', 'Distinction', 'Atonement', 'Dedication', 'Fellowship'],
        'required_purity': ['High', 'High', 'High', 'High', 'High', 'High'],
        'duration_days': [1, 7, 7, 7, 7, 7]
    }
    df = pd.DataFrame(data)
    return df

def get_priestly_garment_details():
    """제사장 의복 세부사항 데이터를 생성합니다."""
    data = {
        'garment': ['Ephod', 'Breastpiece', 'Robe', 'Tunic', 'Turban', 'Sash'],
        'material': ['Gold, Blue, Purple, Scarlet, Fine Linen', 'Gold, Blue, Purple, Scarlet, Fine Linen', 'Blue', 'Fine Linen', 'Fine Linen', 'Fine Linen'],
        'symbolism': ['Glory, Beauty', 'Judgment, Intercession', 'Holiness', 'Purity', 'Holiness to the Lord', 'Service']
    }
    df = pd.DataFrame(data)
    return df
