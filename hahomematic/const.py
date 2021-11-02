"""
Constants used by hahomematic.
"""

VERSION = "0.0.3"
DEFAULT_ENCODING = "UTF-8"

LOCALHOST = "localhost"
IP_LOCALHOST_V4 = "127.0.0.1"
IP_LOCALHOST_V6 = "::1"
IP_ANY_V4 = "0.0.0.0"
IP_ANY_V6 = "::"
PORT_ANY = 0

PORT_REGA_HSS = 1999
PORT_REGA_HSS_TLS = 41999
PORT_HS485D = 2000
PORT_HS485D_TLS = 42000
PORT_RFD = 2001
PORT_RFD_TLS = 42001
PORT_HMIP = 2010
PORT_HMIP_TLS = 42010
PORT_GROUPS = 9292
PORT_GROUPS_TLS = 49292
PORT_JSON_RPC = 80
PORT_JSON_RPC_TLS = 443
PORT_REGA_SCRIPT = 8181
PORT_REGA_SCRIPT_TLS = 48181

PRIMARY_PORTS = [PORT_HMIP, PORT_HMIP_TLS, PORT_RFD, PORT_RFD_TLS]

JSON_RPC_PATH = "/api/homematic.cgi"
PATH_JSON_RPC = "/api/homematic.cgi"
PATH_TCL_REGA = "/tclrega.exe"

FILE_DEVICES_RAW = None
FILE_DEVICES = "homematic_devices.json"
FILE_PARAMSETS = "homematic_paramsets.json"
FILE_NAMES = "homematic_names.json"

PARAMSET_MASTER = "MASTER"
PARAMSET_VALUES = "VALUES"

RELEVANT_PARAMSETS = [
    PARAMSET_VALUES,
    # PARAMSET_MASTER,
]

HA_DOMAIN = "hahm"

HH_EVENT_DELETE_DEVICES = "deleteDevices"
HH_EVENT_DEVICES_CREATED = "devicesCreated"
HH_EVENT_ENTITIES_CREATED = "entitiesCreated"
HH_EVENT_ENTITY_CREATED = "entityCreated"
HH_EVENT_ERROR = "error"
HH_EVENT_LIST_DEVICES = "listDevices"
HH_EVENT_NEW_DEVICES = "newDevices"
HH_EVENT_RE_ADDED_DEVICE = "readdedDevice"
HH_EVENT_REPLACE_DEVICE = "replaceDevice"
HH_EVENT_UPDATE_DEVICE = "updateDevice"

# When CONFIG_PENDING turns from True to False (ONLY then!) we should re fetch the paramsets.
# However, usually multiple of these events are fired, so we should only
# act on the last one. This also only seems to fire on channel 0.
EVENT_CONFIG_PENDING = "CONFIG_PENDING"
EVENT_ERROR = "ERROR"
# Only available on CCU
EVENT_PONG = "PONG"
EVENT_PRESS = "PRESS"
EVENT_PRESS_SHORT = "PRESS_SHORT"
EVENT_PRESS_LONG = "PRESS_LONG"
EVENT_PRESS_CONT = "PRESS_CONT"
EVENT_PRESS_LONG_RELEASE = "PRESS_LONG_RELEASE"
EVENT_SEQUENCE_OK = "SEQUENCE_OK"
EVENT_UN_REACH = "UNREACH"

EVENT_KEYPRESS = "homematic.keypress"
EVENT_IMPULSE = "homematic.impulse"

CLICK_EVENTS = [
    EVENT_PRESS,
    EVENT_PRESS_SHORT,
    EVENT_PRESS_LONG,
    EVENT_PRESS_CONT,
    EVENT_PRESS_LONG_RELEASE,
]

IMPULSE_EVENTS = [EVENT_CONFIG_PENDING, EVENT_ERROR, EVENT_SEQUENCE_OK, EVENT_UN_REACH]

PARAM_UN_REACH = "UNREACH"
PARAM_CONFIG_PENDING = "CONFIG_PENDING"

