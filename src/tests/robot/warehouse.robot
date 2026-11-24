*** Settings ***
Library         ../warehouse_library.py
Suite Setup     Reset Warehouses
Test Setup      Reset Warehouses
Test Teardown   Reset Warehouses

*** Test Cases ***
Page Opens With No Warehouses
    ${page}=    Get Warehouse Page
    Should Contain    ${page}    Warehouse manager
    Should Contain    ${page}    No warehouses yet

Create And List Several Warehouses
    ${page}=    Create Warehouse    Main storage    100
    Should Contain    ${page}    Main storage
    ${page}=    Create Warehouse    Cold room    40
    Should Contain    ${page}    Main storage
    Should Contain    ${page}    Cold room
    Should Contain    ${page}    of 100.00
    Should Contain    ${page}    of 40.00

Add And Remove Stock
    ${page}=    Create Warehouse    Parts    20
    ${page}=    Add Stock    1    12
    Should Contain    ${page}    12.00
    ${page}=    Remove Stock    1    5
    Should Contain    ${page}    7.00
    Should Contain    ${page}    13.00 capacity remaining

Warehouse Capacity Is Not Exceeded
    ${page}=    Create Warehouse    Small store    10
    ${page}=    Add Stock    1    15
    Should Contain    ${page}    10.00
    Should Contain    ${page}    0.00 capacity remaining

Invalid Warehouse Input Is Rejected
    ${page}=    Create Warehouse    ${EMPTY}    0
    Should Contain    ${page}    Enter a name for the warehouse.
    Should Contain    ${page}    No warehouses yet
