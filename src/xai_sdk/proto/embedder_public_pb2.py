# fmt: off
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: embedder_public.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x65mbedder_public.proto\x12\nprompt_ide\"1\n\x0c\x45mbedRequest\x12\r\n\x05texts\x18\x01 \x03(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\":\n\rEmbedResponse\x12)\n\nembeddings\x18\x01 \x03(\x0b\x32\x15.prompt_ide.Embedding\".\n\tEmbedding\x12\x12\n\x06values\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\r\n\x05shape\x18\x02 \x03(\x05\x32J\n\x08\x45mbedder\x12>\n\x05\x45mbed\x12\x18.prompt_ide.EmbedRequest\x1a\x19.prompt_ide.EmbedResponse\"\x00\x42\x1cZ\x1ax.ai/prompt_ide;prompt_ideb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'embedder_public_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032x.ai/prompt_ide;prompt_ide'
  _EMBEDDING.fields_by_name['values']._options = None
  _EMBEDDING.fields_by_name['values']._serialized_options = b'\020\001'
  _globals['_EMBEDREQUEST']._serialized_start=37
  _globals['_EMBEDREQUEST']._serialized_end=86
  _globals['_EMBEDRESPONSE']._serialized_start=88
  _globals['_EMBEDRESPONSE']._serialized_end=146
  _globals['_EMBEDDING']._serialized_start=148
  _globals['_EMBEDDING']._serialized_end=194
  _globals['_EMBEDDER']._serialized_start=196
  _globals['_EMBEDDER']._serialized_end=270
# @@protoc_insertion_point(module_scope)
