# Zeroconf custom component for ESPHome


Example configuration without DNS TXT records:

```yaml
zeroconf:
  - service: esphome_zb_gw_efr32
    protocol: tcp
    port: 6638
 ```
 
 
 Result:
 
 ```
 _esphome_zb_gw_efr32._tcp      local
   hostname = [esphome_zb_gw_efr32.local]
   address = [172.16.0.174]
   port = [6638]
   txt = []
```


Now an example with also adding some DNS TXT records as parameters for esphome-zbbridge gateway application version, location, and Zigbee radio configuration to be based along to ZHA integration:

```yaml
zeroconf:
  - service: esphome_zb_gw_efr32
    protocol: tcp
    port: 6638
    txt:
      version: 1.0
      location: basement
      radio_type: ezsp
      baud_rate: 115200
      data_flow_control: software
 ```
 
 
 Result:
 
 ```
 _esphome_zb_gw_efr32._tcp      local
   hostname = [esphome_zb_gw_efr32.local]
   address = [172.16.0.174]
   port = [6638]
   txt = ["version=1.0" "location=basement" "radio_type=ezsp" "baud_rate=115200" "data_flow_control=software"]
```

(Test results obtained with `avahi-browse -a -r`)