# Parameters within the paramsets for which we don't create entities.
IGNORED_PARAMETERS = [
    "STICKY_UNREACH",
    "AES_KEY",
    "DEVICE_IN_BOOTLOADER",
    "INSTALL_TEST",
    "STICKY_UNREACH",
    "UPDATE_PENDING",
    "ERROR_CODE",
    "PROCESS",
    "SECTION",
    "WOCHENPROGRAMM",
    "QUICK_VETO_TIME",
    "FROST_PROTECTION",
    "EMERGENCY_OPERATION",
    "HEATING_COOLING",
    "BOOST_TIME",
    "PARTY_TIME_START",
    "PARTY_TIME_END",
    "PARTY_SET_POINT_TEMPERATURE",
    "SWITCH_POINT_OCCURED",
    "HUMIDITY_ALARM",
    "WEEK_PROGRAM_CHANNEL_LOCKS",
    "ERROR_NON_FLAT_POSITIONING",
    "ERROR_OVERLOAD",
    "TIME_OF_OPERATION",
    "TEMPERATURE_OUT_OF_RANGE",
    "ERROR_POWER_FAILURE",
    "ERROR_DEGRADED_CHAMBER",
    "ERROR_REDUCED",
    "ERROR_UPDATE",
    "INCLUSION_UNSUPPORTED_DEVICE",
    "ERROR_WIND_COMMUNICATION",
    "ERROR_WIND_NORTH",
    "BOOT",
]

IGNORED_PARAMETERS_WILDCARDS = [
    "ACTIVE",
    "OVERFLOW",
    "OVERHEAT",
    "OVERRUN",
    "RESULT",
    "STATUS",
    "WORKING",
]

ATTRIBUTES = ["VALVE_ADAPTION", "SMOKE_DETECTOR_TEST_RESULT"]

HIDDEN_PARAMETERS = [PARAM_UN_REACH, PARAM_CONFIG_PENDING]

BACKEND_UNKNOWN = 0
BACKEND_CCU = 1
BACKEND_HOMEGEAR = 2

PROXY_INIT_FAILED = 0
PROXY_INIT_SUCCESS = 1
PROXY_INIT_SKIPPED = 2

DATA_LOAD_SUCCESS = 10
DATA_LOAD_FAIL = 100
DATA_NO_LOAD = 99

ATTR_ADDRESS = "address"
ATTR_CALLBACK_HOST = "callback_host"
ATTR_CALLBACK_PORT = "callback_port"
ATTR_CHANNELS = "channels"
ATTR_CONNECT = "connect"
ATTR_ERROR = "error"
ATTR_HOST = "host"
ATTR_ID = "id"
ATTR_INTERFACE = "interface"
ATTR_INTERFACE_ID = "interface_id"
ATTR_IP = "ip"
ATTR_JSON = "json"
ATTR_JSON_PORT = "json_port"
ATTR_METADATA = "metadata"
ATTR_NAME = "name"
ATTR_PASSWORD = "password"
ATTR_PARAMETER = "parameter"
ATTR_PARAMSET_KEY = "paramset_key"
ATTR_PARAMSET = "paramset"
ATTR_RX_MODE = "rx_mode"
ATTR_PATH = "path"
ATTR_PORT = "port"
ATTR_RESOLVE_NAMES = "resolve_names"
ATTR_RESULT = "result"
ATTR_SESSION_ID = "_session_id_"
ATTR_TLS = "tls"
ATTR_TYPE = "type"
ATTR_UNIQUE_ID = "unique_id"
ATTR_USERNAME = "username"
ATTR_VALUE = "value"
ATTR_VALUE_TYPE = "value_type"
ATTR_VERIFY_TLS = "verify_tls"

