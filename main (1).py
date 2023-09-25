def LinearSearchProduct(product, target):
    indices = []
    for i in range(len(product)):
        if product[i]["name"] == target:
            indices.append(i)
    return indices
products = [{"name": "shoes"}, {"name": "boots"}, {"name": "loafers"}, {"name": "shoes"}, {"name": "sandals"}, {"name": "shoes"}]
target = "shoes"
result = LinearSearchProduct(products, target)
print(result)  # This will output [0, 2] for the example list.