import pandas as pd


print(pd)


text1 = 'Your feedback is important to us! Follow the link below and take a quick survey to help us serve you better in the future!'
text2 = text1.lower().strip().split(' ')
print(set(text2))

