# This file is generated by wxPython's SIP generator.  Do not edit by hand.
#
# Copyright: (c) 2018 by Total Control Software
# License:   wxWindows License

"""
The :class:`RichTextCtrl` is a generic, ground-up implementation of a rich
text control capable of showing multiple text styles and images.  This module
contains the control and many supporting classes needed for using the features
of the :class:`RichTextCtrl`.

.. note:: Due to some internal dynamic initialization in wxWidgets, this
          module should be imported **before** the :class:`wx.App` object is
          created.
"""

from ._richtext import *

import wx

def _RichTextRange_GetIM(self):
    """
    Returns an immutable representation of the ``wx.RichTextRange`` object, based on ``namedtuple``.
    
    This new object is hashable and can be used as a dictionary key,
    be added to sets, etc.  It can be converted back into a real ``wx.RichTextRange``
    with a simple statement like this: ``obj = wx.RichTextRange(imObj)``.
    """
    return _im_RichTextRange(*self.Get())
RichTextRange.GetIM = _RichTextRange_GetIM
del _RichTextRange_GetIM
def _RichTextRange___str__(self):
    return str(self.Get())
RichTextRange.__str__ = _RichTextRange___str__
del _RichTextRange___str__
def _RichTextRange___repr__(self):
    return "RichTextRange"+str(self.Get())
RichTextRange.__repr__ = _RichTextRange___repr__
del _RichTextRange___repr__
def _RichTextRange___len__(self):
    return len(self.Get())
RichTextRange.__len__ = _RichTextRange___len__
del _RichTextRange___len__
def _RichTextRange___nonzero__(self):
    return self.Get() != (0,0)
RichTextRange.__nonzero__ = _RichTextRange___nonzero__
del _RichTextRange___nonzero__
def _RichTextRange___bool__(self):
    return self.Get() != (0,0)
RichTextRange.__bool__ = _RichTextRange___bool__
del _RichTextRange___bool__
def _RichTextRange___reduce__(self):
    return (RichTextRange, self.Get())
RichTextRange.__reduce__ = _RichTextRange___reduce__
del _RichTextRange___reduce__
def _RichTextRange___getitem__(self, idx):
    return self.Get()[idx]
RichTextRange.__getitem__ = _RichTextRange___getitem__
del _RichTextRange___getitem__
def _RichTextRange___setitem__(self, idx, val):
    if idx == 0: self.Start = val
    elif idx == 1: self.End = val
    else: raise IndexError
RichTextRange.__setitem__ = _RichTextRange___setitem__
del _RichTextRange___setitem__
RichTextRange.__safe_for_unpickling__ = True

RICHTEXT_ALL = RichTextRange(-2, -2)
RICHTEXT_NONE = RichTextRange(-1, -1)
RICHTEXT_NO_SELECTION = RichTextRange(-2, -2)

def _RichTextRangeArray___repr__(self):
    return "RichTextRangeArray: " + repr(list(self))
RichTextRangeArray.__repr__ = _RichTextRangeArray___repr__
del _RichTextRangeArray___repr__
def _RichTextAttrArray___repr__(self):
    return "RichTextAttrArray: " + repr(list(self))
RichTextAttrArray.__repr__ = _RichTextAttrArray___repr__
del _RichTextAttrArray___repr__
def _RichTextVariantArray___repr__(self):
    return "RichTextVariantArray: " + repr(list(self))
RichTextVariantArray.__repr__ = _RichTextVariantArray___repr__
del _RichTextVariantArray___repr__
def _RichTextObjectList___repr__(self):
    return "RichTextObjectList: " + repr(list(self))
RichTextObjectList.__repr__ = _RichTextObjectList___repr__
del _RichTextObjectList___repr__
def _RichTextLineList___repr__(self):
    return "RichTextLineList: " + repr(list(self))
RichTextLineList.__repr__ = _RichTextLineList___repr__
del _RichTextLineList___repr__
def _RichTextObjectPtrArray___repr__(self):
    return "RichTextObjectPtrArray: " + repr(list(self))
RichTextObjectPtrArray.__repr__ = _RichTextObjectPtrArray___repr__
del _RichTextObjectPtrArray___repr__
def _RichTextObjectPtrArrayArray___repr__(self):
    return "RichTextObjectPtrArrayArray: " + repr(list(self))
