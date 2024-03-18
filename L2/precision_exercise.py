import numpy as np

cm = np.array(
[
[ .801, .104, .009, .006, .031, .041, .008],
[ .104, .780, .007, .003, .057, .012, .037],
[ .015, .020, .898, .012, .016, .030, .009],
[ .032, .003, .016, .910, .002, .029, .008],
[ .080, .108, .012, .013, .738, .022, .027],
[ .078, .021, .061, .021, .030, .760, .029],
[ .037, .106, .016, .006, .051, .037, .746]
])

print(cm.shape)


def precision(label,confusion_matrix):
  col = confusion_matrix[:label]
  return confusion_matrix[label, label] / col.sum()

def recall(label, confusion_matrix):
  row = confusion_matrix[label, :]
  return confusion_matrix[label, label] / row.sum()


def precision_macro_average(confusion_matrix):
  rows, columns = confusion_matrix.shape
  sum_of_precisions = 0
  for label in range(rows):
    sum_of_precisions += precision(label, confusion_matrix)

  return sum_of_precisions / rows

def recall_macro_average(confusion_matrix):
  rows, columns = confusion_matrix.shape
  sum_of_recalls = 0
  for label in range(columns): 
    sum_of_recalls += recall(label, confusion_matrix)
  return sum_of_recalls / columns

print("label precision recall")
for label in range(7):
  print(f"{label:5d} {precision(label, cm):9.3f} {recall(label, cm):6.3f}")

print("precision total:", precision_macro_average(cm))
print("recall total:", recall_macro_average(cm))

def accuracy(confusion_matrix):
  diagonal_sum = confusion_matrix.trace()
  sum_of_all_elements = confusion_matrix.sum()
  return diagonal_sum / sum_of_all_elements

print("accuracy:", accuracy(cm))