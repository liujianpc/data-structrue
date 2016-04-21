#!/usr/bin/env python
#coding=utf-8
class _const:
    class ConstError(TypeError):
        pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError,"can not rebind const instance attribute (%s)" % name
        self.__dict__[name] = value
    def __delattr__(self, name):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't unbind const const instance attribute (%s)" % name

        raise AttributeError, "const instance has no attribute '%s'" % name

import sys
sys.modules[__name__] = _const()