RichTextObjectPtrArrayArray.__repr__ = _RichTextObjectPtrArrayArray___repr__
del _RichTextObjectPtrArrayArray___repr__
from collections import namedtuple
_im_RichTextRange = namedtuple('_im_RichTextRange', ['Start', 'End'])
del namedtuple

def _RichTextObjectList____repr__(self):
    return "RichTextObjectList_: " + repr(list(self))
RichTextObjectList_.__repr__ = _RichTextObjectList____repr__
del _RichTextObjectList____repr__
def _RichTextFileHandlerList___repr__(self):
    return "RichTextFileHandlerList: " + repr(list(self))
RichTextFileHandlerList.__repr__ = _RichTextFileHandlerList___repr__
del _RichTextFileHandlerList___repr__
def _RichTextDrawingHandlerList___repr__(self):
    return "RichTextDrawingHandlerList: " + repr(list(self))
RichTextDrawingHandlerList.__repr__ = _RichTextDrawingHandlerList___repr__
del _RichTextDrawingHandlerList___repr__
def _RichTextActionList___repr__(self):
    return "RichTextActionList: " + repr(list(self))
RichTextActionList.__repr__ = _RichTextActionList___repr__
del _RichTextActionList___repr__
def _RichTextCtrl_GetDefaultStyle(self):
    return self.GetDefaultStyleEx()
RichTextCtrl.GetDefaultStyle = wx.deprecated(_RichTextCtrl_GetDefaultStyle, "Use GetDefaultStyleEx instead")
del _RichTextCtrl_GetDefaultStyle
RichTextCtrl.DefaultStyle = property(RichTextCtrl.GetDefaultStyle, RichTextCtrl.SetDefaultStyle)
EVT_RICHTEXT_LEFT_CLICK = wx.PyEventBinder(wxEVT_RICHTEXT_LEFT_CLICK)
EVT_RICHTEXT_RIGHT_CLICK = wx.PyEventBinder(wxEVT_RICHTEXT_RIGHT_CLICK)
EVT_RICHTEXT_MIDDLE_CLICK = wx.PyEventBinder(wxEVT_RICHTEXT_MIDDLE_CLICK)
EVT_RICHTEXT_LEFT_DCLICK = wx.PyEventBinder(wxEVT_RICHTEXT_LEFT_DCLICK)
EVT_RICHTEXT_RETURN = wx.PyEventBinder(wxEVT_RICHTEXT_RETURN)
EVT_RICHTEXT_CHARACTER = wx.PyEventBinder(wxEVT_RICHTEXT_CHARACTER)
EVT_RICHTEXT_DELETE = wx.PyEventBinder(wxEVT_RICHTEXT_DELETE)

EVT_RICHTEXT_STYLESHEET_CHANGING = wx.PyEventBinder(wxEVT_RICHTEXT_STYLESHEET_CHANGING)
EVT_RICHTEXT_STYLESHEET_CHANGED = wx.PyEventBinder(wxEVT_RICHTEXT_STYLESHEET_CHANGED)
EVT_RICHTEXT_STYLESHEET_REPLACING = wx.PyEventBinder(wxEVT_RICHTEXT_STYLESHEET_REPLACING)
EVT_RICHTEXT_STYLESHEET_REPLACED = wx.PyEventBinder(wxEVT_RICHTEXT_STYLESHEET_REPLACED)

EVT_RICHTEXT_CONTENT_INSERTED = wx.PyEventBinder(wxEVT_RICHTEXT_CONTENT_INSERTED)
EVT_RICHTEXT_CONTENT_DELETED = wx.PyEventBinder(wxEVT_RICHTEXT_CONTENT_DELETED)
EVT_RICHTEXT_STYLE_CHANGED = wx.PyEventBinder(wxEVT_RICHTEXT_STYLE_CHANGED)
EVT_RICHTEXT_STYLE_CHANGED = wx.PyEventBinder(wxEVT_RICHTEXT_PROPERTIES_CHANGED)
EVT_RICHTEXT_SELECTION_CHANGED = wx.PyEventBinder(wxEVT_RICHTEXT_SELECTION_CHANGED)
EVT_RICHTEXT_BUFFER_RESET = wx.PyEventBinder(wxEVT_RICHTEXT_BUFFER_RESET)
EVT_RICHTEXT_FOCUS_OBJECT_CHANGED = wx.PyEventBinder(wxEVT_RICHTEXT_FOCUS_OBJECT_CHANGED)

