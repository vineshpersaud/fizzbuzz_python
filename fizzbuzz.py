def fizzbuzz():
  counter = 0
  while counter < 100:
    counter += 1
    if counter % 3 ==  0 and counter % 5 ==  0:
      print('FizBuzz!')
    elif counter % 3 ==  0:
      print('fizz')
    elif  counter % 5 == 0:
        print('buzz')
    else:
      print(counter)


fizzbuzz()
