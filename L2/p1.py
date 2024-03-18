import sklearn
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
 
 
y_pred = [0,1,0,0,0,1,0,1,0,0,1,0]
 
y_act  = [0,1,0,0,1,1,0,0,0,0,0,0]
 
confusion = confusion_matrix(y_true=y_act, y_pred=y_pred)
 
accuracy = accuracy_score(y_act, y_pred)
 
precision = precision_score(y_act, y_pred, average=None)
 
sensitivity = recall_score(y_act, y_pred, average= None)
 
 
print("confusion_Matrix:\n", confusion)
 
print("accuracy:\n", accuracy)
print("precision:\n", precision)
print("sensitivity:\n", sensitivity)