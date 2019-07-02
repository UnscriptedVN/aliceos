#  AliceOS Definitions

To make referencing common AliceOS build settings and structures easier, AliceOS provides the following definitions and dictionaries. These are located in `System/ASDefinitions.rpy` and can be modified if necessary.

## Directory definitions
| Definition name | Points to | Used for |
| -- | -- | -- |
| `AS_SYSTEM_DIR` | `System/` | The default System directory. |
| `AS_FRAMEWORKS_DIR` | `System/Frameworks/` | The default Frameworks directory. |
| `AS_CORESERVICES_DIR` | `System/CoreServices/` | The default Core Services directory. |
| `AS_DEFAULT_APP_DIR` | `System/Applications/` | The default System applications directory. This isn't necessary for developer use. |
| `AS_FONTS_DIR` | `System/Fonts/` | The default Fonts directory. |
| `AS_APPS_DIR` | `Applications/` | The default Applications directory. |

## Framework directory definitions

`AS_FRAMEWORK_DIR(FRAMEWORK_NAME="Default")`

The directory where a particular Framework is located. Makes use of `AS_FRAMEWORKS_DIR`.

**Parameters**

- `FRAMEWORK_NAME`: The name of the framework to reference. Example: `NotificationKit`

**Returns**

The path to the framework. Example: `System/Frameworks/NotificationKit.aosframework/`

## Permissions definitions

These definitions are used to specify important strings when asking the user permission for a particular item. These are dictionaries that include the values for a particular permission.

- `AS_REQUIRE_PERMS_NAME`: The dictionary containing the name of the permission name. Example: "Send Notifications"
- `AS_REQUIRE_PERMS_DESC`: The dictionary containing the description of a permission. Example: "Notifications may include banners, alerts, and sounds. These can be configured in Settings."