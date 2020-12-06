import numpy as np
import csv


def findCorrelation(data_path, name1, name2):
  arr1 = []
  arr2 = []

  with open(data_path, 'r') as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for row in csv_reader:
      arr1.append(float(row[name1]))
      arr2.append(float(row[name2]))

  correlation = np.corrcoef(arr1, arr2)
  return ("Correlation between " + name1 + " vs " + name2 + ": " + str(correlation[0, 1]))

print(findCorrelation("data1.csv", "Marks In Percentage", "Days Present"))
print(findCorrelation("data2.csv", "Coffee in ml", "sleep in hours"))
