# asm-n_infra
asm-n Infra repository

### ДЗ№3: Запуск VM в Yandex Cloud, управление правилами фаервола, настройка SSH подключения, настройка SSH подключения через Bastion Host, настройка VPN сервера и VPN-подключения.

Для подключения в одну команду:
```
ssh -t -i ~/.ssh/appuser -A appuser@62.84.114.170 ssh appuser@10.128.0.3
```

Для подключения по алиасу добавить в ~/.ssh/config:
```
Host bastion
	HostName 62.84.114.170
	IdentityFile ~/.ssh/appuser
	User appuser

Host someinternalhost
	ProxyCommand ssh -q bastion nc -q0 10.128.0.3 22
	IdentityFile ~/.ssh/appuser
	User appuser
```


### Данные для подключения:
bastion_IP = 62.84.114.170
someinternalhost_IP = 10.128.0.3
