// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

#pragma once
#include "core/common/common.h"
#include "core/framework/op_kernel.h"
#include "core/providers/cuda/cuda_common.h"

namespace onnxruntime {
namespace contrib {
namespace cuda {

using namespace onnxruntime::cuda;

template <typename T>
class SkipLayerNorm final : public CudaKernel {
 public:
  SkipLayerNorm(const OpKernelInfo& op_kernel_info);
  Status ComputeInternal(OpKernelContext* context) const override;

 private:
  size_t gamma_size_;
  size_t beta_size_;

  IAllocatorUniquePtr<float> gamma_data_;  // gpu copy of weight
  IAllocatorUniquePtr<float> beta_data_;   // gpu copy of bias

};

}  // namespace cuda
}  // namespace contrib
}  // namespace onnxruntime
