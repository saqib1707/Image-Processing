Image Registration: Image registration invloves matching features in a set of images or using direct alignment methods that search for image alignments that minimize the sum of absolute difference between overlapping pixels. In image registration, to estimate a robust model from the data, a common model used is RANSAC(random sample Consensus). It is a iterative method and hence used for estimating a parameter for a mathematical model from sets of observed data points which may contain outliers.The algo is non-deterministic with this probability increasing as the number of iterations increases. 
inliers- whose distribution can be fitted by a mathematical model and outliers- are those whose data do not fit the model.Outliers are points which come from erroneous points and incorrect measurements. 
For the problem of homography estimation, RANSAC works by trying to fit several models using some of the point pairs and then checking if the models were able to relate most of the points.The best model i.e the homography with highest number of correct matches is then chosen as the answer to the problem . thus if the number of outliers to the data is very less then ransac gives a decent model fitting the data.

ransac pseudo code:

while iterations<k
    maybeinliers= n randomly selected points from the dataset
    alsoinliers = empty set
    maybemodel = model parameters fitted to maybeinliers
    for every point in dataset and not in maybeinlier:
        if point value fits the maybemodel with an error smaller than t
            add point to alsoinlier
    
    if no. of points in alsoinlier > d:
        bettermodel = model parameter fitted to both alsoinlier as well as maybeinlier
        thiserr = a measure of how well model fits these points
        if thiserr < besterr:
            bestmodel = bettermodel
            besterr = thiserr
