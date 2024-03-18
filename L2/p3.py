import pandas as pd
import seaborn as sn
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
 
data = {'Y_actual': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No','Yes', 'No'],
        'Y_predicted':['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No' , 'Yes', 'No', 'No', 'No']}
 
df = pd.DataFrame(data, columns=['Y_actual', 'Y_predicted'])
 
print(df['Y_predicted'])
my_confusion = pd.crosstab(df['Y_actual'], df['Y_predicted'], rownames=['Actual'], colnames=['Predicted'])
plt.subplot(1,2,1)
sn.heatmap(my_confusion, annot=True)
 
 
#Convert Yes/No to 1/0
df['Y_actual']    = df['Y_actual'].map({'Yes':1, 'No':0})
df['Y_predicted'] = df['Y_predicted'].map({'Yes':1, 'No':0})
 
 
my_Converted_confusion = pd.crosstab(df['Y_actual'], df['Y_predicted'], rownames=['Actual'], colnames=['Predictted'])
plt.subplot(1,2,2)
sn.heatmap(my_Converted_confusion, annot=True)