ATTR_HM_ADDRESS = "ADDRESS"
ATTR_HM_CONTROL = "CONTROL"
ATTR_HM_FIRMWARE = "FIRMWARE"
ATTR_HM_OPERATIONS = "OPERATIONS"
ATTR_HM_PARAMSETS = "PARAMSETS"
ATTR_HM_TYPE = "TYPE"
ATTR_HM_PARENT_TYPE = "PARENT_TYPE"
ATTR_HM_VERSION = "VERSION"
ATTR_HM_LIST = "LIST"
ATTR_HM_LOGIC = "LOGIC"
ATTR_HM_NAME = "NAME"
ATTR_HM_NUMBER = "NUMBER"
ATTR_HM_FLAGS = "FLAGS"
ATTR_HM_UNIT = "UNIT"
ATTR_HM_MAX = "MAX"
ATTR_HM_MIN = "MIN"
ATTR_HM_DEFAULT = "DEFAULT"
# Optional member for TYPE: FLOAT, INTEGER
ATTR_HM_SPECIAL = "SPECIAL"  # Which has the following keys
ATTR_HM_ID = "ID"  # String
ATTR_HM_VALUE = "VALUE"  # Float or integer, depending on TYPE
# Members for ENUM
ATTR_HM_VALUE_LIST = "VALUE_LIST"

OPERATION_NONE = 0
OPERATION_READ = 1
OPERATION_WRITE = 2
OPERATION_EVENT = 4

TYPE_FLOAT = "FLOAT"
TYPE_INTEGER = "INTEGER"
TYPE_BOOL = "BOOL"
TYPE_ENUM = "ENUM"
TYPE_STRING = "STRING"
TYPE_ACTION = "ACTION"  # Usually buttons, send Boolean to trigger

FLAG_VISIBLE = 1
FLAG_INTERAL = 2
FLAG_TRANSFORM = 4
FLAG_SERVICE = 8
FLAG_STICKY = 10  # This might be wrong. Documentation says 0x10

DEFAULT_CALLBACK_HOST = None
DEFAULT_CALLBACK_PORT = None
DEFAULT_CONNECT = True
DEFAULT_JSON_PORT = 80
DEFAULT_NAME = "default"
DEFAULT_PASSWORD = None
DEFAULT_PATH = None
DEFAULT_USERNAME = "Admin"
DEFAULT_REMOTE = "default"
DEFAULT_RESOLVE_NAMES = False
DEFAULT_TIMEOUT = 5
DEFAULT_INIT_TIMEOUT = 90
DEFAULT_TLS = False
DEFAULT_VERIFY_TLS = False

HA_PLATFORM_BINARY_SENSOR = "binary_sensor"
HA_PLATFORM_CLIMATE = "climate"
HA_PLATFORM_COVER = "cover"
HA_PLATFORM_EVENT = "event"
HA_PLATFORM_LIGHT = "light"
HA_PLATFORM_LOCK = "lock"
HA_PLATFORM_NUMBER = "number"
HA_PLATFORM_SELECT = "select"
HA_PLATFORM_SENSOR = "sensor"
HA_PLATFORM_SWITCH = "switch"
HA_PLATFORM_TEXT = "text"

HA_PLATFORMS = [
    HA_PLATFORM_BINARY_SENSOR,
    HA_PLATFORM_CLIMATE,
    HA_PLATFORM_COVER,
    HA_PLATFORM_LIGHT,
    HA_PLATFORM_LOCK,
    HA_PLATFORM_NUMBER,
    HA_PLATFORM_SELECT,
    HA_PLATFORM_SENSOR,
    HA_PLATFORM_SWITCH,
]

HM_ENTITY_UNIT_REPLACE = {'"': "", "100%": "%"}

