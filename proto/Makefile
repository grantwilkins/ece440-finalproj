OUTPUT=/Users/grantwilkins/ece460-finalproj/src/grpc/


all: lights

lights: lights.proto
	python3 -m grpc_tools.protoc lights.proto -I$(PWD) --python_out=$(OUTPUT) --pyi_out=$(OUTPUT) --grpc_python_out=$(OUTPUT)