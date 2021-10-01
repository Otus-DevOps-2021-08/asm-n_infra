#output "external_ip_address_app" {
#  value = tolist(tolist(yandex_lb_network_load_balancer.app_lb.listener)[0].external_address_spec)[0].address
#}
output "external_port_app" {
  value = var.external_app_port
}
