import requests, json, datetime, random
from dateutil import parser

while True:
    #Setup
    random_time = random.randint(1,6)
    current_time = datetime.datetime.now() - datetime.timedelta(seconds=random_time)

    #Request and Response
    url = 'http://127.0.0.1:8000'
    response = requests.get(url, {'client_time': current_time})
    dict_response = json.loads(response.text)

    #Data parse
    client_time = parser.parse(dict_response['client_time'])
    server_request_time = parser.parse(dict_response['server_request_time'])
    server_response_time = parser.parse(dict_response['server_response_time'])
    client_received_response_time = datetime.datetime.now() - datetime.timedelta(seconds=random_time)

    #Computation of result
    t0 = client_time
    t1 = server_request_time
    t2 = server_response_time 
    t3 = client_received_response_time
    p1 = t1-t0
    p2 = t2-t3
    print(f'P1: {p1} P2: {p2}')
    discrepancy_time = ((t1-t0) + (t2-t3))/2
    adjusted_hour = datetime.datetime.now() + discrepancy_time

    #Results
    print(f'T0 Client request time: {client_time}')
    print(f'T1 Server received request time: {server_request_time}')
    print(f'T2 Server response time: {server_response_time}')
    print(f'T3 Client received response time: {client_received_response_time}')
    print(f'Discrepancy time: {discrepancy_time}')
    print(f'Unadjusted Hour: {datetime.datetime.now()}')
    print(f'Adjusted Hour: {adjusted_hour}')

    #Tests
    assert server_request_time != server_response_time
    if client_time >= server_request_time:
        print('Error T0>T1, client request time is greater than server received request time')
        break
    elif server_request_time > server_response_time:
        print('Error T1>T2, server received request time is greater than server response time')
        break
    else:
        print('Time adjusted correctly')
        
    print('##############################################################\n')

    
