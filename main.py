#!/usr/bin/python3

import dbus, uuid

from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 5000

bus = dbus.SystemBus()

dbusObject = bus.get_object("com.helium.Miner", "/")
dbusInterface = dbus.Interface(objTest, "com.helium.Miner")

class ConfigAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("Helium Hotspot B5D9")
        self.include_tx_power = True

class DeviceInformationService(Service):
    DEVINFO_SVC_UUID = "180A"

    def __init__(self, index):

        Service.__init__(self, index, self.DEVINFO_SVC_UUID, True)
        self.add_characteristic(ManufactureNameCharacteristic(self))
        self.add_characteristic(FirmwareRevisionCharacteristic(self))
        self.add_characteristic(SerialNumberCharacteristic(self))

class ManufactureNameCharacteristic(Characteristic):
    MANUFACTURE_NAME_CHARACTERISTIC_UUID = "2A29"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.MANUFACTURE_NAME_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "Nebra LTD."
        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class FirmwareRevisionCharacteristic(Characteristic):
    FIRMWARE_REVISION_CHARACTERISTIC_UUID = "2A26"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.FIRMWARE_REVISION_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        #CHANGE THIS LINE FOR NEW VERSIONS
        val = "2021.01.05"
        for c in val:
            value.append(dbus.Byte(c.encode()))

        return value

class SerialNumberCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "2A25"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = open("/sys/class/net/eth0/address").readline().strip().replace(":","")

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class HeliumService(Service):
    DEVINFO_SVC_UUID = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"

    def __init__(self, index):

        Service.__init__(self, index, self.DEVINFO_SVC_UUID, True)
        self.add_characteristic(OnboardingKeyCharacteristic(self))
        self.add_characteristic(PublicKeyCharacteristic(self))
        self.add_characteristic(WiFiServicesCharacteristic(self))
        self.add_characteristic(DiagnosticsCharacteristic(self))
        self.add_characteristic(MacAddressCharacteristic(self))
        self.add_characteristic(LightsCharacteristic(self))
        self.add_characteristic(WiFiSSIDCharacteristic(self))
        self.add_characteristic(AssertLocationCharacteristic(self))
        self.add_characteristic(AddGatewayCharacteristic(self))
        self.add_characteristic(WiFiConnectCharacteristic(self))
        self.add_characteristic(EthernetOnlineCharacteristic(self))

class OnboardingKeyCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "d083b2bd-be16-4600-b397-61512ca2f5ad"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class PublicKeyCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "0a852c59-50d3-4492-bfd3-22fe58a24f01"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class WiFiServicesCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "d7515033-7e7b-45be-803f-c8737b171a29"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class DiagnosticsCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "b833d34f-d871-422c-bf9e-8e6ec117d57e"

    #Returns proto of eth, wifi, fw, ip, p2pstatus

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []

        dbusInterface.P2PStatus()
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class MacAddressCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "9c4314f2-8a0c-45fd-a58d-d4a7e64c3a57"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = open("/sys/class/net/eth0/address").readline().strip().replace(":","")

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class LightsCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "180efdef-7579-4b4a-b2df-72733b7fa2fe"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "false"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class WiFiSSIDCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "7731de63-bc6a-4100-8ab1-89b2356b038b"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class AssertLocationCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "d435f5de-01a4-4e7d-84ba-dfd347f60275"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class AddGatewayCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "df3b16ca-c985-4da2-a6d2-9b9b9abdb858"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class WiFiConnectCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "398168aa-0111-4ec0-b1fa-171671270608"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class EthernetOnlineCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "e5866bd6-0288-4476-98ca-ef7da6b4d289"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []


        val = "false"

        if(open("/sys/class/net/eth0/carrier").readline().strip()== "1" or open("/sys/class/net/wlan0/carrier").readline().strip()== "1"):
            val = "true"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value





app = Application()
app.add_service(DeviceInformationService(0))
app.add_service(HeliumService(1))
app.register()


adv = ConfigAdvertisement(0)
adv.register()

try:
    app.run()
except KeyboardInterrupt:
    app.quit()
