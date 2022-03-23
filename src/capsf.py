from __future__ import print_function, absolute_import, division
import capsf
import f90wrap.runtime
import logging

def caps_f(y, n, stiffness, pct):
    """
    res = caps_f(y, n, stiffness, pct)
    
    
    Defined at capsf.f95 lines 35-179
    
    Parameters
    ----------
    y : float
    n : int
    stiffness : int
    pct : float
    
    Returns
    -------
    res : float
    
    """
    res = capsf.f90wrap_caps_f(y=y, n=n, stiffness=stiffness, pct=pct)
    return res

