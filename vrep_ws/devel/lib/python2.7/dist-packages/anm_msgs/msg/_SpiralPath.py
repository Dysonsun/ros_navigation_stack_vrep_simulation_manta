# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from anm_msgs/SpiralPath.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import anm_msgs.msg
import std_msgs.msg

class SpiralPath(genpy.Message):
  _md5sum = "cbdb9aa67633991647d7cd82b98e0d51"
  _type = "anm_msgs/SpiralPath"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This message is a parametric representation of a spiral curve
# The curve is used to define a local path
#
# a, b, c, d = parameters that define the spiral curve
# sf = total length of curve (meters)
# reference_state = current position on the curve
# goal_state = endpoint of the curve

Header header
float64 a
float64 b
float64 c
float64 d
float64 sf
PathState reference_state
PathState goal_state

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: anm_msgs/PathState
# This message defines a position along a spiral curve
#
# x = x position in global frame (meters)
# y = y position in global frame (meters)
# theta = angle of curve tangent at position x, y (radians)
# k = curvature of curve at position x, y (1/meters)
# s = length in along (meters)

float64 x
float64 y
float64 theta
float64 k
float64 s
"""
  __slots__ = ['header','a','b','c','d','sf','reference_state','goal_state']
  _slot_types = ['std_msgs/Header','float64','float64','float64','float64','float64','anm_msgs/PathState','anm_msgs/PathState']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,a,b,c,d,sf,reference_state,goal_state

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SpiralPath, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.a is None:
        self.a = 0.
      if self.b is None:
        self.b = 0.
      if self.c is None:
        self.c = 0.
      if self.d is None:
        self.d = 0.
      if self.sf is None:
        self.sf = 0.
      if self.reference_state is None:
        self.reference_state = anm_msgs.msg.PathState()
      if self.goal_state is None:
        self.goal_state = anm_msgs.msg.PathState()
    else:
      self.header = std_msgs.msg.Header()
      self.a = 0.
      self.b = 0.
      self.c = 0.
      self.d = 0.
      self.sf = 0.
      self.reference_state = anm_msgs.msg.PathState()
      self.goal_state = anm_msgs.msg.PathState()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_15d().pack(_x.a, _x.b, _x.c, _x.d, _x.sf, _x.reference_state.x, _x.reference_state.y, _x.reference_state.theta, _x.reference_state.k, _x.reference_state.s, _x.goal_state.x, _x.goal_state.y, _x.goal_state.theta, _x.goal_state.k, _x.goal_state.s))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.reference_state is None:
        self.reference_state = anm_msgs.msg.PathState()
      if self.goal_state is None:
        self.goal_state = anm_msgs.msg.PathState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 120
      (_x.a, _x.b, _x.c, _x.d, _x.sf, _x.reference_state.x, _x.reference_state.y, _x.reference_state.theta, _x.reference_state.k, _x.reference_state.s, _x.goal_state.x, _x.goal_state.y, _x.goal_state.theta, _x.goal_state.k, _x.goal_state.s,) = _get_struct_15d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_15d().pack(_x.a, _x.b, _x.c, _x.d, _x.sf, _x.reference_state.x, _x.reference_state.y, _x.reference_state.theta, _x.reference_state.k, _x.reference_state.s, _x.goal_state.x, _x.goal_state.y, _x.goal_state.theta, _x.goal_state.k, _x.goal_state.s))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.reference_state is None:
        self.reference_state = anm_msgs.msg.PathState()
      if self.goal_state is None:
        self.goal_state = anm_msgs.msg.PathState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 120
      (_x.a, _x.b, _x.c, _x.d, _x.sf, _x.reference_state.x, _x.reference_state.y, _x.reference_state.theta, _x.reference_state.k, _x.reference_state.s, _x.goal_state.x, _x.goal_state.y, _x.goal_state.theta, _x.goal_state.k, _x.goal_state.s,) = _get_struct_15d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_15d = None
def _get_struct_15d():
    global _struct_15d
    if _struct_15d is None:
        _struct_15d = struct.Struct("<15d")
    return _struct_15d