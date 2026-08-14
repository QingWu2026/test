# Structure v_code; Date: 8/12/2026; Author: Qing Wu; Version: 0.2; 
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
    
def v_coin_space(v_coin_init_const, v_coin_name):

    #v_coin associates to space
    while v_coin_init(v_coin_init_const): # default 4x4 sized regional blocker
        return v_coin_space = uncollided(v_coin_name)
        
def v_coin_init(v_coin_init_ops): #initial operations: broadcasting
    
    #different init group with different expectations
    v_coin_init_const = ["0-venture capitals", "1-individual developers", "2-corporate developers", \
                         "3-investors",        "4-mutual funds",          "5-nonprofit funds",      \
                         "6-stocks",           "7-composite funds",       "8-bonds",                \
                         "9-futures",          "10-debts",                "11-options",             \
                         "12-securities",      "13-shares",               "14-spots",               \
                         "15-entities",        "16-agencies",             "17-aritifical investors" ]
                         
    group_name = v_coin_init_ops.group_name
    if group_name in v_coin_init_const:
        print("Virtual coin initial groups: ", group_name)
    else:
        print("A new group is waiting to creat")
        [networks, error_reports] = v_coin_init_ops.broadcast() #a initialization node broadcast to vote
        
    agreements = networks.agreements  #[8, 9, 5, ...] notes voting back from various networks
    
    if error_reports:
        print("Error operations!")
        return
        
    for idx in range(0, len(agreements)):
        if networks[idx] and agreements[idx] == networks[idx].notes_number: # all group agreed
            n = 0
            v_coin_init_tmp[n] = networks[idx]
            n = n + 1
   
    agreed_time_stamps = v_coin_init_tmp.time_stamps
    chosen_time_stamp = min(agreed_time_stamps)
    agreed_groups = []
    
    while tmp in v_coin_init_tmp:
        time_stamp_tmp = tmp.time_stamp
        if time_stamp_tmp <= chosen_time_stamp:
            agreed_groups.append(networks.group_name)
            
    return agreed_groups

def outboundInfoCoder(inboundInfo):
    
    abbrieviations = {'ST#':}
    merchandise_info = []
    

