# fmt: off
# fmt: off
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import models_pb2 as models__pb2


class ModelsStub(object):
    """A service that exposes the models which are available on the platform.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListLanguageModels = channel.unary_unary(
                '/xai_api.Models/ListLanguageModels',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=models__pb2.ListLanguageModelsResponse.FromString,
                )
        self.ListEmbeddingModels = channel.unary_unary(
                '/xai_api.Models/ListEmbeddingModels',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=models__pb2.ListEmbeddingModelsResponse.FromString,
                )
        self.GetLanguageModel = channel.unary_unary(
                '/xai_api.Models/GetLanguageModel',
                request_serializer=models__pb2.GetLanguageModelRequest.SerializeToString,
                response_deserializer=models__pb2.LanguageModel.FromString,
                )
        self.GetEmbeddingModel = channel.unary_unary(
                '/xai_api.Models/GetEmbeddingModel',
                request_serializer=models__pb2.GetEmbeddingModelRequest.SerializeToString,
                response_deserializer=models__pb2.EmbeddingModel.FromString,
                )


class ModelsServicer(object):
    """A service that exposes the models which are available on the platform.
    """

    def ListLanguageModels(self, request, context):
        """Lists all language models available on the platform.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEmbeddingModels(self, request, context):
        """Lists all embedding models available on the platform.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLanguageModel(self, request, context):
        """Get specific language model by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEmbeddingModel(self, request, context):
        """Get specific embedding model by name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListLanguageModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLanguageModels,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=models__pb2.ListLanguageModelsResponse.SerializeToString,
            ),
            'ListEmbeddingModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEmbeddingModels,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=models__pb2.ListEmbeddingModelsResponse.SerializeToString,
            ),
            'GetLanguageModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLanguageModel,
                    request_deserializer=models__pb2.GetLanguageModelRequest.FromString,
                    response_serializer=models__pb2.LanguageModel.SerializeToString,
            ),
            'GetEmbeddingModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmbeddingModel,
                    request_deserializer=models__pb2.GetEmbeddingModelRequest.FromString,
                    response_serializer=models__pb2.EmbeddingModel.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'xai_api.Models', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Models(object):
    """A service that exposes the models which are available on the platform.
    """

    @staticmethod
    def ListLanguageModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xai_api.Models/ListLanguageModels',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            models__pb2.ListLanguageModelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEmbeddingModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xai_api.Models/ListEmbeddingModels',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            models__pb2.ListEmbeddingModelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLanguageModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xai_api.Models/GetLanguageModel',
            models__pb2.GetLanguageModelRequest.SerializeToString,
            models__pb2.LanguageModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEmbeddingModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xai_api.Models/GetEmbeddingModel',
            models__pb2.GetEmbeddingModelRequest.SerializeToString,
            models__pb2.EmbeddingModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
