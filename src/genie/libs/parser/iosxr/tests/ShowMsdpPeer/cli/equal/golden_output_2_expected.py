

expected_output = {
    'vrf': {
        'VRF1': {
            'peer': {
                '10.4.1.1': {
                    'connect_source_address': '10.151.22.23',
                    'description': 'R1',
                    'elapsed_time': '18:19:47',
                    'nsr': {
                        'oper_downs': 0,
                        'state': 'Unknown',
                        'up_down_time': '22:46:31'},
                    'password': 'None',
                    'peer_as': 0,
                    'peer_name': '?',
                    'reset': '0',
                    'sa_filter': {
                        'in': {
                            '(S,G)': {
                                'filter': 'safilin'},
                            'RP': {
                                'filter': 'none'}},
                        'out': {
                            '(S,G)': {
                                'filter': 'safilout'},
                            'RP': {
                                'filter': 'none'}}},
                    'sa_request': {
                        'input_filter': 'none',
                        'sa_request_to_peer': 'disabled'},
                    'session_state': 'Listen',
                    'statistics': {
                        'conn_count_cleared': '22:46:31',
                        'output_message_discarded': 0,
                        'queue': {
                            'size_input': 0,
                            'size_output': 0},
                        'received': {
                            'sa_message': 0,
                            'tlv_message': 0},
                        'sent': {
                            'tlv_message': 0}},
                    'timer': {
                        'keepalive_interval': 30,
                        'peer_timeout_interval': 75},
                    'ttl_threshold': 222}}}}}