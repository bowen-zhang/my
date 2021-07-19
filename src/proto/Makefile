PYTHON = python3

build:
	rm -f *_pb2*.py
	rm -f *_pb.js
	protoc -I=. *.proto --js_out=import_style=commonjs:. --plugin=protoc-gen-grpc=../../protoc-gen-grpc-web-1.2.1-linux-x86_64 --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.
	$(PYTHON) -m grpc_tools.protoc -I=. *.proto --python_out=. --grpc_python_out=.
	sed -i -E "s/^import ([a-zA-Z0-9_]+_pb2) as/from . import \\1 as/" *_pb2*.py
