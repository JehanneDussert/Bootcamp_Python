# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mse.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdussert <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 19:40:03 by jdussert          #+#    #+#              #
#    Updated: 2020/01/21 19:47:38 by jdussert         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mse(y, y_hat):
	"""Computes the mean squared error of two non-empty numpy.ndarray, using
a for-loop. The two arrays must have the same dimensions.
    Args:
     y: has to be an numpy.ndarray, a vector.
     y_hat: has to be an numpy.ndarray, a vector.
    Returns:
     The mean squared error of the two vectors as a float.
     None if y or y_hat are empty numpy.ndarray.
     None if y and y_hat does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
	"""
	m = np.shape(y)[0]
	if m == 0 or m != np.shape(y_hat)[0]:
	 	return None
	res = float(0)
	for i in range(m):
		res += (y_hat[i] - y[i])**2
	res /= m
	return float(res)

# Examples :
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print("Mse :\n", mse(X, Y))
