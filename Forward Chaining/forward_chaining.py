# forward chaining

facts = {"browsed electronics", "another product","browsed fitness gear", "bought earbuds", "interested in health and fitness category"
        , "not purchased smartwatch", "give positive review", "lives in warm climate", "prefer well-rated item"
        , "prefer mid-range item"}
# inferred = set()    # set 
rules = [({"browsed electronics"}, "interestd in tech"),
         ({"buys fitness products"}, "intersted in fitness"),
         ({"browsed fitness gear"}, "interested in fitness"),
         ({"interestd in tech", "interested in fitness"}, "interested in wearable tech"),
         ({"interested in wearable tech", "not purchased smartwatch"}, "smarthwatches recommended"),
         ({"smarthwatches recommended", "prefer mid-range item"}, "FitPlus Smart Band Pro"),
         ({"smarthwatches recommended", "prefer high-range item", "prefer well-rated item", "lives in warm climate"}, "Galaxy Watch X")
        ]

        # another list

def forward_chain(f,r):
    inferred = list()
    all_facts = f

    while True:
        #new_inference = 0    #flag to see whether the new inference is added or not
        print("hello")
        conditions = None
        conclusion = None
        for x in r:
            conditions = x[0]
            conclusion = x [1]
            #print(f"IF {conditions} THEN {conclusion}")

            

            #print(conditions.issubset(all_facts))

            if conditions.issubset(all_facts) and conclusion not in set(inferred):
                #print("here")
                inferred.append(conclusion)
                all_facts.add(conclusion)
                print(conditions,conclusion)
                #print("here")



            # if conditions.issubset(facts) and conclusion not in inferred:
            #     print(f"Adding {conclusion} to inferred")
            #     inferred.add(conclusion)
            #     facts.append(conclusion)

        break

    print(inferred)

    return inferred

recommendation = forward_chain(facts, rules)


print(f"The recommendation for the customer is {recommendation[-1]}.")