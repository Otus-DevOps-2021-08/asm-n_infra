# asm-n_infra
asm-n Infra repository

### ДЗ№5: Подготовка базового образа VM при помощи Packer.

Для создания базового образа:
```
packer build -var-file variables.json ubuntu16.json
```

Для создания полного образа:
```
packer build immutable.json
```
