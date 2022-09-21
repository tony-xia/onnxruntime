# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OpIdKernelTypeStrArgsEntry(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsOpIdKernelTypeStrArgsEntry(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OpIdKernelTypeStrArgsEntry()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def OpIdKernelTypeStrArgsEntryBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x52\x54\x4D", size_prefixed=size_prefixed)

    # OpIdKernelTypeStrArgsEntry
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OpIdKernelTypeStrArgsEntry
    def OpId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OpIdKernelTypeStrArgsEntry
    def KernelTypeStrArgs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.KernelTypeStrArgsEntry import KernelTypeStrArgsEntry
            obj = KernelTypeStrArgsEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OpIdKernelTypeStrArgsEntry
    def KernelTypeStrArgsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OpIdKernelTypeStrArgsEntry
    def KernelTypeStrArgsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def OpIdKernelTypeStrArgsEntryStart(builder): builder.StartObject(2)
def OpIdKernelTypeStrArgsEntryAddOpId(builder, opId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(opId), 0)
def OpIdKernelTypeStrArgsEntryAddKernelTypeStrArgs(builder, kernelTypeStrArgs): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(kernelTypeStrArgs), 0)
def OpIdKernelTypeStrArgsEntryStartKernelTypeStrArgsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def OpIdKernelTypeStrArgsEntryEnd(builder): return builder.EndObject()
