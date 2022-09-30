// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

#include "core/providers/opwrapper/opwrapper_execution_provider.h"

#include <memory>
#include <string>
#include <utility>
#include "core/framework/allocatormgr.h"
#include "core/graph/constants.h"

namespace onnxruntime {

OpWrapperExecutionProvider::OpWrapperExecutionProvider(ProviderOptionsMap provider_options_map)
    : IExecutionProvider{onnxruntime::kOpWrapperExecutionProvider}, provider_options_map_(std::move(provider_options_map)) {
  AllocatorCreationInfo device_info(
      [](int /*unused*/) {
        return std::make_unique<CPUAllocator>(OrtMemoryInfo("OpWrapper", OrtAllocatorType::OrtDeviceAllocator));
      });

  InsertAllocator(CreateAllocator(device_info));
}

ProviderOptions OpWrapperExecutionProvider::GetOpProviderOptions(const std::string& op_name) const {
  auto it = provider_options_map_.find(op_name);
  return (it == provider_options_map_.end()) ? ProviderOptions{} : it->second;
}

}  // namespace onnxruntime
