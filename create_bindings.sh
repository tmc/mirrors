#!/usr/bin/env bash

python -m grpc_tools.protoc -I../../backend/proto  -I../../backend/proto/google/api --python_out=src/xai_sdk/proto --pyi_out=src/xai_sdk/proto --grpc_python_out=src/xai_sdk/proto ../../backend/proto/chat.proto ../../backend/proto/sampler_public.proto ../../backend/proto/google/api/annotations.proto ../../backend/proto/google/api/http.proto ../../backend/proto/files.proto ../../backend/proto/stateless_chat.proto

# Change imports to be relative
for file in src/xai_sdk/proto/*; do
  # Check if the file is a regular file
  if [[ -f "$file" ]]; then
    sed -i '' 's/^import sampler_public_pb2/from . import sampler_public_pb2/' "$file"
    sed -i '' 's/^import chat_pb2/from . import chat_pb2/' "$file"
    sed -i '' 's/^import files_pb2/from . import files_pb2/' "$file"
    sed -i '' 's/^import stateless_chat_pb2/from . import stateless_chat_pb2/' "$file"
    sed -i '' 's/^from google.api/from .google.api/' "$file"
  fi
done

for file in src/xai_sdk/proto/google/api/*; do
  if [[ -f "$file" ]]; then
    sed -i '' 's/^from google.api import/from . import/' "$file"
  fi
done

# Recursively find all Python files in a directory and insert the comment "fmt: off" at the top of
# every file.Without this, the presubmit check makes noise.
find ./src/xai_sdk/proto -type f -name "*.py" -not -path "*/__init__.py" | while read file; do
    # Insert the comment at the top of the file
    echo "# fmt: off" | cat - "$file" > temp && mv temp "$file"
done