terraform {
  required_providers {
    yandex = "~> 0.35"
  }
}

provider "yandex" {
  service_account_key_file = var.service_account_key_file
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  zone                     = var.zone
}

resource "yandex_storage_bucket" "app_storage" {
  bucket     = "app-storage"
  access_key = var.access_key
  secret_key = var.service_key
}
