# Zeroconf custom component for ESPHome


Example configuration:

```yaml
external_components:
  - source: github://thegroove/esphome-zeroconf@main

zeroconf:
  - service: myservice
    protocol: tcp
    port: 8080
 ```
 
 
 Result:
 
 ```
 _myservice._tcp      local
   hostname = [my_esphome_node.local]
   address = [172.16.0.174]
   port = [8080]
   txt = []
```


Adding some txt records:

```yaml
external_components:
  - source: github://thegroove/esphome-zeroconf@main

zeroconf:
  - service: myservice
    protocol: tcp
    port: 8080
    txt:
      version: 1.0
      location: basement
 ```
 
 
 Result:
 
 ```
 _myservice._tcp      local
   hostname = [my_esphome_node.local]
   address = [172.16.0.174]
   port = [8080]
   txt = ["version=1.0" "location=basement"]
```

(Test results obtained with `avahi-browse -a -r`)
