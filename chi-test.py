from scipy import stats
rvs1 = stats.norm.rvs(loc=5, scale=10, size=1000)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=1000)
result = stats.ttest_ind(rvs1, rvs2)

print(result)


# with significance level of 5% we will reject null hypothesis with p value <= 5%

if result.pvalue <= 0.05:
    print("we reject null hypothesis")
else:
    print("we don't reject null hypothesis")
