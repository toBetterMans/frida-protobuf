# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/AttentTimeConfigType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/AttentTimeConfigType.proto',
  package='com.tencent.qqlive.protocol.pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"pyproto/AttentTimeConfigType.proto\x12\x1e\x63om.tencent.qqlive.protocol.pb*\xa2\x01\n\x14\x41ttentTimeConfigType\x12\'\n#ATTENT_TIME_CONFIG_TYPE_UNSPECIFIED\x10\x00\x12.\n*ATTENT_TIME_CONFIG_TYPE_WITH_EXPLICIT_TIME\x10\x01\x12\x31\n-ATTENT_TIME_CONFIG_TYPE_WITHOUT_EXPLICIT_TIME\x10\x02\x62\x06proto3'
)

_ATTENTTIMECONFIGTYPE = _descriptor.EnumDescriptor(
  name='AttentTimeConfigType',
  full_name='com.tencent.qqlive.protocol.pb.AttentTimeConfigType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATTENT_TIME_CONFIG_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTENT_TIME_CONFIG_TYPE_WITH_EXPLICIT_TIME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTENT_TIME_CONFIG_TYPE_WITHOUT_EXPLICIT_TIME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=71,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_ATTENTTIMECONFIGTYPE)

AttentTimeConfigType = enum_type_wrapper.EnumTypeWrapper(_ATTENTTIMECONFIGTYPE)
ATTENT_TIME_CONFIG_TYPE_UNSPECIFIED = 0
ATTENT_TIME_CONFIG_TYPE_WITH_EXPLICIT_TIME = 1
ATTENT_TIME_CONFIG_TYPE_WITHOUT_EXPLICIT_TIME = 2


DESCRIPTOR.enum_types_by_name['AttentTimeConfigType'] = _ATTENTTIMECONFIGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
