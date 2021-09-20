# asm-n_infra
asm-n Infra repository

### ДЗ№4: Практика управления ресурсами yandex cloud через YC.

Для создания инстанса с запущенным приложением:
```
yc compute instance create \
  --name reddit-app \
  --hostname reddit-app \
  --memory=4 \
  --create-boot-disk image-folder-id=standard-images,image-family=ubuntu-1604-lts,size=10GB \
  --network-interface subnet-name=default-ru-central1-a,nat-ip-version=ipv4 \
  --metadata serial-port-enable=1 \
  --metadata-from-file user-data=./user-data.yml
```

#### Test:
testapp_IP = 193.32.218.215
testapp_port = 9292
