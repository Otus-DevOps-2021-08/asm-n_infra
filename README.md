# asm-n_infra
asm-n Infra repository

### ДЗ№7: Создание Terraform модулей для управления компонентами инфраструктуры.

Настройка модулей для создания app и db инстансов, настройка prod и stage окружений. Настройка remote backend. Деплой приложения.

Secret key для бэкенда находится в secrets/backend.tf. Поэтому:
```
terraform init -backend-config="../storage-backend.tf" -backend-config="../../secrets/backend.tf"
```

Переменные:
```
cloud_id                 = ""
folder_id                = ""
zone                     = "ru-central1-a"
app_disk_image           = ""
db_disk_image            = ""
subnet_id                = ""
public_key_path          = ""
private_key_path         = ""
service_account_key_file = ""
```
