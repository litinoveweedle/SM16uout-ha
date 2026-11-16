FULL_NAME="Sixteen 0-10V Analog Outputs"
LINK="https://sequentmicrosystems.com/products/sixteen-0-10v-analog-outputs"

import SM16uout
API = SM16uout.SM16uout
DOMAIN = "sm16uout"
NAME_PREFIX = "sm16uo"
SM_MAP = {
    "button": {
        "watchdog_reload": {
            "chan_no": 1, "optional": True, "com": {"set": "wdt_reload"},
        },
    },
    "sensor": {
        "watchdog_count": {
            "chan_no": 1, "optional": True, "com": {"get": "wdt_get_reset_count"},
        },
    },
    "switch": {
        "led": {
                "chan_no": 16,
                "com": {
                    "get": "get_led",
                    "set": "set_led"
                },
        }
    },
    "number": {
        "watchdog_period": {
            "chan_no": 1, "optional": True, "uom": "s",
            "min_value": 1, "max_value": 65535, "step": 1,
            "com": {"get": "wdt_get_period", "set": "wdt_set_period"},
        },
        "watchdog_initial": {
            "chan_no": 1, "optional": True, "uom": "s",
            "min_value": 1, "max_value": 65535, "step": 1,
            "com": {"get": "wdt_get_init_period", "set": "wdt_set_init_period"},
        },
        "out": {
                "chan_no": 16,
                "uom": "V",
                "min_value": 0.0,
                "max_value": 10.0,
                "step": 0.01,
                "com": {
                    "get": "get_u_out",
                    "set": "set_u_out"
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    },
}
