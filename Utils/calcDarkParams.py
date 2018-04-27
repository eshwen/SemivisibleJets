#!/bin/env python 
# Calculates alpha_d from Lambda_d, n_c, n_f
import math

def calcAlphaD(n_c, n_f, Lambda_d):
    b_param = calcBParam(n_c, n_f)
    alpha_d = -2*math.pi / ( b_param * math.log(Lambda_d/1000) )
    return alpha_d

def calcLambdaD(n_c, n_f, alpha_d):
    b_param = calcBParam(n_c, n_f)
    Lambda_d = 1000 * math.exp( -2*math.pi / (alpha_d*b_param) )
    return Lambda_d

def calcBParam(n_c, n_f):
    b_param = (11/3)*n_c - (2/3)*n_f
    return b_param
