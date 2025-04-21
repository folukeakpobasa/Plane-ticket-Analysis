# Create conditions for values in flight_categories to be created
conditions = [
    (planes["Duration"].str.contains("^0h|^1h|^2h|^3h|^4h")),
    (planes["Duration"].str.contains( '^5h|^6h|^7h|^8h|^9h')),
    (planes["Duration"].str.contains('10h|11h|12h|13h|14h|15h|16h'))
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()