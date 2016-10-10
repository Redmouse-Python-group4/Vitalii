from abc import ABCMeta, abstractmethod, abstractproperty

class Param(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def param():
    	pass