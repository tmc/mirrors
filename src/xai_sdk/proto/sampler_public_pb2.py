# fmt: off
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sampler_public.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from .google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14sampler_public.proto\x12\nprompt_ide\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8d\x01\n\x13SampleTokensRequest\x12\x0e\n\x06prompt\x18\x01 \x03(\r\x12,\n\x08settings\x18\x02 \x01(\x0b\x32\x1a.prompt_ide.SampleSettings\x12\x18\n\x10return_attention\x18\x04 \x01(\x08\x12\x12\n\nmodel_name\x18\x05 \x01(\tJ\x04\x08\x03\x10\x04J\x04\x08\x06\x10\x07\"w\n\x14SampleTokensResponse\x12\"\n\x05token\x18\x01 \x01(\x0b\x32\x11.prompt_ide.TokenH\x00\x12)\n\x06\x62udget\x18\x02 \x01(\x0b\x32\x17.prompt_ide.TokenBudgetH\x00\x42\n\n\x08responseJ\x04\x08\x03\x10\x04\"\xe9\x01\n\x0eSampleSettings\x12\x0f\n\x07max_len\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\x12\x11\n\tnucleus_p\x18\x03 \x01(\x02\x12\x13\n\x0bstop_tokens\x18\x04 \x03(\t\x12\x14\n\x0cstop_strings\x18\x07 \x03(\t\x12\x10\n\x08rng_seed\x18\x05 \x01(\x04\x12.\n\x0e\x61llowed_tokens\x18\x06 \x03(\x0b\x32\x16.prompt_ide.InputToken\x12\x31\n\x11\x64isallowed_tokens\x18\x08 \x03(\x0b\x32\x16.prompt_ide.InputToken\"A\n\nInputToken\x12\x16\n\x0cstring_token\x18\x01 \x01(\tH\x00\x12\x12\n\x08token_id\x18\x02 \x01(\rH\x00\x42\x07\n\x05token\"\xca\x01\n\x05Token\x12&\n\x0b\x66inal_logit\x18\x01 \x01(\x0b\x32\x11.prompt_ide.Logit\x12 \n\x05top_k\x18\x04 \x03(\x0b\x32\x11.prompt_ide.Logit\x12\x11\n\tattention\x18\x05 \x03(\x02\x12/\n\ntoken_type\x18\x03 \x01(\x0e\x32\x1b.prompt_ide.Token.TokenType\"-\n\tTokenType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04USER\x10\x01\x12\t\n\x05MODEL\x10\x02J\x04\x08\x02\x10\x03\"=\n\x05Logit\x12\x10\n\x08token_id\x18\x01 \x01(\r\x12\x14\n\x0cstring_token\x18\x02 \x01(\t\x12\x0c\n\x04prob\x18\x03 \x01(\x02\"3\n\x0fTokenizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\"5\n\x10TokenizeResponse\x12!\n\x06tokens\x18\x01 \x03(\x0b\x32\x11.prompt_ide.Token\"N\n\x18ListTransactionsResponse\x12\x32\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1c.prompt_ide.TokenTransaction\"\x95\x01\n\x10TokenTransaction\x12\x19\n\x11num_prompt_tokens\x18\x01 \x01(\x05\x12\x1c\n\x14num_generated_tokens\x18\x02 \x01(\x05\x12\x17\n\x0f\x63ost_multiplier\x18\x03 \x01(\x05\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\x0bTokenBudget\x12\x13\n\x0btoken_limit\x18\x01 \x01(\x05\x12\x14\n\x0ctokens_spent\x18\x02 \x01(\x05\x32\xcd\x03\n\x07Sampler\x12{\n\x0cSampleTokens\x12\x1f.prompt_ide.SampleTokensRequest\x1a .prompt_ide.SampleTokensResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/rest/sampler/sample-tokens:\x01*0\x01\x12h\n\x08Tokenize\x12\x1b.prompt_ide.TokenizeRequest\x1a\x1c.prompt_ide.TokenizeResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/rest/sampler/tokenize:\x01*\x12t\n\x10ListTransactions\x12\x16.google.protobuf.Empty\x1a$.prompt_ide.ListTransactionsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/rest/sampler/transactions\x12\x65\n\x0eGetTokenBudget\x12\x16.google.protobuf.Empty\x1a\x17.prompt_ide.TokenBudget\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/rest/sampler/token-budgetB\x1cZ\x1ax.ai/prompt_ide;prompt_ideb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sampler_public_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032x.ai/prompt_ide;prompt_ide'
  _SAMPLER.methods_by_name['SampleTokens']._options = None
  _SAMPLER.methods_by_name['SampleTokens']._serialized_options = b'\202\323\344\223\002 \"\033/rest/sampler/sample-tokens:\001*'
  _SAMPLER.methods_by_name['Tokenize']._options = None
  _SAMPLER.methods_by_name['Tokenize']._serialized_options = b'\202\323\344\223\002\033\"\026/rest/sampler/tokenize:\001*'
  _SAMPLER.methods_by_name['ListTransactions']._options = None
  _SAMPLER.methods_by_name['ListTransactions']._serialized_options = b'\202\323\344\223\002\034\022\032/rest/sampler/transactions'
  _SAMPLER.methods_by_name['GetTokenBudget']._options = None
  _SAMPLER.methods_by_name['GetTokenBudget']._serialized_options = b'\202\323\344\223\002\034\022\032/rest/sampler/token-budget'
  _globals['_SAMPLETOKENSREQUEST']._serialized_start=129
  _globals['_SAMPLETOKENSREQUEST']._serialized_end=270
  _globals['_SAMPLETOKENSRESPONSE']._serialized_start=272
  _globals['_SAMPLETOKENSRESPONSE']._serialized_end=391
  _globals['_SAMPLESETTINGS']._serialized_start=394
  _globals['_SAMPLESETTINGS']._serialized_end=627
  _globals['_INPUTTOKEN']._serialized_start=629
  _globals['_INPUTTOKEN']._serialized_end=694
  _globals['_TOKEN']._serialized_start=697
  _globals['_TOKEN']._serialized_end=899
  _globals['_TOKEN_TOKENTYPE']._serialized_start=848
  _globals['_TOKEN_TOKENTYPE']._serialized_end=893
  _globals['_LOGIT']._serialized_start=901
  _globals['_LOGIT']._serialized_end=962
  _globals['_TOKENIZEREQUEST']._serialized_start=964
  _globals['_TOKENIZEREQUEST']._serialized_end=1015
  _globals['_TOKENIZERESPONSE']._serialized_start=1017
  _globals['_TOKENIZERESPONSE']._serialized_end=1070
  _globals['_LISTTRANSACTIONSRESPONSE']._serialized_start=1072
  _globals['_LISTTRANSACTIONSRESPONSE']._serialized_end=1150
  _globals['_TOKENTRANSACTION']._serialized_start=1153
  _globals['_TOKENTRANSACTION']._serialized_end=1302
  _globals['_TOKENBUDGET']._serialized_start=1304
  _globals['_TOKENBUDGET']._serialized_end=1360
  _globals['_SAMPLER']._serialized_start=1363
  _globals['_SAMPLER']._serialized_end=1824
# @@protoc_insertion_point(module_scope)
