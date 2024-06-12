# fmt: off
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stateless_chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import chat_pb2 as chat__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14stateless_chat.proto\x12\nprompt_ide\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\nchat.proto\"\xeb\x02\n\x15StatelessConversation\x12!\n\x19stateless_conversation_id\x18\x05 \x01(\t\x12\x30\n\tresponses\x18\x01 \x03(\x0b\x32\x1d.prompt_ide.StatelessResponse\x12\x1a\n\x12system_prompt_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x1f\n\x17\x65xpose_username_to_grok\x18\x06 \x01(\x08\x12\x16\n\x0e\x64isable_search\x18\x07 \x01(\x08\x12\x1f\n\x17\x65nable_image_generation\x18\x08 \x01(\x08\x12\x12\n\nmodel_name\x18\t \x01(\t\x12\x18\n\x10x_posts_as_field\x18\n \x01(\x08\x12\x39\n\x12\x61\x64\x64itional_options\x18\x0b \x01(\x0b\x32\x1d.prompt_ide.AdditionalOptions\"\xe0\x02\n\x11StatelessResponse\x12\x34\n\x06sender\x18\x01 \x01(\x0e\x32$.prompt_ide.StatelessResponse.Sender\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\t\x12\x12\n\nquery_type\x18\x05 \x01(\t\x12:\n\x10image_attachment\x18\x06 \x01(\x0b\x32\x1b.prompt_ide.ImageAttachmentH\x00\x88\x01\x01\x12\x12\n\nx_post_ids\x18\x07 \x03(\t\x12/\n\tdebug_log\x18\x08 \x01(\x0b\x32\x1c.prompt_ide.ResponseDebugLog\x12\x14\n\x0cimage_inputs\x18\t \x03(\t\"/\n\x06Sender\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05HUMAN\x10\x01\x12\r\n\tASSISTANT\x10\x02\x42\x13\n\x11_image_attachmentJ\x04\x08\x04\x10\x05\"<\n\x0fImageAttachment\x12\x13\n\x0bimage_bytes\x18\x01 \x01(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t\":\n DeleteLoggedConversationsRequest\x12\x16\n\x0e\x61\x63\x63ounting_key\x18\x01 \x01(\t2\xa8\x03\n\rStatelessChat\x12\x7f\n\x0b\x41\x64\x64Response\x12!.prompt_ide.StatelessConversation\x1a\x1d.prompt_ide.StatelessResponse\",\x82\xd3\xe4\x93\x02&\"!/rest/stateless-chat/add-response:\x01*0\x01\x12\x7f\n\x0fLogForDebugging\x12!.prompt_ide.StatelessConversation\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+\"&/rest/stateless-chat/log-for-debugging:\x01*\x12\x94\x01\n\x19\x44\x65leteLoggedConversations\x12,.prompt_ide.DeleteLoggedConversationsRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+*)/rest/stateless-chat/logged-conversationsB\x1cZ\x1ax.ai/prompt_ide;prompt_ideb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stateless_chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032x.ai/prompt_ide;prompt_ide'
  _STATELESSCHAT.methods_by_name['AddResponse']._options = None
  _STATELESSCHAT.methods_by_name['AddResponse']._serialized_options = b'\202\323\344\223\002&\"!/rest/stateless-chat/add-response:\001*'
  _STATELESSCHAT.methods_by_name['LogForDebugging']._options = None
  _STATELESSCHAT.methods_by_name['LogForDebugging']._serialized_options = b'\202\323\344\223\002+\"&/rest/stateless-chat/log-for-debugging:\001*'
  _STATELESSCHAT.methods_by_name['DeleteLoggedConversations']._options = None
  _STATELESSCHAT.methods_by_name['DeleteLoggedConversations']._serialized_options = b'\202\323\344\223\002+*)/rest/stateless-chat/logged-conversations'
  _globals['_STATELESSCONVERSATION']._serialized_start=108
  _globals['_STATELESSCONVERSATION']._serialized_end=471
  _globals['_STATELESSRESPONSE']._serialized_start=474
  _globals['_STATELESSRESPONSE']._serialized_end=826
  _globals['_STATELESSRESPONSE_SENDER']._serialized_start=752
  _globals['_STATELESSRESPONSE_SENDER']._serialized_end=799
  _globals['_IMAGEATTACHMENT']._serialized_start=828
  _globals['_IMAGEATTACHMENT']._serialized_end=888
  _globals['_DELETELOGGEDCONVERSATIONSREQUEST']._serialized_start=890
  _globals['_DELETELOGGEDCONVERSATIONSREQUEST']._serialized_end=948
  _globals['_STATELESSCHAT']._serialized_start=951
  _globals['_STATELESSCHAT']._serialized_end=1375
# @@protoc_insertion_point(module_scope)
