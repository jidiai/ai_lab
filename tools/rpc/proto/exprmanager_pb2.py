# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/exprmanager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/exprmanager.proto",
    package="rpc",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x17proto/exprmanager.proto\x12\x03rpc"J\n\tTableName\x12\x0f\n\x07primary\x18\x01 \x01(\t\x12\x11\n\tsecondary\x18\x02 \x01(\t\x12\x0b\n\x03src\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\x01"%\n\x08TableKey\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x01"W\n\x04Text\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x0b\n\x03src\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0c\n\x04step\x18\x05 \x01(\x05\x12\x0c\n\x04time\x18\x06 \x01(\x01"\x7f\n\x06Scalar\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x0b\n\x03src\x18\x03 \x01(\t\x12\x10\n\x06op_int\x18\x04 \x01(\x03H\x00\x12\x12\n\x08op_float\x18\x06 \x01(\x02H\x00\x12\x0c\n\x04step\x18\x07 \x01(\x05\x12\x0c\n\x04time\x18\x08 \x01(\x01\x42\x0c\n\nScalarType"k\n\x06\x42inary\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x0b\n\x03src\x18\x03 \x01(\t\x12\x0e\n\x06tensor\x18\x04 \x01(\x08\x12\x0e\n\x06\x62locks\x18\x05 \x01(\x0c\x12\x0c\n\x04step\x18\x06 \x01(\x05\x12\x0c\n\x04time\x18\x07 \x01(\x01")\n\tSendReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x01\x32\x9f\x02\n\x14\x45xperimentManagerRPC\x12,\n\x0b\x43reateTable\x12\x0e.rpc.TableName\x1a\r.rpc.TableKey\x12%\n\x08SendText\x12\t.rpc.Text\x1a\x0e.rpc.SendReply\x12)\n\nSendScalar\x12\x0b.rpc.Scalar\x1a\x0e.rpc.SendReply\x12*\n\tSendImage\x12\x0b.rpc.Binary\x1a\x0e.rpc.SendReply(\x01\x12\x31\n\x10SendBinaryTensor\x12\x0b.rpc.Binary\x1a\x0e.rpc.SendReply(\x01\x12(\n\x07SendObj\x12\x0b.rpc.Binary\x1a\x0e.rpc.SendReply(\x01\x62\x06proto3',
)


_TABLENAME = _descriptor.Descriptor(
    name="TableName",
    full_name="rpc.TableName",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="primary",
            full_name="rpc.TableName.primary",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="secondary",
            full_name="rpc.TableName.secondary",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="src",
            full_name="rpc.TableName.src",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="rpc.TableName.time",
            index=3,
            number=5,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=32,
    serialized_end=106,
)


_TABLEKEY = _descriptor.Descriptor(
    name="TableKey",
    full_name="rpc.TableKey",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="rpc.TableKey.key",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="rpc.TableKey.time",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=108,
    serialized_end=145,
)


_TEXT = _descriptor.Descriptor(
    name="Text",
    full_name="rpc.Text",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="rpc.Text.key",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tag",
            full_name="rpc.Text.tag",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="src",
            full_name="rpc.Text.src",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="text",
            full_name="rpc.Text.text",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="step",
            full_name="rpc.Text.step",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="rpc.Text.time",
            index=5,
            number=6,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=147,
    serialized_end=234,
)


_SCALAR = _descriptor.Descriptor(
    name="Scalar",
    full_name="rpc.Scalar",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="rpc.Scalar.key",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tag",
            full_name="rpc.Scalar.tag",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="src",
            full_name="rpc.Scalar.src",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="op_int",
            full_name="rpc.Scalar.op_int",
            index=3,
            number=4,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="op_float",
            full_name="rpc.Scalar.op_float",
            index=4,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="step",
            full_name="rpc.Scalar.step",
            index=5,
            number=7,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="rpc.Scalar.time",
            index=6,
            number=8,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="ScalarType",
            full_name="rpc.Scalar.ScalarType",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=236,
    serialized_end=363,
)


_BINARY = _descriptor.Descriptor(
    name="Binary",
    full_name="rpc.Binary",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="rpc.Binary.key",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tag",
            full_name="rpc.Binary.tag",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="src",
            full_name="rpc.Binary.src",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tensor",
            full_name="rpc.Binary.tensor",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="blocks",
            full_name="rpc.Binary.blocks",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="step",
            full_name="rpc.Binary.step",
            index=5,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="rpc.Binary.time",
            index=6,
            number=7,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=365,
    serialized_end=472,
)


_SENDREPLY = _descriptor.Descriptor(
    name="SendReply",
    full_name="rpc.SendReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="status",
            full_name="rpc.SendReply.status",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="rpc.SendReply.time",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=474,
    serialized_end=515,
)

_SCALAR.oneofs_by_name["ScalarType"].fields.append(_SCALAR.fields_by_name["op_int"])
_SCALAR.fields_by_name["op_int"].containing_oneof = _SCALAR.oneofs_by_name["ScalarType"]
_SCALAR.oneofs_by_name["ScalarType"].fields.append(_SCALAR.fields_by_name["op_float"])
_SCALAR.fields_by_name["op_float"].containing_oneof = _SCALAR.oneofs_by_name[
    "ScalarType"
]
DESCRIPTOR.message_types_by_name["TableName"] = _TABLENAME
DESCRIPTOR.message_types_by_name["TableKey"] = _TABLEKEY
DESCRIPTOR.message_types_by_name["Text"] = _TEXT
DESCRIPTOR.message_types_by_name["Scalar"] = _SCALAR
DESCRIPTOR.message_types_by_name["Binary"] = _BINARY
DESCRIPTOR.message_types_by_name["SendReply"] = _SENDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TableName = _reflection.GeneratedProtocolMessageType(
    "TableName",
    (_message.Message,),
    {
        "DESCRIPTOR": _TABLENAME,
        "__module__": "proto.exprmanager_pb2"
        # @@protoc_insertion_point(class_scope:rpc.TableName)
    },
)
_sym_db.RegisterMessage(TableName)

TableKey = _reflection.GeneratedProtocolMessageType(
    "TableKey",
    (_message.Message,),
    {
        "DESCRIPTOR": _TABLEKEY,
        "__module__": "proto.exprmanager_pb2"
        # @@protoc_insertion_point(class_scope:rpc.TableKey)
    },
)
_sym_db.RegisterMessage(TableKey)

Text = _reflection.GeneratedProtocolMessageType(
    "Text",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXT,
        "__module__": "proto.exprmanager_pb2"
        # @@protoc_insertion_point(class_scope:rpc.Text)
    },
)
_sym_db.RegisterMessage(Text)

Scalar = _reflection.GeneratedProtocolMessageType(
    "Scalar",
    (_message.Message,),
    {
        "DESCRIPTOR": _SCALAR,
        "__module__": "proto.exprmanager_pb2"
        # @@protoc_insertion_point(class_scope:rpc.Scalar)
    },
)
_sym_db.RegisterMessage(Scalar)

Binary = _reflection.GeneratedProtocolMessageType(
    "Binary",
    (_message.Message,),
    {
        "DESCRIPTOR": _BINARY,
        "__module__": "proto.exprmanager_pb2"
        # @@protoc_insertion_point(class_scope:rpc.Binary)
    },
)
_sym_db.RegisterMessage(Binary)

SendReply = _reflection.GeneratedProtocolMessageType(
    "SendReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _SENDREPLY,
        "__module__": "proto.exprmanager_pb2"
        # @@protoc_insertion_point(class_scope:rpc.SendReply)
    },
)
_sym_db.RegisterMessage(SendReply)


_EXPERIMENTMANAGERRPC = _descriptor.ServiceDescriptor(
    name="ExperimentManagerRPC",
    full_name="rpc.ExperimentManagerRPC",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=518,
    serialized_end=805,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateTable",
            full_name="rpc.ExperimentManagerRPC.CreateTable",
            index=0,
            containing_service=None,
            input_type=_TABLENAME,
            output_type=_TABLEKEY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendText",
            full_name="rpc.ExperimentManagerRPC.SendText",
            index=1,
            containing_service=None,
            input_type=_TEXT,
            output_type=_SENDREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendScalar",
            full_name="rpc.ExperimentManagerRPC.SendScalar",
            index=2,
            containing_service=None,
            input_type=_SCALAR,
            output_type=_SENDREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendImage",
            full_name="rpc.ExperimentManagerRPC.SendImage",
            index=3,
            containing_service=None,
            input_type=_BINARY,
            output_type=_SENDREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendBinaryTensor",
            full_name="rpc.ExperimentManagerRPC.SendBinaryTensor",
            index=4,
            containing_service=None,
            input_type=_BINARY,
            output_type=_SENDREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendObj",
            full_name="rpc.ExperimentManagerRPC.SendObj",
            index=5,
            containing_service=None,
            input_type=_BINARY,
            output_type=_SENDREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_EXPERIMENTMANAGERRPC)

DESCRIPTOR.services_by_name["ExperimentManagerRPC"] = _EXPERIMENTMANAGERRPC

# @@protoc_insertion_point(module_scope)