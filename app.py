from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

# Load components from individual files
def load_component(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

# Map services to their corresponding verb files
service_to_verb_file = {
    # Routing-related services
    "BGP session": "verbs_routing.txt",
    "OSPF adjacency": "verbs_routing.txt",
    "EIGRP": "verbs_routing.txt",
    "BGP route reflector": "verbs_routing.txt",
    "OSPF LSA": "verbs_routing.txt",
    "SD-WAN controller": "verbs_routing.txt",
    "route redistribution": "verbs_routing.txt",

    # Switching-related services
    "spanning tree protocol": "verbs_switching.txt",
    "VLAN trunking protocol": "verbs_switching.txt",
    "EtherChannel bundle": "verbs_switching.txt",
    "switch stack": "verbs_switching.txt",
    "switchport": "verbs_switching.txt",
    "redundant link": "verbs_switching.txt",
    "interface MTU": "verbs_switching.txt",

    # Security-related services
    "ACL": "verbs_security.txt",
    "firewall": "verbs_security.txt",
    "RADIUS server": "verbs_security.txt",
    "TACACS+ server": "verbs_security.txt",

    # Wireless-related services
    "wireless controller": "verbs_wireless.txt",
    "wireless network": "verbs_wireless.txt",

    # General services
    "DHCP server": "verbs_general.txt",
    "NAT translation table": "verbs_general.txt",
    "SNMP community string": "verbs_general.txt",
    "DNS server": "verbs_general.txt",
    "NTP server": "verbs_general.txt",
    "MPLS label switched path": "verbs_general.txt",
    "GRE tunnel": "verbs_general.txt",
    "IP SLA probe": "verbs_general.txt",
    "syslog server": "verbs_general.txt",
    "interface counters": "verbs_general.txt",
    "route-map": "verbs_general.txt",
    "VRF configuration": "verbs_general.txt",
    "DMVPN hub": "verbs_general.txt",
    "core switch power supply": "verbs_general.txt",
    "VSS pair": "verbs_general.txt",
    "NetFlow export": "verbs_general.txt",
    "multicast stream": "verbs_general.txt",
    "TAC case": "verbs_general.txt",
    "switch": "verbs_general.txt",
    "router's flash memory": "verbs_general.txt",
    "DHCP snooping database": "verbs_general.txt",
    "port-channel load balancing algorithm": "verbs_general.txt",
    "core switch CPU": "verbs_general.txt",
    "router ID conflict": "verbs_general.txt",
    "devs": "verbs_general.txt",
    "project manager": "verbs_general.txt",
}

# Map services to their corresponding solution files
service_to_solution_file = {
    # Routing-related services
    "BGP session": "solutions_routing.txt",
    "OSPF adjacency": "solutions_routing.txt",
    "EIGRP": "solutions_routing.txt",
    "BGP route reflector": "solutions_routing.txt",
    "OSPF LSA": "solutions_routing.txt",
    "SD-WAN controller": "solutions_routing.txt",
    "route redistribution": "solutions_routing.txt",

    # Switching-related services
    "spanning tree protocol": "solutions_switching.txt",
    "VLAN trunking protocol": "solutions_switching.txt",
    "EtherChannel bundle": "solutions_switching.txt",
    "switch stack": "solutions_switching.txt",
    "switchport": "solutions_switching.txt",
    "redundant link": "solutions_switching.txt",
    "interface MTU": "solutions_switching.txt",

    # Security-related services
    "ACL": "solutions_security.txt",
    "firewall": "solutions_security.txt",
    "RADIUS server": "solutions_security.txt",
    "TACACS+ server": "solutions_security.txt",

    # Wireless-related services
    "wireless controller": "solutions_wireless.txt",
    "wireless network": "solutions_wireless.txt",

    # General services
    "DHCP server": "solutions_general.txt",
    "NAT translation table": "solutions_general.txt",
    "SNMP community string": "solutions_general.txt",
    "DNS server": "solutions_general.txt",
    "NTP server": "solutions_general.txt",
    "MPLS label switched path": "solutions_general.txt",
    "GRE tunnel": "solutions_general.txt",
    "IP SLA probe": "solutions_general.txt",
    "syslog server": "solutions_general.txt",
    "interface counters": "solutions_general.txt",
    "route-map": "solutions_general.txt",
    "VRF configuration": "solutions_general.txt",
    "DMVPN hub": "solutions_general.txt",
    "core switch power supply": "solutions_general.txt",
    "VSS pair": "solutions_general.txt",
    "NetFlow export": "solutions_general.txt",
    "multicast stream": "solutions_general.txt",
    "TAC case": "solutions_general.txt",
    "switch": "solutions_general.txt",
    "router's flash memory": "solutions_general.txt",
    "DHCP snooping database": "solutions_general.txt",
    "port-channel load balancing algorithm": "solutions_general.txt",
    "core switch CPU": "solutions_general.txt",
    "router ID conflict": "solutions_general.txt",
    "devs": "solutions_general.txt",
    "project manager": "solutions_general.txt",
}

# Load reasons dynamically using verb group files
def load_reasons():
    services = load_component("services.txt")
    reasons = []
    for service in services:
        verb_file = service_to_verb_file.get(service, "verbs_general.txt")
        verbs = load_component(verb_file)
        for verb in verbs:
            reasons.append(f"The fucking {service} {verb}.")
    return reasons

# Load solutions from a file
def load_solutions():
    file_path = os.path.join(os.path.dirname(__file__), "solutions_general.txt")
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

reasons = load_reasons()
solutions = load_solutions()

@app.route("/")
def index():
    # Generate a random service, verb, and solution
    service = random.choice(load_component("services.txt"))
    verb_file = service_to_verb_file.get(service, "verbs_general.txt")
    verb = random.choice(load_component(verb_file))
    
    # Determine the solution file (50/50 chance for non-general services)
    specific_solution_file = service_to_solution_file.get(service, "solutions_general.txt")
    solution_file = specific_solution_file if specific_solution_file == "solutions_general.txt" or random.choice([True, False]) else "solutions_general.txt"
    solution = random.choice(load_component(solution_file))
    
    return render_template("index.html", service=service, verb=verb, solution=solution)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host="0.0.0.0", port=port, debug=False)  # Enable debug mode
