# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.
try:
    stores = {
        'Магнит': ['молоко', 'соль', 'сахар'],
        'Пятерочка': ['мясо', 'молоко', 'сыр'],
        'Перекресток': ['молоко', 'творог', 'сыр', 'сахар']
    }
    
    #1. Полный список всех товаров
    all_products = set()
    for products in stores.values():
        all_products.update(products)
    print("Полный список всех товаров:", all_products)
    
    #2. Магазины, в которых можно приобрести одновременно молоко и сыр
    milk_cheese_stores = []
    for store, products in stores.items():
        if 'молоко' in products and 'сыр' in products:
            milk_cheese_stores.append(store)
    print("Магазины, где можно приобрести молоко и сыр:", milk_cheese_stores)
    
    #3. Магазины, в которых можно приобрести сахар
    sugar_stores = []
    for store, products in stores.items():
        if 'сахар' in products:
            sugar_stores.append(store)
    print("Магазины, где можно приобрести сахар:", sugar_stores)

except Exception as e:
    print("Произошла ошибка:", str(e)) 

    
