# asm-n_infra
asm-n Infra repository

### ДЗ№6: Декларативное описание в виде кода инфраструктуры YC, требуемой для запуска тестового приложения, при помощи Terraform.

Создание var.app_instances_count ВМ, установка тестового приложения, создание группы балансировки, создание балансировщика.

Для запуска:
```
terraform apply
```

Переменные:
```
cloud_id                 = ""
folder_id                = ""
zone                     = "ru-central1-a"
image_id                 = ""
subnet_id                = ""
external_app_port        = 8080
internal_app_port        = 9292
app_instances_count      = 1
public_key_path          = ""
private_key_path         = ""
service_account_key_file = ""
```
