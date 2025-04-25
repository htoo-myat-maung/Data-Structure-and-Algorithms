# forward chaining

facts = {"browsed electronics", "another product","browsed fitness gear", "bought earbuds", "interested in health and fitness category"
        , "not purcahsed smartwatch", "give positive review", "lives in warm climate", "prefer well-rated item"
        , "prefer mid-range item"}
# inferred = set()    # set 
rules = [({"browsed electronics", "another product"}, "interestd tech"),
         ({"browsed fitness gear", "buys fitness products"}, "intersted in fitness"),
         ({"interested tech", "interested in fitness"}, "interested in wearable tech")
        ]

        # another list

def forward_chain(f,r):
    inferred = list()
    all_facts = f

    while True:
        new_inference = 0    #flag to see whether the new inference is added or not
        for x in r:
            conditions = x[0]
            conclusion = x [1]
            #print(f"IF {conditions} THEN {conclusion}")

            print(conditions,conclusion)

            print(conditions.issubset(all_facts))

            if conditions.issubset(all_facts) and conclusion not in inferred:
                print("here")
                inferred.append(conclusion)
                new_inference += 1
                break
        if new_inference > 0:
            break
        inferred.add(new_inference)
        all_facts.add(new_inference)

            # if conditions.issubset(facts) and conclusion not in inferred:
            #     print(f"Adding {conclusion} to inferred")
            #     inferred.add(conclusion)
            #     facts.append(conclusion)
        break



    return inferred

recommendation = forward_chain(facts, rules)


#print the recommended products
for i in recommendation:
    print("\nfinally")
    print(f"{i}")