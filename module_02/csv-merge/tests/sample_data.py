import pytest
import pandas as pd


@pytest.fixture()
def sample_data():
    bank = pd.DataFrame({
        'hostname':   {0: 'ny-res-fw',      1: 'la-sec-sw',     2: 'la-mkt-db'},
        'IPAddress':  {0: '192.250.29.243', 1: '172.46.97.47',  2: '10.79.170.27'},
        'Department': {0: 'Research',       1: 'Security',      2: 'Marketing'},
        'OS':         {0: 'Cisco',          1: 'Cisco',         2: 'Oracle'},
        'Function':   {0: 'firewall',       1: 'switch',        2: 'database'}
    })
    fin = pd.DataFrame({
        'Name':       {0: 'phx-mkt-app',    1: 'hou-res-sw',    2: 'phx-res-rtr'},
        'IP':         {0: '192.22.39.29',   1: '10.241.66.53',  2: '172.125.81.184'},
        'Dept':       {0: 'Marketing',      1: 'Research',      2: 'Research'},
        'Operating System': {0: 'Mac',      1: 'Cisco',         2: 'Cisco'},
        'Function':   {0: 'application',    1: 'switch',        2: 'router'}
    })
    fcu = pd.DataFrame({
        'Host':       {0: 'was-fin-web',    1: 'was-sales-fw',  2: 'por-fin-web'},
        'IP Address': {0: '172.57.191.179', 1: '172.130.30.89', 2: '10.37.13.57'},
        'Department': {0: 'Finance',        1: 'Sales',         2: 'Finance'},
        'OS':         {0: 'Mac',            1: 'Cisco',         2: 'Windows'},
        'Function':   {0: 'web',            1: 'firewall',      2: 'web'}
    })
    return [bank, fin, fcu]


@pytest.fixture()
def renamed_sample_data():
    bank = pd.DataFrame({
        'Host Name':  {0: 'ny-res-fw',      1: 'la-sec-sw',     2: 'la-mkt-db'},
        'IP Address': {0: '192.250.29.243', 1: '172.46.97.47',  2: '10.79.170.27'},
        'Department': {0: 'Research',       1: 'Security',      2: 'Marketing'},
        'OS':         {0: 'Cisco',          1: 'Cisco',         2: 'Oracle'},
        'Function':   {0: 'firewall',       1: 'switch',        2: 'database'}
    })
    fin = pd.DataFrame({
        'Host Name':  {0: 'phx-mkt-app',    1: 'hou-res-sw',    2: 'phx-res-rtr'},
        'IP Address': {0: '192.22.39.29',   1: '10.241.66.53',  2: '172.125.81.184'},
        'Department': {0: 'Marketing',      1: 'Research',      2: 'Research'},
        'OS':         {0: 'Mac',            1: 'Cisco',         2: 'Cisco'},
        'Function':   {0: 'application',    1: 'switch',        2: 'router'}
    })
    fcu = pd.DataFrame({
        'Host Name':  {0: 'was-fin-web',    1: 'was-sales-fw',  2: 'por-fin-web'},
        'IP Address': {0: '172.57.191.179', 1: '172.130.30.89', 2: '10.37.13.57'},
        'Department': {0: 'Finance',        1: 'Sales',         2: 'Finance'},
        'OS':         {0: 'Mac',            1: 'Cisco',         2: 'Windows'},
        'Function':   {0: 'web',            1: 'firewall',      2: 'web'}
    })
    return [bank, fin, fcu]


@pytest.fixture()
def sample_merge_result():
    result = pd.DataFrame({
        'Department':  {0: 'Research',        1: 'Security',       2: 'Marketing',
                        3: 'Marketing',       4: 'Research',       5: 'Research',
                        6: 'Finance',         7: 'Sales',          8: 'Finance'},
         'Function':   {0: 'firewall',        1: 'switch',         2: 'database',
                        3: 'application',     4: 'switch',         5: 'router',
                        6: 'web',             7: 'firewall',       8: 'web'},
         'Host Name':  {0: 'ny-res-fw',       1: 'la-sec-sw',      2: 'la-mkt-db',
                        3: 'phx-mkt-app',     4: 'hou-res-sw',     5: 'phx-res-rtr',
                        6: 'was-fin-web',     7: 'was-sales-fw',   8: 'por-fin-web'},
         'IP Address': {0: '192.250.29.243',  1: '172.46.97.47',   2: '10.79.170.27',
                        3: '192.22.39.29',    4: '10.241.66.53',   5: '172.125.81.184',
                        6: '172.57.191.179',  7: '172.130.30.89',  8: '10.37.13.57'},
         'OS':         {0: 'Cisco',           1: 'Cisco',          2: 'Oracle',
                        3: 'Mac',             4: 'Cisco',          5: 'Cisco',
                        6: 'Mac',             7: 'Cisco',          8: 'Windows'}
        })
    return result