hm = [
    "ACCESS_AUTHORIZATION",
    "ACTIVITY_STATE",
    "ADAPTION_DRIVE",
    "ADJUSTING_COMMAND",
    "ADJUSTING_DATA",
    "AES_KEY",
    "AIR_PRESSURE",
    "ALARM_COUNT",
    "ALL_LEDS",
    "ARMSTATE",
    "ARROW_DOWN",
    "ARROW_UP",
    "BACKLIGHT",
    "BATTERY_STATE",
    "BEEP",
    "BELL",
    "BLIND",
    "BOOST_STATE",
    "BOOST_TIME",
    "BOOT",
    "BULB",
    "CLEAR_WINDOW_OPEN_SYMBOL",
    "CLOCK",
    "COLOR_LIST_1",
    "COLOR_LIST_10",
    "COLOR_LIST_11",
    "COLOR_LIST_12",
    "COLOR_LIST_2",
    "COLOR_LIST_3",
    "COLOR_LIST_4",
    "COLOR_LIST_5",
    "COLOR_LIST_6",
    "COLOR_LIST_7",
    "COLOR_LIST_8",
    "COLOR_LIST_9",
    "COMBINED_PARAMETER",
    "COMMUNICATION_REPORTING",
    "CONFIG_PENDING",
    "CONTROL_DIFFERENTIAL_TEMPERATURE",
    "COUNTERREADING10",
    "CURRENT_PASSAGE_DIRECTION",
    "DATE_TIME_UNKNOWN",
    "DECISION_VALUE",
    "DEVICE_IN_BOOTLOADER",
    "DEW_POINT_ALARM",
    "DIRECTION",
    "DIRECTION_SLATS",
    "DOOR",
    "DURATION_UNIT",
    "DURATION_VALUE",
    "EMERGENCY_OPERATION",
    "ENTER_BOOTLOADER",
    "ERROR",
    "ERROR_ALARM_TEST",
    "ERROR_BATTERY",
    "ERROR_CODE",
    "ERROR_M1",
    "ERROR_M2",
    "ERROR_M3",
    "ERROR_NON_FLAT_POSITIONING",
    "ERROR_OVERHEAT",
    "ERROR_OVERLOAD",
    "ERROR_POWER",
    "ERROR_REDUCED",
    "ERROR_SABOTAGE",
    "ERROR_SMOKE_CHAMBER",
    "ERROR_UNDERVOLTAGE",
    "ERROR_UPDATE",
    "ERR_DETECT_EIA485_SERVICE",
    "ERR_TTCU_INTERNAL_TEST",
    "ERR_TTCU_LOCK_ROLLERS_SHORTED",
    "ERR_TTCU_MAGNET_ERROR",
    "ERR_TTCU_POWER_ONTIME_EXCEEDED",
    "ERR_TTCU_SENSOR_STRIP_DISCONNECTED",
    "ERR_TTCU_SENSOR_STRIP_SHORTED",
    "ERR_TTCU_STOP_AFTER_10_CLOSING_TRIES",
    "ERR_TTCU_TURN_TILT_ACT_ALLOY_MOSFET",
    "ERR_TTCU_TURN_TILT_ACT_ASYNCHRON",
    "ERR_TTCU_TURN_TILT_ACT_BLOCKED",
    "ERR_TTCU_TURN_TILT_ACT_CONTACT_PROBLEM",
    "ERR_TTCU_TURN_TILT_ACT_NO_SPEED_SIGNAL",
    "ERR_TTCU_TURN_TILT_ACT_OVERCURRENT",
    "ERR_TTCU_TURN_TILT_ACT_SHORTED",
    "ERR_TTCU_WRONG_VOLTAGE_POLARITY",
    "ERR_TTM_INTERNAL",
    "ERR_TTM_OVERVOLT",
    "ERR_TTM_UNDERVOLT",
    "ERR_WINDOW_NOT_FOUND",
    "ERR_WIN_STAY_IN_INITIAL_OPERATION",
    "EXTERNAL_CLOCK",
    "FAULT_REPORTING",
    "FILLING_LEVEL",
    "FREE_TO_USE",
    "FROST_PROTECTION",
    "GAS_POWER",
    "HANDLE_LED_MODE",
    "HANDLE_LOCK",
    "HEATER_STATE",
    "HEATING_COOLING",
    "HOLIDAY_MODE",
    "HUMIDITY_ALARM",
    "HUMIDITY_LIMITER",
    "IDENTIFICATION_MODE_KEY_VISUAL",
    "IDENTIFICATION_MODE_LCD_BACKLIGHT",
    "IDENTIFY_DURATION",
    "IDENTIFY_TARGET_LEVEL",
    "INACTIVE_MODE",
    "INHIBIT",
    "INSTALL_MODE",
    "INSTALL_TEST",
    "LOWBAT_REPORTING",
    "LOWBAT_SENSOR",
    "MY_HUMIDITY",
    "NEXT_TRANSMISSION",
    "OLD_LEVEL",
    "ON_TIME",
    "ON_TIME_LIST_1",
    "ON_TIME_LIST_10",
    "ON_TIME_LIST_11",
    "ON_TIME_LIST_12",
    "ON_TIME_LIST_2",
    "ON_TIME_LIST_3",
    "ON_TIME_LIST_4",
    "ON_TIME_LIST_5",
    "ON_TIME_LIST_6",
    "ON_TIME_LIST_7",
    "ON_TIME_LIST_8",
    "ON_TIME_LIST_9",
    "OUTPUT_SELECT_SIZE",
    "PARTY_MODE_SUBMIT",
    "PARTY_SET_POINT_TEMPERATURE",
    "PARTY_START_DAY",
    "PARTY_START_MONTH",
    "PARTY_START_TIME",
    "PARTY_START_YEAR",
    "PARTY_STOP_DAY",
    "PARTY_STOP_MONTH",
    "PARTY_STOP_TIME",
    "PARTY_STOP_YEAR",
    "PARTY_TEMPERATURE",
    "PARTY_TIME_END",
    "PARTY_TIME_START",
    "PHONE",
    "POWER",
    "PRESENCE_DETECTION_ACTIVE",
    "PRESENCE_DETECTION_STATE",
    "PRESS",
    "PRESS_CONT",
    "PRESS_LONG",
    "PRESS_LONG_RELEASE",
    "PRESS_SHORT",
    "PROCESS",
    "QUICK_VETO_TIME",
    "RAMP_STOP",
    "RAMP_TIME",
    "RAMP_TIME_UNIT",
    "RAMP_TIME_VALUE",
    "RELEASE_TURN",
    "RELOCK_DELAY",
    "REPETITIONS",
    "RESET_MOTION",
    "RESET_PRESENCE",
    "SCENE",
    "SECTION",
    "SECTION_STATUS",
    "SECURE_STATE",
    "SELF_CALIBRATION",
    "SELF_CALIBRATION_RESULT",
    "SEQUENCE_OK",
    "SERVICE_COUNT",
    "SET_SYMBOL_FOR_HEATING_PHASE",
    "SHADING_SPEED",
    "SHEV_POS",
    "SMOKE_DETECTOR_ALARM_STATUS",
    "SMOKE_DETECTOR_COMMAND",
    "SMOKE_DETECTOR_TEST_RESULT",
    "SOUNDFILE",
    "SOUNDFILE_LIST_1",
    "SOUNDFILE_LIST_10",
    "SOUNDFILE_LIST_11",
    "SOUNDFILE_LIST_12",
    "SOUNDFILE_LIST_2",
    "SOUNDFILE_LIST_3",
    "SOUNDFILE_LIST_4",
    "SOUNDFILE_LIST_5",
    "SOUNDFILE_LIST_6",
    "SOUNDFILE_LIST_7",
    "SOUNDFILE_LIST_8",
    "SOUNDFILE_LIST_9",
    "STATE_UNCERTAIN",
    "STATUS_FLAG_ERROR",
    "STATUS_FLAG_LOW_BAT",
    "STATUS_FLAG_PLAYING_FILE_ACTIVE",
    "STATUS_FLAG_PLAYLIST_ACTIVE",
    "STICKY_BATTERY",
    "STICKY_ERR_TTM_OVERVOLT",
    "STICKY_ERR_TTM_UNDERVOLT",
    "STICKY_POWER",
    "STICKY_SABOTAGE",
    "STICKY_UNREACH",
    "STOP",
    "SUBMIT",
    "SWITCH_POINT_OCCURED",
    "TEMPERATURE_LIMITER",
    "TEXT",
    "TIME_OF_OPERATION",
    "TIPTRONIC_STATE",
    "UPDATE_PENDING",
    "USER_PROGRAM",
    "VALVE_ADAPTION",
    "WEEK_PROGRAM_CHANNEL_LOCKS",
    "WEEK_PROGRAM_TARGET_CHANNEL_LOCK",
    "WEEK_PROGRAM_TARGET_CHANNEL_LOCKS",
    "WINDOW_OPEN_REPORTING",
    "WINDOW_TYPE",
    "WINTER_MODE",
    "WIN_RELEASE",
    "WIN_RELEASE_ACT",
    "WORKING",
    "WORKING_SLATS",
    "WP_OPTIONS",
]
