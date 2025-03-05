import calculator

calculator.main()

result1 = calculator.add(2, 10)
print(result1)

calculator.add(10, 30)

calculator.div(1.0, 5)

print(calculator.latest_result)
print(calculator.history_of_calculations)


#what is the operator of latest calculation?
print("the operator of latest calculation is",
      calculator.history_of_calculations[-1]['operator']
      )