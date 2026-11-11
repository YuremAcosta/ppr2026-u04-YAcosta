from pathlib import Path
import ipaddress

dispositivos = [
    {
        "nombre": "Router01",
        "interfaz": "G0/0",
        "ip": "192.168.1.1",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "Router02",
        "interfaz": "G0/0",
        "ip": "192.168.2.1",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "SwitchCore",
        "interfaz": "VLAN10",
        "ip": "192.168.10.2",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "FirewallEdge",
        "interfaz": "G0/1",
        "ip": "10.0.0.256",
        "mascara": "255.0.0.0",
    },
    {
        "nombre": "ServidorDNS",
        "interfaz": "Eth0",
        "ip": "192.168.2.1",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "AccessPoint01",
        "interfaz": "BVI1",
        "ip": "172.16.5.10",
        "mascara": "255.255.0.0",
    },
    {
        "nombre": "RouterBranch",
        "interfaz": "S0/0/0",
        "ip": "192.168.100.999",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "ServidorSQL",
        "interfaz": "Eth1",
        "ip": "192.168.20.15",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "SwitchAccess",
        "interfaz": "VLAN1",
        "ip": "192.168.1.254",
        "mascara": "255.255.255.0",
    },
    {
        "nombre": "GatewayVoz",
        "interfaz": "G0/2",
        "ip": "172.16.1.1",
        "mascara": "255.255.255.128",
    },
]

ips_registradas = []
ips_validas = 0
ips_no_validas = 0
ips_duplicadas = 0
dispositivos_validos = []

for dispositivo in dispositivos:
  ip = dispositivo["ip"]
  nombre = dispositivo["nombre"]

  try:
    ipaddress.ip_address(ip)

    if ip in ips_registradas:
      print("-" * 50)
      print(
          f"Error: La dirección IP {ip} del dispositivo {nombre} ya está"
          " registrada."
      )
      ips_duplicadas += 1
      print("-" * 50)
    else:
      ips_registradas.append(ip)
      dispositivos_validos.append(dispositivo)
      print("-" * 50)
      print(
          f"La dirección IP {ip} del dispositivo {nombre} es válida y se ha"
          " registrado correctamente."
      )
      ips_validas += 1
      print("-" * 50)

  except ValueError:
    print("-" * 50)
    print(f"Error: La dirección IP {ip} del dispositivo {nombre} no es válida.")
    ips_no_validas += 1
    print("-" * 50)

print("-" * 50)
print("Resumen:")
print("ips válidas: ", ips_validas)
print("ips no válidas: ", ips_no_validas)
print("ips duplicadas: ", ips_duplicadas)
print("-" * 50)

# Crear la carpeta con los archivos de configuración
carpeta = Path("configuraciones")
carpeta.mkdir(exist_ok=True)

# Generar las configuraciones únicamente para dispositivos válidos y únicos
for dispositivo in dispositivos_validos:
  configuracion = f"""hostname {dispositivo["nombre"]}

interface {dispositivo["interfaz"]}
 ip {dispositivo["ip"]} {dispositivo["mascara"]}
no shut

end
"""
  archivo = carpeta / f'{dispositivo["nombre"]}.txt'
  archivo.write_text(configuracion, encoding="utf-8")