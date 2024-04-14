import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.dpi']=100

def contractiveMap(alpha,beta,initial_point,iterations):
    f = lambda xn: alpha*xn + beta
    seq = [initial_point]
    x = initial_point
    for i in range(iterations-1):
        x = f(x)
        seq.append(x)
    return seq

def plot_contractiveMap(alpha,beta):
  fig,ax = plt.subplots(1,3)
  fig.set_figwidth(4.5*3)
  fig.suptitle("$f(x_n) = {}x_n+{}$".format(alpha,beta))
  ax[0].plot(range(30),contractiveMap(alpha,beta,10,30),label="$x_0 = 10$", color ="red",linestyle = "-")
  ax[0].set_xlabel("Number of iterations")
  ax[0].set_ylabel("$f(x_n)$")
  ax[0].legend()
  ax[0].grid(linestyle = '--', linewidth = 0.5)

  ax[1].plot(range(30),contractiveMap(alpha,beta,20,30),label="$x_0 = 20$",color = "green",linestyle = "-")
  ax[1].set_xlabel("Number of iterations")
  ax[1].set_ylabel("$f(x_n)$")
  ax[1].legend()
  ax[1].grid(linestyle = '--', linewidth = 0.5)

  ax[2].plot(range(30),contractiveMap(alpha,beta,15,30),label="$x_0 = 15$",color = "blue",linestyle = "-")
  ax[2].set_xlabel("Number of iterations")
  ax[2].set_ylabel("$f(x_n)$")
  ax[2].legend()
  ax[2].grid(linestyle = '--', linewidth = 0.5)

if __name__ == "__main__":
  
 plot_contractiveMap(.8,3)
 plt.show()