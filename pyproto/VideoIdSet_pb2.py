# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/VideoIdSet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/VideoIdSet.proto',
  package='com.tencent.qqlive.protocol.pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18pyproto/VideoIdSet.proto\x12\x1e\x63om.tencent.qqlive.protocol.pb\"Z\n\nVideoIdSet\x12\x10\n\x03vid\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03\x63id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03lid\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x06\n\x04_vidB\x06\n\x04_cidB\x06\n\x04_lidb\x06proto3'
)




_VIDEOIDSET = _descriptor.Descriptor(
  name='VideoIdSet',
  full_name='com.tencent.qqlive.protocol.pb.VideoIdSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vid', full_name='com.tencent.qqlive.protocol.pb.VideoIdSet.vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cid', full_name='com.tencent.qqlive.protocol.pb.VideoIdSet.cid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lid', full_name='com.tencent.qqlive.protocol.pb.VideoIdSet.lid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_vid', full_name='com.tencent.qqlive.protocol.pb.VideoIdSet._vid',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cid', full_name='com.tencent.qqlive.protocol.pb.VideoIdSet._cid',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_lid', full_name='com.tencent.qqlive.protocol.pb.VideoIdSet._lid',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=60,
  serialized_end=150,
)

_VIDEOIDSET.oneofs_by_name['_vid'].fields.append(
  _VIDEOIDSET.fields_by_name['vid'])
_VIDEOIDSET.fields_by_name['vid'].containing_oneof = _VIDEOIDSET.oneofs_by_name['_vid']
_VIDEOIDSET.oneofs_by_name['_cid'].fields.append(
  _VIDEOIDSET.fields_by_name['cid'])
_VIDEOIDSET.fields_by_name['cid'].containing_oneof = _VIDEOIDSET.oneofs_by_name['_cid']
_VIDEOIDSET.oneofs_by_name['_lid'].fields.append(
  _VIDEOIDSET.fields_by_name['lid'])
_VIDEOIDSET.fields_by_name['lid'].containing_oneof = _VIDEOIDSET.oneofs_by_name['_lid']
DESCRIPTOR.message_types_by_name['VideoIdSet'] = _VIDEOIDSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoIdSet = _reflection.GeneratedProtocolMessageType('VideoIdSet', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOIDSET,
  '__module__' : 'pyproto.VideoIdSet_pb2'
  # @@protoc_insertion_point(class_scope:com.tencent.qqlive.protocol.pb.VideoIdSet)
  })
_sym_db.RegisterMessage(VideoIdSet)


# @@protoc_insertion_point(module_scope)
