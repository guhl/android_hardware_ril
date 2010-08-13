# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='ctrl.proto',
  package='ril_proto',
  serialized_pb='\n\nctrl.proto\x12\tril_proto\x1a\tril.proto\"9\n\x11\x43trlRspRadioState\x12$\n\x05state\x18\x01 \x02(\x0e\x32\x15.ril_proto.RadioState\"9\n\x11\x43trlReqRadioState\x12$\n\x05state\x18\x01 \x02(\x0e\x32\x15.ril_proto.RadioState*X\n\x07\x43trlCmd\x12\x11\n\rCTRL_CMD_ECHO\x10\x00\x12\x1c\n\x18\x43TRL_CMD_GET_RADIO_STATE\x10\x01\x12\x1c\n\x18\x43TRL_CMD_SET_RADIO_STATE\x10\x02*5\n\nCtrlStatus\x12\x12\n\x0e\x43TRL_STATUS_OK\x10\x00\x12\x13\n\x0f\x43TRL_STATUS_ERR\x10\x01\x42\x37\n(com.android.internal.telephony.ril_protoB\x0bRilCtrlCmds')

_CTRLCMD = descriptor.EnumDescriptor(
  name='CtrlCmd',
  full_name='ril_proto.CtrlCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CTRL_CMD_ECHO', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CTRL_CMD_GET_RADIO_STATE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CTRL_CMD_SET_RADIO_STATE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=154,
  serialized_end=242,
)


_CTRLSTATUS = descriptor.EnumDescriptor(
  name='CtrlStatus',
  full_name='ril_proto.CtrlStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CTRL_STATUS_OK', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CTRL_STATUS_ERR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=244,
  serialized_end=297,
)


CTRL_CMD_ECHO = 0
CTRL_CMD_GET_RADIO_STATE = 1
CTRL_CMD_SET_RADIO_STATE = 2
CTRL_STATUS_OK = 0
CTRL_STATUS_ERR = 1



_CTRLRSPRADIOSTATE = descriptor.Descriptor(
  name='CtrlRspRadioState',
  full_name='ril_proto.CtrlRspRadioState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='state', full_name='ril_proto.CtrlRspRadioState.state', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=93,
)


_CTRLREQRADIOSTATE = descriptor.Descriptor(
  name='CtrlReqRadioState',
  full_name='ril_proto.CtrlReqRadioState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='state', full_name='ril_proto.CtrlReqRadioState.state', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=95,
  serialized_end=152,
)

import ril_pb2

_CTRLRSPRADIOSTATE.fields_by_name['state'].enum_type = ril_pb2._RADIOSTATE
_CTRLREQRADIOSTATE.fields_by_name['state'].enum_type = ril_pb2._RADIOSTATE

class CtrlRspRadioState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CTRLRSPRADIOSTATE
  
  # @@protoc_insertion_point(class_scope:ril_proto.CtrlRspRadioState)

class CtrlReqRadioState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CTRLREQRADIOSTATE
  
  # @@protoc_insertion_point(class_scope:ril_proto.CtrlReqRadioState)

# @@protoc_insertion_point(module_scope)