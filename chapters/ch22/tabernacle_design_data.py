import pandas as pd

def get_tabernacle_components_data():
    """성막 구성 요소 데이터를 생성합니다."""
    data = {
        'section': ['Outer Court', 'Outer Court', 'Holy Place', 'Holy Place', 'Most Holy Place', 'Most Holy Place'],
        'item': ['Altar of Burnt Offering', 'Laver', 'Table of Showbread', 'Golden Lampstand', 'Altar of Incense', 'Ark of the Covenant'],
        'material': ['Bronze', 'Bronze', 'Acacia Wood overlaid with Gold', 'Pure Gold', 'Acacia Wood overlaid with Gold', 'Acacia Wood overlaid with Gold'],
        'dimension_unit': ['Cubits', 'Cubits', 'Cubits', 'Cubits', 'Cubits', 'Cubits'],
        'length': [5, 1, 2, 1, 1, 2.5],
        'width': [5, 1, 1, 1, 1, 1.5],
        'height': [3, 1.5, 1.5, 1.5, 2, 1.5]
    }
    df = pd.DataFrame(data)
    return df

def get_tabernacle_layers_data():
    """성막 덮개 데이터를 생성합니다."""
    data = {
        'layer': ['Innermost', 'Second', 'Third', 'Outermost'],
        'material': ['Fine Twined Linen', 'Goat Hair', 'Ram Skins dyed Red', 'Badger Skins'],
        'symbolism': ['Purity, Righteousness', 'Atonement, Sacrifice', 'Dedication, Blood', 'Protection, Durability']
    }
    df = pd.DataFrame(data)
    return df
