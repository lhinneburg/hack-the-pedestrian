import asyncio
import pyrcrack

async def scan_for_devices():
    airmon = pyrcrack.AirmonNg()
    interfaces = await airmon.interfaces

    for interface in interfaces:
        print(interface)
    
    async with airmon(interfaces[0]) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface):
                print(result.table)
                await asyncio.sleep(2)


asyncio.run(scan_for_devices())
