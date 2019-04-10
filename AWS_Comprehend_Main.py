import AWS_Comprehend
import os
final_list = []
for files in os.listdir('C:/Users/pauls/AWS_Medical'):
    final_list.append(AWS_Comprehend.run_model('C:/Users/pauls/AWS_Medical/'+files))
file = open('C:/Users/pauls/results.txt', 'w') 
file.write(str(final_list))
file.close()
print (final_list)