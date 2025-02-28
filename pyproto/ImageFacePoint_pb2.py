# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/ImageFacePoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/ImageFacePoint.proto',
  package='com.tencent.qqlive.protocol.pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cpyproto/ImageFacePoint.proto\x12\x1e\x63om.tencent.qqlive.protocol.pb\"T\n\x0eImageFacePoint\x12\x14\n\x07x_float\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x14\n\x07y_float\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\n\n\x08_x_floatB\n\n\x08_y_floatb\x06proto3'
)




_IMAGEFACEPOINT = _descriptor.Descriptor(
  name='ImageFacePoint',
  full_name='com.tencent.qqlive.protocol.pb.ImageFacePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_float', full_name='com.tencent.qqlive.protocol.pb.ImageFacePoint.x_float', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y_float', full_name='com.tencent.qqlive.protocol.pb.ImageFacePoint.y_float', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
      name='_x_float', full_name='com.tencent.qqlive.protocol.pb.ImageFacePoint._x_float',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_y_float', full_name='com.tencent.qqlive.protocol.pb.ImageFacePoint._y_float',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=64,
  serialized_end=148,
)

_IMAGEFACEPOINT.oneofs_by_name['_x_float'].fields.append(
  _IMAGEFACEPOINT.fields_by_name['x_float'])
_IMAGEFACEPOINT.fields_by_name['x_float'].containing_oneof = _IMAGEFACEPOINT.oneofs_by_name['_x_float']
_IMAGEFACEPOINT.oneofs_by_name['_y_float'].fields.append(
  _IMAGEFACEPOINT.fields_by_name['y_float'])
_IMAGEFACEPOINT.fields_by_name['y_float'].containing_oneof = _IMAGEFACEPOINT.oneofs_by_name['_y_float']
DESCRIPTOR.message_types_by_name['ImageFacePoint'] = _IMAGEFACEPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageFacePoint = _reflection.GeneratedProtocolMessageType('ImageFacePoint', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEFACEPOINT,
  '__module__' : 'pyproto.ImageFacePoint_pb2'
  # @@protoc_insertion_point(class_scope:com.tencent.qqlive.protocol.pb.ImageFacePoint)
  })
_sym_db.RegisterMessage(ImageFacePoint)


# @@protoc_insertion_point(module_scope)
