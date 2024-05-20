# fmt: off
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import sampler_public_pb2 as sampler__public__pb2


class SamplerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SampleTokens = channel.unary_stream(
                '/prompt_ide.Sampler/SampleTokens',
                request_serializer=sampler__public__pb2.SampleTokensRequest.SerializeToString,
                response_deserializer=sampler__public__pb2.SampleTokensResponse.FromString,
                )
        self.Tokenize = channel.unary_unary(
                '/prompt_ide.Sampler/Tokenize',
                request_serializer=sampler__public__pb2.TokenizeRequest.SerializeToString,
                response_deserializer=sampler__public__pb2.TokenizeResponse.FromString,
                )
        self.TokenizeAndSampleTokens = channel.unary_stream(
                '/prompt_ide.Sampler/TokenizeAndSampleTokens',
                request_serializer=sampler__public__pb2.TokenizeAndSampleTokensRequest.SerializeToString,
                response_deserializer=sampler__public__pb2.SampleTokensResponse.FromString,
                )
        self.ListTransactions = channel.unary_unary(
                '/prompt_ide.Sampler/ListTransactions',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=sampler__public__pb2.ListTransactionsResponse.FromString,
                )
        self.GetTokenBudget = channel.unary_unary(
                '/prompt_ide.Sampler/GetTokenBudget',
                request_serializer=sampler__public__pb2.GetTokenBudgetRequest.SerializeToString,
                response_deserializer=sampler__public__pb2.TokenBudget.FromString,
                )


class SamplerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SampleTokens(self, request, context):
        """Given a sequence of input tokens, returns a sampled sequence of output tokens.
        If the request is successful, the last message holds the current token budget.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Tokenize(self, request, context):
        """Tokenizes the incoming text. Result is delivered in a Logit proto with zero log probs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenizeAndSampleTokens(self, request, context):
        """Tokenizes the text and then samples from the model. This can reduce network latencies when all
        we need to do is tokenize and the immediately sample.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransactions(self, request, context):
        """Returns all token transactions in the current accounting period.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTokenBudget(self, request, context):
        """Returns the current token budget.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SamplerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SampleTokens': grpc.unary_stream_rpc_method_handler(
                    servicer.SampleTokens,
                    request_deserializer=sampler__public__pb2.SampleTokensRequest.FromString,
                    response_serializer=sampler__public__pb2.SampleTokensResponse.SerializeToString,
            ),
            'Tokenize': grpc.unary_unary_rpc_method_handler(
                    servicer.Tokenize,
                    request_deserializer=sampler__public__pb2.TokenizeRequest.FromString,
                    response_serializer=sampler__public__pb2.TokenizeResponse.SerializeToString,
            ),
            'TokenizeAndSampleTokens': grpc.unary_stream_rpc_method_handler(
                    servicer.TokenizeAndSampleTokens,
                    request_deserializer=sampler__public__pb2.TokenizeAndSampleTokensRequest.FromString,
                    response_serializer=sampler__public__pb2.SampleTokensResponse.SerializeToString,
            ),
            'ListTransactions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTransactions,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=sampler__public__pb2.ListTransactionsResponse.SerializeToString,
            ),
            'GetTokenBudget': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTokenBudget,
                    request_deserializer=sampler__public__pb2.GetTokenBudgetRequest.FromString,
                    response_serializer=sampler__public__pb2.TokenBudget.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prompt_ide.Sampler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sampler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SampleTokens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/prompt_ide.Sampler/SampleTokens',
            sampler__public__pb2.SampleTokensRequest.SerializeToString,
            sampler__public__pb2.SampleTokensResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Tokenize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prompt_ide.Sampler/Tokenize',
            sampler__public__pb2.TokenizeRequest.SerializeToString,
            sampler__public__pb2.TokenizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenizeAndSampleTokens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/prompt_ide.Sampler/TokenizeAndSampleTokens',
            sampler__public__pb2.TokenizeAndSampleTokensRequest.SerializeToString,
            sampler__public__pb2.SampleTokensResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTransactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prompt_ide.Sampler/ListTransactions',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            sampler__public__pb2.ListTransactionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTokenBudget(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prompt_ide.Sampler/GetTokenBudget',
            sampler__public__pb2.GetTokenBudgetRequest.SerializeToString,
            sampler__public__pb2.TokenBudget.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
