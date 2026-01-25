CATEGORIES = {
    'TV': 'katalog/vse-televizory/',
    'IPHONE': 'katalog/smartfony-apple/',
    'WATCHES': 'katalog/smart-chasy/',
    'MAC': 'katalog/mac/'
}


def get_value(category):
    for key, value in CATEGORIES.items():
        if key == category:
            return value