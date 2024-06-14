import csv
import click
import datetime
from async_code import async_reboot

api_key = 'yourapikey'
# SNs can come from anywhere - get orgdevices, CSV, etc but they must be in a nested dict like below
serial_numbers = [{'serial': 'XXX-XXX-XXX'}, {'serial': 'XXX-XXX-XXX'}]

click.secho(
    f'The folowing SNs will be rebooted after this operation:\n', fg='white'
    )

click.secho(
    f'{" | ".join(x["serial"] for x in serial_numbers)}\n', fg='green'
    )

if click.confirm(f'You are about to reboot { len(serial_numbers) } devices.  Are you sure?'):
    reboot_status = async_reboot.async_reboot_devices(api_key=api_key, devices=serial_numbers, debug_app=False)

click.secho(
    f'{ reboot_status }', fg='green'
    )

keys = reboot_status[0].keys()
ct = datetime.datetime.now()

f_name = 'reboot_results_' + str(ct) + '.csv'
with open(f_name, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(reboot_status)

click.secho(
    f'Reboot results written to file: { f_name }', fg='green'
    )
