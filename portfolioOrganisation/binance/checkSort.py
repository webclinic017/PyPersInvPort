import pandas as pd 

# There's something fishy about the df.sort_values() function
# If you write with double quotation marks it wouldn't work
# But if you write with single quotation marks then it would
# I've put this here for checking if a df has really been sorted.

df = pd.read_csv('biAcc2.csv')

def arraySortedOrNot(arr):
     
    # Calculating length
    n = len(arr)
 
    # Array has one or no element or the
    # rest are already checked and approved.
    if n == 1 or n == 0:
        return True
 
    # Recursion applied till last element
    return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])

def arrSort(arr):
    if arraySortedOrNot(arr):
        print("Yes")
    else:
        print("No")

arrSort(df['time'].to_list())


# df = df.sort_values(by='Names')
# print(df)