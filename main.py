import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml


data = fetch_openml(name='diabetes', version=1, as_frame=True) #loading the diabetes data

#Since while plotting the data i could not find obvious correlations between pairs
#i have chosen to try using all features and heatmapped the correlations (seen below after
#the histogram plot
fig, axs  = plt.subplots(1, len(features), figsize = (20,3))

for ax, f in zip(axs, features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

#within this plot table we can see that data we expect to be plotted normally is done so
#mass - normal
#there are some values that are missing "missing data" which is why some of the 0 values are larger than expected

#after trying to plot multuple plot tables i could see there were no obvious correlations
#after looking online i could find that this is due to the fact that data in patients can be attributed to multiple
#factors as opposed to just one - which is what we do in an x,y plot
reference_feature = features[3]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(features), figsize = (20,3))

for ax, f in zip(axs, features):
  
  ax.scatter(df[f], y)
  ax.set_xlabel(f)
  ax.set_ylabel(reference_feature)

plt.show()

#using chatgpt I heat maped the 81 different combinations (including duplicates and obvious
#1:1 correlations (skin:skin, insu:insu etc...)
df['class'] = df['class'].map({'tested_positive': 1, 'tested_negative': 0}) 
corr_matrix = df.corr()

# Display heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


#some correlations were a littel higher than the rest but nothing i find significant
#an obvious correlation (however still not perfect) is age:preg. we would
#expect some correlation between age and pregnancy count.

#i have graphed some of the higher correlation graphs, some are more visally obvious than others
reference_feature = ['skin','age','insu','insu'] # The reference feature
comparison_feature = ['mass','preg','skin','plas']  # A feature to compare to

# Create a scatter plot for the selected pair
fig, axs  = plt.subplots(2,2, figsize = (10,10))
for ax, ref,com in zip(axs.ravel() ,reference_feature, comparison_feature):
  ax.scatter(df[ref], df[com], alpha=0.6)
  ax.set_xlabel(ref)
  ax.set_ylabel(com)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()
