'''import numpy as np
x=np.array([1,2,3,4])
y=np.array([3,4,5,6])
#print(np.sum(x*y))
print("mean:",np.mean(x))
print("mean:",np.mean(y))
'''
import numpy as np 
import matplotlib.pyplot as plt 
  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
def predication_values(x,b):
    print("inside the function")
    print(x)
    y_values=[]
    y_values.append(b[0] + b[1]*x)
    return y_values

def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
  
def main(): 
    # observations 
    x = np.array([8266,8777,8682,9000,9378,8368,8496,8982,8363,8444,15502,16066,16760,17639,16920,18865,19977,21476,22076,22192,23681,25321,27486,30114,33239,35272,36303,
40054,42589,44526,46681]) 
    y = np.array([7593,8494,8198,8561,9052,8551,8280,8960,8278,8198,14727,15728,15806,17371,16859,18695,20683,21586,22466,22543,24273,24409,27921,30562,33271,37436,37183,
43354,45277,47100,48881]) 
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {}\\nb_1 = {}".format(b[0], b[1])) 
    '''
    a=1
    y_p=np.array([9144,9268,8954,9654,10119,9619,8709,9578,9649,9745,10154,11354,11291,11504,10909,11186,10650,11773,13388,13984,14233,14689,14291])
    Y=predication_values(y_p,b)
    y_p=list(y_p)
    print(Y)# +"  "+Y[i])'''
       
    # plotting regression line 
    plot_regression_line(x, y, b)

    
if __name__ == "__main__": 
    main() 
