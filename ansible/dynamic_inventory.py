#!/usr/bin/python3

import os
import json
import subprocess


TERRAFORM_STATE_DIR = "../terraform/stage/"
DEFAULT_INVENTORY_FILEPATH = "./dynamic_inventory.json"


def ReadTerraformState(terraformDir: str) -> dict:
  oldCwd = os.getcwd()
  terraformState = dict()
  try:
    os.chdir(terraformDir)
    terraformStateJson = subprocess.run(["terraform", "show", "-json"],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE).stdout
    terraformState = json.loads(terraformStateJson)
  except:
    pass
  finally:
    os.chdir(oldCwd)
  return terraformState


def IsEmptyTerraformState(terraformState: dict) -> bool:
  return "values" not in terraformState


def LoadDefaultInventory() -> dict:
  with open(DEFAULT_INVENTORY_FILEPATH, "r") as inv_file:
      return json.load(inv_file)


def CreateInventory() -> dict:
  inventory = dict()
  inventory["_meta"] = dict()
  inventory["_meta"]["hostvars"] = dict()
  return inventory


def CreateInventoryGroup() -> dict:
  inventoryGroup = dict()
  inventoryGroup["hosts"] = list()
  inventoryGroup["vars"] = dict()
  return inventoryGroup


def AddHostToInventory(hostInfo: dict, inventory: dict):
  hostname = hostInfo["hostname"]
  group = hostInfo["group"]
  ipAddress = hostInfo["ipAddress"]

  inventory[group]["hosts"].append(hostname)
  if hostname not in inventory["_meta"]["hostvars"]:
    inventory["_meta"]["hostvars"][hostname] = dict()
  inventory["_meta"]["hostvars"][hostname]["ansible_host"] = ipAddress


def main():
  terraformState = ReadTerraformState(TERRAFORM_STATE_DIR)
  #print(json.dumps(terraformState, indent=2))

  inventory = CreateInventory()

  if IsEmptyTerraformState(terraformState):
    print(json.dumps(LoadDefaultInventory()))
    return

  for childModule in terraformState["values"]["root_module"]["child_modules"]:
    for resource in childModule["resources"]:
      if resource["type"] != "yandex_compute_instance":
        continue

      hostInfo = dict()
      hostInfo["hostname"] = resource["values"]["name"]
      hostInfo["group"] = resource["values"]["labels"]["group"]
      hostInfo["ipAddress"] = resource["values"]["network_interface"][0]["nat_ip_address"]

      if hostInfo["group"] not in inventory:
        inventory[hostInfo["group"]] = CreateInventoryGroup()

      AddHostToInventory(hostInfo, inventory)

  inventory["all"] = dict()
  inventory["all"]["vars"] = dict()
  inventory["all"]["vars"]["db_internal_ip"] = terraformState["values"]["outputs"]["internal_ip_address_db"]["value"]

  print(json.dumps(inventory))


if __name__ == "__main__":
  main()
