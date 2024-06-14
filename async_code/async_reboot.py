import meraki
import meraki.aio
import asyncio
import tqdm.asyncio
import time

__author__ = 'Zach Brewer'
__email__ = 'zbrewer@cisco.com'
__version__ = '0.0.2'
__license__ = 'MIT'

timestamp = time.time()
'''
simple code that returns the admins for multiple devices
'''
async def _reboot_devices(aiomeraki, device):
    '''  Async function that reboots devices    '''

    try:
        to_reboot = await aiomeraki.devices.rebootDevice(serial=device['serial'])

    except meraki.exceptions.AsyncAPIError as e:
        print(f'Meraki AIO API Error (Device { device["serial"] }"): \n { e }')
        to_reboot = None

    except Exception as e:
        print(f'some other ERROR: {e}')
        to_reboot = None

    reboot_data = []
    if to_reboot:
        status = to_reboot['success']
        reboot_data.append({'serial': device['serial'] ,'reboot_result': status, 'timestamp': timestamp})

    else:
        to_reboot = None
        reboot_data = None


    return reboot_data

async def _async_apicall(api_key, devices, debug_values):
    # Instantiate a Meraki dashboard API session
    # NOTE: you have to use "async with" so that the session will be closed correctly at the end of the usage
    async with meraki.aio.AsyncDashboardAPI(
            api_key,
            base_url='https://api.meraki.com/api/v1',
            log_file_prefix=__file__[:-3],
            #log_path='logs/',
            maximum_concurrent_requests=10,
            maximum_retries= 100,
            wait_on_rate_limit=True,
            output_log=debug_values['output_log'],
            print_console=debug_values['output_console'],
            suppress_logging=debug_values['suppress_logging']
        ) as aiomeraki:
        
        all__reboot_devices = []

        admin_tasks = [_reboot_devices(aiomeraki, device) for device in devices]
        for task in tqdm.tqdm(
                asyncio.as_completed(admin_tasks),
                total = len(admin_tasks),
                colour='green',
                ):

            reboot_json = await task
            for device in reboot_json:
                all__reboot_devices.append(device)
        
        return all__reboot_devices


def async_reboot_devices(api_key, devices, debug_app=False):
    if debug_app:
        debug_values = {'output_log' : True, 'output_console' : True, 'suppress_logging' : False}
    else:
        debug_values = {'output_log' : False, 'output_console' : False, 'suppress_logging' : True}

    #begin async loop
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(_async_apicall(api_key, devices, debug_values))