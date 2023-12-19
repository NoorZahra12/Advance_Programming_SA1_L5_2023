# importing library
import matplotlib.pyplot as plt

# Brand information
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

# Creating a bar graph and setting the numbers in both x and y axis
plt.figure(figsize=(10, 6))
# color of the bars and the variables for x and y axis
plt.bar(brands, values, color='skyblue')
# title at the top of the chart
plt.title('Most Valuable Brands Worldwide in 2023 (in billion U.S. dollars)')
# the title laebl in x axis
plt.xlabel('Brands')
# the tite label in y axis
plt.ylabel('Value (in billion U.S. dollars)')

# Rotating the brand names in x-axis for better look
plt.xticks(rotation=45, ha='right')

# Displaying the values on top of the bars using a for loop on values list
# using enumerate to get the index of an element list as well as the value of an element in the lists
# using the index to put the "values" on the right bars using a  for loop
for i, value in enumerate(values):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom')
# adjusting the layout and making sure all the labels and stuff are shown in the chart.
plt.tight_layout()
# displaying the bar chart
plt.show()