# Structure v_code; Date: 8/11/2026; Author: Qing Wu; Version: 0.0; 
# Descriptions: Structure of a general virtual coin's codes

#define
def v_coin(v_coin_name, v_coin_protocol, v_coin_dict):
    #print("Received virtual coin named as: ", v_coin_name)
    for v_coin_protocol in v_coin_dict.protocols:
        if v_coin_dict[v_coin_name].protocol:
            #print("Searched current ", v_coin_name)
            #print(" under protocol: ", v_coin_dict[v_coin_name].protocol)
            v_coin_name_print = v_coin_dict[v_coin_name].name #protocol_name
            v_coin_network = v_coin_dict[v_coin_name].network     #protocol_network
        else:
            #print("Error! No avaible ", v_coin_name)
            #print(" in library ", v_coin_dict[ERRORS].NOT_FOUND)
            v_coin_network = v_coin_dict[ERRORS].NOT_FOUND
    return [v_coin_name_print, v_coin_network]
    
    