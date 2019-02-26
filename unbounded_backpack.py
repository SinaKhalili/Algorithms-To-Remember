def budgetShopping(n, bundleQuantities, bundleCosts):
    max_costs = [0 for x in range(n+1)]
    for i in range(len(max_costs)):
        for j in range(len(bundleCosts)):
            if (i >= bundleCosts[j]):
                max_costs[i] = max(max_costs[i], max_costs[i - bundleCosts[j]] + bundleQuantities[j])
    return max_costs[n] 
