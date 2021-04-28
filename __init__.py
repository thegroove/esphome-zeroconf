import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_SERVICE, CONF_PROTOCOL, CONF_PORT, CONF_KEY, CONF_VALUE

MULTI_CONF = True

CONF_TXT = 'txt'

ns = cg.esphome_ns.namespace('zeroconf')
class_ = ns.class_('Zeroconf', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(class_),
    cv.Required(CONF_SERVICE): cv.string,
    cv.Required(CONF_PROTOCOL): cv.string,
    cv.Required(CONF_PORT): cv.port,

    cv.Optional(CONF_TXT): cv.ensure_list(
        cv.Schema({
            cv.Required(CONF_KEY): cv.string,
            cv.Required(CONF_VALUE): cv.string, 
        })
    ),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    cg.add(var.set_service(config[CONF_SERVICE], config[CONF_PROTOCOL], config[CONF_PORT]))

    if CONF_TXT in config:
        for txt in config[CONF_TXT]:
            cg.add(var.add_txt(txt[CONF_KEY], txt[CONF_VALUE]))    



