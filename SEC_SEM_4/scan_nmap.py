import nmap
import pandas as pd
# nm = nmap.PortScanner()
# nm.scan(hosts='', arguments='-n -sP -PE -PA21,22,80,3389')
# print(nm.command_line())
# print(nm.scaninfo())
# ip = nm.all_hosts()
# print(nm[ip].hostname())
# print(nm[ip].state())
# print(nm[ip].all_protocols())
# print(nm[ip].has_tcp(22))
# print(nm[ip].has_tcp(80))

# nm.scan(hosts='10.100.30.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# for host, status in hosts_list:
#     print(f'{host} : {status}'.format(host=host, status=status))

# nm.scan(hosts='10.100.30.0/24')
# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# for host in hosts_list:
#     print('----------------------------------------------------')
#     print('Host : %s (%s)' % (host, nm[host].hostname()))
#     print('State : %s' % nm[host].state())
#     for proto in nm[host].all_protocols():
#         print('----------')
#         print('Protocol : %s' % proto)

#         lport = nm[host][proto].keys()
#         lport.sort()
#         for port in lport:
#             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


  
ipadr = input('Enter ip address for dcan: ')
begin = int(input('Enter start port for scan: '))
end = int(input('Enter finish port for scan: '))

scanner = nmap.PortScanner() 

result = []
   
for i in range(begin,end+1):  
 
    res = scanner.scan(ipadr, str(i)) 

    res2 = res['scan'][ipadr]['tcp'][i]['state']

    m = {
        'port' : i,
        'protocol' : 'tcp',
        'port_state' : res2
    }

    result.append(m) 

    # print(f'port {i} is {res2}.') 

print(result)

df = pd.DataFrame(result)
df.to_csv("scan_ports.csv")