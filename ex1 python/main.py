
def price_check(products, productPrices, productSold, soldPrice):
    incorrect_prices = 0

    for i in range(len(productSold)):
        if soldPrice[i] != productPrices[products.index(productSold[i])]:
            incorrect_prices = incorrect_prices + 1

    return incorrect_prices

if __name__ == '__main__':
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese', 'rice']
    soldPrice = [18.99, 400.89, 16.89]

    print("first example", price_check(products, productPrices, productSold, soldPrice))

    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]

    print("second example", price_check(products, productPrices, productSold, soldPrice))

