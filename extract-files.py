#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm6225-common',
    'hardware/qcom-caf/sm6225',
    'hardware/xiaomi',
    'vendor/xiaomi/sm6225-common',
    'vendor/qcom/opensource/commonsys-intf/display',
]

module = ExtractUtilsModule(
    'sapphire',
    'xiaomi',
    namespace_imports=namespace_imports,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6225-common', module.vendor
    )
    utils.run()
