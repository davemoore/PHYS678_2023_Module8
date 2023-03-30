import sys
import numpy as np

def estimate_pi(n):
  """ This function estimates pi via monte carlo, by drawing random numbers in
      a square and finding the fraction lying within an inscribed circle. The 
      resulting estimate is printed to the terminal.

      Parameters:
        n: number of random draws to perform
      
      Returns: 
        estimate: estimated value of pi
  """
  k = 0
  for i in range(n):
    xy = np.random.rand(2) #draw two random numbers n times from the interval [0,1]
    xy = 2*(xy - 0.5) #convert these numbers to random on [-1,1]
    k += (xy[0]**2 + xy[1]**2 <= 1) #sum up the number of elements within the circle of radius=1 to find k
                                            #the terms in square brackets index the rows and columns of the 
  estimate = 4*k/n
  print("Estimate of pi with %d trials is: %f"%(n, estimate))
  return estimate

## Number to append to filename, if specified at the command line
if len(sys.argv) > 1:
  if( len(sys.argv) > 2 ):
    print("Requies only one command line argument specifying file name, ignoring extra arguments")
  fnum = sys.argv[1] 
else:
  fnum = "0"

npts = int(1e7) #number of points to use in calculation
est = estimate_pi(npts)
np.savetxt('pi_' + fnum + '.txt', [est,]) #save to file, appending number from above
