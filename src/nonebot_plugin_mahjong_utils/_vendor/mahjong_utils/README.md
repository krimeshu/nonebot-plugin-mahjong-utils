# Vendored mahjong-utils

Source: https://github.com/ssttkkl/mahjong-utils/tree/v0.7.7/python-lib
Version: mahjong-utils 0.7.7 (MIT; see LICENSE).

Copied from the PyPI wheel mahjong_utils-0.7.7-py3-none-any.whl.
SHA-256: 4be180c7335d07e97f6336b3ceaafdf1226d7280d218342c38a44568c5f812d2

Local changes:
- Internal imports use nonebot_plugin_mahjong_utils._vendor.mahjong_utils.
- Pydantic imports use pydantic.v1, provided by the installed Pydantic v2 package.

The JS engine and source map are kept unchanged. The existing JS, HTTP and
webapi_jar bridge selection and ENV_MAHJONG_UTILS_* settings are preserved.
No top-level mahjong_utils package or sys.modules alias is installed.

When updating, compare with this upstream version, retain the license and JS
resources, reapply the import changes, and run the plugin regression tests.
