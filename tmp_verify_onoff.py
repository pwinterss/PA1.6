from controllers.onoff import OnOffThermostat

# below lower threshold -> turn on

t = OnOffThermostat(setpoint=21.0, deadband=1.0)
t.state = 0
assert t.update(20.4) == 1

# above upper threshold -> turn off

t = OnOffThermostat(setpoint=21.0, deadband=1.0)
t.state = 1
assert t.update(21.6) == 0

# inside deadband -> hold state

t = OnOffThermostat(setpoint=21.0, deadband=1.0)
t.state = 1
assert t.update(21.0) == 1
t.state = 0
assert t.update(21.0) == 0

# safety cutoff -> force off

t = OnOffThermostat(setpoint=21.0, deadband=1.0, safety_high=25.0)
t.state = 1
assert t.update(25.0) == 0

print('onoff checks passed')
