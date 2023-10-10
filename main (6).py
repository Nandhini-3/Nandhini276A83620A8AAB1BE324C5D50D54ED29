def linerSearchProduct(productList,  targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product==targetProduct:            indices.append(index)

  return indices 
  products = ["shoes","boat","loafer","shoes","sadal","shoes"]
  target = "shoes"
  target2 = 'apple'
  result =linerSearchProduct(Products,  target2)
  print(result)
  