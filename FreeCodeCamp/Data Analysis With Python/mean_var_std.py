import numpy as np

# numpy array with 9 digits
digits = np.array([450, 43, 67, 23, 56, 78, 45, 33, 870])


# function to calculate mean, var, std, max, sum for both axis and flattened axis.


def Calculate(digits):
  # Mean Calculation  
  def mean(digits):
        global maxis1, maxis2, mflattaned
        maxis1 = np.mean(digits, 0)
        maxis2 = np.mean(digits, 1)
        flattan = digits.flatten()
        mflattaned = np.mean(flattan)
        maxis1 = maxis1.tolist()
        maxis2 = maxis2.tolist()
        

  # Variance Calculation
    def variance(digits):
        global vaxis1, vaxis2, vflattaned
        vaxis1 = np.var(digits, 0)
        vaxis2 = np.var(digits, 1)
        flattan = digits.flatten()
        vflattaned = np.var(flattan)
        vaxis1 = vaxis1.tolist()
        vaxis2 = vaxis2.tolist()

 
# S. Deviation Calculation
    def std(digits):
        global sdaxis1, sdaxis2, sdflattaned
        sdaxis1 = np.std(digits, 0)
        sdaxis2 = np.std(digits, 1)
        flattan = digits.flatten()
        sdflattaned = np.std(flattan)
        sdaxis1 = sdaxis1.tolist()
        sdaxis2 = sdaxis2.tolist()


# Max value
    def max(digits):
        global mmaxis1, mmaxis2, mmflattaned
        mmaxis1 = np.max(digits, 0)
        mmaxis2 = np.max(digits, 1)
        flattan = digits.flatten()
        mmflattaned = np.max(flattan)
        mmaxis1 = mmaxis1.tolist()
        mmaxis2 = mmaxis2.tolist()

 
# Min value
    def min(digits):
        global miaxis1, miaxis2, miflattaned
        miaxis1 = np.min(digits, 0)
        miaxis2 = np.min(digits, 1)
        flattan = digits.flatten()
        miflattaned = np.min(flattan)
        miaxis1 = miaxis1.tolist()
        miaxis2 = miaxis2.tolist()
 

# sum of axis
    def sum(digits):
        global saxis1, saxis2, sflattaned
        saxis1 = np.sum(digits, 0)
        saxis2 = np.sum(digits, 1)
        flattan = digits.flatten()
        sflattaned = np.sum(flattan)
        saxis1 = saxis1.tolist()
        saxis2 = saxis2.tolist()
    mean(digits)
    variance(digits)
    std(digits)
    max(digits)
    min(digits)
    sum(digits)


    Result = {
        'Mean':[maxis1, maxis2, mflattaned],
        'Variance': [vaxis1, vaxis2, vflattaned],
        'standard deviation': [sdaxis1, sdaxis2, sdflattaned],
        'max': [mmaxis1, mmaxis2, mmflattaned],
        'min': [miaxis1, miaxis2, miflattaned],
        'sum': [saxis1, saxis2, sflattaned]
    }

    for key, value in Result.items():
        print(key, ":", value)


# Checking that the list contains 9 digits
if len(digits) != 9:
    print("List must contain 9 numbers!")
# if it contains 9 then we reshape and execute the calculate function
else:
    digits = digits.reshape(3,3)
    Calculate(digits)
