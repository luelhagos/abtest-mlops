with open('results.txt', 'w') as result:
      result.write('Logistic Regression\n')
      result.write(f'score : 0.518, and loss: 0.701\n')

      result.write('\n')
      result.write('Decision Tree\n')
      result.write(f'score : 0.839, and loss: 12.04  \n')

      result.write('\n')
      result.write('XGBoost\n')
      result.write(f'score : 0.518, and loss: 0.712\n')
