# OPTIER SDK Exception Mapping

This document maps OEM error codes to SDK exceptions.

## Authentication

| OEM Error Code | SDK Exception | Retry |
|---------------|---------------|-------|
| no_login | NotLoggedInError | No |
| expired | SessionExpiredError | No |
| token_invalid | InvalidTokenError | No |
| token_generation_failed | TokenGenerationError | No |
| user_locked_login | UserLockedError | No |
| user_expired_login | UserExpiredLoginError | No |
| first_login | FirstLoginRequiredError | No |
| login_at_other | LoggedInElsewhereError | No |
| forced_offline | ForcedOfflineError | No |

## Permission

| OEM Error Code | SDK Exception |
|---------------|--------------|
| no_permission | PermissionDeniedError |

## Device

| OEM Error Code | SDK Exception |
|---------------|--------------|
| device_busy | DeviceBusyError |
| function_busy | FunctionBusyError |
| data_saving_busy | DataSavingBusyError |
| device_reboot | DeviceRebootingError |

## Search

| OEM Error Code | SDK Exception |
|---------------|--------------|
| search_failed | SearchFailedError |

## Save

| OEM Error Code | SDK Exception |
|---------------|--------------|
| save_failed | SaveFailedError |

## Operation

| OEM Error Code | SDK Exception |
|---------------|--------------|
| operation_failed | OperationFailedError |
| part_failed | PartialOperationError |

> This file will evolve continuously as more OEM APIs are analyzed.