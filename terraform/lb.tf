resource "yandex_lb_target_group" "app_target_group" {
  name = "reddit-app-target-group"

  dynamic "target" {
    for_each = yandex_compute_instance.app
    content {
      subnet_id = var.subnet_id
      address   = target.value.network_interface[0].ip_address
    }
  }

  depends_on = [
    yandex_compute_instance.app
  ]
}

resource "yandex_lb_network_load_balancer" "app_lb" {
  name = "reddit-app-lb"

  listener {
    name        = "listener-${var.external_app_port}"
    port        = var.external_app_port
    target_port = var.internal_app_port
    external_address_spec {
      ip_version = "ipv4"
    }
  }

  attached_target_group {
    target_group_id = yandex_lb_target_group.app_target_group.id

    healthcheck {
      name = "healthcheck-${var.internal_app_port}"
      http_options {
        port = var.internal_app_port
        path = "/"
      }
    }
  }

  depends_on = [
    yandex_lb_target_group.app_target_group
  ]
}
