# menu = {
#     "apple": {
#         "iPhone": {
#             "iPhone SE 64Gb Starlight": {
#                 "1count": "24 300",
#                 "5count": "24 150"
#             },
#             "iPhone SE SE 64Gb Red": {
#                 "1count": "26 350",
#                 "5count": "25 150"
#             }
#         },
#         "Watch": {
#             "Series 8 45mm Sport B M/L Midnight": {
#                 "1count": "26 350",
#                 "5count": "25 150",
#                 "20count": "20 000"
#             }
#         }
#     },
#     "android": {
#         "Redmi": {
#             "Redmi A1 + 2+ 32Gb Blue": {
#                 "1count": "26 350",
#                 "5count": "25 150"
#             }
#         },
#         "Huawei": {
#             "Huawei Y9A 8+ 128Gb Silver": {
#                 "1count": "26 350",
#                 "5count": "25 150"
#             }
#         }
#     }
# }
import json


def main():
    menu = {}
    product_list = {"📱 iPhone": {"current_category": "🍎Apple", "current_subcategory": "iPhone"},
                    "⌚ Series": {"current_category": "🍎Apple", "current_subcategory": "Apple Watch"},
                    "🔳 iPad": {"current_category": "🍎Apple", "current_subcategory": "iPad"},
                    "🖥 iMac": {"current_category": "🍎Apple", "current_subcategory": "iMac"},
                    "🖥 Mac": {"current_category": "🍎Apple", "current_subcategory": "iMac"},
                    "💻 MacBook": {"current_category": "🍎Apple", "current_subcategory": "MacBook"},
                    "🎧 AirPods": {"current_category": "🍎Apple", "current_subcategory": "AirPods & Accs"},
                    "📺 TV": {"current_category": "🍎Apple", "current_subcategory": "AirPods & Accs"},
                    "🖱 Magic Mouse": {"current_category": "🍎Apple", "current_subcategory": "AirPods & Accs"},
                    "🖊 Pencil": {"current_category": "🍎Apple", "current_subcategory": "AirPods & Accs"},
                    "📱 Redmi": {"current_category": "📞Android", "current_subcategory": "Redmi"},
                    "📱 Poco": {"current_category": "📞Android", "current_subcategory": "POCO"},
                    "📱 Mi": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "📱 Xiaomi": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "🔳 miPad": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "🔳 Redmi": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "🎧 Mi": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "🎧 Redmi Buds": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "🔘 Mi": {"current_category": "📞Android", "current_subcategory": "Xiaomi & Mi"},
                    "🔳 Lenovo Tab": {"current_category": "📞Android", "current_subcategory": "Tab"},
                    "SM-": {"current_category": "📞Android", "current_subcategory": "Samsung"},
                    "🔌 Adapter": {"current_category": "📞Android", "current_subcategory": "Samsung"},
                    "📱 OnePlus": {"current_category": "📞Android", "current_subcategory": "One Plus"},
                    "📱 Google Pixel": {"current_category": "📞Android", "current_subcategory": "Google Pixel"},
                    "🎮 DualSense": {"current_category": "🎮Console", "current_subcategory": "Dualsense"},
                    "PlayStation 5": {"current_category": "🎮Console", "current_subcategory": "PS5"},
                    "Nintendo Switch": {"current_category": "🎮Console", "current_subcategory": "Nintendo"}}
    for data in product_list.values():
        if data['current_category'] not in menu.keys():
            menu[data['current_category']] = {}
            menu[data['current_category']][data['current_subcategory']] = {}
        else:
            menu[data['current_category']][data['current_subcategory']] = {}
    # menu['Другое'] = {}
    # menu['Другое']['Все товары'] = {}
    current_category = None
    current_subcategory = None
    product = None
    with open("tgbot/data/price.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            for key, value in product_list.items():
                if key in line:
                    current_category = value['current_category']
                    current_subcategory = value['current_subcategory']
                    product = line
                    menu[current_category][current_subcategory][product] = {}
                elif 'От' in line:
                    menu[current_category][current_subcategory][product][line.split('-')[0]] = line.split('-')[1]
                # else:
                #     current_category = 'Другое'
                #     current_subcategory = 'Все товары'
                #     product = line
                #     menu[current_category][current_subcategory][product] = {}
    with open('tgbot/data/price.json', "w") as outfile:
        json.dump(menu, outfile)


if __name__ == '__main__':
    main()
